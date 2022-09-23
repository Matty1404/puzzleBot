import discord
from discord.ext import commands
from discord import Intents


class gameBot:
    level1 = ([['#', '#', '#', '#', '#', '#', '#'],
               ['#', '#', '#', '   ', '   ', '   ', 'P'],
               ['#', '#', '#', '   ', '#', '#', '#'],
               ['#', '#', '#', '   ', '#', '#', '#'],
               ['#', 'E', '   ', '   ', '#', '#', '#'],
               ['#', '#', '#', '#', '#', '#', '#'],
               ['#', '#', '#', '#', '#', '#',
                '#']], 1, 6)  #stores y and x value
    currLevel = level1
    YPos = currLevel[1]
    XPos = currLevel[2]
    currBoard = currLevel

    def __init__(self, token):
        self.token = token
        self.bot = commands.Bot(command_prefix="!", intents=Intents.all())

    async def on_ready(self):
        print("logged in as {0.user}".format(self))

    def run(self):
        self.bot.run(self.token)

    def newGame(self):

        @self.bot.command()
        async def newGame(ctx):
            board = ""
            for row in self.currLevel:
                for item in row:
                    board += item
                board += '\n'

            msg = await ctx.reply(board)
            await msg.add_reaction("⬅️")
            await msg.add_reaction("⬆️")
            await msg.add_reaction("⬇️")
            await msg.add_reaction("➡️")
            await msg.add_reaction("🛑")

    async def on_reaction_add(self, reaction, user):
        if user != self.user:

            # if str(reaction.emoji) == "➡️":

            # elif str(reaction.emoji) == "⬅️":

            # elif str(reaction.emoji) == "⬆️":

            # elif str(reaction.emoji) == "⬇️":

            # elif str(reaction.emoji) == "🛑":

            await reaction.remove(user)


bot = gameBot('MTAyMjgxNjExODg3Mzc5MjU2Mg.GrjdKD.gDfHtJHK7k5Qly2kwGMT-mU4AGV0yBq4ong2BA')
bot.run()
