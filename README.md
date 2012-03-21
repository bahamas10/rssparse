RSS Parse
============
Parse RSS in python and return a python native object

Example Usage:

	>>> import urllib2
	>>> import rss
	>>> print rss.parse(urllib2.urlopen('http://someurl/rss.xml').read())
	{ put example here }

Copying
=======
Released under the BSD 3-clause license, see LICENSE for details.
