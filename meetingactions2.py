import os
import settings
import json
from pyzoom import ZoomClient

client = ZoomClient.from_environment()

print(client.raw.get_all_pages('/metrics/meetings/71054596550/participants'))
