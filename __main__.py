"""
__main__.py

script entrypoint
"""

from argparse import ArgumentParser
from bot import FoobarExtensionBot
from config import BotConfig

c = BotConfig(**{
            'api' : {
                'key'    : '',
                'cmd_id' : 1
            },
            'interval' : 0.5,
            'outtext'  : ''
        })

b = FoobarExtensionBot(c)

try:
    b.run()
except KeyboardInterrupt:
    b.stop()

# parse config

# build desktop object

# get all windows

# let user pick window

# create and run bot with config

