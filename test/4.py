#!/usr/bin/python 
# -*- coding: utf-8 -*-

import os

filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
	execfile(filename)
