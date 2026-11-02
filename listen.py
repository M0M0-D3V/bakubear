import os
import time

from Adafruit_IO import Client
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('ADAFRUIT_IO_USERNAME')
key = os.getenv('ADAFRUIT_IO_KEY')

aio = Client(username, key)

last_id = None

while True:
    data = aio.receive('bakubear-messages')
    if data.id != last_id:
        print(f"Bakubear says: {data.value}")
        last_id = data.id

    time.sleep(10)
