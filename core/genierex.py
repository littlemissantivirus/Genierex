from discord.ext import commands
import discord
import json
import jishaku

class Genierex(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.admins: list = json.load(open('data/configs/admins.json'))
        self.config: dict = json.load(open('data/configs/config.json'))

        self.load_extensions()
    
    def load_extensions(self):
        extensions = jishaku.modules.resolve_extensions(self, 'cogs.*')
        for ext in extensions:
            try:
                self.load_extension(ext)
                print(f"Loaded {ext[5:]}!")
            except Exception as ex:
                print(f"Was unable to load the extension {ext}!\nStacktrace:{ex}")
