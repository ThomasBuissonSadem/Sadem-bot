import discord
import asyncio
from discord.ext import commands
import os

# Variable Globales
intents = discord.Intents.all()
token = os.getenv("DISCORD_BOT_TOKEN")
client = commands.Bot(command_prefix=".", intents=intents)

# Traitement au démarrage du bot
@client.event
async def on_ready():
    print('Démarrage du Bot : {0.user}'.format(client))

# Envoi un message aux admin lorsqu'un utilisateur rejoint le serveur
@client.event
async def on_member_join(newMember):
    guild = newMember.guild
    for member in guild.members:
        for role in member.roles:
            if(role.name.lower() == "Administrateurs".lower()):
                await member.send(f'L\'utilisateur {newMember.name} vient de rejoindre le serveur {guild.name}.')


# Commande permettant de supprimer 10 messages sur le channel concerné
@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

#Commandes pour tester des fonctionnalités 
@client.command()
@commands.has_role('Administrateurs')
async def testing(ctx):
    await ctx.send('testing')


client.run(token)