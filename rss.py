#!/usr/bin/env python
# Copyright (c) 2012, Dave Eddy <dave@daveeddy.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#        * Redistributions of source code must retain the above copyright
#          notice, this list of conditions and the following disclaimer.
#        * Redistributions in binary form must reproduce the above copyright
#          notice, this list of conditions and the following disclaimer in the
#          documentation and/or other materials provided with the distribution.
#        * Neither the name of the project nor the
#          names of its contributors may be used to endorse or promote products
#          derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Library to parse RSS and return a python object
#

import xml.dom.minidom

def parse(rss, fields = ['pubDate', 'title', 'link', 'description']):
	"""
	Parse RSS

	@param	rss	{string}	The rss given as a string
	@param	fields	{list}		An optional list of fields to extract from each item

	@return	{obj}	A python object with fields extracted from the rss
	"""
	# Create the dom
	dom = xml.dom.minidom.parseString(rss)

	# Get the global information
	title = dom.getElementsByTagName('title')[0].childNodes[0].data
	description = dom.getElementsByTagName('description')[0].childNodes[0].data

	# Loop the items and save them in a list
	items = []
	for item in dom.getElementsByTagName('item'):
		# For each item, fiend the fields and save them in a dict
		item_obj = {}
		for field in fields:
			item_obj[field] = item.getElementsByTagName(field)[0].childNodes[0].data
		items.append(item_obj)

	# Return the object
	return { 'title' : title, 'description' : description, 'items' : items }

if __name__ == '__main__':
	import sys
	import urllib2
	try:
		import json
	except ImportError:
		import simplejson as json

	try:
		url = sys.argv[1]
	except IndexError:
		url = 'http://www.daveeddy.com/feed'

	obj = parse(urllib2.urlopen(url).read())
	print json.dumps(obj, indent=4)
