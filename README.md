# Arch rollback
Roll your arch packages back to a specific date. Handy script to unbork your machine. The script leaves no lasting effects on your machine. If you roll back to a given date, and then run pacman -Syu, it'll run as expected.

# Usage

    git clone git@github.com:lukedupin/arch_rollback.git
    cd arch_rollback
    ./arch_rollback.py 2020-2-12 # Roll all packages back to Febuary 12th, 2020

