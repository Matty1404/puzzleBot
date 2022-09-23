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
    level3=([[w, w, w, w, w, w, w, w, w, w, w, w],
             [w, p, g, g, g, g, w, w, w, w, w, w],
             [w, w, b, w, w, g, w, w, w, w, w, w],
             [w, w, h, w, w, g, g, g, g, g, w, w],
             [w, w, w, w, w, g, g, g, b, g, w, w],
             [w, w, w, w, w, g, g, g, g, g, w, w],
             [w, w, w, w, w, h, w, w, w, w, w, w],
             [w, w, w, w, w, g, g, g, g, e, w, w],
             [w, w, w, w, w, w, w, w, w, w, w, w],
             [w, w, w, w, w, w, w, w, w, w, w, w],
             [w, w, w, w, w, w, w, w, w, w, w, w]], 1, 1)

  
    currLevel = level3
    yPos = currLevel[1]
    xPos = currLevel[2]
    currBoard = copy.deepcopy(currLevel[0])
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
      elif(self.currBoard[y][x] == self.b):
        return True  #to change
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
              self.currBoard = copy.deepcopy(self.currLevel[0])
              self.yPos = self.currLevel[1]
              self.xPos = self.currLevel[2]
          
            await reaction.remove(user)
            


            await self.msg.edit(content = self.genBoard())
          
            if self.completeLevel:
              print("done")

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