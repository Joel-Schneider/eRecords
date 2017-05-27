#!/usr/bin/env python

import pickle, random, time, os, os.path, sys

class patientRecord:
	def __init__(self, CHI = False):
		if not CHI:
			CHI = random.randint(0101010000,3112999999)
		self.file = str(CHI)+".data"
		self.entries = []
		if os.path.isfile(self.file):
			self.loadRecords()
	def addEntry(self, UID, content):
		entry = notesEntry(UID, content)
		self.entries.append(entry)
	def editEntry(self, entryID, UID, content):
		self.entries[entryID].editEntry(UID, content)
	def displayAllEntries(self, allVersions = False):
		count = 0
		for entry in self.entries:
			count += 1
			print "E: ", count,
			entry.display(allVersions)
		count = 0
	def displayEntry(self, entryID, allVersions = False):
		self.entries[entryID].display(allVersions)
	def saveRecords(self):
		fileHandle = open(self.file, 'wb')
		pickle.dump(self, fileHandle)
	def loadRecords(self):
		fileHandle = open(self.file, 'rb')
		oldself = pickle.load(fileHandle)
		self.entries = oldself.entries

class notesEntry:
	def __init__(self, UID = False, content = False):
		self.versions = []
		self.count = 0
		self.editEntry(UID, content)
	def editEntry(self, UID, content):
		self.count += 1
		self.versions.append((self.count, UID, content, time.localtime()))
	def display(self, showOld = False):
		if self.versions == []:
			print "(No entry)"
		elif showOld == False:
			(version, UID, content, timestamp) = self.versions[self.count - 1]
			print "\tV: ", version, "\t", UID, "\t", timeFormat(timestamp), "\t", content
			return
		else:
			for item in self.versions:
				(version, UID, content, timestamp) = item
				if showOld:
						print "\tV: ", version, "\t", UID, "\t", timeFormat(timestamp), "\t", content


def menu():
	while True:
		print "Options:"
		print "1. Open record"
		print "2. Add entry"
		print "3. Edit entry"
		print "4. View records"
		print "5. View records (all versions)"
		print "6. Save record"
		print "7. Quit"
		option = input(": ")
		if option == 1:
			patientID = raw_input("patientID:\t")
			currentPatient =""
			currentPatient = patientRecord(patientID)
			print "Opened"
		elif option == 2:
			content = raw_input("Content:\t")
			UID = raw_input("Sign:\t")
			currentPatient.addEntry(UID, content)
		elif option == 3:
			ID = input("Entry ID:\t")
			currentPatient.displayEntry(ID)
			content = raw_input("New content:\t")
			UID = raw_input("Sign:\t")
			if UID != "":
				if content != "":
					currentPatient.editEntry(ID, UID, content)
		elif option == 4:
			currentPatient.displayAllEntries()
		elif option == 5:
			currentPatient.displayAllEntries(allVersions = True)
		elif option == 6:
			currentPatient.saveRecords()
		elif option == 7:
			return
		else:
			print "Error, try again"

def timeFormat(timestamp):
	return time.strftime("%d/%m/%y %H:%M", timestamp)

menu()
