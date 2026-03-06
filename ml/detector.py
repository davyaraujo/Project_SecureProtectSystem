import cv2
import requests
import os
from ultralytics import YOLO
import time


API_URL = os.getenv("API_URL", "http://localhost:8000")
VIDEO_PATH = os.getenv("VIDEO_PATH", "video/13384448_1920_1080_30fps.mp4")
model = YOLO("yolov8n.pt")
INT = 3 

def send_event(label,confidence,is_alert):
    try:
        requests.post(f"{API_URL}/events/", 
            json={
            "object_detect" : label,
            "confidence" : round(confidence,2),
            "is_alert" : is_alert
            }
        )
    except:
        print("ERROR")

def run():
    video = cv2.VideoCapture(VIDEO_PATH)
    if not video.isOpened():
        print("Erro ao abrir o vídeo")
        return

    while True:
        ret , frame = video.read()

        temp_atual = time.time()
        tempo_final = time.time()

        while temp_atual < tempo_final + INT:
            temp_atual = time.time()
            



        results = model(frame,verbose=False)



        for result in results:
            is_alert = False
            for box in result.boxes:
                label = model.names[int(box.cls)]
                confidence = float(box.conf)
                if confidence > 0.86:
                    if label == "person":
                        is_alert = True
                    print(f"It was detect {label} ({confidence})")
                    send_event(label,confidence,is_alert)
    
        video.release()



if __name__ == "__main__":
    run()