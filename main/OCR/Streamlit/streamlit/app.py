import streamlit as st
import cv2
from PIL import Image
import os

st.title("OCR Application with Frame Capture")

# Create a directory to save frames if it doesn't exist
save_dir = "captured_frames"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Start video capture using OpenCV
video_capture = cv2.VideoCapture(0)  # 0 is the default camera

# Initialize frame counter
frame_counter = 0
captured_frames = 0  # Count how many frames we have saved

# Capture frame-by-frame
while True:
    ret, frame = video_capture.read()  # Read the frame
    if not ret:
        st.write("Failed to capture frame")
        break

    # Check if the frame is the 10th frame
    if frame_counter % 60 == 0:  # Every 10th frame
        # Convert the frame (BGR format) to RGB for Streamlit display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame in Streamlit app
        st.image(frame_rgb, caption=f"Captured Frame {captured_frames}", use_column_width=True)

        # Convert the frame to PIL image
        pil_image = Image.fromarray(frame_rgb)

        # Save the frame as an image
        save_path = os.path.join(save_dir, f"frame_{captured_frames}.png")
        pil_image.save(save_path)

        st.write(f"Captured Frame {captured_frames} saved as {save_path}")
        captured_frames += 1  # Increment captured frames counter

    # Increment the total frame counter
    frame_counter += 1

    # Stop after capturing 10 frames for example (you can adjust this)
    if captured_frames >= 10:  # Stop after 10 captured frames
        break

# Release the capture when done
video_capture.release()
cv2.destroyAllWindows()
