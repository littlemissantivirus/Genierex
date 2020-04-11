from discord.ext import commands
import discord
import jishaku
import json
import logging

class Genierex(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.admins: list = json.load(open('data/configs/admins.json'))
        self.config: dict = json.load(open('data/configs/config.json'))

        logging.basicConfig(filename='logs/genierex.log', level=logging.INFO,
                            format='[%(asctime)s %(levelname)s] %(message)s', datefmt="%H:%M:%S")
        self.logger = logging.getLogger('Genierex')
        
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s %(levelname)s] %(message)s', datefmt="%H:%M:%S")
        console.setFormatter(formatter)
        self.logger.addHandler(console)

        self.load_extensions()
    
    def load_extensions(self):
        extensions = jishaku.modules.resolve_extensions(self, 'cogs.*')
        for ext in extensions:
            try:
                self.load_extension(ext)
                self.logger.info(f"Loaded {ext[5:]}!")
            except Exception as ex:
                self.logger.warn(f"Was unable to load the extension {ext}!\nStacktrace:{ex}")
