import json
import time
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["GET"])
def get_data(request):
    """
    API endpoint that returns cached data or generates new data if cache is expired.
    Cache TTL: 5 minutes (300 seconds)
    """
    cache_key = 'api_data_response'
    
    # Try to get data from cache first
    cached_data = cache.get(cache_key)
    
    if cached_data is not None:
        # Return cached data
        return JsonResponse(cached_data, safe=False)
    
    # Generate new data if not in cache
    print("Generating data")  # Console log for verification
    
    # Generate large JSON response (1000 items)
    data = []
    current_timestamp = datetime.now().isoformat()
    
    for i in range(1, 1001):
        item = {
            'id': i,
            'name': f'Item {i}',
            'description': f'Description for item {i}',
            'timestamp': current_timestamp,
            'category': f'Category {(i % 10) + 1}',
            'value': i * 1.5,
            'active': i % 2 == 0,
            'tags': [f'tag{j}' for j in range(1, (i % 5) + 2)],
            'metadata': {
                'created_at': current_timestamp,
                'version': '1.0',
                'priority': i % 3 + 1
            }
        }
        data.append(item)
    
    response_data = {
        'data': data,
        'total_count': len(data),
        'generated_at': current_timestamp,
        'cache_info': {
            'cached': False,
            'cache_key': cache_key,
            'ttl_seconds': 300
        }
    }
    
    # Cache the response for 5 minutes (300 seconds)
    cache.set(cache_key, response_data, timeout=300)
    
    return JsonResponse(response_data, safe=False)
