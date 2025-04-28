import requests
import threading

def send_requests():
    while True:
        try:
            requests.get('http://127.0.0.1:5000/')
        except:
            pass

# Launch 50 threads
threads = []
for _ in range(50):
    t = threading.Thread(target=send_requests)
    t.start()
    threads.append(t)
