#this will be the file that contains all the important functions
import moviepy

user_video = moviepy.VideoFileClip("test_vid.mp4")

print(user_video.duration)

# def trim_video(video):
#     if user_video.duration > 60
