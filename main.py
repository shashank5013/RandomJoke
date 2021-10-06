  
from replit import db
import discord
import os
import requests 
import json



client=discord.Client()


if "responding" not in db.keys():
  db["responding"] = True


def get_meme():
  ''' Fetches meme images from the internet '''

  response = requests.get("https://meme-api.herokuapp.com/gimme")
  json_object=json.loads(response.text)
  meme_link=json_object['url']
  return meme_link



def get_commands():
  ''' Returns all the commands related to bot '''

  command="`Following commands can be used with the discord bot: \n$meme : View a Random Meme\n$help : Show list of all commands\n$responding {true/false} : Can turn bot on or off`"
  return command

def syntax_error():
  error="`Invalid Command . Use $help`"
  return error


@client.event
async def on_ready():
  ''' Function called when bot is ready to work '''
  print("Hello World")


@client.event
async def on_message(message):
  ''' Function called when a message is received from the user'''
  
  if message.author == client.user:
    return
  msg=message.content
  if msg[0]=='$':
    command=msg[1:]
    if command.split()[0] == "responding":
      value = msg.split("$responding ", 1)[1]
      if value.lower() == "true":
        db["responding"] = True
        await message.channel.send("`Responding is on..`")
      else:
        db["responding"] = False
        await message.channel.send("`Responding is off..`")
    elif db["responding"]:
      if command=='meme':
        await message.channel.send(get_meme())
      elif command =='help':
        await message.channel.send(get_commands())
      else :
        await message.channel.send(syntax_error())

  

client.run(os.environ['TOKEN'])

