"""
__main__.py

script entrypoint
"""

import json
import inquirer
from pathlib                        import Path
from argparse                       import ArgumentParser, Namespace
from bot                            import FoobarExtensionBot, WindowTerminatedError, InvalidTokenError, NoReplaceTokenFoundError
from config                         import ExtensionConfig
from pywinauto                      import Desktop
from pywinauto.controls.uiawrapper  import UIAWrapper

def _exit() -> None:
    """Controlled script exit"""
    input('Press ENTER to exit')
    exit()

def _build_config() -> dict:
    """Script to build config dict from user inputs"""
    d : dict = {}
    d['api'] = {}
    d['interval'] = 3
    d['api']['cmd_id'] = 'dummy'
    d['api']['client_id'] = input('client_id: ')
    d['api']['client_secret'] = input('client_secret: ')
    d['outtext'] = input('output_text: ')
    # build dummy bot to retrieve command info
    try:
        b : FoobarExtensionBot = FoobarExtensionBot(ExtensionConfig(**d))
    except InvalidTokenError:
        print('error: could not retrive access token with your given credentials')
        _exit()
    except NoReplaceTokenFoundError:
        print(f'error: there was no {FoobarExtensionBot.REPLACE_TOKEN} in your given output')
        _exit()
    # get commands and make user select
    cmds : list = b.get_custom_commands()
    cmd_choice : dict = inquirer.prompt(
        [
            inquirer.List(
                'cmd',
                message='Chosen command:',
                choices=[f'{c.id} {c.command_name}' for c in cmds]
            )
        ]
    )
    id : str = cmd_choice['cmd'].split(' ')[0]
    # build and return config
    d['api']['cmd_id'] = id
    return d

if __name__ == '__main__':
    # parse args
    parser = ArgumentParser(
        description='Reads window data from media player and posts it to Nightbot command',
        allow_abbrev=True
    )
    parser.add_argument(
        '-p', '--path',
        help='path to config json file, default: .\config.json',
        default='./config.json'
    )
    args : Namespace = parser.parse_args()
    args.path = Path(args.path)
    # load config
    config : ExtensionConfig
    bot : FoobarExtensionBot
    try:
        with open(args.path, 'r') as file:
            config = ExtensionConfig(**json.loads(file.read()))
        print('Loaded config.json, edit or delete file to reconfigure')
        bot = FoobarExtensionBot(config)
    except Exception as error:
        print(f'Could not load config.json because of the following error: {error}')
        print('You will now be prompted to configure the bot, refer to the README.md for help')
        config = ExtensionConfig(**_build_config())
        bot = FoobarExtensionBot(config)
        with open(args.path, 'w+') as file:
            file.write(json.dumps(config.to_dict(), indent=4, sort_keys=True))
            print('Valid config, saved to file')
    # get window
    windows = Desktop(backend="uia").windows()
    win_choice : dict = inquirer.prompt(
        [
            inquirer.List(
                'win',
                message='Chosen window:',
                choices=[f'{i} {win.window_text()}' for i, win in enumerate(windows)]
            )
        ]
    )
    index : int = int(win_choice['win'].split(' ')[0])
    chosen_window : UIAWrapper = windows[index]
    # run bot
    try:
        print('Bot running with give config and window')
        bot.run(chosen_window)
    except KeyboardInterrupt:
        bot.stop()
        print('Stopped per KeyboardInterrupt')
    except WindowTerminatedError:
        bot.stop()
        print("error: Window was termianted or could otherwise not be accessed")
        _exit()
