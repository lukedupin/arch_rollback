#!/usr/bin/python

import os, sys, re

if len(sys.argv) <= 1:
    print("Usage: sudo ./%s year-month-day" % sys.argv[0])
    exit()

# Split up the date, and make sure it makes some sense
date = sys.argv[1].split("-")
if len(date) < 3 or len(date[0]) != 4:
    print("Invalid date")
    exit()

# Write out our Arch rollback machine
output = open("/tmp/mirrorlist", "w")
output.write("Server=https://archive.archlinux.org/repos/%s/%s/%s/$repo/os/$arch\n" % (date[0], date[1].rjust(2, '0'), date[2].rjust(2, '0')))
output.close()

# backup the user's mirror list
os.system("sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup")
# Copy ARM over user's mirror list
os.system("sudo mv /tmp/mirrorlist /etc/pacman.d/mirrorlist")
# Run pacman update based on ARM mirrorlist
os.system("sudo pacman -Syyuu")
# Restore user's mirrorlist
os.system("sudo cp /etc/pacman.d/mirrorlist.backup /etc/pacman.d/mirrorlist")
