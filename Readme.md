🎬 DVD-Style Bouncing PNG Animation (Python + OpenCV)

Create a smooth DVD logo–style bouncing animation using any PNG image with transparency — exported directly as an MP4 video.
This project uses Python + OpenCV to generate a 30-second bouncing animation where your PNG smoothly moves, hits edges.
✨ Features

✔️ Load any PNG with transparency

✔️ Smooth bouncing animation (DVD screensaver style)

✔️ Adjustable size, speed, duration, and resolution

✔️ Guaranteed corner hit before the video ends

✔️ Clean MP4 export (H.264 / mp4v)

✔️ No external dependencies other than OpenCV

✔️ Extremely simple to customize

📸 Example Use Case

Use a face cut-out, logo, streamer icon, or any transparent PNG and generate a video like this:

Floating around the screen

Bouncing off edges

Corner hits like the classic DVD animation

Completely black background (or customizable)

🚀 Getting Started
1. Install Dependencies

Make sure you have Python 3.7+ installed.

Install OpenCV:

pip install opencv-python

2. Add Your PNG

Place your PNG file somewhere on your computer.

Your PNG must have transparency (RGBA format).

Example:

my_face.png
my_logo.png
cutout_image.png

3. Update the Script

Inside the script, set your PNG path:

PNG_PATH = r"C:\Users\...\your_image.png"


Run the script:

python bouncing_png.py

4. Output

You will get a clean MP4 file:

bouncing_face_png.mp4


This is a 30-second 60FPS animation ready to use anywhere.

🧠 How It Works

The PNG is loaded using cv2.imread(..., cv2.IMREAD_UNCHANGED)

The alpha channel is separated for proper transparency blending

A blank black background is created using NumPy

The PNG moves across the screen each frame

The script detects wall collisions and reverses direction

A guaranteed corner hit is forced near the end if it didn't happen naturally

All frames are written into an MP4 video using OpenCV's VideoWriter

⚙️ Customization

You can easily customize:

🎞 Duration
DURATION = 30

📺 Resolution
SCREEN_W, SCREEN_H = 1280, 720

🖼 PNG Size
BOX_W, BOX_H = 260, 260

🚀 Speed
dx, dy = 5, 4

🔲 Background color

Replace:

frame = np.zeros((SCREEN_H, SCREEN_W, 3), dtype=np.uint8)


With RGB background values:

frame = np.full((SCREEN_H, SCREEN_W, 3), (20, 20, 20), dtype=np.uint8)  # dark gray

🔍 SEO Keywords (to improve discoverability)

This project is optimized for search engines using relevant keywords:

Python DVD bounce animation

OpenCV bouncing logo

PNG transparency animation

Python video generator

Create bouncing PNG video

Python motion graphics script

Floating logo animation

DVD screensaver effect with Python

These keywords help Google surface your project for users searching for similar effects.

Contributing

Pull requests, improvements, and feature additions are welcome.

Ideas:

Glow effects

Color change on bounce

Motion blur

Random speed variation

Multi-image bouncing

License
This project is released under the MIT License.
Feel free to modify and use it anywhere.
