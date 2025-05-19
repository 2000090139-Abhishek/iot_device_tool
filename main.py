from flask import Flask, render_template, request
from device_manager import load_devices, check_device_status
from firmware_manager import push_firmware
from ticket_manager import create_ticket

app = Flask(__name__)

FIRMWARE_VERSION = "v2.0.0"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", results=None)

@app.route("/run-checks", methods=["POST"])
def run_checks():
    devices = load_devices()
    results = []

    offline = []
    for device in devices:
        status = check_device_status(device)

        if not status['online']:
            offline.append(device['id'])
            create_ticket(device['id'], "Device Offline", "Device unreachable", "High")
            results.append(f"🚫 {device['id']} is offline")
        elif status['sensor_status'] != "ok":
            create_ticket(device['id'], "Sensor Error", "Sensor malfunction detected", "Medium")
            results.append(f"⚠️ {device['id']} has sensor error")

        if device['firmware'] != FIRMWARE_VERSION:
            success = push_firmware(device, FIRMWARE_VERSION)
            if success:
                results.append(f"✅ {device['id']} firmware updated to {FIRMWARE_VERSION}")
            else:
                results.append(f"❌ Firmware update failed for {device['id']}")

    results.append(f"🟢 {len(devices) - len(offline)} / {len(devices)} devices online")

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
