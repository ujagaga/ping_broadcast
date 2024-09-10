# Ping Broadcast

I was working with a closed network, using a 16 bit IP range (192.168.x.x) and needed to locate available devices. 
Since this is a large number of addresses (65536) and I do not know which ports are open, I needed a solution using 
the ping command, but in a large number of threads, so they execute at the same time to accelerate scanning.
My script requires that you spacify any IP address within the search range like 192.168.2.3 and it will only use 
the first two numbers to form a start IP (192.168.0.1) and the end IP (192.168.254.254).

Default timeout is 2s, but you can specify your own:

        ping_broadcast.py -i 192.168.1.0 -t 1

# NOTE
This should work on Linux, Mac and Windows. On my computer, with timeout = 2s, scanning takes about 20 minutes.
