import cv2
import numpy as np

PNG_PATH = r"benussy.png"   #replace with your png path 
OUTPUT_VIDEO = "bouncing_face_png.mp4"

SCREEN_W, SCREEN_H = 1280, 720
BOX_W, BOX_H = 260, 260
FPS = 60
DURATION = 30
FORCE_CORNER_HIT = True

img = cv2.imread(PNG_PATH, cv2.IMREAD_UNCHANGED)

if img is None:
    raise Exception("Could not load PNG. Check the path!")

if img.shape[2] != 4:
    raise Exception("PNG does not have transparency (alpha channel).")

img = cv2.resize(img, (BOX_W, BOX_H))

bgr = img[:, :, :3]
alpha = img[:, :, 3] / 255.0  

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, FPS, (SCREEN_W, SCREEN_H))

x, y = 100, 200
dx, dy = 5, 4
total_frames = FPS * DURATION
corner_hit = False

for frame_idx in range(total_frames):
    frame = np.zeros((SCREEN_H, SCREEN_W, 3), dtype=np.uint8)

    x += dx
    y += dy

    hit_h = hit_v = False

    if x <= 0 or x + BOX_W >= SCREEN_W:
        dx = -dx
        hit_h = True

    if y <= 0 or y + BOX_H >= SCREEN_H:
        dy = -dy
        hit_v = True

    if hit_h and hit_v:
        corner_hit = True

    if FORCE_CORNER_HIT and frame_idx > total_frames - FPS and not corner_hit:
        x, y = 0, 0
        dx, dy = abs(dx), abs(dy)

    roi = frame[y:y+BOX_H, x:x+BOX_H]

    for c in range(3):
        roi[:, :, c] = (bgr[:, :, c] * alpha + roi[:, :, c] * (1 - alpha))

    frame[y:y+BOX_H, x:x+BOX_H] = roi

    out.write(frame)

out.release()
print("Exported:", OUTPUT_VIDEO)
