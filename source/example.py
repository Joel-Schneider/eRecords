#!/usr/bin/env python

from erec import patientRecord, notesEntry
import time

bob = patientRecord("1234")
bob.addEntry("Dr X", "Abdo pain ? cause")
time.sleep(0.5)
bob.addEntry("Dr Y", "Obs stable, apyrexial, continue")
time.sleep(0.5)
bob.addEntry("RAD", "Fit for d/c")

bob.displayAllEntries()
print "\n\n"

bob.editEntry(1, "Ed.", "Edited")
bob.editEntry(1, "Dr P", "Er, no")
bob.displayEntry(1, allVersions = True)
print "\n\nCurrent:"
bob.displayEntry(1)

bob.saveRecords()