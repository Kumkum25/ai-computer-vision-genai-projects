import cv2
import os
import shutil

# Input & output folders
input_folder = "Task 1 - RGB Thermal Overlay Algorithm\input-images"
output_folder = "task_1_output"
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith("_Z.JPG"):  # RGB image only
        base = file.replace("_Z.JPG", "")
        rgb_file = os.path.join(input_folder, file)
        thermal_file = os.path.join(input_folder, f"{base}_T.JPG")

        # Copy original RGB image to output folder (as required)
        shutil.copy(rgb_file, os.path.join(output_folder, file))

        if not os.path.exists(thermal_file):
            print(f"⚠ Thermal missing for: {file}")
            continue

        rgb = cv2.imread(rgb_file)
        thermal = cv2.imread(thermal_file)

        # Resize thermal to match RGB image resolution
        thermal_resized = cv2.resize(thermal, (rgb.shape[1], rgb.shape[0]))

        # Overlay/blend images (simple alignment)
        adjusted_thermal = cv2.addWeighted(rgb, 0.6, thermal_resized, 0.4, 0)

        output_filename = f"{base}_AT.JPG"
        output_path = os.path.join(output_folder, output_filename)
        cv2.imwrite(output_path, adjusted_thermal)

        print(f"✔ Output generated: {output_filename}")

print("✨ Task 1 Completed! Check task_1_output folder.")
