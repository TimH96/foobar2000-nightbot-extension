"""
__main__.py

script entrypoint
"""



from argparse import ArgumentParser
from bot import FoobarExtensionBot, WindowTerminatedError
from config import ExtensionConfig
from pywinauto                      import Desktop
from pywinauto.controls.uiawrapper  import UIAWrapper

def _exit():
    """Controlled script exit"""
    input('Press ENTER to exit')
    exit()
"""
desk = Desktop(backend="uia")
win = desk.windows()
for i, w in enumerate(win):
    print(i, w.window_text())

i = int(input())
w : UIAWrapper = win[i]
"""
c = ExtensionConfig(**{
            'api' : {
                'client_id':'test',
                'client_secret':'test',
                'cmd_id' : '1'
            },
            'interval' : 3,
            'outtext'  : r'Currently Playing: %window%'
        })

b = FoobarExtensionBot(c)#
bla = b.get_custom_commands()
for i in bla:
    print(i.command_name, i.id)


try:
    pass#b.run(w)
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



