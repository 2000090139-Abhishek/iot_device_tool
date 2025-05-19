import datetime

def create_ticket(device_id, category, description, priority):
    ticket = {
        "device_id": device_id,
        "category": category,
        "description": description,
        "priority": priority,
        "timestamp": str(datetime.datetime.now())
    }
    print(f"📌 Ticket Created: {ticket}")