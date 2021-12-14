from discord.ext import commands
from json import load

class EmberBot(commands.AutoShardedBot):

    def __init__(self, **kwargs):
        with open("./config.json") as file:
            self.config = load(file)

        super().__init__(command_prefix=self.config["attributes"]["prefix"],
                         description=self.config["attributes"]["description"],
                         **kwargs)

    def begin(self):
        self.run(self.config["token"])

