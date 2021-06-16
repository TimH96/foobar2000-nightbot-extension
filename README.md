This is a lightweight bot script that allows Nightbot commands to post information about songs playing in your local foobar2000 player. It works by simply reading out the players window title (which is customizable in foobar2000) and posting it to the Nightbot API. The bot therefore might also work with other media players that similarly put information in the window title.

### Usage

### Dependencies

This bot was build using Python 3.9 and uses the following external modules:

+ ``requests`` module for simple REST interaction
+ ``NightPy`` API wrapper module
+ ``pywinauto`` module for access to window and desktop information