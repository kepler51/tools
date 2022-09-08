#!/bin/bash

#loops are unrolled for clarity

# synchronized
    # at equal distances
    ../sss.py -i sweep.mp3 -d 40,40,40 -o synched-40-40-40-sweep.mp3
    ../sss.py -i firetruck.mp3 -d 40,40,40 -o synched-40-40-40-firetruck.mp3
    
    # at unequal distances
    ../sss.py -i sweep.mp3 -d 40,200,500 -o synched-40-200-500-sweep.mp3
    ../sss.py -i firetruck.mp3 -d 40,200,500 -o synched-40-200-500-firetruck.mp3


# unsynchronized
    # at equal distances (worst case)
    ../sss.py -U -i sweep.mp3 -d 40,40,40 -o unsynched-40-40-40-sweep.mp3
    ../sss.py -U -i firetruck.mp3 -d 40,40,40 -o unsynched-40-40-40-firetruck.mp3

    # at unequal distances
    ../sss.py -U -i sweep.mp3 -d 40,200,500 -o unsynched-40-200-500-sweep.mp3
    ../sss.py -U -i firetruck.mp3 -d 40,200,500 -o unsynched-40-200-500-firetruck.mp3



#a new siren sound which also sweeps the frequency range, worst-case scenario
../sss.py -U -i allgemeiner.mp3 -d 40,40,40 -o unsynced-40-40-40-allgemeiner.mp3
