"""
lib/config.py

bot config
"""

import json


class NightbotConfig:
    """Nightbot config interface"""
    
    def __init__(self) -> None:
        pass  # define nightbot fields


class BotConfig:
    """Bot config interface"""

    def __init__(self) -> None:
        pass

    def from_file(self, path: str) -> None:
        pass

    def to_file(self, path: str) -> None:
        pass

    def from_dict(self, d: dict) -> None:
        pass

    def to_dict(self) -> dict:
        pass
