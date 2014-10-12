#!/usr/bin/env python

# Copyright 2014 Matthew D'Asaro
# This program is distributed under the terms of the GNU General Purpose License (GPL).
# Refer to http://www.gnu.org/licenses/gpl.txt

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

import serial
import time


class HardwareInterface():

	def __init__(self):
		try:
			self.ser = serial.Serial('/dev/ttyACM0')
			self.ser.flushInput()
			time.sleep(2)
		except:
			pass
		self.chord = 0
		self.tau = 23
		#We must wait a few seconds for the arduino to reboot after its serial connection is reset

	def getChord(self):
		try:
			if self.ser.inWaiting() > 0:
				self.chord = ord(self.ser.read(1)) & 0b00011111
		except:
			pass
		return self.chord

	def setChord(self, chord):
		try:
			self.ser.write(str(chr(int(chord) | 0b00100000)))
		except:
			pass

	def getTau(self):
		return self.tau

	def setTau(self, localtau):
		try:
			self.ser.write(str(chr(int(localtau) | 0b01000000)))
		except:
			pass
		self.tau = localtau

	def chordToList(self, localChord):
		return [(int(localChord) & 0b00010000) >> 4, (int(localChord) & 0b00001000) >> 3, (int(localChord) & 0b00000100) >> 2, (int(localChord) & 0b00000010) >> 1, (int(localChord) & 0b00000001)]
	
	def listToChord(self,chordList):
		if len(chordList) != 5:
			return -1
		return 16*chordList[0]+8*chordList[1]+4*chordList[2]+2*chordList[3]+1*chordList[4]

