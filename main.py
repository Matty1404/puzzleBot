import discord
from discord.ext import commands
from discord import Intents
import os
import copy


class gameBot:


  w = ':brown_square:'
  p = ':slight_smile:'
  g = ':black_large_square:'
  e = ':green_square:'
  h = ':o:'
  b = ':red_circle:'
  t = ':white_square_button:'

  levels = {
    "level1":([[w, w, w, w, w, w], 
               [w, p, g, g, w, w], 
               [w, w, w, g, w, w], 
               [w, w, w, e, w, w], 
               [w, w, w, w, w, w], 
               [w, w, w, w, w, w]], 1, 1),
  
    
    "level2": ([[w, w, w, w, w, w, w, w, w, w, w, w],
            [w, p, g, g, g, w, w, w, w, w, w, w],
            [w, w, w, w, g, w, w, w, w, w, w, w],
            [w, w, w, w, g, w, w, w, w, w, w, w],
            [w, w, w, w, g, g, g, w, w, w, w, w],
            [w, w, w, w, g, w, g, w, w, w, w, w],
            [w, w, w, w, g, g, g, w, w, w, w, w],
            [w, w, w, w, w, w, g, w, w, w, w, w],
            [w, w, w, w, w, w, g, w, w, w, w, w],
            [w, w, w, w, w, w, e, w, w, w, w, w],
            [w, w, w, w, w, w, w, w, w, w, w, w],], 1, 1),

  
    "level3":([[w, w, w, w, w, w, w, w, w, w, w, w],
             [w, p, g, g, g, g, w, w, w, w, w, w],
             [w, w, b, w, w, g, w, w, w, w, w, w],
             [w, w, h, w, w, g, g, g, g, g, w, w],
             [w, w, w, w, w, g, g, g, b, g, w, w],
             [w, w, w, w, w, g, g, g, g, g, w, w],
             [w, w, w, w, w, h, w, w, w, w, w, w],
             [w, w, w, w, w, g, g, g, g, e, w, w],
             [w, w, w, w, w, w, w, w, w, w, w, w],
             [w, w, w, w, w, w, w, w, w, w, w, w]], 1, 1),
  
    "level4": ([[w, w, w, w, w, w, w, w, w, w, w, w],
                [w, p, g, g, w, w, w, w, w, w, w, w],
                [w, g, g, b, g, w, w, w, w, w, w, w],
                [w, g, g, g, g, g, g, h, h, g, w, w],
                [w, w, h, w, w, w, w, w, w, g, w, w],
                [w, w, g, w, g, g, g, g, w, e, w, w],
                [w, w, g, w, g, b, g, g, w, w, w, w],
                [w, w, g, g, g, g, g, g, w, w, w, w],
                [w, w, w, w, g, b, g, g, w, w, w, w],
                [w, w, w, w, w, w, w, w, w, w, w, w]], 1, 1), 

    "level5" : ([[w, w, w, w, w, w, w, w, w, w, w, w],
                 [w, p, g, g, g, g, w, w, w, w, w, w],
                 [w, g, g, b, g, g, w, w, w, w, w, w],
                 [w, g, g, g, g, h, w, w, w, w, w, w],
                 [w, w, g, h, g, h, h, g, g, g, e, w],
                 [w, w, g, h, g, h, g, h, w, w, w, w],
                 [w, w, g, h, g, h, g, h, h, h, w, w],
                 [w, w, g, g, g, g, g, g, g, h, w, w],
                 [w, w, g, g, h, h, g, g, g, h, w, w],
                 [w, w, w, w, w, w, w, w, w, w, w, w]], 1, 1)
  
  }

  levelArray = ["level1", "level2", "level3", "level4", "level5"]
  currLevel = levelArray[0]
  yPos = levels[currLevel][1]
  xPos = levels[currLevel][2]
  currBoard = copy.deepcopy(levels[currLevel][0])
  completeLevel = False
  msg = None

  def __init__(self, token):
      self.token = token
      self.bot = commands.Bot(command_prefix="!", intents=Intents.all())

  async def on_ready(self):
      print("logged in as {0.user}".format(self.bot))

  def run(self):
      self.bot.run(self.token)


  def genBoard(self):
    board = ""
    for row in self.currBoard:
        for item in row:
            board += item
        board += '\n'
    return board

  async def newGame(self,ctx):
    mess = await ctx.reply(self.genBoard())
    self.msg = mess
    await mess.add_reaction("⬅️")
    await mess.add_reaction("⬆️")
    await mess.add_reaction("⬇️")
    await mess.add_reaction("➡️")
    await mess.add_reaction("🛑")      

  def isValidMove(self, x, y):
    if ((not 0 <= y < len(self.currBoard)) or (not 0 <= x < len(self.currBoard[0])) or self.currBoard[y][x] == self.w or self.currBoard[y][x] == self.h):
      return False
    elif self.currBoard[y][x] == self.e:
      self.completeLevel = True
      return True
    return True

  def checkNext(self, y, x):
    if ((not 0 <= y < len(self.currBoard)) or (not 0 <= x < len(self.currBoard[0])) or self.currBoard[y][x] == self.w or self.currBoard[y][x] == self.e):
      return False
    
    return True


  async def on_reaction_add(self, reaction, user):
      if user != self.bot.user:
  
          if str(reaction.emoji) == "➡️":
            if (self.isValidMove(self.xPos + 1, self.yPos)):

              if (self.currBoard[self.yPos][self.xPos + 1] == self.b):
                if (self.checkNext(self.yPos, self.xPos + 2)):
                  if (self.currBoard[self.yPos][self.xPos + 2] == self.h):
                    self.currBoard[self.yPos][self.xPos + 2] = self.g 
                  else:
                    self.currBoard[self.yPos][self.xPos + 2] = self.b
                  self.currBoard[self.yPos][self.xPos] = self.g
                  self.currBoard[self.yPos][self.xPos + 1] = self.p
                  self.xPos += 1
              else:  
                self.currBoard[self.yPos][self.xPos] = self.g
                self.currBoard[self.yPos][self.xPos + 1] = self.p
                self.xPos += 1
          elif str(reaction.emoji) == "⬅️":
            if (self.isValidMove(self.xPos - 1, self.yPos)):

              if (self.currBoard[self.yPos][self.xPos - 1] == self.b):
                if (self.checkNext(self.yPos, self.xPos - 2)):
                  if (self.currBoard[self.yPos][self.xPos - 2] == self.h):
                    self.currBoard[self.yPos][self.xPos - 2] = self.g
                  else:
                    self.currBoard[self.yPos][self.xPos - 2] = self.b
                  self.currBoard[self.yPos][self.xPos] = self.g
                  self.currBoard[self.yPos][self.xPos - 1] = self.p
                  self.xPos -= 1
                  
              else:
                self.currBoard[self.yPos][self.xPos] = self.g
                self.currBoard[self.yPos][self.xPos - 1] = self.p
                self.xPos -= 1
          
          elif str(reaction.emoji) == "⬆️":
            if (self.isValidMove(self.xPos, self.yPos - 1)):

              if (self.currBoard[self.yPos - 1][self.xPos] == self.b):
                if (self.checkNext(self.yPos - 2, self.xPos)):
                  if (self.currBoard[self.yPos - 2][self.xPos] == self.h):
                    self.currBoard[self.yPos - 2][self.xPos] = self.g
                  else:
                    self.currBoard[self.yPos - 2][self.xPos] = self.b
                  self.currBoard[self.yPos][self.xPos] = self.g
                  self.currBoard[self.yPos - 1][self.xPos] = self.p
                  self.yPos -= 1

              else:
                self.currBoard[self.yPos][self.xPos] = self.g
                self.currBoard[self.yPos - 1][self.xPos] = self.p
                self.yPos -= 1

          elif str(reaction.emoji) == "⬇️":
            if (self.isValidMove(self.xPos, self.yPos + 1)):

              if (self.currBoard[self.yPos + 1][self.xPos] == self.b):
                if (self.checkNext(self.yPos + 2, self.xPos)):
                  if (self.currBoard[self.yPos + 2][self.xPos] == self.h):
                    self.currBoard[self.yPos + 2][self.xPos] = self.g
                  else:
                    self.currBoard[self.yPos + 2][self.xPos] = self.b
                  self.currBoard[self.yPos][self.xPos] = self.g
                  self.currBoard[self.yPos + 1][self.xPos] = self.p
                  self.yPos += 1  
              else:
                self.currBoard[self.yPos][self.xPos] = self.g
                self.currBoard[self.yPos + 1][self.xPos] = self.p
                self.yPos += 1

          elif str(reaction.emoji) == "🛑":
            self.currBoard = copy.deepcopy(self.levels[self.currLevel][0])
            self.yPos = self.levels[self.currLevel][1]
            self.xPos = self.levels[self.currLevel][2]
        
          await reaction.remove(user)
          
          if self.completeLevel:  
            self.nextLevel()
            self.completeLevel = False

          await self.msg.edit(content = self.genBoard())

  def nextLevel(self):
    level = self.levelArray.index(self.currLevel) + 1
    if level < len(self.levelArray):
      self.currLevel = self.levelArray[level]
      self.yPos = self.levels[self.currLevel][1]
      self.xPos = self.levels[self.currLevel][2]
      self.currBoard = copy.deepcopy(self.levels[self.currLevel][0])
    else:
      print("congrats")

bot = gameBot(os.environ['DTOKEN'])

@bot.bot.event
async def on_reaction_add(reaction, user):
  await bot.on_reaction_add(reaction, user)

@bot.bot.event
async def on_ready():
  await bot.on_ready()

@bot.bot.command()
async def newGame(ctx):
  await bot.newGame(ctx)

bot.run()