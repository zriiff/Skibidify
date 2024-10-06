#this will be the file that contains all the important functions
from moviepy.editor import VideoFileClip

user_video = VideoFileClip("test_vid.mp4")

print(user_video.duration)

# def trim_video(video):
#     if user_video.duration > 60
