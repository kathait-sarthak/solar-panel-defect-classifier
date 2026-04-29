import requests
import json
import datetime

# Configuration for the central dashboard or database
API_ENDPOINT = "https://your-solar-dashboard.com/api/logs"

def send_alert_to_dashboard(label, confidence):
    """
    Sends detection data from the Jetson edge kit to a central server.
    Used for large-scale monitoring across multiple plant sectors.
    """
    payload = {
        "timestamp": str(datetime.datetime.now()),
        "sector_id": "Sector-A1",  # Hardcoded for each Jetson kit
        "defect_type": label,
        "confidence": float(confidence),
        "status": "Action Required" if label != "Clean" else "Healthy"
    }
    
    try:
        # Sending the data as a POST request[cite: 1]
        response = requests.post(API_ENDPOINT, json=payload, timeout=5)
        if response.status_status == 200:
            print(f"Successfully logged {label} detection.")
    except Exception as e:
        print(f"Connection error: {e}")