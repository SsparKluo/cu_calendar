# CUHK Timetable Generator
This is a py file for automatically timetable generating for **NEW** CUSIS.

## Required package
This program required `ics` module to generate `.ics` file. You need to use 
```
pip install ics
``` 
to install `ics` module before start.

## Usage
1. Copy all the information of **all** your classes from *View My Classes* page in CUSIS.
2. Paste the information into a plaintext file (For example `.exe` file) and copy it's path(relevant of absolute) if you want to.
3. run the program
    ```
    python cu_tt.py
    ```
    and follow the instruction in program.
4. You can import this `.ics` file to your google calendar or iCal or other calendar app. I suggest you to create a new calendar for this file because it will be convenient to delete if there is any bug LOL.

## Other
1. The calendar will be generated based on the information provided by CUSIS, and there may be some misinformation in CUSIS. For example, the timetables about college assemblies.
2. I wrote the program totally based on my computer and timetable, so there must be some bugs. You can edit the program or post in *Issues* or email me: <ssparkluo@gmail.com>
3. Maybe you can give me a star if this is helpful.
