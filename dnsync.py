#!/usr/bin/python
import uisp
import json
import sys
import re

"""
DOMAIN NAME SYNC
- Tool for populating dnsmasq entries from critical devices in UISP

Usage:
    python3 dnsync.py

Flags:
    

"""
def main():

    # Load arguments
    site = ''
    message = ''
    for idx, arg in enumerate(sys.argv):
        if arg in ['-m', '--message']:
            message = sys.argv[idx+1]
        elif arg in ['-s', '--site']:
            site = sys.argv[idx+1]

    # Get list of all devices
    devices = uisp.get_devices()

    # print(json.dumps(devices, indent=4))

    for device in devices:
        if '.' in device['identification']['name'] and device['identification']['name'] is not None and device['ipAddress'] is not None:
            if not re.match(r'^169.', device['ipAddress']):
                print(f"{device['identification']['name'].lower()}    {device['ipAddress'].split('/')[0]}")

if __name__ == '__main__':
    main()