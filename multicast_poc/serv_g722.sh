#!/bin/bash

ADDR=224.0.0.1:4567

#examples that work
#ffmpeg -re -i test.mp3 -c:v copy -c:a copy -f rtp rtp://239.1.2.3:4567?ttl=8
#ffmpeg -re -i test.mp3 -c:a copy -f rtp rtp://${ADDR}?ttl=8

#doesn't quite work
#ffmpeg -re -i test.mp3 -c:a g722 -f rtp rtp://${ADDR}?ttl=8

ffmpeg -re -i test.mp3 -c:a g722 -ar 16000 -sdp_file saved_sdp_file -f rtp rtp://${ADDR}?ttl=8
