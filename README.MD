# AutomateAttendance

Small tool built with Selenium that automatically types "Here" under my name in the Google Forms attendance sheet for my ICS4U/TEJ4M classes, saving ~10s each day. The same exact cell needs to be filled every morning I'm present, thus automation is simple.

## How It Works
1. You run the script
2. A browser window is opened and the direct link to your name in the spreadsheet is opened
3. "Here" is typed
> Note: this does **not** run automatically! This script just automates opening and typing into the spreadsheet. So each day that you're present, you have to run it. 

## Instructions
- Download main.py
- **In the user config, Set cellLink to the link to your cell in the spreadsheet**.
    - NOTE: to get your cell, Right click it>View more cell options>Get link to this cell
- Run main.py then wait a few seconds

## Features
- Cross-browser
- Cross-platform
- Fast and efficent
- One less thing to worry about during the day so you can focus on what actually matters
