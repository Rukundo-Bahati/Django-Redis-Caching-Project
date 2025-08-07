#!/usr/bin/env python3
"""
Setup script for Django Redis Caching Project
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_redis():
    """Check if Redis is running."""
    try:
        import redis
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.ping()
        print("✓ Redis is running")
        return True
    except Exception as e:
        print(f"✗ Redis is not running: {e}")
        print("Please start Redis server before running the application")
        return False

def main():
    """Main setup function."""
    print("=" * 60)
    print("Django Redis Caching Project Setup")
    print("=" * 60)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("✗ Python 3.8 or higher is required")
        return False
    
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        return False
    
    # Check Redis
    if not check_redis():
        print("\nTo start Redis:")
        if platform.system() == "Windows":
            print("  - Install Redis for Windows or use WSL")
            print("  - Or use Docker: docker run -d -p 6379:6379 redis")
        elif platform.system() == "Darwin":  # macOS
            print("  - brew install redis && redis-server")
        else:  # Linux
            print("  - sudo systemctl start redis")
        return False
    
    # Run Django migrations
    if not run_command("python manage.py migrate", "Running Django migrations"):
        return False
    
    print("\n" + "=" * 60)
    print("Setup completed successfully!")
    print("=" * 60)
    print("\nTo run the application:")
    print("1. Start the Django server: python manage.py runserver")
    print("2. Test the API: GET http://localhost:8000/api/data/")
    print("3. Run the test script: python test_cache.py")
    print("\nExpected behavior:")
    print("- First request: 'Generating data' appears in console")
    print("- Subsequent requests: No 'Generating data' message")
    print("- After 5 minutes: Cache expires, new data generated")
    
    return True

if __name__ == "__main__":
    main()
