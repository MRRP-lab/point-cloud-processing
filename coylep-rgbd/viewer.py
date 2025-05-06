import open3d as o3d
import numpy as np
from pathlib import Path

point_cloud = Path("frames/pointcloud_2009.ply")

print("Load a ply point cloud, print it, and render it")
ply_point_cloud = o3d.data.PLYPointCloud()
pcd = o3d.io.read_point_cloud(point_cloud)
print(pcd)
print(np.asarray(pcd.points))
vis = o3d.visualization.Visualizer()
vis.create_window()
vis.get_render_option().background_color = [0.8, 0.8, 0.8]
vis.add_geometry(pcd)
vis.run()
vis.destroy_window()