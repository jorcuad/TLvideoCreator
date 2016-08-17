from moviepy.editor import ImageSequenceClip
from os import listdir
from os.path import isfile, join

images = [f for f in listdir("./") if isfile(join("./",f))]
print images

clip = ImageSequenceClip(images, fps=0.5)
clip.write_videofile("movie.mp4")
