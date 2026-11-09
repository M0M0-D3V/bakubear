import argparse
import os
import time

from Adafruit_IO import Client
from dotenv import load_dotenv

parser = argparse.ArgumentParser(description="Bakubear message listener")
parser.add_argument("--unmuted", action="store_true", help="Allow message output")
args = parser.parse_args()

load_dotenv()

username = os.getenv('ADAFRUIT_IO_USERNAME')
key = os.getenv('ADAFRUIT_IO_KEY')

aio = Client(username, key)

last_id = None
muted = not args.unmuted

try:
    while True:
        data = aio.receive('bakubear-messages')
        if data.id != last_id:
            if not muted:
                print(f"Bakubear says: {data.value}")
            else:
                print("[Muted] Message received")
            last_id = data.id

        time.sleep(10)
except KeyboardInterrupt:
    print("\nBakubear listener stopped.")