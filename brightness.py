import cv2
import numpy as np
import subprocess

def get_frame_brightness(frame):
    """ Calculate the average brightness of the frame """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    brightness = np.mean(hsv[:, :, 2])
    return brightness

def set_screen_brightness(brightness, output_name):
    """ Set the screen brightness using xrandr """
    try:
        subprocess.run(['xrandr', '--output', output_name, '--brightness', str(brightness)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error setting brightness: {e}")

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    output_name = "LVDS-1"  # Replace with your actual output name

    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        return

    brightness = get_frame_brightness(frame)
    print(f"Frame brightness: {brightness}")
    adjusted_brightness = np.interp(brightness, [0, 255], [0.1, 1.0])
    print(f"Adjusted brightness: {adjusted_brightness}")
    set_screen_brightness(adjusted_brightness, output_name)

    cap.release()

if __name__ == "__main__":
    main()
