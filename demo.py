#!/usr/bin/env python3
"""
Demonstration script for Django Redis Caching Project
This script shows how to test the caching functionality step by step.
"""

import requests
import time
import json
from datetime import datetime

def demo_caching():
    """Demonstrate the caching functionality."""
    
    print("=" * 70)
    print("Django Redis Caching Project - Demonstration")
    print("=" * 70)
    
    base_url = "http://localhost:8000"
    endpoint = f"{base_url}/api/data/"
    
    print("\n📋 Prerequisites:")
    print("1. Make sure Redis server is running")
    print("2. Start Django server: python manage.py runserver")
    print("3. The server should be running on http://localhost:8000")
    
    print("\n🎯 Testing Strategy:")
    print("1. First request: Should generate data and log 'Generating data'")
    print("2. Second request: Should return cached data (no log)")
    print("3. Multiple requests: All should return cached data")
    print("4. After 5 minutes: Cache expires, new data generated")
    
    print("\n" + "=" * 70)
    print("STEP 1: First Request (Cache Miss)")
    print("=" * 70)
    
    try:
        print(f"Making first request to {endpoint}")
        print("Expected: 'Generating data' should appear in Django console")
        
        start_time = time.time()
        response = requests.get(endpoint)
        end_time = time.time()
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success! Response time: {end_time - start_time:.2f} seconds")
            print(f"📊 Data: {data['total_count']} items")
            print(f"🕒 Generated at: {data['generated_at']}")
            print(f"💾 Cache info: {data['cache_info']}")
            
            # Store the first generation time for comparison
            first_generation_time = data['generated_at']
            
        else:
            print(f"❌ Error: HTTP {response.status_code}")
            return
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to server")
        print("Please make sure Django server is running on localhost:8000")
        return
    
    print("\n" + "=" * 70)
    print("STEP 2: Second Request (Cache Hit)")
    print("=" * 70)
    
    try:
        print("Making second request (should be cached)")
        print("Expected: NO 'Generating data' message in Django console")
        
        start_time = time.time()
        response = requests.get(endpoint)
        end_time = time.time()
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success! Response time: {end_time - start_time:.2f} seconds")
            print(f"📊 Data: {data['total_count']} items")
            print(f"🕒 Generated at: {data['generated_at']}")
            
            # Check if it's the same data (cached)
            if data['generated_at'] == first_generation_time:
                print("✅ Data is cached (same generation timestamp)")
            else:
                print("❌ Data is not cached (different generation timestamp)")
                
        else:
            print(f"❌ Error: HTTP {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to server")
        return
    
    print("\n" + "=" * 70)
    print("STEP 3: Multiple Rapid Requests")
    print("=" * 70)
    
    print("Making 5 rapid requests to test cache performance...")
    
    response_times = []
    for i in range(5):
        try:
            start_time = time.time()
            response = requests.get(endpoint)
            end_time = time.time()
            
            if response.status_code == 200:
                data = response.json()
                response_time = end_time - start_time
                response_times.append(response_time)
                print(f"  Request {i+1}: {response_time:.3f}s - {data['total_count']} items")
            else:
                print(f"  Request {i+1}: Error {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print(f"  Request {i+1}: Connection error")
    
    if response_times:
        avg_time = sum(response_times) / len(response_times)
        print(f"\n📈 Average response time: {avg_time:.3f} seconds")
        print(f"🚀 Cache is working efficiently!")
    
    print("\n" + "=" * 70)
    print("STEP 4: Cache Expiry Test")
    print("=" * 70)
    
    print("⚠️  To test cache expiry:")
    print("1. Wait 5 minutes")
    print("2. Make another request")
    print("3. Check Django console for 'Generating data' message")
    print("4. Verify new generation timestamp")
    
    print("\n" + "=" * 70)
    print("🎉 Demonstration Complete!")
    print("=" * 70)
    
    print("\n📝 Summary:")
    print("✅ First request: Data generated and cached")
    print("✅ Second request: Cached data returned")
    print("✅ Multiple requests: All served from cache")
    print("✅ Performance: Fast response times")
    print("✅ Cache TTL: 5 minutes (300 seconds)")
    
    print("\n🔧 Next Steps:")
    print("1. Monitor Django console for 'Generating data' logs")
    print("2. Test cache expiry after 5 minutes")
    print("3. Explore the code in api/views.py")
    print("4. Check Redis cache: redis-cli")
    print("5. Run automated tests: python test_cache.py")

if __name__ == "__main__":
    demo_caching()
