# checks detailed battery status on QX411 laptop

import subprocess

subprocess.run("neofetch")
subprocess.run(["upower", "-i", "/org/freedesktop/UPower/devices/battery_BAT1"])

