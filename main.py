import discord
from discord.ext import commands
from discord import Intents

bot = commands.Bot(command_prefix='.', intents=Intents.all())

level1 = [['#','#','#','#','#','#','#'],
          ['#','#','#','   ','   ','   ','P'],
          ['#','#','#','   ','#','#','#'],
          ['#','#','#','   ','#','#','#'],
          ['#','E','   ','   ','#','#','#'],
          ['#','#','#','#','#','#','#'],
          ['#','#','#','#','#','#','#']
         ]

currLevel = level1

currBoard = currLevel

@bot.event
async def on_ready():
    print("logged in as {0.user}".format(bot))

@bot.command()
async def newGame(ctx):
  board = ""
  for row in level1:
    for item in row:
      board += item
    board += '\n'
    
  msg = await ctx.reply(board) 
  await msg.add_reaction("⬅️")
  await msg.add_reaction("⬆️")
  await msg.add_reaction("⬇️")
  await msg.add_reaction("➡️")
  await msg.add_reaction("🛑")
  

@bot.event
async def on_reaction_add(reaction, user):
    if user != bot.user:
        if str(reaction.emoji) == "➡️":
            
        elif str(reaction.emoji) == "⬅️":

        elif str(reaction.emoji) == "⬆️":

        elif str(reaction.emoji) == "⬇️":

        elif str(reaction.emoji) == "🛑":
          
        await reaction.remove(user)


bot.run(
    "MTAyMjU4MjI4NDIzNjM3ODE1Mg.GUpnGv.S5XW3qqETgNDwwcjzrT9tGb33lLvGTPkP5ugpw")