from device_manager import load_devices, check_device_status
from firmware_manager import push_firmware
from ticket_manager import create_ticket

FIRMWARE_VERSION = "v2.0.0"

def main():
    print("🔧 IoT Device Management Tool")
    devices = load_devices()

    offline = []
    for device in devices:
        status = check_device_status(device)

        if not status['online']:
            offline.append(device['id'])
            create_ticket(device['id'], "Device Offline", "Device unreachable", "High")
        elif status['sensor_status'] != "ok":
            create_ticket(device['id'], "Sensor Error", "Sensor malfunction detected", "Medium")

        # Firmware check
        if device['firmware'] != FIRMWARE_VERSION:
            success = push_firmware(device, FIRMWARE_VERSION)
            print(f"Firmware update for {device['id']}: {'✅ Success' if success else '❌ Failed'}")

    print(f"🟢 Online devices: {len(devices) - len(offline)} / {len(devices)}")

if __name__ == "__main__":
    main()