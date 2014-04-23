from moviepy.editor import *


def regular_one():
    regular = VideoFileClip("./brotherBear.mp4").\
                  subclip(42,43).\
                  resize(0.5).\
                  to_gif("regular.gif",fps = None,program = 'ffmpeg') 
    #VideoFileClip.preview()

def cropping():
    VideoFileClip("./brotherBear.mp4").\
                   subclip(12.4,13.4).\
                   resize(0.5).\
                   crop(x1=145,x2=400).\
                   to_gif("cropping.gif", fps = None, program = 'ffmpeg')
def freezing_region():
    first = VideoFileClip("./brotherBear.mp4").\
              subclip(12,13).\
              resize(.4)

    second = first.\
              crop(x2= first.w/2).\
              to_ImageClip(0.2).\
              set_duration(first.duration)

    CompositeVideoClip([first, second]).\
              to_gif("frozen.gif", fps= 15, program = 'ffmpeg')


def time_symetrize(clip):   #forward_backwards():
    """ Returns the clip played forwards then backwards. In case
    you are wondering, vfx (short for Video FX) is loaded by
    >>> from moviepy.editor import * """
    return concatenate([clip, clip.fx( vfx.time_mirror )])

def forward_backwards():
    VideoFileClip("./brotherBear.mp4").\
              subclip(12, 13).\
              resize(0.5).\
              crop(x1=189, x2=433).\
              fx( time_symetrize ).\
              to_gif('backward.gif', fps = 15, program = 'ffmpeg')

def looping():
    castle = VideoFileClip("./brotherBear.mp4").\
                  subclip(12,13).\
                  speedx(0.2).\
                  resize(.4)

    d = castle.duration
    castle = castle.crossfadein(d/2)

    CompositeVideoClip([castle,castle.set_start(d/2),castle.set_start(d)]).\
                   subclip(d/2, 3*d/2).\
                   to_gif('looping.gif', fps=15, program = 'fffmpeg')    

#ADDING TEXT!!!!
##def adding_text():
##    kodak = VideoFileClip("./brotherBear.mp4").\
##            subclip(12,13).\
##            resize(.5).\
##            speedx(0.5).\
##            fx( time_symetrize )
##
##    # Many options are available for the text (requires ImageMagick)
##    text = TextClip("Kodak!",
##                    fontsize=30, color='green',
##                    font='Amiri-Bold', interline=-5).\
##            set_pos(20,30).\
##            set_duration(kodak.duration)
##
##    CompositeVideoClip([kodak, text]).\
##            to_gif('letter.gif', fps=10, program = 'ffmpeg')


def main():
##    regular_one()
##    cropping()
##    freezing_region()
##    forward_backwards()
#    adding_text()
    looping()

    
main()
