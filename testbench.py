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
import HardwareInterface
import time

arduinoInterface = HardwareInterface.HardwareInterface()

#Tests reading from Arduino
while True:
	print arduinoInterface.getChord()
	
#Tests writing to Arduino
# for x in range(32):
# 	arduinoInterface.setChord(x)
# 	time.sleep(1)
# 	print x

#Tests setting Tau
"""
print arduinoInterface.getTau()
arduinoInterface.setTau(31)
print arduinoInterface.getTau()

while True:
	print arduinoInterface.getChord()
"""

#Tests List to chord
print arduinoInterface.listToChord([1,0,0,0,1])

#Test chord to List
print arduinoInterface.chordToList(0)

