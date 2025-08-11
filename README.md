# Django Redis Caching Project

## Description
Django project with Redis caching for improved data retrieval performance.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Start Redis server
3. Run: `python manage.py runserver`
4. Test: `GET /api/data/`

## Features
- Redis caching with 5-minute TTL
- Large JSON response generation
- Console logging for cache verification

# Quick Start Guide - Django Redis Caching Project

## 🚀 Get Started in 5 Minutes

### Prerequisites
- Python 3.8+
- Redis server

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start Redis Server
**Windows:**
```bash
# Option 1: Using Docker
docker run -d -p 6379:6379 redis

# Option 2: Install Redis for Windows
# Download from https://github.com/microsoftarchive/redis/releases
```

**macOS:**
```bash
brew install redis
redis-server
```

**Linux:**
```bash
sudo systemctl start redis
```

### Step 3: Run Django Setup
```bash
python manage.py migrate
```

### Step 4: Start the Server
```bash
python manage.py runserver
```

### Step 5: Test the API
Open your browser or use curl:
```bash
curl http://localhost:8000/api/data/
```

### Step 6: Verify Caching
1. **First request**: Check Django console for "Generating data" message
2. **Second request**: No "Generating data" message should appear
3. **After 5 minutes**: Cache expires, new data generated

## 🧪 Automated Testing

### Run the Demo Script
```bash
python demo.py
```

### Run the Test Script
```bash
python test_cache.py
```

## 📊 Expected Results

### First Request
- Console shows: "Generating data"
- Response time: ~1-2 seconds
- Cache info: `"cached": false`

### Subsequent Requests (within 5 minutes)
- Console: No "Generating data" message
- Response time: ~0.1 seconds
- Cache info: `"cached": true`

### After 5 Minutes
- Console shows: "Generating data" again
- New data generated with different timestamp

## 🔧 Troubleshooting

### Redis Connection Error
```bash
# Check if Redis is running
redis-cli ping
# Should return: PONG
```

### Django Server Error
```bash
# Check if port 8000 is available
netstat -an | grep 8000
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 📁 Project Files

- `api/views.py` - Main caching logic
- `cache_project/settings.py` - Redis configuration
- `test_cache.py` - Automated testing
- `demo.py` - Interactive demonstration
- `setup.py` - Automated setup script

## 🎯 Key Features Demonstrated

✅ **Redis Caching** with 5-minute TTL  
✅ **Large JSON Response** (1000 items)  
✅ **Console Logging** for cache verification  
✅ **Performance Improvement** (cached vs uncached)  
✅ **Automatic Cache Expiry** after 5 minutes  

## 📈 Performance Comparison

| Request Type | Response Time | Console Log |
|-------------|---------------|-------------|
| First (Cache Miss) | ~1-2 seconds | "Generating data" |
| Subsequent (Cache Hit) | ~0.1 seconds | No log |
| After Expiry | ~1-2 seconds | "Generating data" |

---

**Ready to test!** 🚀




# Release Notes - Django Redis Caching Project

## Version 1.0.0 - Initial Release

### 🎯 Project Overview
This project demonstrates the implementation of a caching module using Redis to improve the performance of data retrieval in a Django application. The solution showcases best practices for implementing caching strategies in web applications.

### ✨ Features Implemented

#### Core Functionality
- **Django REST API** with a single endpoint `GET /api/data/`
- **Redis Caching** with 5-minute TTL (Time To Live)
- **Large JSON Response Generation** (1000 items per response)
- **Console Logging** for cache verification
- **Cache Hit/Miss Detection** with detailed response metadata

#### Technical Implementation
- **Django 4.2.7** as the web framework
- **Redis 5.0.1** for in-memory caching
- **django-redis 5.4.0** for seamless Redis integration
- **SQLite** database for Django ORM
- **JSON Response** with comprehensive data structure

### 🔧 API Endpoint Details

#### `GET /api/data/`
**Purpose**: Returns a large JSON response with intelligent caching

**Response Structure**:
```json
{
  "data": [
    {
      "id": 1,
      "name": "Item 1",
      "description": "Description for item 1",
      "timestamp": "2024-01-01T00:00:00Z",
      "category": "Category 1",
      "value": 1.5,
      "active": false,
      "tags": ["tag1", "tag2"],
      "metadata": {
        "created_at": "2024-01-01T00:00:00Z",
        "version": "1.0",
        "priority": 1
      }
    }
    // ... 999 more items
  ],
  "total_count": 1000,
  "generated_at": "2024-01-01T00:00:00Z",
  "cache_info": {
    "cached": false,
    "cache_key": "api_data_response",
    "ttl_seconds": 300
  }
}
```

### 🚀 Caching Behavior

#### Cache Strategy
- **Cache Key**: `api_data_response`
- **TTL**: 300 seconds (5 minutes)
- **Storage**: Redis in-memory cache
- **Backend**: django-redis with Redis client

#### Expected Behavior
1. **First Request**: 
   - Generates new data
   - Logs "Generating data" to console
   - Caches response for 5 minutes
   - Returns fresh data

2. **Subsequent Requests** (within 5 minutes):
   - Retrieves cached data
   - No "Generating data" log
   - Faster response time
   - Same data as first request

3. **After Cache Expiry** (5+ minutes):
   - Cache expires automatically
   - Generates new data
   - Logs "Generating data" again
   - Caches new response

### 📁 Project Structure
```
Task2/
├── requirements.txt          # Python dependencies
├── README.md               # Project documentation
├── manage.py               # Django management script
├── setup.py                # Automated setup script
├── test_cache.py           # Caching verification script
├── RELEASE_NOTES.md        # This file
├── cache_project/          # Django project settings
│   ├── __init__.py
│   ├── settings.py         # Redis cache configuration
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI configuration
└── api/                   # API application
    ├── __init__.py
    ├── views.py           # Caching logic implementation
    └── urls.py            # API endpoint routing
