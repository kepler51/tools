# Super Sound Simulator

## Description:
There was a need to simulate various alert sounds from an arbitrary number of sources at arbitrary distances from an observer.  This tool, given a list of distances (in feet by default) and an mp3 input file of a few seconds long will generate a new mp3 file simulating multiple devices playing that mp3 at the same time.  

Speed of sound is accounted for.  Sound intensity is accounted for.  

Output is monaural so no attempt is made to simulate directionality.

## Requirements:
The ffmpeg library is required by pydub.  Install per your package manager.  
Deb example: apt install ffmpeg 

## usage: 
 ./sss.py -i firetruck.mp3 -d 10,100,650

sss.py [-h] [-u {m,f}] -i INPUT [-o OUTPUT] -d DISTANCES [-U]

optional arguments:
  -h, --help            show this help message and exit
  -u {m,f}, --units {m,f}
                        m or f distances
  -i INPUT, --input INPUT
                        path to source mp3
  -o OUTPUT, --output OUTPUT
                        path to output mp3
  -d DISTANCES, --distances DISTANCES
                        any number of distances like: 10,100,2000
  -U, --unsynched       Default assumes sync and applies speed of sound to distance from observer
