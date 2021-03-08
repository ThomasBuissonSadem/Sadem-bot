import discord
from discord.ext import commands
import os

# Variable Globales
intents = discord.Intents.all()
token = os.getenv("DISCORD_BOT_TOKEN")
guild_id = os.getenv("GUILD_ID")
client = commands.Bot(command_prefix=".", intents=intents)

# Traitement au démarrage du bot
@client.event
async def on_ready():
    print('Démarrage du Bot : {0.user}'.format(client))
    print(f'ID : {client.guild.id}')

# Envoi un message aux admin lorsqu'un utilisateur rejoint le serveur
@client.event
async def on_member_join(newMember):
    try:
        guild = client.get_guild(int(guild_id))
        for member in guild.members:
            for role in member.roles:
                if(role.name.lower() == "Administrateurs".lower()):
                    await member.send(f'L\'utilisateur @{newMember.name} vient de rejoindre le serveur {guild.name}.')
    except discord.ext.commands.errors.MissingRole:
        await ctx.send("vous n'avez pas la permission d'utiliser cette commande.")

# Commande permettant de supprimer 10 messages sur le channel concerné
@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

#Commandes pour tester des fonctionnalités 
@client.command()
@commands.has_role('Administrateurs')
async def testing(ctx):
    await ctx.send(f'{guild_id}')
    await ctx.send(f'{client.guild.id}')
        

client.run(token)