```

### 🛠️ Installation & Setup

#### Prerequisites
- Python 3.8 or higher
- Redis server running locally

#### Quick Start
```bash
# 1. Clone repository
git clone <repository-url>
cd Task2

# 2. Run automated setup
python setup.py

# 3. Start Django server
python manage.py runserver

# 4. Test the API
curl http://localhost:8000/api/data/

# 5. Run verification tests
python test_cache.py
```

#### Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Start Redis server
redis-server

# Run Django migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

### 🧪 Testing & Verification

#### Manual Testing
1. **First Request**: Call `GET /api/data/` and check Django console for "Generating data" log
2. **Subsequent Requests**: Call the same endpoint multiple times within 5 minutes
3. **Cache Verification**: Confirm no "Generating data" logs appear for cached requests
4. **Expiry Testing**: Wait 5+ minutes and verify new data generation

#### Automated Testing
```bash
python test_cache.py
```
This script performs:
- Initial request verification
- Cache hit testing
- Multiple rapid request testing
- Response validation

### 🔍 Technical Details

#### Redis Configuration
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'TIMEOUT': 300,  # 5 minutes
    }
}
```

#### Caching Logic
```python
# Cache key for API responses
cache_key = 'api_data_response'

# Check cache first
cached_data = cache.get(cache_key)

if cached_data is not None:
    return JsonResponse(cached_data, safe=False)

# Generate new data if not cached
print("Generating data")
# ... data generation logic ...

# Cache for 5 minutes
cache.set(cache_key, response_data, timeout=300)
```

### 📊 Performance Benefits

#### Before Caching
- Every request generates 1000 items
- High CPU usage for data generation
- Slower response times
- Database/file system overhead

#### After Caching
- First request: Generates data once
- Subsequent requests: Instant cache retrieval
- Reduced server load
- Improved user experience
- 5-minute data freshness guarantee

### 🔒 Security Considerations
- CSRF protection disabled for API endpoints
- Redis connection limited to localhost
- No sensitive data in cache
- Proper error handling implemented

### 🚀 Future Enhancements
- Cache invalidation strategies
- Multiple cache keys for different data types
- Cache warming mechanisms
- Monitoring and metrics
- Distributed caching support

### 📝 Development Notes
- **Framework**: Django 4.2.7
- **Cache Backend**: Redis with django-redis
- **Database**: SQLite (development)
- **Python Version**: 3.8+
- **Dependencies**: See requirements.txt

### 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### 📄 License
MIT License - See LICENSE file for details

---

**Release Date**: January 2024  
**Version**: 1.0.0  
**Status**: Production Ready  
**Maintainer**: Development Team
