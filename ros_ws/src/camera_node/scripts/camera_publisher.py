import rospy
from std_msgs.msg import String
import cv2
import base64
import os


VIDEO_PATH = os.getenv("VIDEO_PATH", "/mnt/ssd100/ENSTA/smart-security-system/secureversion-lite/ml/video/13384448_1920_1080_30fps.mp4")
def main():
    rospy.init_node("camera_node", anonymous=True)
    pub = rospy.Publisher("camera/frame",String,queue_size=10)
    rate = rospy.Rate(30)

    video = cv2.VideoCapture(VIDEO_PATH)

    if not video.isOpened():
        rospy.logerr(f"Erro ao abrir o vídeo: {VIDEO_PATH}")
        return
    
    rospy.loginfo("Camera Begins")

    while not rospy.is_shutdown():
        ret , frame = video.read()
        if not ret:
            rospy.loginfo("Vídeo finalizado")
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break

        _, buffer = cv2.imencode('.jpg', frame)
        frame_b64 = base64.b64encode(buffer).decode('utf-8')
        pub.publish(frame_b64)
        rate.sleep()

    video.release()

if __name__ == '__main__':
    main()
