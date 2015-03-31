machobot  
========  
  
A Python toolbox for Mach-O files analysis. Heavily relies on
``macholib``.   
  
Installation  
------------  
  
For usage
'''''''''

::

	$ [sudo] pip install machobot

For development
'''''''''''''''

::

	$ pip install nose macholib
	$ git clone https://github.com/rodionovd/machobot.git machobot
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

--------------

Found an issue? `Sumbit an issue`_.

.. _Sumbit an issue: https://github.com/rodionovd/machobot/issues/new
