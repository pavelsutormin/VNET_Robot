#!/bin/bash

touch cmd.txt
lxterminal -e "sudo python3 vnet.py"
lxterminal -e "python3 ttshelloserver.py"
gnome-terminal --full-screen -e "python3 curses_smile_builder.py"
