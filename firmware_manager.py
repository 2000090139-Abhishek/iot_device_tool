from ticket_manager import create_ticket

def push_firmware(device, new_version):
    # Simulate update success/fail
    success = device['firmware'] != new_version
    if success:
        device['firmware'] = new_version
    else:
        create_ticket(device['id'], "Firmware Update Failed", "Firmware update failed", "Medium")
    return success