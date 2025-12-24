#!/bin/bash
ADDR=224.0.0.1:4567

#ffplay rtp://@${ADDR}

#ffplay -ar 16000 -acodec g722 rtp://@${ADDR}

#ffplay -protocol_whitelist "file,udp,rtp" -i saved_sdp_file
ffplay -reorder_queue_size 20 -protocol_whitelist "file,udp,rtp" -i static.sdp

