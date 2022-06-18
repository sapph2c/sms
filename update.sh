#!/bin/bash
#
# Script to update all packages on the system, and then
# send out an alert to your phone number
#

sudo apt-get update -y

python3 test.py --body "\n[*] Finished updating all packages!\nYou're welcome~"
