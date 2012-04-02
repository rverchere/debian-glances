#!/usr/bin/env python

import os
from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(  name='Glances',
	version='1.3.7',
	download_url='https://github.com/downloads/nicolargo/glances/glances-1.3.7.tar.gz',
	url='https://github.com/nicolargo/glances',
	description='CLI curses-based monitoring tool',
	author='Nicolas Hennion',
	author_email='nicolas@nicolargo.com',
	license = "LGPL",
	keywords = "cli curse monitoring system",
	long_description=read('README'),
	packages=['src'],
 	install_requires=['pystatgrab>=0.5']
)
