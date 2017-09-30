#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip_address, client_id, client_username, time, time_zome, request_method, file_name, protocol, status_code, size\
            = data
        print ip_address
