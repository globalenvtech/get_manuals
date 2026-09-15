from pathlib import Path
from moviepy import VideoFileClip

mp4_path = Path("C:\\Users\\chenk\\Videos\\Screen Recordings\\Screen Recording 2026-09-14 153358.mp4")
print(mp4_path)
res_path = Path('C:\\Users\\chenk\\Videos\\Screen Recordings\\Screen Recording 2026-09-14 153358.gif')
videoClip = VideoFileClip(mp4_path, target_resolution=[780,406])

print(videoClip.size)
videoClip.write_gif(res_path, fps=1)