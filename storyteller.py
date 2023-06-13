import logging
import time

import discord
from colorama import Back, Fore, Style
from discord.ext import commands
import os
import platform

import config

MY_GUILD = discord.Object(id=config.botConfig["hub-server-guild-id"])


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!-&%XC', intents=discord.Intents.all())

    async def setup_hook(self):
        for fileName in os.listdir('./Commands'):
            if fileName.endswith('.py'):
                await self.load_extension(f'Commands.{fileName[:-3]}')

        await self.tree.sync()

    async def on_ready(self):
        pfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC",
                                                       time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        print(f"{pfx} Logged in as {Fore.YELLOW} {self.user.name}")
        print(f"{pfx} Bot ID {Fore.YELLOW} {str(self.user.id)}")
        print(f"{pfx} Discord Version {Fore.YELLOW} {discord.__version__}")
        print(f"{pfx} Python Version {Fore.YELLOW} {str(platform.python_version())}")
        print(f"{pfx} Bot Version 0.1")
        # db.init_database(config.botConfig)
        logging.warning("Now logging..")


client = Client()
client.run(config.botConfig["token"])
