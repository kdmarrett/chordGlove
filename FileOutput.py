#!/usr/bin/env python

# Copyright 2'\x00'14 Matthew D'Asaro
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

class FileOutput():

	def writeFile(self, dictionary, path):
		outputBuffer = ['\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00','\x00']
		#Sort the dictionary by chord integer
		for character, chordValue in dictionary.items():
			outputBuffer[chordValue]=character

		#Write the file
		f = open(path, 'w')
		f.write(b''.join(outputBuffer))
		f.close()

	def readFile(self, path):
		#Read the file
		f = open(path, 'r')
		inputBuffer = f.read()
		f.close()

		#Create and fill the dictionary
		dictionary = dict()
		for i in range(0, len(inputBuffer)):
			dictionary[i]=inputBuffer[i];

		return dictionary
		

