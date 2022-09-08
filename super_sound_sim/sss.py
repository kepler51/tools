#!/usr/bin/env python3

import math, random, argparse
from pydub import AudioSegment

Cm=344 #speed of sound in m/s
Cf=1128 #speed of sound in fps

def getargs():
    # arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--units", help="m or f distances",  choices=['m','f'], default='f')
    parser.add_argument("-i", "--input", help="path to source mp3", required=True)
    parser.add_argument("-o", "--output", help="path to output mp3", default="out.mp3") 
    parser.add_argument("-d", "--distances", help="any number of distances like: 10,100,2000", required=True)
    parser.add_argument("-U", "--unsynched", help="Default assumes sync and applies speed of sound to distance from observer", action='store_true')
    args = parser.parse_args()
   
    global C
    if args.units == 'm':
        C=Cm
    elif args.units == 'f':
        C=Cf
  
    print(type(C))
    return(args)


args = getargs()

#lowest distance will be 100 in intensity
source_distances = list(map(int, args.distances.split(",")))
source_distances.sort()
c = 0
d1 = 0
mastersound = AudioSegment.silent(duration=6000)
unsync_delay=0
for d in source_distances:
    #debug
    #mastersound.export("mixed_sounds_" + str(c)+".mp3", format="mp3")
    c += 1
    
    #delay from C speed of sound
    delay = d/C

    if args.unsynched: 
        #introduce unsync delay and increment .5 seconds 
        delay = delay + unsync_delay
        unsync_delay = unsync_delay+.5
    print("delay: "+str(delay))

    #intensity relative to first distance (which is always 100)
    if c == 1:
        d1 = d
        i1 = intensity = 100
        gaindB = 0 
    else: 
        # solve for i2 relative to i1 (inverse square law) for each source distance
        intensity = (i1/((d**2)/(d1**2)))
        gaindB = 10 * math.log10(intensity/i1)
    

    sound = AudioSegment.from_mp3(args.input)
    adjusted_sound = sound.apply_gain(gaindB) 
    overlayX = mastersound.overlay(adjusted_sound, position=(delay*1000))

    mastersound = overlayX
    print(str(c), str(d), str(intensity), str(gaindB), str(delay))
    
mastersound.export(args.output, format="mp3")


