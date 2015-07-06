Helper Scripts
==============

## rmount.py ##
Mounts/unmounts a remote filesystem to/from a specified directory.

Uses a dictionary of property names and their remote path

Example: `"server": "user@192.168.0.55:/"`

### Usage ###
Mounting: `rmount.py propertyName`

Unmounting: `rmount.py -u propertyName`

Note that when attempting to unmount, the script will not check if the target is a valid property.