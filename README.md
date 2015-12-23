# Visitor-Python-Wx
A URL driven slideshow in python (now with a GUI)  - an IR showcase tool for the screen or the wall during your next wine + cheese! 

Load a .csv file of URLs, set the type of loop, set the length of time for each visit. 

###What you need


    import os
    import wx
    import csv
    import time
    from webdriverplus import WebDriver
    from itertools import *
    

Firefox is the default broswer for webdriverplus, if you want to use something else see the<a href="https://webdriver-plus.readthedocs.org/en/latest/browsers.html"> webdriverplus docs</a>

Webdriver plus requires an up to date version of <a href="http://www.seleniumhq.org/"> selenium </a> to function. Do it this way: `pip install -U selenium` . . . if you please.

###Usage

1: Start it up from the terminal:     `python visitor.py`

2: Follow the buttons in order: Select the .csv of URLs that you have already prepped (no headers), specify the type of loop, set the length of delay, press start.

3: Have a glass of wine, a piece of cheese, and enjoy the show. 

4: Bring it down by closing the browser, using the stop button, or if you must, a CTRL + C 



###Road Map

1: Bundle as an executable

2: Make the "Stop" button more responsive [thread it . . . ]

3: Get it working with the library's digital signage





