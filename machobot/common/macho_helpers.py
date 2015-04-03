
import os.path

from macholib.MachO import MachO
from .fileutils import save_macho

def modify_macho_file_headers(macho_file_path, modificator_func):
	""" Modifies headers of a Mach-O file at the given path by calling
	the modificator function on each header.
	
	Returns True on success, otherwise rises an exeption (e.g. from macholib)
	"""
	if not os.path.isfile(macho_file_path):
		raise Exception("You must specify a real executable path as a target")
		return False
		
	m = MachO(macho_file_path)
	apply_to_headers(m, modificator_func)
	save_macho(m, macho_file_path)
	return True

def apply_to_headers(macho_object, func):
	""" Calls the given function on every header in the Mach-O object """
	map(func, macho_object.headers)
