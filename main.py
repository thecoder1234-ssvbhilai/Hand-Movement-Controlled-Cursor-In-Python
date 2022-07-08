import cv2
import mediapipe as mp
import pyautogui
import webbrowser as wb
import time as t
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
                    pyautogui.moveTo(thumb_x, thumb_y)
                if id == 8:
                    # drawing_utils.draw_landmarks(frame, hand)
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    if abs(index_y - thumb_y) < 40:
                        pyautogui.click()
                        pyautogui.sleep(1)
                # if id == 12:
                #     cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                #     middle_x = screen_width/frame_width*x
                #     middle_y = screen_height/frame_height*y
                #     print(middle_x - index_x, middle_y)
                #     if (middle_x - index_x) < 70 and middle_y < 400:
                #         wb.open('youtube.com')
                #         t.sleep(8)

                        


    cv2.imshow('Virtueal Mouse', frame)
    cv2.waitKey(1)