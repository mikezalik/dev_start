# quick script to speed up app start up for dev work

import subprocess

print("Starting Spotify, Chromium, Code and Slack...")

subprocess.run("/snap/bin/spotify")
subprocess.run("/snap/bin/chromium")
subprocess.run("/snap/bin/code")
subprocess.run("/snap/bin/slack")

