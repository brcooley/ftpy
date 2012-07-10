#! /usr/bin/python3
# -*- coding: utf-8 -*-

import time

from .ft import *
from functools import wraps

SUPPORTED_CMDS = [
	'cd',
	'cp',
	'ls',
	'mv',
	'rm'
]

PROG_TITLE = "ft.py"
VERSION = "0.1a"
LOG_FILE = time.strftime('.%Y-%m-%d.log')
CONFIG_FILE = '.ftpyrc'

# CONSTANTS
FTP_SUCCESS = 0
FTP_FAILURE = 1


### PRIVATE ###
  # DECORATORS

def _api(level,stability):
	def wrapper(fn):
		fn.__doc__ = fn.__doc__.format(level,stability)
		return fn
	return wrapper


  # FACTORIES
def _new_cmd(name):
	'''Private function factory which outputs all the command specific globals.'''
	def runtime_cmd(server=None,*args):
		return ft.cmd(server, [name] + list(args))
	return runtime_cmd

for cmd in SUPPORTED_CMDS:
	ft.__dict__[cmd] = _new_cmd(cmd)


### HIGH LEVEL API

@_api(1,"Stable")
def login(server=None,connections=1):
	'''
	Allows n login(s) to a remote server.

	API Level: {}
	Stability: {}
	'''


@_api(1,"Stable")
def logout(server=None,connections=-1):
	'''
	Logs out of n login(s) to a remote server.

	API Level: {}
	Stability: {}
	Args:
	    connections:	Number of connections to logout from (default: all)
	'''


@_api(1,"Stable")
def upload(server=None,localName="."):
	'''
	Abstraction of uploading files, uses active connection(s) if server is not given.

	API Level: {}
	Stability: {}
	'''


@_api(1,"Stable")
def download(server=None,remoteName="."):
	'''
	Abstraction of downloading files, uses active connection(s) if server is not given.

	API Level: {}
	Stability: {}
	'''


@_api(1,"Experimental")
def connections(server=None,number=1):
	'''
	Sets the number of connections to the given or active server.

	API Level: {}
	Stability: {}
	'''


@_api(1,"Experimental")
def info(server=None,**kwargs):
	'''
	Allows for queries against the current state of the session with the given or active server.

	API Level: {}
	Stability: {}
	'''


@_api(1,"Experimental")
def secure(server=None,connections=-1):
	'''
	Enables (a) secure connection(s) to the given or active server.

	API Level: {}
	Stability: {}
	'''


@_api(1,"Experimental")
def insecure(server=None,connections=-1):
	'''
	Disables (a) secure connection(s) to the given or active server.

	API Level: {}
	Stability: {}
	'''


@_api(1,"Stable")
def cmd(server=None,*args):
	'''
	Executes the commands listed in *args for the specified server.

	API Level: {}
	Stability: {}
	'''