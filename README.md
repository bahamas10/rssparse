RSS Parse
============
Parse RSS in python and return a python native object

Usage
=====
Example Usage:

``` python
>>> import urllib2
>>> import rss
>>> print rss.parse(urllib2.urlopen('http://someurl/rss.xml').read())
{ 'title' : 'Title of RSS', 'description' : 'Description of RSS', items : [ {}, {}, ... ] }
```

Command line:

	$ ./rss.py http://www.daveeddy.com/feed

Copying
=======
Released under the BSD 3-clause license, see LICENSE for details.
