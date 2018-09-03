# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:50:26 2017

@author: Matt
"""

#creating new program to run through all files in every folder 
#was not able to recover the bad video files

import os 
WD='E:\\HDV to be Processed\\'
os.chdir(WD)
DIR=os.listdir()

from moviepy.editor import *

for x in range(len(DIR)):
    os.chdir(WD+DIR[x])
    FILE = os.listdir()
    if len(FILE)==1:
        v1=VideoFileClip(FILE[0])
        txt = TextClip(DIR[x], color='white', fontsize = 32, font='Arial') 
        txt = txt.set_position(['left', 'bottom']).set_duration(30)
        vided = CompositeVideoClip([v1, txt])
        vided.write_videofile(DIR[x]+'compiled.mp4')
    elif len(FILE)==2:
        v1=VideoFileClip(FILE[0])
        v2=VideoFileClip(FILE[1])
        vid=concatenate_videoclips([v1,v2])
        txt = TextClip(DIR[x], color='white', fontsize = 32, font='Arial') 
        txt = txt.set_position(['left', 'bottom']).set_duration(30)
        vided = CompositeVideoClip([vid, txt])
        vided.write_videofile(DIR[x]+'compiled.mp4')        
    elif len(FILE)==3:
        v1=VideoFileClip(FILE[0])
        v2=VideoFileClip(FILE[1])
        v3=VideoFileClip(FILE[2])
        vid=concatenate_videoclips([v1,v2,v3])
        txt = TextClip(DIR[x], color='white', fontsize = 32, font='Arial') 
        txt = txt.set_position(['left', 'bottom']).set_duration(30)
        vided = CompositeVideoClip([vid, txt])
        vided.write_videofile(DIR[x]+'compiled.mp4')        
    elif len(FILE)==4:
        v1=VideoFileClip(FILE[0])
        v2=VideoFileClip(FILE[1])
        v3=VideoFileClip(FILE[2])
        v4=VideoFileClip(FILE[3])
        vid=concatenate_videoclips([v1,v2,v3,v4])
        txt = TextClip(DIR[x], color='white', fontsize = 32, font='Arial') 
        txt = txt.set_position(['left', 'bottom']).set_duration(30)
        vided = CompositeVideoClip([vid, txt])
        vided.write_videofile(DIR[x]+'compiled.mp4')        
    elif len(FILE)==5:
        v1=VideoFileClip(FILE[0])
        v2=VideoFileClip(FILE[1])
        v3=VideoFileClip(FILE[2])
        v4=VideoFileClip(FILE[3])
        v5=VideoFileClip(FILE[4])
        vid=concatenate_videoclips([v1,v2,v3,v4,v5])
        txt = TextClip(DIR[x], color='white', fontsize = 32, font='Arial') 
        txt = txt.set_position(['left', 'bottom']).set_duration(30)
        vided = CompositeVideoClip([vid, txt])
        vided.write_videofile(DIR[x]+'compiled.mp4')        
    elif len(FILE)==6:
        v1=VideoFileClip(FILE[0])
        v2=VideoFileClip(FILE[1])
        v3=VideoFileClip(FILE[2])
        v4=VideoFileClip(FILE[3])
        v5=VideoFileClip(FILE[4])
        v6=VideoFileClip(FILE[5])
        vid=concatenate_videoclips([v1,v2,v3,v4,v5,v6])
        txt = TextClip(DIR[x], color='white', fontsize = 32, font='Arial') 
        txt = txt.set_position(['left', 'bottom']).set_duration(30)
        vided = CompositeVideoClip([vid, txt])
        vided.write_videofile(DIR[x]+'compiled.mp4')        
    elif len(FILE)==7:
        v1=VideoFileClip(FILE[0])
        v2=VideoFileClip(FILE[1])
        v3=VideoFileClip(FILE[2])
        v4=VideoFileClip(FILE[3])
        v5=VideoFileClip(FILE[4])
        v6=VideoFileClip(FILE[5])
        v7=VideoFileClip(FILE[6])
        vid=concatenate_videoclips([v1,v2,v3,v4,v5,v6,v7])
        txt = TextClip(DIR[x], color='white', fontsize = 32, font='Arial') 
        txt = txt.set_position(['left', 'bottom']).set_duration(30)
        vided = CompositeVideoClip([vid, txt])
        vided.write_videofile(DIR[x]+'compiled.mp4')        
    elif len(FILE)==8:
        v1=VideoFileClip(FILE[0])
        v2=VideoFileClip(FILE[1])
        v3=VideoFileClip(FILE[2])
        v4=VideoFileClip(FILE[3])
        v5=VideoFileClip(FILE[4])
        v6=VideoFileClip(FILE[5])
        v7=VideoFileClip(FILE[6])
        v8=VideoFileClip(FILE[7])
        vid=concatenate_videoclips([v1,v2,v3,v4,v5,v6,v7,v8])
        txt = TextClip(DIR[x], color='white', fontsize = 32, font='Arial') 
        txt = txt.set_position(['left', 'bottom']).set_duration(30)
        vided = CompositeVideoClip([vid, txt])
        vided.write_videofile(DIR[x]+'compiled.mp4')    
    else:
        print("File length exceeds 8!!")