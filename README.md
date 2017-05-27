# eRecords
Testing area for simple electronic health records

Very (very!) simple patient record software, written in python.

## Features
* interactive (command line)
* saves the record as a python pickle, named after the patient's CHI (name: CHI__NUM.data)

## What is CHI?
CHI is Community Health Index number, used in Scotland, format DDMMYYABCE, where DDMMYY is DOB, C is odd/even and indicates male/female respectively, E is a check digit, and ABC allocated uniquely otherwise. It's a unique number for every patient in Scotland.
See https://en.wikipedia.org/wiki/National_Health_Service_Central_Register_(Scotland) for a more detailed description.

## Requirements
* python (2.x)
* tested on linux, should work on other platforms

## Usage
### Interactive
``` $ python erec.py```
### Example programmatic entry
``` $ python example.py```

## TODO
There is a lot to do yet. However, this is merely a proof of concept: EHR does not need to be complex.
This (interactive) prealpha version is only 100 lines of code, and the non-interactive example only 22 lines.
It's obviously not production ready...
