# Background
I have a problem with setting the background of the wxPython control staticText on raspberry pi. Works as expected on Windows 10 but not on a Raspberry pi 3b+ running Raspbian

**UPDATE:** See answer on Stack Overflow: [https://stackoverflow.com/questions/53630830/fails-to-set-bgcolor-on-statictext-on-raspberry-pi-but-not-in-win10](https://stackoverflow.com/questions/53630830/fails-to-set-bgcolor-on-statictext-on-raspberry-pi-but-not-in-win10)

# Installing on Raspberry pi

Goto a folder you want to create project in

`>>cd temp_folder`


Clone this repository

`>>https://github.com/danneedebro/Problem_bgcolor_static_text.git`


Go into newly created folder

`>>cd Problem_bgcolor_static_text/`


Create virtual enviroment

`>>python3 -m venv venv`


Install wxPython from wheel-file

`>>pip3 install wxPython-4.0.3-cp35-cp35m-linux_armv7l.whl`


Run file

`>>python Main.py`
