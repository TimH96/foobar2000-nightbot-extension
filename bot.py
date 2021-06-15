"""
bot.py
"""

from config                         import BotConfig
from threading                      import Event
from pywinauto.controls.uiawrapper  import UIAWrapper


class WindowTerminatedError(Exception):
    """Error thrown by bot when window is terminated"""
    pass


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
        while not self.stopped.wait(self.config.interval):
            self._main_loop()

    def stop(self) -> None:
        """Stops bot"""
        self.stopped.set()
        del self.window

    def post_to_nightbot(self, data: str) -> None:
        """Process a given data string to output format and post it to configured API"""
        pass  # TODO

    def _main_loop(self) -> None:
        """Private main loop wrapper"""
        o : str = self.window.window_text()
        if self.window.process_id() is None:
            raise WindowTerminatedError
        if o != self.cur_out:
            self.cur_out = o
            self.post_to_nightbot(o)
