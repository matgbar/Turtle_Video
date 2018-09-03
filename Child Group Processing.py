#Note that this is program requires that files be saved using same strucure
#Each file should be saved as follows: 
#001_PCI_T1 Video 1 3_18_2015 12_06_41 PM 1
#The most important are the initial values: 001_PCI_T1

#Basic function - set working directory 
import os 
os.chdir('E:\\Child Group to be Processed')

#Get the moviepy functions needed for this process
from moviepy.editor import *

#Import list of Files from working directory 
FILE = os.listdir()

for x in range(len(FILE)):
    vid = VideoFileClip(FILE[x])
    f1 = FILE[x]
    txt = TextClip(f1[0:23], color='white', fontsize = 32, font='Arial')
    txt = txt.set_position(['left', 'bottom']).set_duration(30)
    vided = CompositeVideoClip([vid, txt])
    vided.write_videofile('E:\\Child Group to be Processed\\'+f1[0:23]+'.mp4')