import imageio.v2 as imageio
import cv2

left = cv2.imread("left.png")
right = cv2.imread("right.png")
frames = []

# Add more blend steps for a smoother loop
blend_steps = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 0.8, 0.6, 0.4, 0.2]  # Forward & reverse

for alpha in blend_steps:
    blended = cv2.addWeighted(left, 1 - alpha, right, alpha, 0)
    frames.append(blended)

# Save with shorter duration for faster animation
imageio.mimsave("results/depth_animated.gif", frames, duration=0.1, loop=0)
