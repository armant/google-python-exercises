#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_path(dir):
	path_list = []
	filenames = os.listdir(dir)
	
	for filename in filenames:
		special = re.search(r'__\w+__', filename)
		if special: path_list.append(os.path.abspath(os.path.join(dir, filename)))
	
	return path_list

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  
  ans = []
  
  for dir in args:
	ans.append(get_special_path(dir))
	
  for list_of_path in ans:
    for path in list_of_path:
	  if todir != '':
	    if not os.path.exists(todir): os.makedirs(todir)
	    shutil.copy(path, todir)
	  
	  elif tozip == '': print path
	 
  if tozip != '':
	ans_string = ''
	
	for list_of_path in ans:
		for path in list_of_path:
			ans_string = ans_string + ' ' + path
	
	cmd = 'zip -j ' + tozip + ans_string
	print "Command I'm going to do:", cmd
	(status, output) = commands.getstatusoutput(cmd)
	
	if status:
		sys.stderr.write(output)
		sys.exit(1)
  
  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
