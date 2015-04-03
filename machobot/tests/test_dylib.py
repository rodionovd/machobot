# tests/test_dylib.py - machobot
# Copyright (c) 2015 Dmitry Rodionov
# https://github.com/rodionovd/machobot
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.

import os
import tempfile
import machobot.dylib as dylib

from subprocess import call
from shutil import copy2
from unittest import TestCase

class TestDylib(TestCase):
	library_path = None
	magic_return_value = 0xFD
					
	def test_inserting_load_command_into_32bit_target(self):
		# given
		target = self.request_asset("target32")
		# when
		regular_return_value = call(target)
		inserted = dylib.insert_load_command(target, self.install_name)
		new_return_value = call(target)
		# then
		self.assertEqual(regular_return_value, 0x0)
		self.assertTrue(inserted)
		self.assertEqual(new_return_value, TestDylib.magic_return_value)
				
	def test_inserting_load_command_into_64bit_target(self):
		# given
		target = self.request_asset("target64")
		# when
		regular_return_value = call(target)
		inserted = dylib.insert_load_command(target, self.install_name)
		new_return_value = call(target)
		# then
		self.assertEqual(regular_return_value, 0x0)
		self.assertTrue(inserted)
		self.assertEqual(new_return_value, TestDylib.magic_return_value)
		
	def test_inserting_load_command_into_fat_target(self):
		# given
		target = self.request_asset("fat_target")
		# when
		regular_return_value = call(target)
		inserted = dylib.insert_load_command(target, self.install_name)
		new_return_value = call(target)
		# then
		self.assertEqual(regular_return_value, 0x0)
		self.assertTrue(inserted)
		self.assertEqual(new_return_value, TestDylib.magic_return_value)
		
		
	def __init__(self, *args, **kwargs):
		super(TestDylib, self).__init__(*args, **kwargs)
		self.install_name = "@executable_path/injectee.dylib"
		self.requested_files = set()
	
	def tearDown(self):
		self.cleanup()
		
	@classmethod
	def tearDownClass(cls):
		""" Since the injectee library is shared across all targets,
		we only delete it after executing all the tests.
		"""
		if TestDylib.library_path is not None:
			delete_file(TestDylib.library_path)
	
	def request_asset(self, filename):
		""" Copies the required target and the injectee library (if needed) into a temporary directory.
		Returns a new path for the target.
		"""
		
		target_src = os.path.dirname(__file__) + "/assets/" + filename
		target_dst = tempfile.gettempdir() + "/machobot_test_" + filename
		# Copy the target
		if not copy_file(target_src, target_dst):
			return None
		self.requested_files.add(target_dst)
		# Also copy the injectee library if needed
		if TestDylib.library_path:
			return target_dst
		lib_src = os.path.dirname(__file__) + "/assets/" + "injectee.dylib"
		lib_dst = tempfile.gettempdir() + "/injectee.dylib"
		if copy_file(lib_src, lib_dst):
			TestDylib.library_path = lib_dst
			return target_dst
		return None
	
	def cleanup(self):
		""" Just removes all the files we've requested during a test. """
		for path in self.requested_files:
			delete_file(path)


# Some nice wrappers, 'cause why not	
def copy_file(src, dst):
	""" Copies a file using shutil.copy2() and reports errors. """
	try:
		copy2(src, dst)
	except OSError as err:
		raise Exception("Unable to copy file <%s> to <%s> due to error: %s" % (src, dst, err))
		return False
	return True
	
def delete_file(path):
	""" You name it. """
	os.remove(path)