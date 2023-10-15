# AutomateAttendance

Small tool built with Selenium that automatically types "Here" under my name in the Google Forms attendance sheet for my classes, saving ~10s each day. The same exact cell needs to be filled every morning I'm present, thus automation is simple.

## How It Works
1. You run the script
2. A browser window is opened and it navigates to your name in the spreadsheet via the direct link
3. "Here" is typed
> Note: this does **not** happen automatically on a scheduled basis! This program just automates opening and typing into the spreadsheet so each day that you're present, you have to start it.

## Instructions/Setup
Pre-requisites: Python 3

- Download main.py
- **In the user config, set cellLink to the link to your cell in the spreadsheet**.
    - NOTE: to get it, Right click the specific cell>View more cell options>Get link to this cell
- Uncomment/comment whatever browser you use (Chrome, Firefox, Edge, etc.)
- Run main.py then wait a few seconds

## Features
- Cross-browser
- Cross-platform
- Fast and efficent
- One less thing to worry about during the day so you can focus on what actually matters
