import psutil
import time

def monitor_bandwidth(interval=5):
    while True:
        counters = psutil.net_io_counters()
        print(f"Bytes Sent: {counters.bytes_sent / (1024 ** 2):.2f} MB, Bytes Received: {counters.bytes_recv / (1024 ** 2):.2f} MB")
        time.sleep(interval)

if __name__ == "__main__":
    monitor_bandwidth()
