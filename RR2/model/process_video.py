import cv2
import json
import requests
import time
import os
import random
from pathlib import Path

# Config
API_URL = "http://127.0.0.1:3000/api/violations"
TEMP_DIR = Path("_temp_clips")
TEMP_DIR.mkdir(exist_ok=True)

def process_video(video_path):
    print(f"[Model] Starting processing on: {video_path}")
    
    # 1. Simulate reading the video and detecting objects
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video {video_path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0: fps = 30.0

    print(f"[Model] Extracting 3-second violation clip...")
    # Read first frame for the image evidence
    ret, first_frame = cap.read()
    if not ret: return
    
    evidence_img_path = str(TEMP_DIR / "evidence.jpg")
    cv2.imwrite(evidence_img_path, first_frame)

    # Note: In a real scenario, you'd run YOLO/EasyOCR here on the frames.
    # We simulate a "NO_HELMET" violation being found.
    plate_number = f"UP{random.randint(10, 99)}AB{random.randint(1000, 9999)}"
    
    print(f"[Model] Violation detected: NO HELMET. Plate: {plate_number}")
    print("[Model] Pushing payload to Central Dashboard...")
    
    # Prepare JSON payload mirroring demo_data.json schema
    payload_data = {
        "id": f"RRK-2026-{random.randint(10000, 99999)}",
        "plate": plate_number,
        "camera": "CAM-01",
        "location": "Round-about",
        "city": "Greater Noida",
        "type": "NO_HELMET",
        "label": "No Helmet",
        "severity": "red",
        "fine": 1000,
        "section": "Section 129 r/w 194D",
        "vehicle": "Two Wheeler",
        "confidence": 0.94,
        "sourceVideo": os.path.basename(video_path)
    }

    # Post to Node.js API via multipart/form-data
    with open(evidence_img_path, 'rb') as f:
        files = {
            'media': ('evidence.jpg', f, 'image/jpeg')
        }
        data = {
            'payload': json.dumps(payload_data)
        }
        
        try:
            response = requests.post(API_URL, files=files, data=data)
            print(f"[Model] Dashboard response: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"[Model] Failed to connect to dashboard: {e}")

    cap.release()
    print("[Model] Done.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python process_video.py <path_to_video.mp4>")
    else:
        process_video(sys.argv[1])
