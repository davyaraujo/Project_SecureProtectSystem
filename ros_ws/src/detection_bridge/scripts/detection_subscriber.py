#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import cv2
import base64
import numpy as np
import requests
import os
from ultralytics import YOLO
import time

API_URL = os.getenv("API_URL", "http://localhost:8000")
model = YOLO("yolov8n.pt")
INT = 0.1
last_time = 0

def send_event(label, confidence, is_alert):
    try:
        requests.post(f"{API_URL}/events/", json={
            "object_detect": label,
            "confidence": round(confidence, 2),
            "is_alert": is_alert
        })
    except Exception as e:
        rospy.logerr(f"Erro ao enviar evento: {e}")

def callback(msg):
    frame_bytes = base64.b64decode(msg.data)
    frame_array = np.frombuffer(frame_bytes, dtype=np.uint8)
    frame = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)

    results = model(frame, verbose=False)

    current_time = time.time()

    for result in results:
        for box in result.boxes:
            is_alert = False
            label = model.names[int(box.cls)]
            confidence = float(box.conf)
            if confidence > 0.86:
                if label == "person":
                    is_alert = True
                print(f"It was detect {label} ({confidence})")
                send_event(label,confidence,is_alert)

def main():
    rospy.init_node('detection_bridge', anonymous=True)
    rospy.Subscriber('/camera/frame', String, callback)
    rospy.loginfo("Detection bridge iniciado!")
    rospy.spin()

if __name__ == '__main__':
    main()