import cv2
import os
import shutil

input_folder = "Task 2 - Change Detection Algorithm\input-images"
output_folder = "task_2_output"
os.makedirs(output_folder, exist_ok=True)

before_images = [f for f in os.listdir(input_folder) if f.endswith(".jpg") and "~2" not in f]

for before_file in before_images:
    before_path = os.path.join(input_folder, before_file)
    after_file = before_file.replace(".jpg", "~2.jpg")
    after_path = os.path.join(input_folder, after_file)

    # Copy the before image into output folder (as required)
    shutil.copy(before_path, os.path.join(output_folder, before_file))

    if not os.path.exists(after_path):
        print(f"⚠ After image missing for: {before_file}")
        continue

    before = cv2.imread(before_path)
    after = cv2.imread(after_path)

    diff = cv2.absdiff(before, after)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) > 50:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(after, (x, y), (x + w, y + h), (0, 0, 255), 3)

    output_annotated = before_file.replace(".jpg", "~3.jpg")
    output_path = os.path.join(output_folder, output_annotated)
    cv2.imwrite(output_path, after)

    print(f"✔ Output saved: {output_annotated}")

print(" Task 2 Completed!")
