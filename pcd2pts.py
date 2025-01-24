import open3d as o3d
import typer

def convert_pcd_to_pts(input_pcd_file, output_pts_file, options=None):
    try:
        # Load the PCD file
        point_cloud = o3d.io.read_point_cloud(input_pcd_file)
        
        # Get the points and colors (if available)
        points = point_cloud.points
        colors = point_cloud.colors if point_cloud.has_colors() else None
        with open(output_pts_file, 'w') as f:
            # Write the number of points as the first line
            f.write(f"{len(points)}\n")
            
            # Write each point in the format: X Y Z Intensity R G B
            for i, point in enumerate(points):
                x, y, z = point
                if colors:
                    r, g, b = [int(c * 255) for c in colors[i]]
                    f.write(f"{x} {y} {z} 255 {r} {g} {b}\n")  # Intensity is set to 0
                else:
                    f.write(f"{x} {y} {z} 255 255 255 255\n")  # Default white color
                
        print(f"Successfully converted {input_pcd_file} to {output_pts_file}")
    except Exception as e:
        print(f"Error: {e}")

def main(input: str, output: str):
    convert_pcd_to_pts(input, output)

if __name__ == "__main__":
    typer.run(main)