# -*- coding: utf-8 -*-

# Board config for desktop

import os
import subprocess
import netifaces

class Board(object):
	@staticmethod
	def configDir():
		return os.environ['HOME'] + '/.config/Telldus'

	@staticmethod
	def getMacAddr():
		try:
			with open(Board.configDir() + '/boardinfo.conf', 'r') as f:
				for line in f:
					if line.startswith('mac'):
						return line.split('=')[1].rstrip()
		except:
			pass
		return "000000000000"

	@staticmethod
	def firmwareVersion():
		return subprocess.check_output(['git', 'describe'])[1:]

	@staticmethod
	def networkInterface():
		for ifname in netifaces.interfaces():
			if ifname == 'lo':
				continue
			addresses = netifaces.ifaddresses(ifname)
			if netifaces.AF_INET not in addresses:
				continue
			if netifaces.AF_LINK not in addresses:
				continue
			for addr in addresses[netifaces.AF_INET]:
				if 'addr' in addr:
					return ifname
		return 'eth0'  # Fallback

	@staticmethod
	def gpioConfig():
		return {
			'status:green': {'type': 'none'},
			'status:red': {'type': 'none'},
			'zwave:reset': {'type': 'none'},
		}

	@staticmethod
	def hw():
		try:
			with open(Board.configDir() + '/boardinfo.conf', 'r') as f:
				for line in f:
					if line.startswith('hw'):
						return line.split('=')[1].rstrip()
		except:
			pass
		return "Dev-hardware"

	@staticmethod
	def liveServer():
		return 'api.telldus.net'

	@staticmethod
	def luaScriptPath():
		return '%s/build/scripts/lua' % os.getcwd()

	@staticmethod
	def pluginPath():
		return '%s/build/plugins' % os.getcwd()

	@staticmethod
	def product():
		return 'tellstick-desktop'

	@staticmethod
	def rf433Port():
		# return 'hwgrep://10c4:ea60'
		return 'hwgrep://1781:0c32'

	@staticmethod
	def secret():
		return ''

	@staticmethod
	def zwavePort():
		return 'hwgrep://067b:2303'
