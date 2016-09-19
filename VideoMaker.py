from moviepy.editor import ImageSequenceClip
from os import listdir
from os.path import isfile, join

images = ["./pics/blended/"+f for f in listdir("./pics/blended") if isfile(join("./pics/blended",f))]
print images

clip = ImageSequenceClip(images, fps=1)
clip.write_videofile("./video/movie.mp4")