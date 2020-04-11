from core.genierex import Genierex
import json

bot = Genierex(
    command_prefix="genie ",
    help_command=None, 
    case_insensitive=True,
    owner_id=247143014575636480)

bot.run(bot.config['token'])