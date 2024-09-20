import time
from models.device import Device

class NetworkManagement:
    def __init__(self, network_name, location):
        self.network_name = network_name
        self.location = location
        self.devices = []
    
    def monitor(self):
        print(f"Monitoring network: {self.network_name}")
        for device in self.devices:
            device.get_status()
            time.sleep(1)

    def add_device(self, device):
        self.devices.append(device)
        device.save_to_db()
