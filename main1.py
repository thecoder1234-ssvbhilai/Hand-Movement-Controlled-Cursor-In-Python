import cv2
import mediapipe as mp
import time as t
import pyautogui
from pynput.keyboard import Key, Controller
import time
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 4:
                    # drawing_utils.draw_landmarks(frame, hand)
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    if thumb_x > 900:
                        time.sleep(0.5)

                        keyboard = Controller()
                        key = "a"

                        keyboard.press(key)
                        keyboard.release(key)

                if id == 8:
                    # drawing_utils.draw_landmarks(frame, hand)
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    print(index_y, thumb_x)
                    if index_y > 530:
                        time.sleep(0.5)

                        keyboard = Controller()
                        key = "b"

                        keyboard.press(key)
                        keyboard.release(key)

                if id == 12:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    middle_x = screen_width/frame_width*x
                    middle_y = screen_height/frame_height*y
                    

                if id == 16:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    ring_x = screen_width/frame_width*x
                    ring_y = screen_height/frame_height*y

                if id == 20:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    small_x = screen_width/frame_width*x
                    small_y = screen_height/frame_height*y

                        


    cv2.imshow('Virtueal Mouse', frame)
    cv2.waitKey(1)