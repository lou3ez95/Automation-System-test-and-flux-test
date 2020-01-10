#!/usr/bin/python
import sys
import json

with open(sys.argv[1], "r") as f:
    distros_dict = json.load(f)

for distro in distros_dict:
 shell_script = distro["item"],distro["stderr_lines"],distro["start"]
 print (shell_script)

