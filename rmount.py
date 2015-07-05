#####
# Quick sshfs mounting script
# 
# Mounts/unmounts a remote filesystem to/from a specified directory
# 
# Uses a dictionary of property names and their remote path
# Example: "server": "user@192.168.0.55:/"
#
# Usage:
# Mounting: python rmount.py propertyName
# Unmounting: python rmount.py -u propertyName
# Note that when attempting to unmount the script will not check
# if the target is a valid property.
#####

import subprocess
from sys import argv

properties = {\
	"server": "user@1.1.1.1:/"}
	
mountDir = "/path/to/servers/"

# If the first argument is the unmount flag,
# we want to use the 2nd argument as our property
if argv[1] == "-u":
	mountLoc = mountDir + argv[2] + "/"
	print "Attempting to unmount " + argv[2] + " from " + mountLoc
	subprocess.call(["fusermount", "-u", mountLoc])
	subprocess.call(["rm", "-r", mountLoc])
	
elif argv[1] in properties.keys():
	mountLoc = mountDir + argv[1] + "/"
	print "Attempting to mount " + argv[1] + " in " + mountLoc
	subprocess.call(["mkdir", mountLoc])
	subprocess.call(["sshfs", properties[argv[1]], mountLoc])
	
else:
	print "Property not available."