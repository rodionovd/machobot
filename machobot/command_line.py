# command_line.py - machobot
# Copyright (c) 2015 Dmitry Rodionov
# https://github.com/rodionovd/machobot
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.

from __future__ import print_function
import sys
import machobot.dylib as dylib

def main():
	args = sys.argv[1:]
	if len(args) < 2:
		print("Usage: %s target_path dynamic_library_path" % (sys.argv[0]), file = sys.stderr)
		return -1
		
	return 0 if dylib.insert_load_command(args[0], args[1]) else -2