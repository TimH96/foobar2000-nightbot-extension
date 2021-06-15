"""
bot.py
"""

from config                         import BotConfig
from threading                      import Event
from pywinauto.controls.uiawrapper  import UIAWrapper


class FoobarExtensionBot():
    """Bot polling a given window and posting its content to Nightbot API"""

    def __init__(self, config: BotConfig) -> None:
        self.config  : BotConfig  = config
        self.stopped : Event      = Event()
        self.cur_out : str        = ''

    def run(self, window: UIAWrapper) -> None:
        """Run bot with a given window handle"""
        self.window : UIAWrapper = window
        self.stopped.clear()        
        while not self.stopped.wait(2):
            self._main_loop()
        
    def stop(self) -> None:
        """Stops thread"""
        self.stopped.set()

    def _main_loop(self) -> None:
        """Private run main loop"""
        print('oiiii')
        print(self.stopped.is_set(), self.stopped)
        
