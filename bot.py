"""
bot.py
"""

from config                         import BotConfig
from pywinauto.controls.uiawrapper  import UIAWrapper


class FoobarExtensionBot:
    """Bot polling a given window and posting its content to Nightbot API"""

    def __init__(self, config: BotConfig) -> None:
        self.config  : BotConfig  = config
        self.cur_out : str        = ''

    def run(self, window: UIAWrapper) -> None:
        """Run bot with a given window handle"""
        self.window : UIAWrapper = window
        self._run()
        