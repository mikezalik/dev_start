# sets up custom resolution on debian-based distro for older Samsung laptop

import subprocess

subprocess.run("xrandr --newmode '1600x900'  118.25  1600 1696 1856 2112  900 903 908 934 -hsync +vsync")
subprocess.run("xrandr --addmode LVDS-1 '1600x900'")
subprocess.run("xrandr --output LVDS-1 --mode '1600x900'")
