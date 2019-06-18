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
		intCode = self.intParameter('code', 1, 10000000)

		if method != Device.BELL:
			return ''

		l = chr(132)  # 0
		h = chr(255)  # 1
		s = chr(69)   # space between bits
		pb = chr(110) # preamble big
		ps = chr(84)  # preamble small

		bits = [l + s,h + s]
		strCode = pb + ps + s

		for i in range(23, -1, -1):
			b = (intCode>>i)&0x01
			strCode = strCode + bits[b]

		return {'R': 20, 'P': 110, 'S': strCode}
