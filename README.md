This is a lightweight bot script that allows Nightbot commands to post information about songs playing in your local foobar2000 player. It works by simply reading out the players window title (which is customizable in foobar2000) and posting it to the Nightbot API. The bot therefore might also work with other media players that similarly put information in the window title.

### Usage

#### Install

To install, you can either clone the repo and install the listed dependencies:

```bash
$ git clone https://github.com/TimH96/foobar2000-nightbot-extension
$ pip install requests
$ pip install NightPy
$ pip install pywinauto
```

Or you can simply download and run the latest executable from the [releases page](https://github.com/TimH96/foobar2000-nightbot-extension/releases).

#### Config

The bot will need to be configured upon first execution with the following information:

+ ``client_id`` and ``client_secret`` are required to interact with the Nightbot API. You will need to make an application on [this page](https://nightbot.tv/account/applications) (name it ``FoobarExtension`` or something along those lines, you can leave the redirect URI field empty) and get your client ID and secret from there.
+ ``output_text`` is the text that shows when using the command. Use ``%win%`` as a substitute for the actual information in the window title, for example ``Currently playing: %win%``. There will be an error if you don't use the ``%win%`` token in your output text.
+ ``cmd_id`` is which command to ultimately change and post the song information to. Simply type in the number corresponding to your desired command from the given list.

#### Run

After the configuration, simply run the exectuable. Upon each run you will be prompted to select which window to take the information from. If you ever want to change your configuration, you can manually edit the ``config.json`` or delete/move it and reconfigure from scratch. Note that you can also use alternative paths to the config file via the ``--path``/``-p`` command line argument.

### Dependencies

This bot was build using Python 3.9 and uses the following external modules:

+ ``requests`` module for simple REST interaction
+ ``NightPy`` API wrapper module
+ ``pywinauto`` module for access to window and desktop information