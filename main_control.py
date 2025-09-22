from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import sys 
import os
import screen_brightness_control as sbc
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks import python as mp_tasks
from smarthomegui import SmartHomeGUI

import time
import tkinter as tk
import threading

import pyautogui
class GestureRecognition:
    def __init__(self, model_path):
        # Path to the gesture recognition model
        self.model_path = model_path

        # Initialize MediaPipe Gesture Recognizer
        base_options = mp_tasks.BaseOptions(model_asset_path=self.model_path)
        options = vision.GestureRecognizerOptions(base_options=base_options)
        self.recognizer = vision.GestureRecognizer.create_from_options(options)

        # Start capturing from webcam
        self.cap = cv2.VideoCapture(0)
        print("Running... Press 'q' to quit.")

    def control_volume(self, gesture_name):
        """Control system volume based on gesture."""
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, 1, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)

        if gesture_name == "Pointing_Up":
            current_volume = volume.GetMasterVolumeLevelScalar()
            volume.SetMasterVolumeLevelScalar(min(current_volume + 0.1, 1.0), None)
        elif gesture_name == "Closed_Fist":
            current_volume = volume.GetMasterVolumeLevelScalar()
            volume.SetMasterVolumeLevelScalar(max(current_volume - 0.1, 0.0), None)

    def control_brightness(self, gesture_name):
        """Control screen brightness based on gesture."""
        current_brightness = sbc.get_brightness()

        if gesture_name == "Thumb_Up":
            new_brightness = min(current_brightness[0] + 10, 100) 
            
            print(current_brightness) # Max brightness 100%
            sbc.set_brightness(new_brightness)
        elif gesture_name == "Thumb_Down":
          
            new_brightness = max(current_brightness[0] - 10, 0)  # Min brightness 0%
            sbc.set_brightness(new_brightness)
    def gesture_overlay(self,gesture_image_path):
         # Capture the live feed from the camera (use 0 for default camera)
        cap = cv2.VideoCapture(0)

        # Load the gesture image (check if it has an alpha channel)
        gesture_img = cv2.imread(gesture_image_path, cv2.IMREAD_UNCHANGED)  # Include alpha channel if available
        
        # Check if gesture image has an alpha channel
        if gesture_img.shape[2] == 4:
            has_alpha = True
            gesture_rgb = gesture_img[:, :, :3]  # RGB channels
            gesture_alpha = gesture_img[:, :, 3]  # Alpha channel
        else:
            has_alpha = False
            gesture_rgb = gesture_img  # Only RGB channels
            gesture_alpha = None  # No alpha channel

        # Resize the gesture image to a fixed size (100x100)
        gesture_img_resized = cv2.resize(gesture_rgb, (100, 100))  # Resize gesture image to 100x100 pixels

        # If alpha channel exists, resize it as well
        if has_alpha:
            gesture_alpha_resized = cv2.resize(gesture_alpha, (100, 100))
        
        # Get the dimensions of the resized gesture image
        gesture_height, gesture_width = gesture_img_resized.shape[:2]

        while True:
            # Read the live feed frame
            ret, frame = cap.read()
            
            if not ret:
                print("Failed to grab frame.")
                break
            
            # Overlay the gesture image on the live feed at a specified position (e.g., top-left corner)
            x_offset, y_offset = 50, 50  # Position of the gesture image on the frame
            
            # Ensure the gesture image fits within the frame dimensions
            if x_offset + gesture_width > frame.shape[1] or y_offset + gesture_height > frame.shape[0]:
                print("Gesture image too large for the frame!")
                break
            
            # Get the region of interest (ROI) from the frame where the gesture image will be placed
            roi = frame[y_offset:y_offset+gesture_height, x_offset:x_offset+gesture_width]

            if has_alpha:
                # Alpha blending if the gesture image has an alpha channel
                for c in range(0, 3):  # Iterate over RGB channels
                    roi[:, :, c] = roi[:, :, c] * (1 - gesture_alpha_resized / 255.0) + gesture_img_resized[:, :, c] * (gesture_alpha_resized / 255.0)
            else:
                # If no alpha channel, simply overlay the RGB gesture image
                roi[:, :, :] = gesture_img_resized[:, :, :]

            # Show the frame with the gesture image
            cv2.imshow("Live Feed with Gesture", frame)

            # Exit condition
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
                break

        # Release the camera and close all windows
        cap.release()
        cv2.destroyAllWindows()
       
    def recognize_gesture(self):
        """Recognize gesture and return gesture name and confidence."""
        success, frame = self.cap.read()
        

        if not success:
            print("Skipping empty frame...")
            return None, None

        # Flip and convert BGR to RGB
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Wrap in MediaPipe Image format
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        # Run recognition
        result = self.recognizer.recognize(mp_image)

        # Extract top gesture result (if any)
        if result.gestures:
            top_gesture = result.gestures[0][0]
            gesture_name = top_gesture.category_name
            confidence = top_gesture.score
            return gesture_name, confidence
        return None, None
    
    def close(self):
        """Release the webcam and close the OpenCV window."""
        self.cap.release()
        cv2.destroyAllWindows()
    
if __name__ == "__main__":
    def run_gesture_loop():
        current_brightness = sbc.get_brightness()
        print(f"Current Brightness: {current_brightness}")
        

        while True:
            gesture_name, confidence = gesture_recognition.recognize_gesture()

            if gesture_name:
                print(f"Gesture recognized: Yo-Yo with confidence {confidence:.2f}" if gesture_name == "ILoveYou" else f"Gesture recognized: {gesture_name} with confidence {confidence:.2f}")

                if  gesture_name == "Thumb_Up":
                    gui.gesture_thumb_up()  # Turns Bulb ON
                elif gesture_name == "Thumb_Down":
                    gui.gesture_thumb_down()  # Turns Bulb OFF

                elif gesture_name == "Closed_Fist":
                    gui.gesture_closed_fist()  # Turns Fan ON

                elif gesture_name == "Open_Palm":
                    gui.gesture_open_palm()  # Turns Fan OFF

                elif gesture_name == "Victory":
                    gui.gesture_victory()  # Turns Music ON

                elif gesture_name == "Pointing_Up":
                    gui.gesture_iloveyou()  # Turns Music OFF

            # Display the webcam feed
            cv2.imshow("Gesture Recognition", cv2.flip(gesture_recognition.cap.read()[1], 1))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        gesture_recognition.close()
    root = tk.Tk()
    gui = SmartHomeGUI(root)

    MODEL_PATH = r"C:\baddeep\Python-codes\mini_project\main_part\activity_based_on_gesture\ui\main work\gesture_recognizer.task"
    gesture_recognition = GestureRecognition(MODEL_PATH)

    # Start gesture recognition in a separate thread
    gesture_thread = threading.Thread(target=run_gesture_loop)
    gesture_thread.daemon = True
    gesture_thread.start()

    # Start the Tkinter main loop (non-blocking now)
    root.mainloop()