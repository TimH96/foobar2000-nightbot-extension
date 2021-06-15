"""
config.py

bot config
"""


class NightbotConfig:
    """Nightbot config interface"""

    def __init__(self, *, key: str, cmd_id: int) -> None:
        self.key    : str = key
        self.cmd_id : int = cmd_id


class BotConfig:
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
