#!/usr/bin/env python3
"""
Test script to verify Redis caching functionality.
This script makes multiple requests to the API endpoint to demonstrate caching behavior.
"""

import requests
import time
import json
from datetime import datetime

def test_caching():
    """Test the caching functionality of the API endpoint."""
    base_url = "http://localhost:8000"
    endpoint = f"{base_url}/api/data/"
    
    print("=" * 60)
    print("Testing Django Redis Caching Functionality")
    print("=" * 60)
    
    # Test 1: First request (should generate data)
    print(f"\n[1] First request at {datetime.now().strftime('%H:%M:%S')}")
    print("Expected: 'Generating data' should appear in Django console")
    
    try:
        response1 = requests.get(endpoint)
        if response1.status_code == 200:
            data1 = response1.json()
            print(f"✓ Response received: {data1['total_count']} items")
            print(f"  Generated at: {data1['generated_at']}")
            print(f"  Cache info: {data1['cache_info']}")
        else:
            print(f"✗ Error: {response1.status_code}")
    except requests.exceptions.ConnectionError:
        print("✗ Error: Could not connect to server. Make sure Django is running on localhost:8000")
        return
    
    # Wait 2 seconds
    time.sleep(2)
    
    # Test 2: Second request (should return cached data)
    print(f"\n[2] Second request at {datetime.now().strftime('%H:%M:%S')}")
    print("Expected: No 'Generating data' message in Django console")
    
    try:
        response2 = requests.get(endpoint)
        if response2.status_code == 200:
            data2 = response2.json()
            print(f"✓ Response received: {data2['total_count']} items")
            print(f"  Generated at: {data2['generated_at']}")
            print(f"  Cache info: {data2['cache_info']}")
            
            # Check if it's the same data (cached)
            if data1['generated_at'] == data2['generated_at']:
                print("✓ Data is cached (same generation timestamp)")
            else:
                print("✗ Data is not cached (different generation timestamp)")
        else:
            print(f"✗ Error: {response2.status_code}")
    except requests.exceptions.ConnectionError:
        print("✗ Error: Could not connect to server")
        return
    
    # Test 3: Multiple rapid requests
    print(f"\n[3] Making 5 rapid requests at {datetime.now().strftime('%H:%M:%S')}")
    print("Expected: All should return cached data without regeneration")
    
    for i in range(3, 8):
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                data = response.json()
                print(f"  Request {i}: ✓ {data['total_count']} items, generated at {data['generated_at'][:19]}")
            else:
                print(f"  Request {i}: ✗ Error {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"  Request {i}: ✗ Connection error")
    
    print("\n" + "=" * 60)
    print("Caching Test Summary:")
    print("1. First request should show 'Generating data' in Django console")
    print("2. Subsequent requests should NOT show 'Generating data'")
    print("3. After 5 minutes, cache expires and new data is generated")
    print("=" * 60)

if __name__ == "__main__":
    test_caching()
