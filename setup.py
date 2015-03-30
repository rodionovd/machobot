from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

setup(name = 'machobot',
	version = '0.1.1',
	description = 'A set of tools for Mach-O executables analysis on OS X',
	long_description = readme(),
	url = 'http://github.com/rodionovd/machobot',
	author = 'Dmitry Rodionov',
	author_email = 'i.am.rodionovd@gmail.com',
	license = 'MIT',
	packages = ['machobot'],
	entry_points = {
		'console_scripts': ['inject_dylib=machobot.command_line:main'],
	},
	install_requires=[
	    'macholib',
	],
	test_suite = 'nose.collector',
	tests_require = ['nose'],
	zip_safe = False,
	include_package_data = True,
	classifiers = [
		'Development Status :: 3 - Alpha',
		'License :: OSI Approved :: MIT License',
	])