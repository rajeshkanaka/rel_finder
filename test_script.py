#!/usr/bin/env python3
"""
Simple test script to validate the Ezekia API connection and basic functionality
"""

import requests
import json

def test_api_connection():
    """Test basic API connection"""
    API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiOGM4ZGM4N2JhNGM2NWNkM2RmMWY3NTY0ZmU3OTRkNDdlZTEyMDkzNDdlYjEyNjVlMmI3N2QwNzkzNzY4MmMxN2NiZGZkZGIxZTU0NjVmNDciLCJpYXQiOjE3NTM5NDI4MTMuNjIxNTMzLCJuYmYiOjE3NTM5NDI4MTMuNjIxNTM3LCJleHAiOjE3NTY1MzQ4MTMuNjEyNTY3LCJzdWIiOiIxOTc1ODgzIiwic2NvcGVzIjpbXX0.1-ZqgbGCpjEmrCii_O4SK-UsdmXvkcSTrwXUzLxpvrbXnbSWBVTsmeP5k4i6LRpEQJ4kgXCf8C7GpYfIJAJFs8-W8HIBRze11u42LiDA0EBn7PasH8ZGTEc4RzEyl7aDMblwGYQxO-uNDmbEMV4LaDiwHScdR2r084903FjxoA8omcevSRUqk26EpR45lE--tYkyjtHfHCbhAw7daXXzDf4xm0MWWhJXsP8dV_dwhHZKH5YzK2kpVOdxi9L98zyDT-6PazpjaWioe6u65yPssiJ9E2Lvm7P_sRgUGurCvqjB5JUFIefJte9JCn1lPOPPJRmpRBfZFAI0zniS3sVdjAXOR14pqW2VOfk4nqOjg8TazY0_mzNLWozFpzSm3G9c41s7PK2P8TrDCvsuGDNuL34RIuOgqxVX8SKHZD8Ef5VrP3KmeC2XBVoxSjX6zHNWtjlbAh5lg3Gcwe8P3CCuJdr3MS2-sA570umzGxUT7OJ-A76kulXHD4xTczYOb2_PwwaEr7jernx6HuTzhXjLtLuamhDo-JWNtyHQL47h2jyv41hjTvu3jbeV10Qs2_capc-qLDrSmhWHAEjSu-kAFKehw1X16uBIkdj5fdxmUZ6ayLUvx-hz1QuymowRpzbUHYErpYKj80Y1_uARvBDqMxMDbSfBFBQl1LrDqtQbqtw"
    BASE_URL = "https://ezekia.com/api"
    
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    print("Testing API connection...")
    
    # Test endpoints
    test_endpoints = [
        '/companies',
        '/projects',
        '/people'
    ]
    
    for endpoint in test_endpoints:
        try:
            url = f"{BASE_URL}{endpoint}"
            print(f"Testing {endpoint}...")
            
            response = requests.get(url, headers=headers, timeout=10)
            
            print(f"  Status: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    if isinstance(data, list):
                        print(f"  Records: {len(data)}")
                    elif isinstance(data, dict):
                        if 'data' in data:
                            print(f"  Records: {len(data['data'])}")
                        else:
                            print(f"  Response: {type(data)}")
                    print("  ✅ Success")
                except json.JSONDecodeError:
                    print("  ❌ Invalid JSON response")
            else:
                print(f"  ❌ Error: {response.text[:100]}")
                
        except Exception as e:
            print(f"  ❌ Exception: {str(e)}")
        
        print()

if __name__ == "__main__":
    test_api_connection()

