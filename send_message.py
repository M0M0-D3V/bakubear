import os

from Adafruit_IO import Client
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('ADAFRUIT_IO_USERNAME')
key = os.getenv('ADAFRUIT_IO_KEY')

aio = Client(username, key)

message = "TESTING NEW MESSAGE DORK"
aio.send_data('bakubear-messages', message)
print(f"Sent message: {message}")