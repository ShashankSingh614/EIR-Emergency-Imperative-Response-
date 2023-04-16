import cv2  #importing cv2 module

# Set up video capture device
cap = cv2.VideoCapture(0)

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Video_Output.mp4', fourcc, 25.0, (640, 480))

# Record video for 15 seconds
duration = 15  # seconds
start_time = cv2.getTickCount()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Write frame to output video
    out.write(frame)
    # Check if recording time has reached the desired duration
    elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
    if elapsed_time >= duration:
        break

# Release video capture device and video writer
cap.release()
out.release()
cv2.destroyAllWindows()
