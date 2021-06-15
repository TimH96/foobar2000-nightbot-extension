"""
config.py

bot config
"""


class NightbotConfig:
    """Nightbot config interface"""

    def __init__(self, *, client_id: str, client_secret: str, cmd_id: str) -> None:
        self.cmd_id        : str = cmd_id
        self.client_id     : str = client_id
        self.client_secret : str = client_secret


class ExtensionConfig:
    """Bot config interface"""

    def __init__(self, *, interval: int, outtext: str, api: dict) -> None:
        self.interval : int            = interval
        self.outtext  : str            = outtext
        self.api      : NightbotConfig = NightbotConfig(**api)

    def to_dict(self) -> dict:
        """Returns dict representation of """
        return {
            'api' : {
                'key'    : self.api.key,
                'cmd_id' : self.api.cmd_id
            },
            'interval' : self.interval,
            'outtext'  : self.outtext
        }
