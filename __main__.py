"""
__main__.py

script entrypoint
"""

from argparse import ArgumentParser
from bot import FoobarExtensionBot, WindowTerminatedError
from config import ExtensionConfig

c = ExtensionConfig(**{
            'api' : {
                'key'    : '',
                'cmd_id' : 1
            },
            'interval' : 3,
            'outtext'  : ''
        })

b = FoobarExtensionBot(c)

try:
    b.run()
except KeyboardInterrupt:
    b.stop()
except WindowTerminatedError:
    b.stop()
    print("yo smth went wrong bro")
    
# parse config

# build desktop object

# get all windows

# let user pick window

# create and run bot with config


"""

from pywinauto                      import Desktop
from pywinauto.controls.uiawrapper  import UIAWrapper

desk = Desktop(backend="uia")
win = desk.windows()
for i, w in enumerate(win):
    print(i, w.window_text())

i = int(input())
b : UIAWrapper = win[i]



def get_desktop(backend: str = 'uia') -> Desktop:
    return Desktop(backend=backend)


while True:
    print(b.process_id())  # process id goes None when gone
    print(b.window_text())
    print(b.handle)
"""
