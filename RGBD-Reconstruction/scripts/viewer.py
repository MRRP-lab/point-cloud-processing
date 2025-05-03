# Use this to open a point cloud and view it

import laspy
import open3d as o3d
import numpy as np

# load tbe LAS file using laspy
las_file = laspy.read('RGBD-Reconstruction/data/raw/forest.las')

# extract XYZ coordinates from the LAS file 
points = np.vstack((las_file.x, las_file.y, las_file.z,)).transpose()

# create a PointCloud object for Open3D
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)

# Visualize the point cloud
o3d.visualization.draw_geometries([point_cloud])

