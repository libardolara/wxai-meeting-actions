import os
from moviepy.editor import *
import sys, getopt


def main(argv):
  try:
    # Defines the options -h -n and -u and their respective longer version
    opts, args = getopt.getopt(argv,"f:",["file"])
    if len(opts)==0:
      # If no option is used the program guides the user.
      print( 'Command line error' )
      print('Command must be -f')
      print( '  extractAudio.py -f <your-file>')

  except getopt.GetoptError:
    # If a different option is used the program guides the user.
    print( 'Command line error' )
    print( '  extractAudio.py -f <your-file>')
    sys.exit(2)  
  for opt, arg in opts:
    if opt in ("-f", "--file"):
        video = VideoFileClip(os.path.join(arg))
        video.audio.write_audiofile("audio.mp3")
        sys.exit()
    else:
        print( 'Command line error' )
        print( '  extractAudio.py -f <your-file>')
        sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])