"""
bot.py
"""

import json
from config                         import ExtensionConfig, NightbotConfig
from threading                      import Event
from NightPy.nightpy                import NightPy
from requests                       import post, Response
from requests.exceptions            import HTTPError
from pywinauto.controls.uiawrapper  import UIAWrapper


class InvalidTokenError(Exception):
    """Error thrown when Nightbot access token request fails"""
    pass


class NoReplaceTokenFoundError(Exception):
    """Error thrown when no replace token in output string"""
    pass


class WindowTerminatedError(Exception):
    """Error throw when window is terminated"""
    pass


class FoobarExtensionBot():
    """Bot polling a given window and posting its content to Nightbot API"""

    REPLACE_TOKEN  : str = r'%win%'
    TOKEN_ENDPOINT : str = 'https://api.nightbot.tv/oauth2/token'
    STATIC_DEFAULT : str = 'foobar2000 extension is not running'
    STD_INTERVAL   : int = 3

    def __init__(self, config: ExtensionConfig) -> None:
        self.config  : ExtensionConfig = config
        self.stopped : Event = Event()
        self.cur_out : str   = ''
        # check for valid outstring
        if self.config.outtext.find(FoobarExtensionBot.REPLACE_TOKEN) < 0:
            raise NoReplaceTokenFoundError
        # create nightbot api
        self._construct_api(self.config.api)

    def process_output_str(base: str, rep: str) -> str:
        """Replaces token in base with rep"""
        return base.replace(FoobarExtensionBot.REPLACE_TOKEN, rep)

    def run(self, window: UIAWrapper) -> None:
        """Run bot with a given window handle"""
        self.window : UIAWrapper = window
        self.stopped.clear()
        while not self.stopped.wait(self.config.interval):
            self._main_loop()

    def stop(self) -> None:
        """Stops bot"""
        self.stopped.set()
        self.deinit_output()
        del self.window

    def _construct_api(self, config: NightbotConfig) -> None:
        """Gets access token and builds Nightbot API wrapper"""
        # get access token
        try:
            res : Response = post(
                FoobarExtensionBot.TOKEN_ENDPOINT,
                data={
                    'grant_type':    'client_credentials',
                    'scope':         'commands',
                    'client_id':     config.client_id,
                    'client_secret': config.client_secret
                }
            )
            if res.status_code != 200:
                raise HTTPError
        except (HTTPError, KeyError):
            raise InvalidTokenError
        # build api object
        token_d  : dict    = json.loads(res.content)
        self.api : NightPy = NightPy(token_d['access_token'])

    def get_custom_commands(self) -> list:
        """Returns list of known custom commands"""
        return self.api.get_custom_commands()

    def deinit_output(self) -> None:
        """Resets output to static text"""
        self._post_to_nightbot(FoobarExtensionBot.STATIC_DEFAULT)

    def _post_to_nightbot(self, data: str) -> None:
        """Post a given string to configured API"""
        self.api.edit_custom_command_by_id(self.config.api.cmd_id, None, None, data, None, None)

    def _main_loop(self) -> None:
        """Private main loop wrapper"""
        o : str = self.window.window_text()
        if self.window.process_id() is None:
            raise WindowTerminatedError
        if o != self.cur_out:
            self.cur_out = o
            processed : str = FoobarExtensionBot.process_output_str(self.config.outtext, o)
            print(f' >> {processed}')
            self._post_to_nightbot(processed)
