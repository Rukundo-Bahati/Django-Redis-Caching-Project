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
