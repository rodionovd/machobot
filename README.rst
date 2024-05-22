machobot  
========  

.. image:: https://travis-ci.org/rodionovd/machobot.svg?branch=master
    :target: https://travis-ci.org/rodionovd/machobot
.. image:: https://codeclimate.com/github/rodionovd/machobot/badges/gpa.svg
   :target: https://codeclimate.com/github/rodionovd/machobot
   :alt: Code Climate

A Python toolbox for Mach-O files analysis. Heavily relies on
``macholib``.   
  
Installation  
------------  
  
For usage
'''''''''

::

	$ [sudo] pip install machobot*.zip

For development
'''''''''''''''

::

	$ pip install nose macholib
	$ git clone https://github.com/Solaree/machobot.git machobot
	$ cd ./machobot
	$ nosetests # run the test suite

Usage
-----

-  As a command-line util:

	.. code:: bash

	   $ inject_dylib ./target "@rpath/mylib.dylib"

-  As a Python module:

	.. code:: python

	   import machobot

	Example usage:

	.. code:: python

	   import machobot.dylib as dylib

	   dylib.insert_load_command("output.a", "@executable_path/../../libk.dylib")
	   
Modules
-------

dylib
'''''''''

	.. code:: python

	   insert_load_command (target_path, library_install_name)

Inserts a new ``LC_LOAD_DYLIB`` load command into the target Mach-O
header.

+----------------------------+-------------------------------------------------------------------------------------------------+
| Argument                   | Description                                                                                     |
+============================+=================================================================================================+
| ``target_path``            | A path to the target Mach-O executable file. **This file will be overwritten**.                 |
+----------------------------+-------------------------------------------------------------------------------------------------+
| ``library_install_name``   | An install name for the library to inject. This string is used as a part of the load command.   |
+----------------------------+-------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| Return value                                                          |
+=======================================================================+
| Returns ``True`` if everything is OK. Otherwise rises an exception.   |
+-----------------------------------------------------------------------+



	.. code:: python

	   macho_dependencies_list (target_path, header_magic=None)

Generates a list of libraries the given Mach-O file depends on.

In that list a single library is represented by its "install path": for some
libraries it would be a full file path, and for others it would be a relative
path (sometimes with dyld templates like @executable_path or @rpath in it).

Note: I don't know any reason why would some architectures of a fat Mach-O depend
on certain libraries while others don't, but *it's technically possible*.
So that's why you may want to specify the `header_magic` value for a particular header.

+----------------------------+-------------------------------------------------------------------------------------------------+
| Argument                   | Description                                                                                     |
+============================+=================================================================================================+
| ``target_path``            | A path to the target Mach-O executable file.                                                    |
+----------------------------+-------------------------------------------------------------------------------------------------+
| ``header_magic``           | Mach-O MAGIC value for a header you want to inspect. If this argument is not provided, the      |
|                            | function returns a list of the first header's dependencies.                                     |
+----------------------------+-------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| Return value                                                          |
+=======================================================================+
| An object with two properties: ``weak`` and ``strong`` that hold lists|
| of weak and strong dependencies respectively.                         |
+-----------------------------------------------------------------------+

See ``machobot/tests/test_dylib.py`` for usage examples.

--------------

Found an issue? Submit an issue! :shipit:
