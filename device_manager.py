import json
import random

def load_devices(file='devices.json'):
    with open(file) as f:
        return json.load(f)

def ping_device(ip):
    # Simulated ping (random offline)
    return random.choice([True, True, True, False])  # Mostly online

def check_device_status(device):
    online = ping_device(device['ip'])
    return {'id': device['id'], 'online': online, 'sensor_status': device['sensor_status']}