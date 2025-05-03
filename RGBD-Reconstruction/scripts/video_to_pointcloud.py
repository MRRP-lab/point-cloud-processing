import numpy as np
import cv2 as cv

# * Steps for project 
# * 1. **Extract synchronized color and depth frames** from the videos.

# Load the color and depth videos
color_cap = cv.VideoCapture('../RGBD-Reconstruction/6-14442C1091CCC4D600/CAM_A_bitstream.mp4')
depth_cap = cv.VideoCapture('../RGBD-Reconstruction/6-14442C1091CCC4D600/7_depth.avi')

# Check if both videos opened successfully
if not color_cap.isOpened() or not depth_cap.isOpened():
    print("Error: Couldn't open video files.")
    exit()

while True:
    # Read color and depth frames
    ret_color, color_frame = color_cap.read()
    ret_depth, depth_frame = depth_cap.read()

    # Check if the frames were read correctly
    if not ret_color or not ret_depth:
        print("Error: Couldn't receive frame (stream end?). Exiting...")
        break

    # Convert depth frame to grayscale (helps see depth)
    gray_depth = cv.cvtColor(depth_frame, cv.COLOR_BGR2GRAY)

    # Normalize depth values for better visualization 
    gray_normalized = cv.normalize(gray_depth, None, 0, 255, cv.NORM_MINMAX)

    # Apply color map to the normalized depth
    depth_colormap = cv.applyColorMap(gray_normalized, cv.COLORMAP_VIRIDIS)

    # Resize depth_colormap to match color_frame size 
    depth_colormap_resized = cv.resize(depth_colormap, (color_frame.shape[1], color_frame.shape[0]))

    # Synchronize the display both color and depth frames side by side
    combined_frame = np.hstack((color_frame, depth_colormap_resized))

    # Show the synchronized frames
    cv.imshow('Synchronized Color and Depth', combined_frame)

    # Break loop if 'q' is pressed
    if cv.waitKey(30) & 0xFF == ord('q'):
        break

# Release the video capture objects
color_cap.release()
depth_cap.release()

cv.destroyAllWindows()


    
# 2. **Use calibration data (`calib.json`)** to correctly map depth and color.
    
# 3. **Create a single colored 3D point cloud** from a color + depth frame pair.
    
# 4. **Visualize the point cloud** using **Open3D**.
    
# 5. **Check if the result looks correct** (good shape, no distortion).
   
# 6. **Prepare to scale it up** into processing whole videos automatically.