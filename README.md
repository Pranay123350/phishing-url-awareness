# Phishing URL Awareness Checker

An educational project for EWB to detect suspicious phishing URLs.

## What it does
This Python tool checks URLs for common phishing tricks:
- IP address instead of domain name
- @ symbol trick
- Too many dots / too long URL
- No HTTPS

## How to Run
```bash
python phishing_checker.pyThen enter any URL to check.
Example:javascriptEnter URL to check: http://192.168.1.1@google.com
Result: SUSPICIOUS - URL contains IP address, URL contains @ symbolFiles
phishing_checker.py - Main logicrequirements.txt - DependenciesREADME.md - DocumentationFor EWB
This is an awareness tool, not a 100% security solution. Purpose is to teach how phishing URLs look.
Author: Pranay123350
