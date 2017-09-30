#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip_address, client_id, client_username, time, time_zome, request_method, file_name, protocol, status_code, size\
            = data
        cleaned_file_name = re.sub(r"^http://www.the-associates.co.uk", '', file_name)
        print cleaned_file_name
