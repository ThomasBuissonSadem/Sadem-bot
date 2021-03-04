import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
    print('Démarrage du Bot : {0.user}'.format(client))

# Commande permettant de supprimer 5 messages sur le channel concerné
@client.command()
async def clear(ctx, amount=5) :
    await ctx.channel.purge(limit=amount)

client.run(token)