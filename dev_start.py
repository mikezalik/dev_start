# quick script to speed up app start up for dev work

import subprocess

print("Hello Michael, let me start the apps you need...")

subprocess.run("/snap/bin/spotify")
subprocess.run("/snap/bin/chromium")
subprocess.run("/snap/bin/code")
subprocess.run("/snap/bin/slack")

