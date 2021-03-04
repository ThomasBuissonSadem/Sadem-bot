import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Démarrage du Bot : {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.content.startswith('hello'):
      for member in message.guild.members:
        print(f'Membre: {member} \n')
        if 'Administrateurs' in member.roles:
          print(f'MESSAGE')
          await member.send("Hello")
  

client.run(os.getenv('TOKEN')) 