import argparse
import os

from Adafruit_IO import Client
from dotenv import load_dotenv

parser = argparse.ArgumentParser(description="Bakubear message sender")
parser.add_argument("--message", type=str, required=True, help="Message to send")
args = parser.parse_args()

load_dotenv()

username = os.getenv('ADAFRUIT_IO_USERNAME')
key = os.getenv('ADAFRUIT_IO_KEY')

aio = Client(username, key)

# message = "TESTING NEW MESSAGE DORK"
message = args.message
aio.send_data('bakubear-messages', message)
print(f"Sent message: {message}")