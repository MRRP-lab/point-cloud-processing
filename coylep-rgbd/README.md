
# Setup

- Install Python 3.10
- Run the following to setup and enter the virtual environment
```
py -3.10 -m venv venv
venv\Scripts\activate
```
- Pip install the required packages
```
pip install -r requirements.txt
```
# vizualizer.py
Takes the video stream from the camera and converts each frame into a point cloud for live viewing.
Modified from the depthAI's example code, you can press 's' to save a given frame.
The frame is saved both as a .png image and a .ply point cloud.

# viewer.py
Loads and displays the .ply point clouds.
To use, edit the path and add your file name
```
point_cloud = Path("frames/pointcloud_2009.ply")
```
The background color can be changed to make certain points more visible
```
vis.get_render_option().background_color = [0.8, 0.8, 0.8] # Grey
```