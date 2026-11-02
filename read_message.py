import os

from Adafruit_IO import Client
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('ADAFRUIT_IO_USERNAME')
key = os.getenv('ADAFRUIT_IO_KEY')

aio = Client(username, key)

data = aio.receive('bakubear-messages')
print(f"Received message: {data.value}")