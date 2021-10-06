
import discord
import os
import requests 
import json



client=discord.Client()
def get_meme():
  response = requests.get("https://meme-api.herokuapp.com/gimme")
  json_object=json.loads(response.text)
  meme_link=json_object['url']
  return meme_link

def get_commands():
  command="`Following commands can be used with the discord bot: \n$meme : View a Random Meme\n$help : Show list of all commands\n`"
  return command

def syntax_error():
  error="`Invalid Command . Use $help`"
  return error

@client.event
async def on_ready():
  print("Hello World")


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg=message.content
  if msg[0]=='$':
    command=msg[1:]
    
    if command=='meme':
      await message.channel.send(get_meme())
    elif command =='help':
      await message.channel.send(get_commands())
    else :
      await message.channel.send(syntax_error())

  


client.run(os.environ['TOKEN'])

