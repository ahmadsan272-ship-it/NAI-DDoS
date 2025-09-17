import requests
import time

def test_simple():
    url = https://httpbin.org/get" # Website untuk testing

    print("Mengirim request ke:", url)
    start_time = time.time

    try:
        response = requests.get(url)
        end_time = time = time()
        
        latency = (end_time - start_time) * 1000 # Convert ke milliseconds
        
        print(f" Status Code: {response.status_code}")
        print (f" Waktu Response: {latency:.2f} ms")
        print(("Berhasil!")

    except Exception as e:
        print(f"Error: {e}")

# Jalankan test
test_simple()
  
