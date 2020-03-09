#!/usr/bin/python

import os, sys, re

if len(sys.argv) <= 1:
    print("Usage: sudo ./downgrade.py year-month-day")
    exit()

date = sys.argv[1].split("-")
if len(date) < 3 or len(date[0]) != 4:
    print("Invalid date")
    exit()

# Write out our Arch rollback machine
output = open("/tmp/mirrorlist", "w")
output.write("Server=https://archive.archlinux.org/repos/%s/%s/%s/$repo/os/$arch\n" % (date[0], date[1].rjust(2, '0'), date[2].rjust(2, '0')))
output.close()

# Copy the user's mirror list
os.system("sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.downgrade")
os.system("sudo mv /tmp/mirrorlist /etc/pacman.d/mirrorlist")
os.system("sudo pacman -Syyuu")
os.system("sudo cp /etc/pacman.d/mirrorlist.downgrade /etc/pacman.d/mirrorlist")
