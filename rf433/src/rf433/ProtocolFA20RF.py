 # -*- coding: utf-8 -*-

from Protocol import Protocol
from telldus import Device
import logging

class ProtocolFA20RF(Protocol):
	def methods(self):
		return (Device.BELL)

	def decodeData(self, data):
		if 'data' not in data:
			return None

		value = int(data['data'], 16)

		retval = {}
		retval['class'] = 'command'
		retval['protocol'] = 'fa20rf'
		retval['model'] = 'smokealarm'
		retval['code'] = value
		retval['method'] = Device.BELL
		return retval

	def stringForMethod(self, method, data=None):
		intCode = self.intParameter('code', 1, 10000000) # 9954226 
		logging.info("StringForMethod %i:%s" % (intCode, method))

		if method != Device.BELL:
			return ''

		l = chr(130)   # 0
		h = chr(255)  # 1
		s = chr(62)   # space between bits
		pb = chr(250) # preable big
		ps = chr(82)  # preable small

		bits = [l + s,h + s]

		strCode = pb + ps + s

		for i in range(23, -1, -1):
			strCode = strCode + bits[(intCode>>i)&0x01]

		logging.info("Sending %s" % (strCode))

		return {'S': strCode}