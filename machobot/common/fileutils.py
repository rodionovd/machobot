# common/fileutils.py - machobot
# Copyright (c) 2015 Dmitry Rodionov
# https://github.com/rodionovd/machobot
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.

from macholib.MachO import MachO

def save_macho(macho, path):
	""" Serializes the provided Mach-O object to a file at the given path. """
	# TODO: I suppose this way we can corrupt an original file.
	#       Should I came up with something better?
	
	# We use 'r+' mode here because MachO.write() doesn't rewrite a whole
	# file, but just a header of it; so we must not truncate the thing.
	# There're also lots of fseek(), so 'a[+]' modes don't belong here too.
	f = open(path, "rb+")
	return macho.write(f)
