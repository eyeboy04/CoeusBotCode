import discord, colorama, nekos
from colorama import Fore, Back, Style
from colorama import init
from discord.ext import commands
import requests
import random
import asyncio
import re
import json
import sys, traceback
from random import randint
import math
import uuid
import urllib
import aiohttp
import os
import functools
import unicodedata
import time 
import random
import pyTigerGraph as tg
import akinator as ak
import urllib.request as u
import xml.etree.ElementTree as et
import rule34
from urllib import request
from itertools import cycle
from aiohttp import request
from PIL import Image,ImageFont,ImageDraw,ImageOps
from io import BytesIO
from urllib.parse import quote_plus
from collections import deque
from discord.ext.commands import cooldown, BucketType
from discord.ext.commands import has_permissions, MissingPermissions, CheckFailure
from discord import DMChannel
from datetime import datetime   
from pytz import timezone
from discord.ext.commands import clean_content
from typing import Union
from functools import partial
from discord import RawReactionActionEvent
from operator import itemgetter

os.chdir("removed for safety purposes")
intents = discord.Intents.all()
intents.members = True

def get_prefix(client, message):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)
	return prefixes[str(message.guild.id)]
	
client = commands.Bot(command_prefix = (get_prefix) , intents=intents)
ltime = time.asctime(time.localtime())
r = rule34.Rule34
client.remove_command("help")

acceptableImageFormats = [".png",".jpg",".jpeg",".gif",".gifv",".webm",".mp4","imgur.com"]
memeHistory = deque()
memeSubreddits = ["BikiniBottomTwitter", "memes", "2meirl4meirl", "deepfriedmemes", "MemeEconomy"]
awwSubreddits = ["Eyebleach", "aww", "StuffOnCats", "PuppySmiles", "tuckedinkitties", "Catloaf"]


def xmlparse(str):
    root = et.parse(u.urlopen(str))
    for i in root.iter('post'):
        fileurl = i.attrib['file_url']
        return fileurl

def xmlcount(str):
    root = et.parse(u.urlopen(str))
    for i in root.iter('posts'):
        count = i.attrib['count']
        return count

def pidfix(str):
    ye = int(xmlcount(r.urlGen(tags=str,limit=1)))
    ye = ye - 1
    return ye

def rdl(str,int):
    print(f'[INFO {ltime}]: integer provided: {int}')

    if int > 2000:
        int = 2000
    if int == 0:
        int == 0
        print(f'[INFO {ltime}]: Integer is 0, accommodating for offset overflow bug. ') 
    elif int != 0:  
        int = random.randint(1,int)
    print(f'[INFO {ltime}]: integer after randomizing: {int}')
    xurl = r.urlGen(tags=str,limit=1,PID=int)
    print(xurl)
    wr = xmlparse(xurl)
    
    if 'webm' in wr:
        if 'sound' not in str:
            if 'webm' not in str:
                print(f'[INFO {ltime}]: We got a .webm, user didnt specify sound. Recursing. user tags: {str}')
                wr = rdl(str,pidfix(str))
        else:
            pass
    elif 'webm' not in wr:
        print(f'[INFO {ltime}]: Not a webm, dont recurse.')
    return wr

@client.event
async def on_command_error(ctx, error):
	print(error)


@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game(name="nl!help | 121 Commands"))
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
    

@client.command(name='Anon', aliases=['anon'])
async def Anon(ctx, *, msg):
	await ctx.send("{}" .format(msg))
	await ctx.message.delete()


@client.command(name='Hotlines', aliases=['hotlines'])
async def Hotlines(ctx):
    embed = discord.Embed(
        title = 'Helplines', 
        description = 'Here is a list of continents with links to websites which show helplines in those continents, nearly every country has a helpline ^-^. If you need to talk to someone theres always people on the server too',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_image(url='https://cdn.dribbble.com/users/506831/screenshots/5807495/ok-to-ask-for-help.gif')
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    icon_url=('https://assets.change.org/photos/5/oe/en/wVoEENmUBcLEAhU-800x450-noPad.jpg?1531231373')
    embed.add_field(name='Africa', value='https://www.iasp.info/resources/Crisis_Centres/Africa/page-1.html?s=A', inline=True)
    embed.add_field(name='Asia', value='https://www.iasp.info/resources/Crisis_Centres/Asia/', inline=False)
    embed.add_field(name='Australia and Oceania', value='https://trystressmanagement.com/mental-health-resources/australia-and-oceanias-hotlines/', inline=False)
    embed.add_field(name='Europe', value='https://www.mhe-sme.org/library/youth-helplines/?', inline=False)
    embed.add_field(name='North America', value='https://www.iasp.info/resources/Crisis_Centres/North_America/', inline=False)
    embed.add_field(name='South America', value='https://www.iasp.info/resources/Crisis_Centres/South_America/', inline=False)

    await ctx.message.delete()
    await ctx.author.send(embed=embed)

@client.command(name='avatar', aliases=['Avatar'])
async def avatar(ctx, member: discord.Member):
    show_avatar = discord.Embed(

        color = discord.Color.dark_blue()
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    show_avatar.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=show_avatar)

@client.command()
async def help(ctx):
	embed=discord.Embed(title=" ", description=f"Welcome to Coeus Bots help menu")
	embed.set_author(name="Coeus Bot Help", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	embed.add_field(name = ":slight_smile: **Actions** - `nl!actions`", value = "These commands show your emotions by sending gifs", inline=False)
	embed.add_field(name = ":wrench: **Admin** - `nl!admin`", value = "These commands are to be used only by admins and normal members can not use them", inline=False)
	embed.add_field(name = ":8ball: **Fun** - `nl!fun`", value = "These commands allow you to have fun and joke around with other members", inline=False)
	embed.add_field(name = ":frame_photo: **Images** - `nl!images`", value = "These commands are to do with image manipulation or they showcase images", inline=False)
	embed.add_field(name = ":grey_question: **Misc.** - `nl!misc`", value = "These commands do not fit into any other category so they are in their own separate category", inline=False)
	embed.add_field(name = ":warning: **NSFW** - `nl!nsfw`", value = "These commands are highly nsfw so if you use them you accept to seeing in detail photos and gifs", inline=False)
	embed.add_field(name = ":space_invader: **Reddit** - `nl!reddit`", value   = "These commands display subreddit images", inline=False)
	embed.add_field(name = ":performing_arts: **Social** - `nl!social`", value = "These commands are to do with social actions towards other people and other actions", inline=False)
	embed.add_field(name = ":scroll: **Text** - `nl!text`", value = "These commands are to do with editing messages in fun ways", inline=False)
	embed.set_footer(text="Coeus Bot#5544 made by I Am A Trash Panda#5717", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	embed.add_field(name = "Note : The bot is case sensitive so if you would like extra info on commands make sure your command follows the same capitalization as it says above.", value = "_ _")
	await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def admin(ctx):
	embed = discord.Embed(title = "`Some commands dont have an example as its a stand alone command`\n \n<command> ✿ <explanation> ✿ <example>", description = "nl!announce ✿ Announce something in a channel ✿ nl!announce #announcements Coeus Bot is best bot\n \nnl!ban ✿ Ban a member from your server ✿ nl!ban @Coeus Bot#5544 <optional reason>\n \n nl!changeprefix ✿ Change the prefix of the bot ✿ nl!changeprefix ? \n \n nl!clear ✿ clears messages, if you do not put a number it will clear 5 messages automatically. ✿ nl!clear 4\n \n nl!kick ✿ Kick a member from your sever ✿ nl!kick @Coues Bot#5544 <optional reason> \n \n nl!lockdown ✿ locks a channel so people are unable to talk. **Admins are exempt**\n \n nl!membercount ✿ Display the servers member count\n\nl!poll ✿ Makes a poll with a 👍 and a 👎 reaction ✿ nl!poll Is Coeus Bot a dumb bot?\n \n nl!serverinfo ✿ displays server information.\n \n nl!setnickname ✿ set someones nickname on the server ✿ nl!setnickname @Coeus Bot#5544 <nickname>\n \n nl!unlock ✿ unlocks the locked channel.\n \n nl!userinfo ✿ displays a users information ✿ nl!userinfo @Coeus Bot#5544	")
	embed.set_footer(text="Coeus Bot#5544 made by I Am A Trash Panda#5717", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	embed.set_author(name="Welcome to Coeus Bot admin help!", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	await ctx.send(embed=embed)

@client.command()
async def actions(ctx):
	embed = discord.Embed(title = "<command> ✿ <explanation>", description = "nl!bamboozle ✿ when you feel bamboozled.\n \n nl!blush ✿ show everyone your blushing.\n \n nl!cry ✿ show everyone you doing the cry.\n \n nl!dance ✿ show your lil dancy dance.\n \n nl!lenny ✿ when you need to hit that ( ͡° ͜ʖ ͡°).\n \n nl!pout ✿ be a bottom bitch and pout.")
	embed.set_footer(text="Coeus Bot#5544 made by I Am A Trash Panda#5717", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	embed.set_author(name="Welcome to Coeus Bot admin help!", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	await ctx.send(embed=embed)

@client.command()
async def fun(ctx):
	embed = discord.Embed(title = "`Some commands dont have an example as its a stand alone command`\n \n<command> ✿ <explanation> ✿ <example>", description = "nl!akinator ✿ play a game of akinator.\n \n nl!bubblewrap ✿ show the different types of bubblewrap you can have.\n \n nl!catfact ✿ show a cat fact.\n \n nl!combine ✿ combine two names ✿ nl!combine [name1] [name2]\n \n nl!clap ✿ Clap between words ✿ nl!clap Coeus Bot is best bot\n \n nl!dadjoke ✿ my bot will be your new dad with these jokes.\n \n nl!pp ✿ show your or other peoples pp size ✿ nl!pp ✿ nl!pp @Coeus Bot#5544\n \n nl!Coeusball ✿ ask Coeus Bots magic ball a question ✿ nl!Coeus Botball [question]\n \n nl!f ✿ show them respects ; - ; ✿ nl!f ✿ nl!f [reason]\n \n nl!flipcoin ✿ Command allows you to flip a coin. You can give a reason but its optional ✿ nl!flipcoin ✿ nl!flipcoin if its heads Coeus Bot is a Coeus Bot\n \n nl!gay ✿ test your or other peoples gayness amount ✿ nl!gay ✿ nl!gay @Coeus Bot#5544\n \n nl!hotcalc ✿ check yours or others peoples hot amount ✿ nl!hotcalc ✿ nl!hotcalc @Coeus Bot#5544\n \n nl!roast ✿ roast yourself you masochist fuck.\n \n nl!roll ✿ Command allows you to roll dice ✿ nl!roll 1d20 ✿ nl!roll 3d6 \n \n nl!weather ✿ Display the weather of a country/city/town in real time ✿ nl!weather London")
	embed.set_footer(text="Coeus Bot#5544 made by I Am A Trash Panda#5717", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	embed.set_author(name="Welcome to Coeus Bot fun help!", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	await ctx.send(embed=embed)

@client.command()
async def images(ctx):
	embed = discord.Embed(title = "`Some commands dont have an example as its a stand alone command`\n \n <command> ✿ <explanation> ✿ <example>", description = " nl!affect ✿ ruh roh scoob kid is simping ✿ nl!affect ✿ nl!affect @Coeus Bot#5544\n \n nl!avatar ✿ displays a persons profile picture ✿ nl!avatar @Coeus Bot#5544\n \n nl!beautiful ✿ people are beautiful ✿ nl!beautiful ✿ nl!beautiful @Coeus Bot#5544\n \n nl!bird ✿ shows a picture of a bird.\n \n nl!cat ✿ shows a picture of a cat.\n \n nl!delete ✿ Delete that meme ✿ nl!delete ✿ nl!delete @Coeus Bot#5544\n \n nl!disabled ✿ Some disabilities are not visual ✿ nl!disabled ✿ nl!disabled @Coeus Bot#5544\n \n nl!dog ✿ shows a picture of a dog.\n \n nl!egg ✿ make yourself or someone else into an egg ✿ nl!egg ✿ nl!egg @Coeus Bot#5544\n \n nl!horny ✿ Create a horny license ✿ nl!horny ✿ nl!horny @Coeus Bot#5544 \n \n nl!fox ✿ shows a picture of a fox.\n \n nl!lgbt ✿ Make someones profile picture have the lgbt flag ✿ nl!lgbt ✿ nl!lgbt @Coeus Bot#5544\n\n nl!poopy ✿ Command allows you to poop to show dominance ✿ nl!poopy @I Am A Trash Panda#5717 @Coeus Bot#5544. \n \n nl!shibe ✿ shows you a picture of a shibe.\n \n nl!sick ✿ Simply get rid of that filth ✿ nl!sick ✿ nl!sick @Coeus Bot#5544\n \n nl!simp ✿ Make a simp license ✿ nl!simp ✿ nl!simp @Coeus Bot#5544\n \n nl!wanted ✿ make yourself a wanted poster ✿ nl!wanted ✿ nl!wanted @Coeus Bot#5544")
	embed.set_footer(text="Coeus Bot#5544 made by I Am A Trash Panda#5717", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	embed.set_author(name="Welcome to Coeus Bot image help!", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	await ctx.send(embed=embed)

@client.command()
async def misc(ctx):
	embed = discord.Embed(title = "<command> ✿ <explanation>", description = "nl!emotes ✿ Display all the emotes in your server\n \n nl!invite ✿ Give yourself a bot invite.\n \n nl!ping ✿ Display the bots reaction time to a command.\n \n nl!prefix ✿ Display the bots prefix")
	embed.set_footer(text="Coeus Bot#5544 made by I Am A Trash Panda#5717", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	embed.set_author(name="Welcome to Coeus Bot misc help!", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	await ctx.send(embed=embed)

@client.command()
async def reddit(ctx):
	embed = discord.Embed(title = "<command> ✿ <explanation>", description = "nl!aww ✿ This will send something from reddits r/aww, r/Eyebleach, r/Catloaf, r/tuckedinkitties, r/PuppySmiles, r/StuffOnCats.\n \n nl!dankmemes ✿ This will send something from reddits r/dankmemes.\n \n nl!fml ✿ This will send something from reddits r/fml.\n \n nl!me_irl ✿ This will send something from reddits r/me_irl.\n \n nl!meme ✿ This will send something from reddits r/memes.\n \n nl!trashpandas ✿ This will send something from reddits r/trashpandas.\n \n nl!wmemes ✿ This will send something from reddits r/wholesomememes.")
	embed.set_footer(text="Coeus Bot#5544 made by I Am A Trash Panda#5717", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	embed.set_author(name="Welcome to Coeus Bot reddit help!", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	await ctx.send(embed=embed)

@client.command()
async def social(ctx):
	embed = discord.Embed(title = "`Some commands dont have an example as its a stand alone command`\n \n <command> ✿ <explanation> ✿ <example>", description = "nl!bonk ✿ Command will allow you to bonk another member ✿ nl!bonk @Coeus Bot#5544 \n \n nl!cuddle ✿ Command allows you to cuddle another member ✿ nl!cuddle @Coeus Bot#5544\n \nnl!holdhands ✿ Command allows you to hold hands with someone else ✿ nl!holdhands @Coeus Bot#5544\n \n nl!head ✿ Command allows you to give some one that sloppy top ✿ nl!head @Coeus Bot#5544\n \n nl!hug ✿ Command allows you to hug someone ✿ nl!hug @Coeus Bot#5544\n \n nl!kiss ✿ Command allows you to kiss someone else ✿ nl!kiss @Coeus Bot#5544\n \n nl!pat ✿ Command allows you to pat another member ✿ nl!pat @Coeus Bot#5544")
	embed.set_footer(text="Coeus Bot#5544 made by I Am A Trash Panda#5717", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	embed.set_author(name="Welcome to Coeus Bot social help!", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	await ctx.send(embed=embed)

@client.command()
async def text(ctx):
	embed = discord.Embed(title = "`Some commands dont have an example as its a stand alone command`\n \n <command> ✿ <explanation> ✿ <example>", description = "nl!anon ✿ Command will allow you to vent anonymously. To be used in a server dedicated vent channel or anonymous vent channel ✿ nl!anon yoink and zoink big depresso espresso \n \n nl!embed ✿ Command will allow you to send your message as an embed ✿ nl!embed Coeus Bot is best bot\n \n nl!emojify ✿ Command allows you to turn your message into emojis ✿ nl!emojify Coeus Bot is best bot\n \n nl!expand ✿ Command allows you to expand your text bit by bit ✿ nl!expand 5 Coeus Bot is best bot\n \n nl!drunkify ✿ Command allows you to make your text look drunk ✿ nl!drunkify Coeus Bot is best bot\n \n nl!fancify ✿ Command allows you to turn your text into a cursive font ✿ nl!fancify Coeus Bot is best bot\n \n nl!hotlines ✿ Command sends you a dm of hotlines in every continent. Your original message will be delete\n \n nl!owoify ✿ Command sends your message as an owo girl ✿ nl!owoify Coeus Bot please help me.\n \n nl!reverse ✿ Command takes your text and reverses it ✿ nl!reverse Coeus Bot is best bot\n \n nl!snipe ✿ Command allows you to snipe the deleted message. Deleted messages will be deleted from bot storage after 60 seconds\n \n nl!spoiler ✿ Command allows you to spoiler every character in your text ✿ nl!spoiler Coeus Bot is best bot\n \n nl!yell ✿ Command allows you to turn your text into all caps ✿ nl!yell Coeus Bot is best bot")
	embed.set_footer(text="Coeus Bot#5544 made by I Am A Trash Panda#5717", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	embed.set_author(name="Welcome to Coeus Bot text help!", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	await ctx.send(embed=embed)

@client.command()
async def nsfw(ctx):
	if not ctx.channel.is_nsfw():
		error_embed = discord.Embed(colour=discord.Colour.red())
		error_embed.add_field(name="Error", value="You tried running an __**NSFW**__ channel only command in a non __**NSFW**__ channel.\nsorry for the inconvience this might have caused, have a cookie 🍪.")
		await ctx.author.send(embed=error_embed)
		await ctx.message.delete()
		sys.stderr = object

	if ctx.channel.is_nsfw():
  		page1 = discord.Embed(colour=discord.Color.blurple())
  		page1.set_author(name="Available NSFW commands")
  		page1.add_field(name="nl!feet", value='NSFW feet pics', inline=False)
  		page1.add_field(name="nl!yuri", value='NSFW yuri pics', inline=False)
  		page1.add_field(name="nl!trap", value='NSFW trap pics', inline=False)
  		page1.add_field(name="nl!futanari",value='NSFW futanari pics', inline=False)
  		page1.add_field(name="nl!hololewd",value='NSFW hololewd pics', inline=False)
  		page1.add_field(name="nl!lewdkemo",value='NSFW lewdkemo pics', inline=False)
  		page1.add_field(name="nl!cum",value='NSFW cum on catgirls pics', inline=False)
  		page1.add_field(name="nl!erokemo", value='NSFW erokemo pics', inline=False)
  		page1.add_field(name="nl!les", value='NSFW les pics', inline=False)
  		page1.add_field(name="nl!wallpaper", value='cute wallpapers', inline=False)
  		page1.add_field(name="nl!lewdk", value='NSFW lewdk pics', inline=False)
  		page1.add_field(name="nl!lewd",value='lewd catgirls', inline=False)
  		page1.add_field(name="nl!gegc",value='genetically engineered catgirl memes', inline=False)
  		page1.add_field(name="nl!eroyuri",value='NSFW eroyuri', inline=False)
  		page1.add_field(name="nl!eron",value='NSFW eron', inline=False)
  		page1.add_field(name="nl!bj",value='NSFW bj', inline=False)
  		page1.add_field(name="nl!solo",value='NSFW solo pic', inline=False)
  		page1.add_field(name="nl!kemonomimi",value="kemonomimi", inline =False)
  		page1.add_field(name="nl!kuni",value="random kuni gif", inline =False)
  		page1.add_field(name="nl!nsfw_avatar", value='NSFW avatar pic for u horny virgins',inline=False)
  		page1.add_field(name="nl!anal", value='NSFW anal pic', inline=False)
  		page1.add_field(name="nl!hentai", value='NSFW hentai pic', inline=False)
  		page1.add_field(name="nl!erofeet", value='NSFW erofeet', inline=False)
  		page1.add_field(name="nl!pussy", value='NSFW pussy', inline=False)
  		page1.add_field(name="nl!tits", value='NSFW tits', inline=False)


  		page2 = discord.Embed(colour=discord.Color.orange())
  		page2.set_author(name="Available NSFW commands")
  		page2.add_field(name="nl!waifu",value='waifu. self explanatory you weeb', inline=False)
  		page2.add_field(name="nl!boobs", value='boobs', inline=False)
  		page2.add_field(name="nl!foxgirl", value='fox girl pics', inline=False)
  		page2.add_field(name="nl!neko", value='neko pics', inline=False)

  		pages = [page1, page2]

  		message = await ctx.send(embed = page1)
  		await message.add_reaction('◀')
  		await message.add_reaction('▶')

  		def check(reaction, user):
  			return user == ctx.author

  		i = 0
  		reaction = None

  		while True:
  			if str(reaction) == '◀':
  				if i > 0:
  					i -= 1
  					await message.edit(embed = pages[i])
  			elif str(reaction) == '▶':
  				if i < 2:
  					i += 1
  					await message.edit(embed = pages[i])
  			try:
  				reaction, user = await client.wait_for('reaction_add', timeout = 260.0, check = check)
  				await message.remove_reaction(reaction, user)

  			except:
  				break

  		await message.clear_reactions()

@client.command(pass_context=True, name='bonk', aliases=['Bonk', 'b'])
async def bonk(ctx, member: discord.Member):
    
    responses = ["https://media4.giphy.com/media/30lxTuJueXE7C/giphy.gif" , "https://media1.tenor.com/images/c18e9d2fe73f7a7a511761ee8b476ecc/tenor.gif?itemid=19823428", "https://i.imgur.com/cRDjkrU.gif", "https://i.pinimg.com/originals/b0/d2/70/b0d270b7c07757cc6c3fb6efc60229e8.gif", "https://media1.tenor.com/images/d9386a331ecabad070b6cf0249467294/tenor.gif?itemid=17979427", "https://media.tenor.com/images/39ea61de1402fa18f8452ac8074a4726/tenor.gif", "https://emoji.gg/assets/emoji/3867_BONK.gif", "https://thumbs.gfycat.com/BowedConsciousKitfox-size_restricted.gif", "https://thumbs.gfycat.com/SoulfulThirstyClingfish-size_restricted.gif", "https://i.imgur.com/0IxjsfM.gif", "https://i.gifer.com/FoFy.gif", "https://media1.tenor.com/images/2cdbc6e9f0fba26e8bb5bb835096bf53/tenor.gif?itemid=13024165", "https://i.kym-cdn.com/photos/images/original/001/716/464/d19.gif", "https://media.tenor.com/images/f7140007b3441e132f52cca8484e5bbf/tenor.gif", "https://media.tenor.com/images/b40070faac8e00f9803d3f637d258bba/tenor.gif", "https://media1.tenor.com/images/0f145914d9e66a19829d7145daf9abcc/tenor.gif?itemid=19401897", "https://media1.tenor.com/images/119ca32322ba24e4ffc4f0d84a6839f1/tenor.gif?itemid=17402810", "https://media1.tenor.com/images/eac385de6da3b57f99a6e0c769594ee0/tenor.gif?itemid=19397213"]
    embed=discord.Embed(title="Get bonked you bonkin bonk", description="**{1}** bonk **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)  
    embed.set_image(url=random.choice(responses))
    await ctx.send(embed=embed)


@client.command(pass_context=True, name='weather', aliases=['Weather', 'w'])
async def weather(ctx, *, loc):
    """Fetch the current weather of a town."""
    await ctx.send("https://wttr.in/{0}.png?m".format(loc))


@client.command(aliases=['coin', 'fc','Flipcoin', 'FlipCoin', 'FC'])
async def flipcoin(ctx, *, text: commands.clean_content = None):
    choices = ['You got Heads', 'You got Tails']
    color = discord.Color.dark_gold()
    reason = f"**{text}**" if text else ""
    if text:
    	em = discord.Embed(color=color, title='Coinflip:', description=f"{random.choice(choices)} -> {reason}")   
    	await ctx.send(embed=em)
    else:
    	em = discord.Embed(color=color, title='Coinflip:', description=f"{random.choice(choices)}")   
    	await ctx.send(embed=em)


@client.command(pass_context=True, name='hug', aliases=['Hug', 'HUG'])
async def hug(ctx, member: discord.Member):
    
    responses = [
    "https://media.tenor.com/images/b6d0903e0d54e05bb993f2eb78b39778/tenor.gif",
    "https://media1.tenor.com/images/78d3f21a608a4ff0c8a09ec12ffe763d/tenor.gif?itemid=16509980",
    "https://media1.tenor.com/images/4db088cfc73a5ee19968fda53be6b446/tenor.gif?itemid=14637016",
    "https://media1.tenor.com/images/e9d7da26f8b2adbb8aa99cfd48c58c3e/tenor.gif?itemid=14721541",
    "https://media.tenor.com/images/c3d766c61bedb6d02fc8aa13a4539933/tenor.gif",
    "https://media1.tenor.com/images/4e9c3a6736d667bea00300721cff45ec/tenor.gif?itemid=14539121",
    "https://media.tenor.com/images/d5c635dcb613a9732cfd997b6a048f80/tenor.gif",
    "https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075",
    "https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587",
    "https://media.tenor.com/images/0847bfca1f5e51983a61908438e9735a/tenor.gif",
    "https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/tenor.gif?itemid=11074788",
    "https://media.tenor.com/images/fec973cdb301f5179dca6eef16499ab0/tenor.gif",
    "https://media.tenor.com/images/983289cffea282cb8bcb5c828496d5db/tenor.gif",
    "https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif?itemid=9200935",
    "https://media1.tenor.com/images/5ccc34d0e6f1dccba5b1c13f8539db77/tenor.gif?itemid=17694740",
    "https://media1.tenor.com/images/7e30687977c5db417e8424979c0dfa99/tenor.gif?itemid=10522729",
    "https://media.tenor.com/images/9cb10b09ec1a52d9f7f571cbd7ca3596/tenor.gif",
    "https://media1.tenor.com/images/e58eb2794ff1a12315665c28d5bc3f5e/tenor.gif?itemid=10195705",
    "https://media.tenor.com/images/fa4b1a5fc7b85618bed176b256fc23be/tenor.gif",
    "https://media1.tenor.com/images/ee3c3831a62667dc84ec4149a1651d8b/tenor.gif?itemid=14924015",
    "https://media1.tenor.com/images/b35c2462c7b623d050e28e6f1886a41f/tenor.gif?itemid=7419864",
    "https://media1.tenor.com/images/c7efda563983124a76d319813155bd8e/tenor.gif?itemid=15900664",
    "https://media1.tenor.com/images/c2156769899d169306d16b063a55d0b2/tenor.gif?itemid=14584871",
    "https://media1.tenor.com/images/203df2c2d6288d8c73fd56b1e2da559e/tenor.gif?itemid=14898682",
    "https://media1.tenor.com/images/228cc8397577141822195070c88f6083/tenor.gif?itemid=4977890",
    "https://media1.tenor.com/images/460c80d4423b0ba75ed9592b05599592/tenor.gif?itemid=5044460",
    "https://media1.tenor.com/images/b0de026a12e20137a654b5e2e65e2aed/tenor.gif?itemid=7552093",
    "https://media1.tenor.com/images/c1058ebe89313d50dfc878d38630036b/tenor.gif?itemid=13976210",
    "https://media1.tenor.com/images/42922e87b3ec288b11f59ba7f3cc6393/tenor.gif?itemid=5634630",
    "https://media1.tenor.com/images/f9c540c2b5cdb52f22ed835478b0a36f/tenor.gif?itemid=10751424",
    "https://media1.tenor.com/images/b7487d45af7950bfb3f7027c93aa49b1/tenor.gif?itemid=9882931",
    "https://media1.tenor.com/images/b62f047f8ed11b832cb6c0d8ec30687b/tenor.gif?itemid=12668480",
    "https://media1.tenor.com/images/cc805107341e281102a2280f08b582e0/tenor.gif?itemid=13925386",
    "https://media1.tenor.com/images/d19bfd9ba90422611ec3c2d835363ffc/tenor.gif?itemid=18374323",
    "https://media1.tenor.com/images/45b1dd9eaace572a65a305807cfaec9f/tenor.gif?itemid=6238016",
    "https://media1.tenor.com/images/40aed63f5bc795ed7a980d0ad5c387f2/tenor.gif?itemid=11098589",
    "https://media1.tenor.com/images/16f4ef8659534c88264670265e2a1626/tenor.gif?itemid=14903944",
    "https://media1.tenor.com/images/074d69c5afcc89f3f879ca473e003af2/tenor.gif?itemid=4898650"

    ]
    embed=discord.Embed(title="Hugsss", description="Awww **{1}** hugs **{0}** how sweet!".format(member.name, ctx.message.author.name), color=0x176cd5)  
    embed.set_image(url=random.choice(responses))
    await ctx.send(embed=embed)

@client.command(pass_context=True, name='emojify', aliases=['Emojify', 'emj', 'Emj'])
async def emojify(ctx, *, text: str):
    '''
    Converts the alphabet and spaces into emoji
    '''
    author = ctx.message.author
    emojified = ''
    formatted = re.sub(r'[^A-Za-z ]+', "", text).lower()
    if text == '':
        await ctx.send('Remember to say what you want to convert!')
    else:
        for i in formatted:
            if i == ' ':
                emojified += '     '
            else:
                emojified += ':regional_indicator_{}: '.format(i)
        if len(emojified) + 2 >= 2000:
            await ctx.send('Your message in emojis exceeds 2000 characters!')
        if len(emojified) <= 25:
            await ctx.send('Your message could not be converted!')
        else:
            await ctx.send(''+emojified+'')


@client.command(aliases=["fancy", "cursive", "Fancify", "Fancy"])
async def fancify(ctx, *, text):
    """Makes text fancy!"""
    try:
        def strip_non_ascii(string):
            """Returns the string without non ASCII characters."""
            stripped = (c for c in string if 0 < ord(c) < 127)
            return ''.join(stripped)

        text = strip_non_ascii(text)
        if len(text.strip()) < 1:
            return await ctx.send(":x: ASCII characters only please!")
        output = ""
        for letter in text:
            if 65 <= ord(letter) <= 90:
                output += chr(ord(letter) + 119951)
            elif 97 <= ord(letter) <= 122:
                output += chr(ord(letter) + 119919)
            elif letter == " ":
                output += " "
        await ctx.send(output)

    except:
        await ctx.send(config.err_mesg_generic)



@client.command(pass_context=True, name='cat', aliases=['Cat'])
async def cat(ctx):
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()

    cat_em = discord.Embed(title='Have a cat.',color=0xff80ff)
    cat_em.set_image(url=f'{r[0]["url"]}')

    await ctx.send(embed=cat_em)

@client.command(pass_context=True, name='dog', aliases=['Dog'])
async def dog(ctx):
    r = requests.get("https://api.thedogapi.com/v1/images/search").json()

    cat_em = discord.Embed(title='Have a dog.',color=0xff80ff)
    cat_em.set_image(url=f'{r[0]["url"]}')
    cat_em.set_footer(text="Coeus Bot - Created by I Am A Trash Panda#5717",icon_url='https://images-ext-2.discordapp.net/external/2k3AybPS8lnMbesLCyQgU04Vbv4d3RGkpIk7H7GoT0I/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/1be8fcd718759eb92f0aa6ff9f2df7db.webp?width=702&height=702')

    await ctx.send(embed=cat_em)



@client.command(bame='fox', aliases=['Fluf', 'Fox', 'Floof', 'fluf', 'floof'])
async def fox(ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://randomfox.ca/floof/") as r:
                    data = await r.json()

                    embed = discord.Embed(title='Have a fox.',color=0xff80ff)
                    embed.set_image(url=data['image'])
                    embed.set_footer(text="Coeus Bot - Created by I Am A Trash Panda#5717",icon_url='https://images-ext-2.discordapp.net/external/2k3AybPS8lnMbesLCyQgU04Vbv4d3RGkpIk7H7GoT0I/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/1be8fcd718759eb92f0aa6ff9f2df7db.webp?width=702&height=702')


                    await ctx.send(embed=embed)



@client.group(invoke_without_command=True)
async def bubblewrap(ctx):
    em = discord.Embed(title = "Sizes of Bubblewrap", description = "**nl!bubblewrap <size>**",color=0x77dd77)
    
    em.add_field(name = "Sizes", value = "`small` `medium` `large`", inline=False)
    em.add_field(name = "Pictures", value = "`house` `dollar`", inline=False)
    await ctx.send(embed = em)

@bubblewrap.command(name='small', aliases=['Small', 's'])
async def small (ctx):
    small = [ "(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)"]

    await ctx.send(random.choice(small))

@bubblewrap.command(name='medium', aliases=['Medium', 'm'])
async def medium (ctx):
    medium = [ "(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)"]

    await ctx.send(random.choice(medium))

@bubblewrap.command(name='large', aliases=['Large', 'l'])
async def large (ctx):
    large = [ "(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)(||pop||)"]

    await ctx.send(random.choice(large))


@bubblewrap.command(name='house')
async def house (ctx):
    house = ["_                                          _||pop||\n_                                  _||pop||_         _||pop||\n_                            _||pop||_                     _||pop||\n_                     _||pop||_                                   _||pop||\n_              _||pop||||pop||_       _||pop||||pop||||pop||_       _||pop||||pop||\n_                     _||pop||_       _||pop||_       _||pop||_       _||pop||\n_                     _||pop||_       _||pop||||pop||||pop||_       _||pop||\n_                     _||pop||_                                   _||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||"]

    await ctx.send(random.choice(house))

@bubblewrap.command(name='dollar', aliases=['Dollar', 'Dollarsign', '$'])
async def dollar (ctx):
    dollar = ["_              _||pop||\n_       _||pop||||pop||||pop||\n||pop||_                     _||pop||\n||pop||\n_       _||pop||||pop||||pop||\n_                            _||pop||\n||pop||_                     _||pop||\n_       _||pop||||pop||||pop||\n_              _||pop||"]

    await ctx.send(random.choice(dollar))


snipe_message_content = None
snipe_message_author = None
snipe_message_author_display_name = None

@client.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author
    global snipe_message_author_display_name

    snipe_message_content = message.content
    snipe_message_author = message.author.name
    snipe_message_author_display_name = message.author.display_name
    await asyncio.sleep(60)
    snipe_message_author = None
    snipe_message_content = None
    snipe_message_author_display_name = None

@client.command(name='snipe', aliases=['Snipe'])
async def snipe(message):
    if snipe_message_content==None:
        await message.channel.send("Nothing to snipe is found here!")

    else:

        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(text= f"Requested By {message.author.name}#{message.author.discriminator}")
        embed.set_author(name = f"Sniped the message deleted by : {snipe_message_author} | {snipe_message_author_display_name}")
        await message.channel.send(embed=embed)
        return


@client.command(name = 'dadjoke', aliases=['Dadjoke', 'dj', 'Dj'])
async def dadjoke(ctx):

	api = 'https://icanhazdadjoke.com/'
	async with aiohttp.request('GET', api, headers={'Accept': 'text/plain'}) as r:
		result = await r.text()
		await ctx.send('`' + result + '`')

@client.command(name = 'clear', aliases = ['Clear', 'Clr', 'clr', 'Purge', 'purge'])
@has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    amount = amount+1
    await ctx.channel.purge(limit=amount)

#this is a custom command for another server which requested it
@client.listen()
async def on_message(message):
    if (message.channel.id == 818971981549404160): 
        await asyncio.sleep(2)
        await message.delete()
#this is a custom command for another server which requested it
    
#this is a custom command for another server which requested it    
@client.listen()
async def on_message(message):
    if (message.channel.id == 861998966413721620): 
        await asyncio.sleep(1)
        await message.delete()        
#this is a custom command for another server which requested it
    


@client.command(pass_context=True, name='head', aliases=['Head', 'HEAD'])
async def head(ctx, member: discord.Member):


    
    responses = ["https://media1.tenor.com/images/ff7adf1db8f5ed19347a27217efea2f5/tenor.gif?itemid=5094083",
                 "https://cdn.discordapp.com/attachments/764465461768355840/819300637237706793/image0.gif",
                 "https://media1.tenor.com/images/797eec5204f825adbe46d2b733433aab/tenor.gif?itemid=11978338",
                 "https://cdn.discordapp.com/attachments/764465461768355840/819300768485605418/image0.gif",
                 "https://media1.tenor.com/images/1588c436e29a859b0021d5f87be910f3/tenor.gif?itemid=5985258",
                 "https://media.tenor.com/images/cc2c3278ce2694ecec58e3557ecbaa37/tenor.gif",
                 "https://media1.tenor.com/images/0f03f68b1e9c6f68ac72a18d87e0b763/tenor.gif?itemid=12002082",
                 "https://media.tenor.com/images/734dc2d14de23fd564e1de4a8e8a3c08/tenor.gif",
                 "https://media.tenor.com/images/220d3bf3742cf115563cf16ce5b1c75d/tenor.gif",
                 "https://media.tenor.com/images/a96274a445ae21a140d6187ee1910352/tenor.gif",
                 "https://media.tenor.com/images/0aa64e81f6c71f5dedf2fec4a58b04ce/tenor.gif",
                 "https://media1.tenor.com/images/8c59ea78c20dc556f946d4b36432b6a4/tenor.gif?itemid=13763394",
                 "https://i.imgur.com/FDRiR84.gif",
                 "https://i.pinimg.com/originals/5b/bf/e7/5bbfe72d3faca25bdac64d85442ff553.gif",
                 "https://media.tenor.com/images/6a142cfb2922c5f026af73ba90fe4518/tenor.gif",
                 "https://media1.tenor.com/images/baa1b555e5c312ea6917c4187a91a44f/tenor.gif?itemid=3512304",
                 "https://media1.tenor.com/images/dc851cb63c81d2c75aa1a7d3b523ed93/tenor.gif?itemid=8120832https://media1.tenor.com/images/dc851cb63c81d2c75aa1a7d3b523ed93/tenor.gif?itemid=8120832",
                 "https://media1.tenor.com/images/778ac5849626f52c2dd9a020b58ec55a/tenor.gif?itemid=15810606",
                 "https://media.tenor.com/images/ffa77f40f8ea9e77fbd17ed05ffbc111/tenor.gif",
                 "https://media.tenor.com/images/8280c571c91ea215aec7b78c95fd0be1/tenor.gif",
                 "https://media.tenor.com/images/92639e025cd79dd4f14a5ef3372b6f01/tenor.gif"]

    headhead = ["Ladies and Gentlemen **{1}** has give surpreme head to **{0}**!",
                "**{1}** Has sinned against God with **{0}**",
                "**{1}** Gave **{0}** Head, feelin good",
                "**{1}** and **{0}** got freaaky.... I think that’s what they call third base",
                "**{1}** and **{0}** both got sloppy toppy",
                "**{1}** Had blown **{0}'s** whistle baby whistle baby",
                "**{1}** Couldnt last 5 minutes with **{0}** And their massive sexy dumptruck of an ass",
                "**{1}** Made **{0}'s** pull out game WEAK",
                "**{1}** gives **{0}** the sucky wucky uwu",
                "**{0}** Ranked S tier for **{1}** giving them good top"]

    selfsuck = ["I'll break your ribs",
    			"No",
    			"good luck breaking your back bitch",
    			"sucks to suck... but you won’t be sucking yourself off, That’s for sure",
    			"just cause someone else won’t give you head... pathetic",
    			"get a life"]
    embed=discord.Embed(title="Gawk Gawk", description=random.choice(headhead).format(member.name, ctx.message.author.name), color=0x176cd5)      
    embed.set_image(url=random.choice(responses))
    if ctx.message.author in ctx.message.mentions:
        await ctx.channel.send(random.choice(selfsuck))
    else:
    	await ctx.channel.send(embed=embed)


@client.command(aliases=['howhot'])
async def hotcalc(ctx, member : discord.Member = None):
	r = random.randint(0, 100)
	emoji = "💔"
	if r > 25:
		emoji = "❤"
		if r > 50:
			emoji = "💖"
			if r > 75:
				emoji = "💞"

	if member:
		embed = discord.Embed(title=f"How hot is {member.name}", description=f"**{member.name}** is **{r:.2f}%** hot {emoji}")
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(title=f"How hot is {ctx.author.name}", description=f"**{ctx.author.name}** is **{r:.2f}%** hot {emoji}")
		await ctx.send(embed=embed)

@client.command(aliases=['Reverse'])
async def reverse( ctx, *, text: str):
	t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
	await ctx.send(f"🔁 {t_rev}")

@client.command(aliases = ["F"]     )
async def f(ctx, *, text: commands.clean_content = None):
        """ Press F to pay respect """
        hearts = ['❤', '💛', '💚', '💙', '💜']
        reason = f"for **{text}** " if text else ""
        await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")


@client.command(aliases=["whois"])
@has_permissions(manage_roles=True)
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@client.command()
async def catfact(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://catfact.ninja/fact") as response:
            fact = (await response.json())["fact"]
            length = (await response.json())["length"]
            embed = discord.Embed(title=f'Random Cat Fact Number: **{length}**', description=f'Cat Fact: {fact}', colour=0x400080)
            embed.set_footer(text="")
            await ctx.send(embed=embed)



@client.command(pass_context=True, name='handholding', aliases=['HandHolding', 'HH', 'hh', 'holdhands'])
async def handholding(ctx, member: discord.Member):
    
    responses = ["https://media4.giphy.com/media/O1w2wSTriddUA/giphy.gif",
                 "https://media4.giphy.com/media/X7JROeqSgx4Dbwo053/giphy.gif",
                 "https://media1.giphy.com/media/NAUtEs7cbhRAc/giphy.gif",
                 "https://i.giphy.com/media/mBv1yHMdmEsZCnR9MI/giphy.webp",
                 "https://media1.giphy.com/media/k8ijaVQ9SPWZG/giphy.gif",
                 "https://media3.giphy.com/media/26wyAJEgQmkg761Ik/giphy.gif",
                 "https://media0.giphy.com/media/MBy4FK3UjLfiLI81j6/giphy.gif",
                 "https://media2.giphy.com/media/26u458eVD7z0CbpdK/giphy.gif",
                 "https://media0.giphy.com/media/6pkSzqwBqjK216D5Tb/giphy.gif",
                 "https://media3.giphy.com/media/l2SpNzGq8wH66KqI0/giphy.gif",
                 "https://media1.giphy.com/media/l31TPG1xWOU8SQPjOX/giphy.gif",
                 "https://media3.giphy.com/media/POsdF8IsWPmZlve858/giphy.gif",
                 "https://media4.giphy.com/media/xTiTnLU7kcAGIz6XJK/giphy.gif",
                 "https://media3.giphy.com/media/1xmlYh65ZA8rOjKwr3/giphy.gif",
                 "https://media2.giphy.com/media/fvN5S96o1p9WyGNvdv/giphy.gif",
                 "https://media1.giphy.com/media/NElCe2QW8Qxo6rQAeX/giphy.gif",
                 "https://media1.giphy.com/media/PMo4TlMff7r9e/giphy.gif",
                 "https://media3.giphy.com/media/d1FKV0q6kqU32uwE/giphy.gif",
                 "https://i.pinimg.com/originals/0e/6f/52/0e6f524f25fbc80c666d6541822e2522.gif",
                 "https://media1.giphy.com/media/w7RGPBLGO8rjq/giphy.gif",
                 "https://carnivorouslreviews.files.wordpress.com/2018/08/interlocking.gif",
                 "https://i.pinimg.com/originals/59/e4/9c/59e49c83dc5b7042b6b697bcce742fb5.gif",
                 "https://thumbs.gfycat.com/FrigidDefenselessHammerkop-size_restricted.gif",
                 "https://i.pinimg.com/originals/8f/70/71/8f70714a8fc965fdcae4d7d11bc4c683.gif",
                 "https://i.pinimg.com/originals/0e/6f/52/0e6f524f25fbc80c666d6541822e2522.gif",
                 "https://litakinoanimecorner.files.wordpress.com/2017/04/tumblr_nxh46uaokr1tsmah5o2_500.gif",
                 "https://data.whicdn.com/images/105641409/original.gif"

    ]
    embed=discord.Embed(title="Hand Holding", description="Awww **{1}** holds **{0}** hand!".format(member.name, ctx.message.author.name), color=0x176cd5)  
    embed.set_image(url=random.choice(responses))
    if ctx.message.author in ctx.message.mentions:
        await ctx.send("I mean to each their own but you dont get a gif for this. Ask someone I dont care if they are taken.")
    else:
        await ctx.send(embed=embed)


#this is a custom command for another server which requested it
@client.listen()
async def on_message(message):
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',message.content.lower())
	if urls and message.channel.id == 857703395154722877:
		await message.pin()
#this is a custom command for another server which requested it

@client.command(aliases = ['Coeusball', '8ball'])
async def coeusball(ctx, *, text: commands.clean_content):
    responses = ["As I see it, yes", "Yes", "No", "Very likely", "Not even close", "Maybe", "Very unlikely", "Cole's mom told me yes", "Cole's mom told me no", "Ask again later", "Better not tell you now", "Concentrate and ask again", "Don't count on it", " It is certain", "My sources say no", "Outlook good", "You may rely on it", "Very Doubtful", "Without a doubt"]
    color = discord.Color.dark_gold()
    embed = discord.Embed(title = "Coeus Bot's 8Ball", description = "_ _")
    embed.add_field(name = f"**{ctx.author.display_name} asked:**", value = f"{text}")
    embed.add_field(name = "**Answer:**", value = f"{random.choice(responses)}", inline=False)
    await ctx.send(embed=embed)

@client.command(name = 'blush', aliases = ['Blush'])
async def blush(ctx):

    face = ["(*^.^*)",
            "＠＾▽＾＠",
            "(´ω｀*)",
            "(‘-’*)",
            "(/ε＼*)",
            "(*^^*)",
            "(*^_^*)",
            "(•ﾟдﾟ•)",
            "(*ﾟ∀ﾟ*)",
            "(^-^*)ノ",
            "(・´ｪ｀・)",
            "(*´ω｀*)",
            "(〃￣ω￣〃ゞ)",
            "v(・∀・*)",
            "(*≧∀≦*)",
            "v(^∀^*)"
            ]

    blush = ["https://cdn.weeb.sh/images/SkckMIXP-.gif",
             "https://cdn.weeb.sh/images/BkalMI7Db.gif",
             "https://cdn.weeb.sh/images/SyIbfImDb.gif",
             "https://cdn.weeb.sh/images/rJa-zUmv-.gif",
             "https://cdn.weeb.sh/images/Sy1-ML7vW.gif",
             "https://cdn.weeb.sh/images/Hkx8xMLQw-.gif",
             "https://media.tenor.com/images/0d4260a30ddf2647a9e1824b8e68defd/tenor.gif",
             "https://media4.giphy.com/media/HPI9m7McNPGN2/200.gif",
             "https://i.pinimg.com/originals/dd/6d/47/dd6d47837ba2952f8ccadfa4167e706b.gif",
             "https://i.imgur.com/hFkeViW.gif",
             "https://media.tenor.com/images/0a8c1ae735519df6b91d05a6f28fd374/tenor.gif",
             "https://i.pinimg.com/originals/91/e1/db/91e1db4a35959c0b4ed2a5cad1f9e41e.gif",
             "https://i.imgur.com/BVzWdzX.gif",
             "https://media1.giphy.com/media/T3Vvyi6SHJtXW/giphy.gif",
             "https://thumbs.gfycat.com/GracefulMessyKitten-small.gif",
             "https://acegif.com/wp-content/gif/blushing-35.gif",
             "https://thumbs.gfycat.com/AcidicSecondhandBanteng-small.gif",
             "http://33.media.tumblr.com/578f4a1f9eecc7c944b7b2721880fdbb/tumblr_n02m902fgm1r4kkpvo1_500.gif",
             "https://animemotivation.com/wp-content/uploads/2020/09/umiko-ahagon-blush-gif.gif",
             "https://i.gifer.com/OUum.gif",
             "https://i0.wp.com/gifimage.net/wp-content/uploads/2017/07/anime-blushing-gif-17.gif?resize=650,400"
             "https://media1.tenor.com/images/cbfd2a06c6d350e19a0c173dec8dccde/tenor.gif?itemid=15727535",
             "http://gifimage.net/wp-content/uploads/2017/07/anime-blushing-gif-16.gif",
             "https://media0.giphy.com/media/10nXVGtagsTPd6/source.gif",
             "https://38.media.tumblr.com/6936c5d959402f30545b1cf75171179d/tumblr_n53aj6KX9Z1smcbm7o1_500.gif",
             "https://animemotivation.com/wp-content/uploads/2020/09/Kosaki-Onodera-blush-nisekoi-gif.gif",
             "http://media4.giphy.com/media/bMLGNRoAy0Yko/giphy.gif",
             "http://denarii.info/filedump/gifs/anime-blush.gif",
             "https://thumbs.gfycat.com/UnfinishedBitterChevrotain-size_restricted.gif",
             "https://media3.giphy.com/media/OpfkuToK5gSHK/giphy.gif",
             "https://media0.giphy.com/media/DURbX7oesHiaA/giphy.gif",
             "https://thumbs.gfycat.com/CraftyUntriedCaudata-size_restricted.gif",
             "https://acegif.com/wp-content/gif/blushing-70.gif",
             "https://media2.giphy.com/media/3KYGq82Lb74TbVXLVc/giphy.gif",
             "https://media0.giphy.com/media/3IQsGPmOK8s4U/giphy.gif",
             "https://media0.giphy.com/media/FlHuACrCGXkc0/giphy.gif",
             "https://thumbs.gfycat.com/WeepyPresentCub-size_restricted.gif",
             "https://66.media.tumblr.com/tumblr_lyc19hoNZV1rn95k2o1_500.gif",
             "https://media3.giphy.com/media/eHpWHuEUxHIre/200_d.gif",
             "https://64.media.tumblr.com/69ce83873d6fa516883d4fd286da1ff9/f85433a3beaebe13-91/s500x750/e3b12faf1570814d1494b8c32ea272f8eb8b282e.gifv",
             "https://i.pinimg.com/originals/60/eb/9c/60eb9c8165abba55a78bb24bc3ff1796.gif",
             "https://i0.wp.com/media2.giphy.com/media/36vZ9fy5nK0HS/giphy.gif",
             "https://i.makeagif.com/media/8-19-2018/cg9viJ.gif",
             "https://thumbs.gfycat.com/WideeyedLimitedBlacklab-size_restricted.gif",
             "https://media3.giphy.com/media/INlJUYclnafdu/giphy.gif",
             "https://i.gifer.com/8RID.gif",
             "https://media3.giphy.com/media/WRWT7mUOiMEqnnTUvz/giphy.gif",
             "https://thumbs.gfycat.com/ExcellentMinorGharial-size_restricted.gif",
             "https://data.whicdn.com/images/229290641/original.gif"]

    action = ["'s face goes red",
              "is blushing!",
              "blushes",
              "blushed!!"]
    embed=discord.Embed(title=f"`{ctx.author.name} {random.choice(action)} {random.choice(face)}`", description="_ _", color=0xFF69B4)
    embed.set_image(url=random.choice(blush))
    await ctx.send(embed=embed)


@client.command(name = 'cry', aliases = ['Cry'])
async def cry(ctx):

    face = ["(T⌓T)",
            "أ‿أ",
            "╥﹏╥",
            "(;﹏;)",
            "(ToT)",
            "(┳Д┳)",
            "(ಥ﹏ಥ)",
            "（；へ：）",
            "(T＿T)",
            "（πーπ）",
            "(⋟﹏⋞)",
            "（ｉДｉ）",
            "(つ﹏⊂)",
            "༼☯﹏☯༽",
            "(ノ﹏ヽ)",
            "; - ;"
            ]

    cry = ["https://cdn.weeb.sh/images/H1p77LmvW.gif",
             "https://cdn.weeb.sh/images/B1Jg1eqJM.gif",
             "https://cdn.weeb.sh/images/r1O8QUmvb.gif",
             "https://cdn.weeb.sh/images/SkbN7LQv-.gif",
             "https://cdn.weeb.sh/images/Hy4CS1h5G.gif",
             "https://cdn.weeb.sh/images/rk8DrJhcf.gif",
             "https://i.pinimg.com/originals/b4/b1/64/b4b1640525ecadfa1030e6096f3ec842.gif",
             "https://i.imgur.com/I18iVJC.gif",
             "https://i.pinimg.com/originals/d4/96/7f/d4967fd1672fecb50f7f7c400ddef92c.gif",
             "https://media0.giphy.com/media/ukfn7kMzzLqLeyi5Tt/giphy.gif",
             "https://i.imgur.com/CwUSjuy.gif",
             "https://i.pinimg.com/originals/b1/ae/3c/b1ae3cd36795f45af901e3d07df50667.gif",
             "https://media0.giphy.com/media/Ui7MfO6OaLz4k/giphy.gif",
             "https://media2.giphy.com/media/8YutMatqkTfSE/200.gif",
             "https://image.myanimelist.net/ui/_3fYL8i6Q-n-155t3dn_4oJj9VS43d_Xmz7O0AvrWo9XYsmw8t808dA00uFySKD2",
             "https://media2.giphy.com/media/L95W4wv8nnb9K/giphy.gif",
             "https://media1.giphy.com/media/BEob5qwFkSJ7G/giphy.gif",
             "https://media3.giphy.com/media/3o6wrvdHFbwBrUFenu/giphy.gif",
             "https://media1.giphy.com/media/l41K1OWf4uhAw6Oru/giphy-downsized.gif",
             "https://i.gifer.com/7JF.gif",
             "https://thumbs.gfycat.com/OilyFragrantAfricanharrierhawk-max-1mb.gif",
             "https://thumbs.gfycat.com/EmotionalRecentBirdofparadise-size_restricted.gif",
             "https://media4.giphy.com/media/RLtX0ELcFMtSoR5Boy/source.gif",
             "https://media2.giphy.com/media/g0yPLFTYpr283dUJBs/source.gif",
             "https://data.whicdn.com/images/288165213/original.gif",
             "http://68.media.tumblr.com/a2149154770a07c3e24ab979c185df76/tumblr_nz44v0iKy81so18vqo1_1280.gif",
             "https://thumbs.gfycat.com/MintyNauticalAxolotl-size_restricted.gif",
             "https://media3.giphy.com/media/4q11PwNfzT2BG/giphy.gif",
             "https://data.whicdn.com/images/334483981/original.gif",
             "https://thumbs.gfycat.com/GlitteringScratchyIberianbarbel-size_restricted.gif",
             "https://64.media.tumblr.com/d26c8156d3b54e614ecddf6dd9b5c66c/tumblr_mor9bc68q61rbavngo2_500.gifv",
             "https://i.pinimg.com/originals/62/c7/67/62c76760e00580d79d4f4fb3c023273f.gif",
             "https://i.pinimg.com/originals/fb/ef/06/fbef0640dad620227b825e13b1fb0752.gif",
             "http://37.media.tumblr.com/46f9c7eb89118eae41a964f1860f764a/tumblr_n2jjoxRZ4A1rw79q6o1_500.gif",
             "https://ohmy.disney.com/wp-content/uploads/sites/25/2015/09/01-kuzco-crying.gif",
             "https://64.media.tumblr.com/tumblr_lwnyi9wwGa1qm6oc3o1_500.gif",
             "http://cdn.lowgif.com/full/f0360996737708e9-what-type-of-person-are-you-according-to-disney-crying-disney.gif",
             "https://i.gifer.com/3FfO.gif",
             "http://24.media.tumblr.com/361f9cf57eaa7a6f2a33867eaeae6e38/tumblr_mv4s94mvU91r8rg3jo4_r1_250.gif"]

    action = ["'s eyes start to tear up",
              "is crying!",
              "cries",
              "cried!!"]
    embed=discord.Embed(title=f"`{ctx.author.name} {random.choice(action)} {random.choice(face)}`", description="_ _", color=0xFF69B4)
    embed.set_image(url=random.choice(cry))
    await ctx.send(embed=embed)

@client.command(name = 'dance', aliases = ['Dance'])
async def dance(ctx):

    face = ["♪(┌・。・)┌",
            "┏(･o･)┛♪┗ (･o･) ┓",
            "┗(＾0＾)┓",
            "(ﾉﾟ▽ﾟ)ﾉ",
            "(ノ‥)ノ",
            "ヾ(･ω･*)ﾉ",
            "ヘ(^_^ヘ)",
            "ヾ(*д*)ﾉ゛",
            "(ノ°ο°)ノ",
            "(∫˘▽˘)∫",
            "(σ‾▿‾)-σ",
            "ƪ(˘⌣˘)┐ ƪ(˘⌣˘)ʃ ┌(˘⌣˘)ʃ",
            "└（★ｏ★）┐",
            "〜(￣▽￣〜)(〜￣▽￣)〜",
            "ヾ(-_- )ゞ",
            "ح˚௰˚づ"
            ]

    dance = ["https://cdn.weeb.sh/images/SJHu_I7vZ.gif",
             "https://cdn.weeb.sh/images/SkzY_Lmv-.gif",
             "https://cdn.weeb.sh/images/S1Vju87Pb.gif",
             "https://cdn.weeb.sh/images/H1DckmS6b.gif",
             "https://cdn.weeb.sh/images/BJYVd8QPb.gif",
             "https://cdn.weeb.sh/images/ByhduIQP-.gif",
             "https://media.tenor.com/images/fe3826b59f80f5e6c7cc04eb474fb44d/tenor.gif",
             "https://i.pinimg.com/originals/1a/13/c1/1a13c111736f868f9abab76e8ac9009d.gif",
             "https://media3.giphy.com/media/HZboJ5Pkti9k4/giphy.gif",
             "https://media.tenor.com/images/9770d9c99bf00ae01a35cc7ff12fe060/tenor.gif",
             "https://i2.wp.com/kakuchopurei.com/wp-content/uploads/2019/02/haruhisuzumiyaGIF.gif?fit=498%2C278&ssl=1",
             "https://pa1.narvii.com/6243/f7ccee5acbe2b70dba8ceef184c88f80b3bbea22_hq.gif",
             "https://i.gifer.com/8UYb.gif",
             "https://pa1.narvii.com/6629/d838019a15d2c1b888a4e12214e30f4e26fa81c7_00.gif",
             "http://cdn.lowgif.com/small/d101cf95aaac1b39-.gif",
             "https://i.pinimg.com/originals/13/57/e1/1357e1eca09347163da302058cae5b3c.gif",
             "https://media2.giphy.com/media/It3ZU6cM0i6Pu/giphy.gif",
             "https://media4.giphy.com/media/ykUYsNYRvrprq/source.gif",
             "https://ohmy.disney.com/wp-content/uploads/sites/25/2015/06/01-emp-kuzco-dance-small.gif",
             "https://i.pinimg.com/originals/5e/91/10/5e91108a3b204d8f7e68cd4e3a928ac6.gif",
             "https://media0.giphy.com/media/8OpVoc3ZMk1mE/source.gif",
             "https://i.gifer.com/Rhrz.gif",
             "http://24.media.tumblr.com/84ad387754f8dd326845fe6e33d2e43c/tumblr_mv7s15QCsg1s392ayo1_500.gif",
             "https://media2.giphy.com/media/26xBIbh7wgIMAZKsE/source.gif",
             "https://media2.giphy.com/media/26xBIbh7wgIMAZKsE/source.gif",
             "https://i.gifer.com/1YQ.gif",
             "https://i.gifer.com/2DSa.gif",
             "http://25.media.tumblr.com/b493aea6a712ab319339f9c8320eae78/tumblr_mv3gynqAO61rd0rbzo1_500.gif",
             "https://media1.giphy.com/media/pO4UHglOY2vII/giphy.gif",
             "http://33.media.tumblr.com/0860732d5421b2f03db050503c3f2154/tumblr_mti4b9vHrU1qd5qeyo1_500.gif",
             "https://media2.giphy.com/media/PWgHoRkLD2bwk/source.gif",
             "https://ohmy.disney.com/wp-content/uploads/2014/03/BertDancing.gif",
             "https://media1.tenor.com/images/57a3c3408c6b75ffb8c5a4e488507ce0/tenor.gif?itemid=6142639",
             "https://media0.giphy.com/media/g0KIsQZHeLn3lqRp5G/giphy.gif",
             "https://media0.giphy.com/media/WmhWN5VCNsBGg/giphy.gif",
             "https://laughingsquid.com/wp-content/uploads/2017/10/animated-dance-scenes-from-classic-disney-movies.gif?w=750",
             "https://ohmy.disney.com/wp-content/uploads/sites/25/2014/03/PinocchioDancing.gif",
             "https://thumbs.gfycat.com/CalculatingCrazyIndianpangolin-small.gif"
             ]

    action = ["'s legs shuffle onto the dance floor",
              "is dancing!",
              "dances",
              "danced!!",
              "breaks the dance floor with those epic moves"]
    embed=discord.Embed(title=f"`{ctx.author.name} {random.choice(action)} \n{random.choice(face)}`", description="_ _", color=0xFF69B4)
    embed.set_image(url=random.choice(dance))
    await ctx.send(embed=embed)

@client.command(name = 'pout', aliases = ['Pout'])
async def pout(ctx):


    pout = ["https://cdn.weeb.sh/images/B10og1FPb.gif",
            "https://cdn.weeb.sh/images/Bkl3xJFP-.gif",
            "https://cdn.weeb.sh/images/S1iol1YwW.gif",
            "https://cdn.weeb.sh/images/Bk5D5wuUf.gif",
            "https://cdn.weeb.sh/images/S1VieJYv-.gif",
            "https://cdn.weeb.sh/images/ryzRx1twZ.gif",
            "https://media2.giphy.com/media/TEJe85dPYW0Uw/giphy-downsized-large.gif",
            "https://i.pinimg.com/originals/e5/6e/1a/e56e1ae197ea11668756e6e82407e5c5.gif",
            "https://media.tenor.com/images/a99567676e95306432c8eaae14b7d89f/tenor.gif",
            "https://media.tenor.com/images/0f5d12aa3dfa6d8fd9e8a41bc51ec421/tenor.gif",
            "https://i.pinimg.com/originals/a9/a1/ee/a9a1ee151d114920f6914bd507f8b3c5.gif",
            "https://media.tenor.com/images/9ee03c5f29aa8ee30dfbf95dea30d1d0/tenor.gif",
            "https://thumbs.gfycat.com/BonyFarawayBlackcrappie-size_restricted.gif",
            "https://i.imgur.com/p0F1Pqk.gif",
            "https://media0.giphy.com/media/U77FFxuyoIPvHEIgkq/giphy.gif",
            "https://media3.giphy.com/media/X3VrxPijowGC4/giphy.gif",
            "https://data.whicdn.com/images/219799600/original.gif",
            "https://thumbs.gfycat.com/ConsciousLavishGosling-max-14mb.gif",
            "https://64.media.tumblr.com/c4213b1a16cfd1ba7462af00753a018e/tumblr_pmrkrdI7QD1th206io1_1280.gif",
            "https://i.pinimg.com/originals/b7/e1/32/b7e132fd3f4e110ea54ef8aa8f4eebbe.gif",
            "https://i.gifer.com/lq.gif"]

    action = ["'s starts to pout",
              "is pouting!",
              "pouts",
              "pouted!!",]
    embed=discord.Embed(title=f"`{ctx.author.name} {random.choice(action)}`", description="_ _", color=0xFF69B4)
    embed.set_image(url=random.choice(pout))
    await ctx.send(embed=embed)

@client.command()
async def roast(ctx):
    response = requests.get(url="https://evilinsult.com/generate_insult.php?lang=en&type=json")
    roast = json.loads(response.text)
    await ctx.send(roast['insult'])

@client.command(aliases = ["mwah", "KISS", "Mwah", "MWAH", "Kiss", "mwa", "Mwa", "MWA"])
async def kiss(ctx, member : discord.Member):

    kiss = [ "https://cdn.weeb.sh/images/SJ3dXCKtW.gif",
             "https://cdn.weeb.sh/images/H1e7nadP-.gif",
             "https://cdn.weeb.sh/images/SyY0j6Ov-.gif",
             "https://cdn.weeb.sh/images/Bkuk26uvb.gif",
             "https://cdn.weeb.sh/images/B13D2aOwW.gif",
             "https://cdn.weeb.sh/images/B12g3TOPZ.gif",
             "https://media2.giphy.com/media/bGm9FuBCGg4SY/giphy.gif",
             "https://media.tenor.com/images/197df534507bd229ba790e8e1b5f63dc/tenor.gif",
             "https://i.pinimg.com/originals/e0/0f/31/e00f3104927ae27d7d6a32393d163176.gif",
             "https://37.media.tumblr.com/70d58855d3d6dc8fcda71e68fe6889d0/tumblr_n5hm4rqX6O1skkm34o1_500.gif",
             "https://i.pinimg.com/originals/d0/8b/c5/d08bc5bec3ebff5805ae2d984c4eccd5.gif",
             "https://24.media.tumblr.com/5d51b3bbd64ccf1627dc87157a38e59f/tumblr_n5rfnvvj7H1t62gxao1_500.gif",
             "https://media2.giphy.com/media/m1FDIHtq2Vko8/giphy.gif",
             "https://thumbs.gfycat.com/SpeedyConventionalArthropods-small.gif",
             "https://thumbs.gfycat.com/AlertIncompleteBighornsheep-size_restricted.gif",
             "https://data.whicdn.com/images/326284870/original.gif",
             "https://i.gifer.com/3wih.gif",
             "http://giphygifs.s3.amazonaws.com/media/bm2O3nXTcKJeU/giphy.gif",
             "https://i.imgur.com/OE7lSSY.gif",
             "http://24.media.tumblr.com/56614f2adbcecd04ab527ce1a067f297/tumblr_mn64lwbR0w1rsbc8eo1_500.gif",
             "https://media1.giphy.com/media/nyGFcsP0kAobm/giphy.gif",
             "https://pa1.narvii.com/5832/b65b3178e18e6da8086ddcc2201580d9d6ce4d66_hq.gif",
             "https://acegif.com/wp-content/uploads/anime-kiss-11.gif",
             "https://giffiles.alphacoders.com/188/188370.gif",
             "https://i.gifer.com/2NHg.gif",
             "http://33.media.tumblr.com/7817433a9e6ac88e546790cc743b5a55/tumblr_n2g40woqJ81s0t69oo1_500.gif",
             "https://64.media.tumblr.com/92a40e336aef4db1aa5de29e90c76850/tumblr_inline_pd4hqkIBcj1qa7yzy_500.gif",
             "http://49.media.tumblr.com/7d3afc4a0af8d96fb644fc728e7741df/tumblr_o2uyxgwxLM1so18vqo1_500.gif"]
             
    embed = discord.Embed(title="Mwah", description="Awww **{1}** kisses **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)  
    embed.set_image(url=random.choice(kiss))
    if ctx.message.author in ctx.message.mentions:
        await ctx.send("I mean to each their own but you dont get a gif for this. Ask someone I dont care if they are taken.")
    else:
        await ctx.send(embed=embed)
@client.command()
async def yell(ctx, *, text: str):
    t_upper = text.upper().replace("@", "@\u200B").replace("&", "&\u200B")
    await ctx.send(f"⬆️ {t_upper}")
@client.command()
async def bamboozle(ctx):
    await ctx.send(f"**{ctx.author.name}** just got heckin' bamboozled!")


@client.command()
async def roll(ctx, die_string: str):
    dice, value = (int(term) for term in die_string.split("d"))
    if dice <= 25:
        rolls = [randint(1, value) for i in range(dice)]

        await ctx.send(" + ".join([str(r) for r in rolls]) + f" = {sum(rolls)}")
    else:
        await ctx.send("I can't roll that many dice. Please try a lower number.")

@client.command()
async def pp(ctx, member : discord.Member = None):
	length = random.randrange(15)
	if member:
		embed = discord.Embed(description=f"8{'='*length}D", color=0x77dd77)
		embed.set_author(name=f"{member.display_name}'s pp", icon_url=member.avatar_url)
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(description=f"8{'='*length}D", color=0x77dd77)
		embed.set_author(name=f"{ctx.author.display_name}'s pp", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)
@client.command()
async def gay(ctx, member : discord.Member = None):
	gayness = random.randint(0,100)
	if gayness <= 33:
		gayStatus = random.choice(["No Homo","Wearing Socks","Only Sometimes","Straight-ish","No Homo Bro","Hella Straight"])
	elif 33 < gayness < 66:
		gayStatus = random.choice(["Possible Homo","My gay-sensor is picking something up","I can't tell if the socks are on or off","Gay-ish","Looking a bit homo","lol half  g a y","safely in between for now"])
	else:
		gayStatus = random.choice(["LOL YOU GAY XD FUNNY MOMENT HAHA COMEDIAN","HOMO ALERT","MY GAY-SENSOR IS OFF THE CHARTS","BIG GEAY","THE SOCKS HAVE BEEN OFF FOR A WHILE","HELLA GAY"])
	if member:
			embed = discord.Embed(description = f"Gayness for **{member.name}**", color = 0xFF69B4)
			embed.add_field(name = "Gayness:", value = f"{gayness}% gay")
			embed.add_field(name = "Comment:", value = f"{gayStatus} 💞")
			embed.set_author(name = "Gay Scanner", icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/ICA_flag.svg/2000px-ICA_flag.svg.png")
			await ctx.send(embed=embed)
	else:
		embed = discord.Embed(description = f"Gayness for **{ctx.author.name}**", color = 0xFF69B4)
		embed.add_field(name = "Gayness:", value = f"{gayness}% gay")
		embed.add_field(name = "Comment:", value = f"{gayStatus} 💞")
		embed.set_author(name = "Gay Scanner", icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/ICA_flag.svg/2000px-ICA_flag.svg.png")
		await ctx.send(embed=embed)

@client.listen()
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		m, s = divmod(error.retry_after, 60)
		h, m = divmod(m, 60)
		if int(h) == 0 and int(m) == 0:
			await ctx.send(f' You must wait {int(s)} seconds to use this command!')
		elif int(h) == 0 and int(m) != 0:
			await ctx.send(f' You must wait {int(m)} minutes and {int(s)} seconds to use this command!')
		else:
			await ctx.send(f' You must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use this command!')
@client.command()
@commands.has_permissions(manage_messages = True)
async def poll(ctx, *, pollInfo):
	embed = discord.Embed(description=pollInfo, colour=0x400080)
	embed.set_author(name=f"Poll by {ctx.message.author}", icon_url="https://lh3.googleusercontent.com/7ITYJK1YP86NRQqnWEATFWdvcGZ6qmPauJqIEEN7Cw48DZk9ghmEz_bJR2ccRw8aWQA=w300")
	nope = discord.Embed(title="You do not have the correct permissions to run this command.", description="_ _")
	pollMessage = await ctx.send(embed=embed)
	await pollMessage.add_reaction("\N{THUMBS UP SIGN}")
	await pollMessage.add_reaction("\N{THUMBS DOWN SIGN}")

@client.command()
@commands.has_permissions(manage_channels = True)
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send( ctx.channel.mention + " ***is now in lockdown.***")

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " ***has been unlocked.***")



@client.command()
async def combine(ctx, name1: clean_content, name2: clean_content):
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(color=0x36393e, description = f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}", icon_url="https://images-ext-2.discordapp.net/external/OknEEX3TVD1I45s24UXgeEpvp_uwujejd_dt_CVZA-Q/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/803274877347692555/f4af4977dd6829c8a37129093daec333.webp")
    await ctx.send(embed=emb)

@client.command()
async def drunkify(ctx, *, s: commands.clean_content = None):
    lst = [str.upper, str.lower]
    newText = await commands.clean_content().convert(ctx, ''.join(random.choice(lst)(c) for c in s))
    if len(newText) <= 380:
    	await ctx.send(newText)
    else:
        try:
        	if len(newText) <= 0:
        		await ctx.send("Put something dumby")
        except Exception:
        	await ctx.send(f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**")


@client.command()
async def expand(ctx,  num: int, *, s: clean_content):
    spacing = ""
    if num > 0 and num <= 5:
        for _ in range(num):
            spacing+=" "
            result = spacing.join(s)
            if len(result) <= 200:
                await ctx.send(result)
            else:
                try:
                    await ctx.author.send(result)
                    await ctx.send(f"**{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:**")
                except Exception:
                    await ctx.send(f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**")
                else:
                    await ctx.send("```fix\nError: The number can only be from 1 to 5```")

async def getSub(ctx, sub):
    async with ctx.typing():
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.reddit.com/r{sub}/hot.json?limit=100") as response:
                request = await response.json()

        attempts = 1
        while attempts < 5:
            if 'error' in request:
                print("failed request {}".format(attempts))
                await asyncio.sleep(2)
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://www.reddit.com/r/{sub}/hot.json?limit=100") as response:
                        request = await response.json()
                attempts += 1
            else:
                index = 0

                for index, val in enumerate(request['data']['children']):
                    if 'url' in val['data']:
                        url = val['data']['url']
                        urlLower = url.lower()
                        accepted = False
                        for j, v, in enumerate(acceptableImageFormats):
                            if v in urlLower:
                                accepted = True
                        if accepted:
                            if url not in memeHistory:
                                memeHistory.append(url)
                                if len(memeHistory) > 63:
                                    memeHistory.popleft()

                                break
                await ctx.send(memeHistory[len(memeHistory) - 1])
                return
        await ctx.send("_{}! ({})_".format(str(request['message']), str(request['error'])))

@client.command()
async def meme(ctx):
    async with ctx.typing():
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.reddit.com/r/{0}/hot.json?limit=100".format(random.choice(memeSubreddits))) as response:
                request = await response.json()
    attempts = 1
    while attempts < 5:
        if 'error' in request:
            print("failed request {}".format(attempts))
            await asyncio.sleep(2)
            async with aiohttp.ClientSession() as session:
                async with session.get("https://www.reddit.com/r/{0}/hot.json?limit=100".format(random.choice(memeSubreddits))) as response:
                    request = await response.json()
            attempts += 1
        else:
            index = 0

            for index, val in enumerate(request['data']['children']):
                if 'url' in val['data']:
                    url = val['data']['url']
                    urlLower = url.lower()
                    accepted = False
                    for j, v, in enumerate(acceptableImageFormats): 
                        if v in urlLower:
                            accepted = True
                    if accepted:
                        if url not in memeHistory:
                            memeHistory.append(url)  
                            if len(memeHistory) > 63: 
                                memeHistory.popleft() 

                            break
            await ctx.send(memeHistory[len(memeHistory) - 1])
            return
    await ctx.send("_{}! ({})_".format(str(request['message']), str(request['error'])))

@client.command()
async def dankmemes(ctx):
    await getSub(ctx, 'dankmemes')

@client.command()
async def me_irl(ctx):
    await getSub(ctx, 'me_irl')

@client.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  
  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)
  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description="_ _",
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)


  await ctx.send(embed=embed)

@client.command()
async def wmemes(ctx):
    await getSub(ctx, 'wholesomememes')        

@client.command()
async def trashpandas(ctx):
    await getSub(ctx, 'trashpandas')

@client.command()
async def aww(ctx):
    async with ctx.typing():
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.reddit.com/r/{0}/hot.json?limit=100".format(random.choice(awwSubreddits))) as response:
                request = await response.json()
    attempts = 1
    while attempts < 5:
        if 'error' in request:
            print("failed request {}".format(attempts))
            await asyncio.sleep(2)
            async with aiohttp.ClientSession() as session:
                async with session.get("https://www.reddit.com/r/{0}/hot.json?limit=100".format(random.choice(awwSubreddits))) as response:
                    request = await response.json()
            attempts += 1
        else:
            index = 0

            for index, val in enumerate(request['data']['children']):
                if 'url' in val['data']:
                    url = val['data']['url']
                    urlLower = url.lower()
                    accepted = False
                    for j, v, in enumerate(acceptableImageFormats): 
                        if v in urlLower:
                            accepted = True
                    if accepted:
                        if url not in memeHistory:
                            memeHistory.append(url)  
                            if len(memeHistory) > 63: 
                                memeHistory.popleft() 

                            break
            await ctx.send(memeHistory[len(memeHistory) - 1])
            return
    await ctx.send("_{}! ({})_".format(str(request['message']), str(request['error'])))

async def audio_playing(ctx):
    """Checks that audio is currently playing before continuing."""
    client = ctx.guild.voice_client
    if client and client.channel and client.source:
        return True
    else:
        raise commands.CommandError("Not currently playing any audio.")

@client.command()
async def invite(ctx):
	qrcode = Image.open("qrcode.png")
	await ctx.send("Bot Invite : https://soo.gd/CoeusBot")
	await ctx.send(file = discord.File("qrcode.png"))

@client.command()
async def wanted(ctx, user : discord.Member = None):
    if user == None:
        user = ctx.author

    wanted = Image.open("Wanted.jpg")

    asset = ctx.author.avatar_url_as(size = 128)

    data = BytesIO(await asset.read())

    pfp = Image.open(data)

    pfp = pfp.resize((285,285))

    wanted.paste(pfp, (154,231))

    wanted.save("profile.jpg")

    await ctx.send(file = discord.File("profile.jpg"))



@client.command()
async def ping(ctx):
    await ctx.send("**pong! {0:.2f}ms**".format(client.latency * 1000))


@client.command()
async def shibe(ctx):
    r = requests.get('https://shibe.online/api/shibes?count=1')
    y = r.json()
    embed= discord.Embed(title='Have a shibe.',color=0xff80ff)
    embed.set_author(name=f'{ctx.author.display_name}',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=f'{y[0]}')
    embed.set_footer(text="Coeus Bot - Created by I Am A Trash Panda#5717",icon_url='https://images-ext-2.discordapp.net/external/2k3AybPS8lnMbesLCyQgU04Vbv4d3RGkpIk7H7GoT0I/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/1be8fcd718759eb92f0aa6ff9f2df7db.webp?width=702&height=702')
    await ctx.send(embed=embed)

@client.command()
async def bird(ctx):
    r = requests.get('https://shibe.online/api/birds?count=1')
    y = r.json()
    embed= discord.Embed(title='Have a bird.',color=0xff80ff)
    embed.set_author(name=f'{ctx.author.display_name}',icon_url=f'{ctx.author.avatar_url}')
    embed.set_image(url=f'{y[0]}')
    embed.set_footer(text="Coeus Bot - Created by I Am A Trash Panda#5717",icon_url='https://images-ext-2.discordapp.net/external/2k3AybPS8lnMbesLCyQgU04Vbv4d3RGkpIk7H7GoT0I/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/1be8fcd718759eb92f0aa6ff9f2df7db.webp?width=702&height=702')
    await ctx.send(embed=embed)

@client.command()
@has_permissions(manage_nicknames=True)
async def setnickname(ctx, user: discord.Member, *, nickname: str = None):
        try:
            if nickname != None:
                await user.edit(nick = nickname[:32])
            else:
                await user.edit(nick = nickname)

            em = discord.Embed(color = discord.Color.red())

            if nickname is None:
                em.add_field(name = "Reset Nickname", value = f"{user.mention}'s nickname has been reset.")
            else:
                em.add_field(name = "Set Nickname", value = f"{user.mention}'s nickname has been set to `{nickname}`")

            await ctx.send(embed = em)
        except discord.Forbidden:
            em = discord.Embed(color = discord.Color.dark_teal())
            em.add_field(name = "Forbidden", value = "Couldn't set users nickname. Check if the bot is higher than the user then try again.")
            await ctx.send(embed = em)

@client.command()
async def spoiler(ctx, *, spoiler: str):
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass

        x = ""
        for b in spoiler:
            x += f"||{b}||"
        await ctx.send(x)

@client.command()
async def lenny(ctx, *, message : str = None):
		"""Give me some Lenny."""

		# Log the user
		

		msg = f"{ctx.author.name} jus heckin ( ͡° ͜ʖ ͡°)"
		if message:
			msg += "\n{}".format(message)
		# Send new message first, then delete original
		await ctx.channel.send(msg)

@client.command(aliases = ["aki"])
async def akinator(ctx):
    await ctx.send("Akinator is here to guess!")
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n","p","b"]
    try:
        aki = ak.Akinator()
        q = aki.start_game()
        while aki.progression <= 1000:
            await ctx.send(q)
            await ctx.send("Your answer:(y/n/p/b)")
            msg = await client.wait_for("message", check=check)
            if msg.content.lower() == "b":
                try:
                    q=aki.back()
                except ak.CantGoBackAnyFurther:
                    await ctx.send(e)
                    continue
            else:
                try:
                    q = aki.answer(msg.content.lower())
                except ak.InvalidAnswerError as e:
                    await ctx.send(e)
                    continue
        aki.win()
        await ctx.send(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?(y/n)\n{aki.first_guess['absolute_picture_path']}\n\t")
        correct = await client.wait_for("message", check=check)
        if correct.content.lower() == "y":
            await ctx.send("Yay\n")
        else:
            await ctx.send("Oof\n")
    except Exception as e:
        await ctx.send(e)

@client.command()
async def poopy(ctx, user: discord.Member):

	user1 = ctx.author
	
	user2 = user
	
	poopy = Image.open("poopy.png").convert("RGBA")

	asset = ctx.author.avatar_url

	asset2 = user.avatar_url

	data = BytesIO(await asset.read())

	data2 = BytesIO(await asset2.read())

	pfp = Image.open(data)

	pfp = pfp.resize((99,101))

	pfp2 = Image.open(data2)

	pfp2 = pfp2.resize((99,101))

	poopy.paste(pfp, (34,67))

	poopy.paste(pfp2, (286,349))

	poopy.save("poopy.png")

	
	if ctx.message.author in ctx.message.mentions:
		await ctx.send("EW STINKY FUCKING EW")
	else:
		await ctx.send(file = discord.File("poopy.png"))

@client.command()
async def embed(ctx, *, msg):
    embed = discord.Embed(description = "{}".format(msg))
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command()
async def fml(ctx):
    await getSub(ctx, 'FML')


@client.command()
async def affect(ctx, user : discord.Member = None):

	if user:

		wanted = Image.open("affect.png")

		asset = user.avatar_url_as(size = 128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((201,158))

		wanted.paste(pfp, (180,382))

		wanted.save("newaffect.png")

		await ctx.send(file = discord.File("newaffect.png"))

	else:

		wanted = Image.open("affect.png")

		asset = ctx.author.avatar_url_as(size = 128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((201,158))

		wanted.paste(pfp, (180,382))

		wanted.save("newaffect.png")

		await ctx.send(file = discord.File("newaffect.png"))

@client.command()
async def beautiful(ctx, user : discord.Member = None):

	if user:

		wanted = Image.open("beautiful.png")

		asset = user.avatar_url_as(size = 128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((86,99))

		wanted.paste(pfp, (258,27))

		wanted.paste(pfp, (258,227))

		wanted.save("newbeautiful.png")

		await ctx.send(file = discord.File("newbeautiful.png"))

	else:

		wanted = Image.open("beautiful.png")

		asset = ctx.author.avatar_url_as(size = 128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((86,99))

		wanted.paste(pfp, (258,227))

		wanted.paste(pfp, (258,27))

		wanted.save("newbeautiful.png")

		await ctx.send(file = discord.File("newbeautiful.png"))





@client.command()
async def membercount(ctx):
	embed = discord.Embed(title = "Member Count", description = f"Members In This Server **{ctx.guild.member_count}**")
	embed.set_footer(text="Coeus Bot#5544 made by I Am A Trash Panda#5717", icon_url="https://images-ext-1.discordapp.net/external/mJHEuaVaJRHwDAsqUIQV8llNW0mz5yfqkXqQ0xM9G6o/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859282901123465266/eeb5fb172fa962f6a19a34d65b948375.webp")
	membercount = await ctx.send(embed=embed)
	await membercount.add_reaction("👑") 


@client.command()
async def disabled(ctx, user : discord.Member = None):

	if user:

		wanted = Image.open("disabled.jpg")

		asset = user.avatar_url_as(size = 128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((176,176))

		wanted.paste(pfp, (536,380))

		wanted.save("newdisabled.jpg")

		await ctx.send(file = discord.File("newdisabled.jpg"))

	else:

		wanted = Image.open("disabled.jpg")

		asset = ctx.author.avatar_url_as(size = 128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((176,176))

		wanted.paste(pfp, (536,380))

		wanted.save("newdisabled.jpg")

		await ctx.send(file = discord.File("newdisabled.jpg"))

@client.command()
async def egg(ctx, user : discord.Member = None):

	if user:

		wanted = Image.open("egg.png")

		asset = user.avatar_url_as(size = 128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((46,46))

		wanted.paste(pfp, (128,168))

		wanted.save("newegg.png")

		await ctx.send(file = discord.File("newegg.png"))

	else:

		wanted = Image.open("egg.png")

		asset = ctx.author.avatar_url_as(size = 128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((46,46))

		wanted.paste(pfp, (128,168))

		wanted.save("newegg.png")

		await ctx.send(file = discord.File("newegg.png"))

@client.command()
async def sick(ctx, user : discord.Member = None):

	if user:

		wanted = Image.open("sickban.png")

		asset = user.avatar_url_as(size = 128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((404,404))

		wanted.paste(pfp, (68,340))

		wanted.save("newsickban.png")

		await ctx.send(file = discord.File("newsickban.png"))

	else:

		wanted = Image.open("sickban.png")

		asset = ctx.author.avatar_url_as(size = 128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((404,404))

		wanted.paste(pfp, (68,340))

		wanted.save("newsickban.png")

		await ctx.send(file = discord.File("newsickban.png"))

@client.command()
async def delete(ctx, user : discord.Member = None):

	if user:
		wanted = Image.open("delete.png")

		asset = user.avatar_url_as(size = 128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((181,181))

		wanted.paste(pfp, (106,120))

		wanted.save("newdelete.png")

		await ctx.send(file = discord.File("newdelete.png"))

	else: 
		wanted = Image.open("delete.png")

		asset = ctx.author.avatar_url_as(size = 128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((181,181))

		wanted.paste(pfp, (106,120))

		wanted.save("newdelete.png")

		await ctx.send(file = discord.File("newdelete.png"))

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason = None):
  if not reason:
    await user.kick()
    await ctx.send(f"**{user}** has been kicked for **no reason**.")
    await DMChannel.send(user, f"You have been kicked from **{ctx.guild}**") 
  else:
    await user.kick(reason=reason)
    await ctx.send(f"**{user}** has been kicked for **{reason}**.")
    await DMChannel.send(user, f"You have been kicked from **{ctx.guild}** for **{reason}**") 

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} has been bannned sucessfully")

#start of nsfw commands

@client.command()
async def feet(ctx):
    await nsfwimgfetchfuncs(ctx,"feet","","")

@client.command()
async def yuri(ctx):
    await nsfwimgfetchfuncs(ctx,"yuri","","")

@client.command()
async def trap(ctx):
    await nsfwimgfetchfuncs(ctx,"trap","","")

@client.command()
async def futanari(ctx):
    await nsfwimgfetchfuncs(ctx,"futanari","","")

@client.command()
async def hololewd(ctx):
    await nsfwimgfetchfuncs(ctx,"hololewd","","")

@client.command()
async def lewdkemo(ctx):
    await nsfwimgfetchfuncs(ctx,"lewdkemo","","")

@client.command()
async def cum(ctx):
    await nsfwimgfetchfuncs(ctx,"cum","","")


@client.command()
async def erokemo(ctx):
    await nsfwimgfetchfuncs(ctx,"erokemo","","")

@client.command()
async def les(ctx):
    await nsfwimgfetchfuncs(ctx,"les","","")

@client.command()
async def wallpaper(ctx):
    await nsfwimgfetchfuncs(ctx,"wallpaper","","")

@client.command()
async def lewdk(ctx):
    await nsfwimgfetchfuncs(ctx,"lewdk","","")

@client.command()
async def kuni(ctx):
    await nsfwimgfetchfuncs(ctx,"kuni","","")

@client.command()
async def lewd(ctx):
    await nsfwimgfetchfuncs(ctx, "lewd", "","")

@client.command()
async def gecg(ctx):
    await imgfetchfuncs(ctx,"gecg","","")

@client.command()
async def eroyuri(ctx):
    await nsfwimgfetchfuncs(ctx,"eroyuri", "", "")    

@client.command()
async def eron(ctx):
    await nsfwimgfetchfuncs(ctx,"eron", "", "")

@client.command()
async def bj(ctx):
    await nsfwimgfetchfuncs(ctx,"bj", "", "")

@client.command()
async def solo(ctx):
    await nsfwimgfetchfuncs(ctx,"solo", "", "")

@client.command()
async def kemonomimi(ctx):
    await nsfwimgfetchfuncs(ctx,"kemonomimi", "", "")

@client.command()
async def nsfwavatar(ctx):
    await nsfwimgfetchfuncs(ctx, "nsfw_avatar", "", "")

@client.command()
async def anal(ctx):
    await nsfwimgfetchfuncs(ctx, "anal", "", "")

@client.command()
async def hentai(ctx):
    await nsfwimgfetchfuncs(ctx,"hentai","","")

@client.command()
async def erofeet(ctx):
    await nsfwimgfetchfuncs(ctx,"erofeet","","")

@client.command()
async def pussy(ctx):
    await nsfwimgfetchfuncs(ctx,"pussy","","")

@client.command()
async def tits(ctx):
    await nsfwimgfetchfuncs(ctx,"tits","","")

@client.command()
async def waifu(ctx):
    await imgfetchfuncs(ctx,"waifu","","")

@client.command()
async def boobs(ctx):
        await nsfwimgfetchfuncs(ctx,"boobs","","")

@client.command()
async def foxgirl(ctx):
    await imgfetchfuncs(ctx, "fox_girl", "", "fox girls > all")

@client.command()
async def neko(ctx):
    await imgfetchfuncs(ctx, "neko", "", "")

@client.command()
async def owoify(ctx,*, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    author = ctx.message.author


    embed = discord.Embed(
        colour=discord.Color.from_rgb(r, g, b)
    )
    text = nekos.owoify(reason)
    await ctx.send(text[0:256])
    #print(text)
    #embed.add_field(name=text[0:256], value='‎', inline=False)
    #await ctx.send(embed=embed)

async def imgfetchfuncs(ctx, img_endpoint, title, description):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title="Here you go you horny fuck.",
        description="_ _",
        colour=discord.Color.from_rgb(r, g, b)
    )
    img = nekos.img(img_endpoint)

    embed.set_image(url=img)

    await ctx.send(embed=embed)

async def nsfwimgfetchfuncs(ctx,img_endpoint,title,description):
    if not ctx.channel.is_nsfw():
        error_embed = discord.Embed(
            colour=discord.Colour.red()
        )
        error_embed.add_field(name="Error", value="You tried running an __**NSFW**__ channel only command in a non __**NSFW**__ channel.\nsorry for the inconvience this might have caused, have a neko.")
        error_img = nekos.img("neko")
        error_embed.set_image(url=error_img)
        await ctx.author.send(embed=error_embed)
        await ctx.message.delete()
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
        title="Here you go you horny fuck.",
        description="_ _",
        colour=discord.Color.from_rgb(r, g, b)
    )
    img = nekos.img(img_endpoint)

    embed.set_image(url=img)

    await ctx.send(embed=embed)
#end of nsfw commands


@client.event
async def on_guild_join(guild):
	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefixes[str(guild.id)] = 'nl!'

	with open("prefixes.json", "w") as f:
		json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes.pop(str(guild.id))

	with open('prefixes.json', 'w') as f:
		json.dump(prefixes, f, indent=4)

@client.command()
@has_permissions(administrator=True)
async def changeprefix(ctx, *, pre):
	with open(r"C:\\Users\\Idiot\\OneDrive\\Desktop\\Coeus Bot\\prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefixes[str(ctx.guild.id)] = pre
	await ctx.send(f"New prefix is `{pre}`")

	with open(r"C:\\Users\\Idiot\\OneDrive\\Desktop\\Coeus Bot\\prefixes.json", "w") as f:
		json.dump(prefixes, f,indent=4)

@client.command()
async def simp(ctx, user : discord.Member = None):

	if user:

		wanted = Image.open("simp.png")

		asset = user.avatar_url_as(size=128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((170,242))

		wanted.paste(pfp, (90,139))

		wanted.save("newsimp.png")

		await ctx.send(file = discord.File("newsimp.png"))

	else:

		wanted = Image.open("simp.png")

		asset = ctx.author.avatar_url_as(size=128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((170,242))

		wanted.paste(pfp, (90,139))

		wanted.save("newsimp.png")

		await ctx.send(file = discord.File("newsimp.png"))

@client.command()
async def horny(ctx, user : discord.Member = None):

	if user:

		wanted = Image.open("horny.jpg")

		asset = user.avatar_url_as(size=128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((321,317))

		wanted.paste(pfp, (65,199))

		draw = ImageDraw.Draw(wanted)

		font = ImageFont.truetype("arial.ttf", 24)

		draw.text((708,768), user.display_name, (0, 0, 0), font=font)

		wanted.save("newhorny.jpg")

		await ctx.send(file = discord.File("newhorny.jpg"))

	else:

		wanted = Image.open("horny.jpg")

		asset = ctx.author.avatar_url_as(size=128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((321,317))

		wanted.paste(pfp, (65,199))

		draw = ImageDraw.Draw(wanted)

		font = ImageFont.truetype("arial.ttf", 24)

		draw.text((708,768), ctx.author.display_name, (0, 0, 0), font=font)
	
		wanted.save("newhorny.jpg")

		await ctx.send(file = discord.File("newhorny.jpg"))

@client.command()
async def lgbt(ctx, user : discord.Member = None):
	if user:
		asset = user.avatar_url_as()
		data = BytesIO(await asset.read())
		pfp = Image.open(data)
		pfp.save("pfp.png")

		im1 = Image.open('pfp.png')
		im2 = Image.open("lgbtflag.png").resize(im1.size)

		im5 = im1.convert("RGBA")
		im6 = im2.convert("RGBA")

		alphaBlend1 = Image.blend(im5, im6, alpha = .75)

		alphaBlend1.save("pfpflag.png")

		file = discord.File("C:\\Users\\Idiot\\OneDrive\\Desktop\\Coeus Bot\\pfpflag.png", filename = "pfpflag.png")

		embed = discord.Embed(color= discord.Colour.random())
		embed.set_image(url = "attachment://pfpflag.png")

		await ctx.send(file=file,embed=embed)

	else:
		asset = ctx.author.avatar_url_as()
		data = BytesIO(await asset.read())
		pfp = Image.open(data)
		pfp.save("pfp.png")

		im1 = Image.open('pfp.png')
		im2 = Image.open("lgbtflag.png").resize(im1.size)

		im5 = im1.convert("RGBA")
		im6 = im2.convert("RGBA")

		alphaBlend1 = Image.blend(im5, im6, alpha = .75)

		alphaBlend1.save("pfpflag.png")

		file = discord.File("C:\\Users\\Idiot\\OneDrive\\Desktop\\Coeus Bot\\pfpflag.png", filename = "pfpflag.png")

		embed = discord.Embed(color= discord.Colour.random())
		embed.set_image(url = "attachment://pfpflag.png")

		await ctx.send(file=file,embed=embed)


@client.command()
async def ugly(ctx, user : discord.Member = None):

	if user:

		wanted = Image.open("ugly.png")

		asset = user.avatar_url_as(size=128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((183,183))

		wanted.paste(pfp, (116,53))

		wanted.save("newugly.png")

		await ctx.send(file = discord.File("newugly.png"))

	else:

		wanted = Image.open("ugly.png")

		asset = ctx.author.avatar_url_as(size=128)

		data = BytesIO(await asset.read())

		pfp = Image.open(data)

		pfp = pfp.resize((183,183))

		wanted.paste(pfp, (116,53))

		wanted.save("newugly.png")

		await ctx.send(file = discord.File("newugly.png"))


@client.command()
async def clap(ctx, *, msg):
	clap_emoji = " 👏 "
	text = msg.replace(" ", clap_emoji)
	await ctx.send(text)

@client.command(aliases=["cuddles", "Cuddle", "Cuddles", "spoon", "Spoon"])
async def cuddle(ctx, member : discord.Member):

	cuddles = ["https://i.imgur.com/p2Jt2P5.gif",
			   "https://media1.tenor.com/images/cc97ccaa57b356fb1ea040cfa830970c/tenor.gif?itemid=16558579",
			   "https://thumbs.gfycat.com/EnergeticQuaintHornedtoad-size_restricted.gif",
			   "https://images-ext-2.discordapp.net/external/upPbrR5f3Mytsi0lDgPVBDLsH9fXE3I92MopkH6anOM/https/cdn.weeb.sh/images/SkeHkUU7PW.gif",
			   "https://images-ext-2.discordapp.net/external/O4IHGSp18qB9033IY0xfZe5WFoJUjtS4zAiCscQU4gU/https/cdn.weeb.sh/images/rkBl8LmDZ.gif",
			   "https://images-ext-1.discordapp.net/external/NLl_nyzLp_Drq1bQyl2e6rLvIJPOsVxqGxhVSyMJz-Q/https/cdn.weeb.sh/images/r1XEOymib.gif",
			   "https://images-ext-2.discordapp.net/external/v96Ta_KPLMw94ZnN3H166MLO8bXDIi5fGA6zb6YnEQ4/https/cdn.weeb.sh/images/ByXs1AYKW.gif?width=453&height=473",
			   "https://images-ext-1.discordapp.net/external/ajddIhPZ_XgV1D6S6lsZdQaFKYZzMxhspzspH9b43RA/https/cdn.weeb.sh/images/SJbGLUQwZ.gif",
			   "https://images-ext-1.discordapp.net/external/UUo1ZBXzczbMAjBeEk3PolotXEDNuA16tCd9Y-KRMHw/https/cdn.weeb.sh/images/ryURHLXP-.gif",
			   "https://images-ext-1.discordapp.net/external/_Zga5EaW-1USVM3kUF3BC7FLxawdXjvzCv7ZIpy1X34/https/cdn.weeb.sh/images/SJceIU7wZ.gif",
			   "https://images-ext-2.discordapp.net/external/WTezF_lBdL2PKmcOFQVo7xocXD9pJLmGMJhDRvzjiug/https/cdn.weeb.sh/images/rkA6SU7w-.gif",
			   "https://images-ext-1.discordapp.net/external/no-ZYHnPdBboFs2y19kSLk1gWnnf2h1_Tj1K0Qt-9uA/https/cdn.weeb.sh/images/BJwpw_XLM.gif",
			   "https://i.imgur.com/nrdYNtL.gif",
			   "http://25.media.tumblr.com/cd5fc6a0a57fa3c133328ca7bee20b6d/tumblr_mlrz1c22SK1rarypbo1_500.gif",
			   "https://i.pinimg.com/originals/4b/22/5d/4b225d7e33c35131ddf24c831eca11b8.gif",
			   "https://i.imgur.com/eTZ063r.gif?noredirect",
			   "https://66.media.tumblr.com/1b537d658df2f2a9594b83d3e768bbe1/tumblr_o373tkcR7E1ub9qlao1_400.gifv",
			   "https://64.media.tumblr.com/12dba5d6b60ee757a3aa08917876c22a/a009e8fb440c673e-64/s400x600/7566e58321446a9afa6bedbd7fca1cabcfe8d018.gifv",
			   "https://media1.tenor.com/images/f8c810e24acbdfde36d1908e10e39c28/tenor.gif?itemid=13041470",
			   "https://media0.giphy.com/media/QlFyrikSI01Fe/giphy.gif",
			   "https://i.imgur.com/oltglhh.gif",
			   "https://media2.giphy.com/media/r6JG0CPc3yQ7u/giphy.gif",
			   "https://acegif.com/wp-content/gif/anime-hug-30.gif",
			   "https://thumbs.gfycat.com/FemaleTotalBlacknorwegianelkhound-size_restricted.gif",
			   "https://i.imgur.com/LqdoObW.gif",
			   "https://acegif.com/wp-content/gif/anime-hug-21.gif",
			   "https://i.pinimg.com/originals/f5/8d/c0/f58dc05305285aefd2efdb8b5671d2c8.gif",
			   "https://i.imgur.com/gSGeZJF.gif",
			   "https://pa1.narvii.com/6472/0bb16033352529eaa6eec73a63f347967e330c62_hq.gif",
			   "https://images-ext-1.discordapp.net/external/j2lZhG1iY9jAPEab8SxR6FFo4V9uVghg92yJUZDCwiI/https/cdn.weeb.sh/images/BJkABImvb.gif?width=428&height=473",
			   "https://images-ext-1.discordapp.net/external/gRGzIxTDKkaXSG_OmaIfyNNxzkV_bqorHdLUsgIPmhw/https/cdn.weeb.sh/images/SykzL87D-.gif",
			   "https://images-ext-1.discordapp.net/external/n5gCINmkwNJc4EFNBDv-6y30bNh7dx53Rovm484lKbM/https/cdn.weeb.sh/images/BkZCSI7Pb.gif"
			   ]

	face = ["(*^.^*)",
			"＠＾▽＾＠",
			"(´ω｀*)",
			"(‘-’*)",
			"(/ε＼*)",
			"(*^^*)",
			"(*^_^*)",
			"(•ﾟдﾟ•)",
			"(*ﾟ∀ﾟ*)",
			"(^-^*)ノ",
			"(・´ｪ｀・)",
			"(*´ω｀*)",
			"(〃￣ω￣〃ゞ)",
			"v(・∀・*)",
			"(*≧∀≦*)",
			"v(^∀^*)",
			"^-^"]

	action = [ f"{ctx.author.display_name} snuggles up to {member.display_name} ~ how cute!",
			   f"{ctx.author.display_name} cuddles {member.display_name} ~ adorable!",
			   f"{member.display_name} gets great cuddles from {ctx.author.display_name}"]

	embed = discord.Embed(title = f"Yay cuddles {random.choice(face)}", description = f"{random.choice(action)}", color = 0x176cd5)
	embed.set_image(url=random.choice(cuddles))
	if ctx.message.author in ctx.message.mentions:
		await ctx.send("Hey someone get this person some cuddles pronto!")
	else:
		await ctx.send(embed=embed)

@client.command(aliases=["pats", "Pat", "Pats"])
async def pat(ctx, member : discord.Member):

	cuddles = ["https://media.tenor.com/images/ad8357e58d35c1d63b570ab7e587f212/tenor.gif",
			   "https://media.tenor.com/images/385a8d13c1ee5213e560e07d12320d02/tenor.gif",
			   "https://media4.giphy.com/media/ARSp9T7wwxNcs/200.gif",
			   "https://media.tenor.com/images/da8431374a530ae516c0cc8f966d1c2b/tenor.gif",
			   "https://thumbs.gfycat.com/CoordinatedVainGermanwirehairedpointer-size_restricted.gif",
			   "https://thumbs.gfycat.com/AgileHeavyGecko-max-1mb.gif",
			   "https://i.imgur.com/UWbKpx8.gif",
			   "https://i.gifer.com/7eXV.gif",
			   "https://i.pinimg.com/originals/d7/c3/26/d7c326bd43776f1e0df6f63956230eb4.gif",
			   "https://i.imgur.com/4ssddEQ.gif",
			   "https://media.tenor.com/images/a671268253717ff877474fd019ef73e9/tenor.gif",
			   "https://media3.giphy.com/media/Z7x24IHBcmV7W/giphy.gif",
			   "https://thumbs.gfycat.com/FlimsyDeafeningGrassspider-max-1mb.gif",
			   "https://i.pinimg.com/originals/70/96/0e/70960e87fb9454df6a1d15c96c9ad955.gif",
			   "https://media.tenor.com/images/1d37a873edfeb81a1f5403f4a3bfa185/tenor.gif",
			   "https://64.media.tumblr.com/80f4e1aeee44dee530b1e6b416a8459d/83ad7e3b43d48041-53/s500x750/ddbb45d884338428dd0f1e042099b353fd3f49b3.gif",
			   "https://68.media.tumblr.com/1c433aeea03d0fcee34c22696ba1307b/tumblr_osl1kmMWL91qbvovho1_500.gif",
			   "https://64.media.tumblr.com/1e92c03121c0bd6688d17eef8d275ea7/tumblr_pjgkb7Q1oi1ubu1ls_500.gifv",
			   "https://thumbs.gfycat.com/EnchantingObedientGermanspitz-max-1mb.gif",
			   "https://i.pinimg.com/originals/3c/ac/21/3cac213405fcb7dcbd16983b333375f0.gif",
			   "http://pa1.narvii.com/6260/3fc8451fb1cba6fc5b0483b144d2507229a80305_hq.gif",
			   "https://memestatic.fjcdn.com/gifs/Headpat_17fcf6_6500559.gif",
			   "https://media.tenor.com/images/37e36267891a33899bb2d88232f9f637/tenor.gif",
			   "https://i.imgur.com/d9CH89Q.gif",
			   "https://i.gifer.com/7MOk.gif",
			   "https://thumbs.gfycat.com/ImpurePleasantArthropods-max-1mb.gif",
			   "https://i.imgur.com/LUypjw3.gif",
			   "https://i.gifer.com/Jxpz.gif",
			   "https://i.imgur.com/nC4Vyhm.gif",
			   "https://i.imgur.com/OM9eiJ1.gif",
			   "https://media1.giphy.com/media/PHZ7v9tfQu0o0/200w.gif?cid=82a1493bj3c1iqso5cqklvew753qx3gzod3xmg6kso8o4gtv&rid=200w.gif&ct=g",
			   "https://i.imgur.com/IG5ddNO.gif"
			   ]

	face = ["(*^.^*)",
			"＠＾▽＾＠",
			"(´ω｀*)",
			"(‘-’*)",
			"(/ε＼*)",
			"(*^^*)",
			"(*^_^*)",
			"(•ﾟдﾟ•)",
			"(*ﾟ∀ﾟ*)",
			"(^-^*)ノ",
			"(・´ｪ｀・)",
			"(*´ω｀*)",
			"(〃￣ω￣〃ゞ)",
			"v(・∀・*)",
			"(*≧∀≦*)",
			"v(^∀^*)",
			"^-^"]

	action = [ f"{ctx.author.display_name} pats {member.display_name} ~ how cute!",
			   f"{ctx.author.display_name} gives pats to {member.display_name} ~ adorable!",
			   f"{member.display_name} gets amazing pats from {ctx.author.display_name}"]

	embed = discord.Embed(title = f"Aww pats {random.choice(face)}", description = f"{random.choice(action)}", color = 0x176cd5)
	embed.set_image(url=random.choice(cuddles))
	if ctx.message.author in ctx.message.mentions:
		await ctx.send("Hey someone get this person pats now!")
	else:
		await ctx.send(embed=embed)

@client.command()
@has_permissions(manage_messages=True)
async def announce(ctx, channel : discord.TextChannel, *, message):
	embed = discord.Embed(color = discord.Colour.random())
	embed.add_field(name = f"Announcement by {ctx.author.display_name}", value = message)
	await channel.send(embed=embed)
	await ctx.message.delete()


@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(embed=discord.Embed(title = "Thank you for adding me to your server! 👉😎👉", description = "To display the category of commands use the command help `nl!help` to show commands for emotes, games and more\n \n If any concerns or help is needed please contact our developer ||I Am A Trash Panda#5717||\n \n Furthermore if any requests or any suggestions are thought of please contact the developer who is previously aforementioned.\n \n Once again I hope you have fun with 121 available commands."))
        user = await client.fetch_user("474261671918174232")
        await DMChannel.send(user, f"I just joined {guild.name}")
        break

@client.command(pass_context=True)
async def emotes(ctx, msg: str = None):
    if msg:
        server, found = client.find_server(msg)
        if not found:
            return await client.send(server)
    else:
        server = ctx.guild
    emojis = [str(x) for x in server.emojis]
    embed = discord.Embed(title = f"Here are the emojis from {ctx.guild.name}",description = (" ".join(emojis)), color = discord.Color.random())
    await ctx.send(embed=embed)


@client.command(aliases=["bites", "Bite", "Bites"])
async def bite(ctx, member : discord.Member):

	bites = ["https://media1.tenor.com/images/f308e2fe3f1b3a41754727f8629e5b56/tenor.gif?itemid=12390216",
			   "https://media1.tenor.com/images/b308e5535251c436fbfaf424fa7a4b75/tenor.gif?itemid=13859648",
			   "https://media1.tenor.com/images/06f88667b86a701b1613bbf5fb9205e9/tenor.gif?itemid=13417199",
			   "https://media1.giphy.com/media/OqQOwXiCyJAmA/giphy.gif",
			   "https://media1.tenor.com/images/963e4620c8b6345f09d7d22ef1c91420/tenor.gif?itemid=12045584",
			   "https://thumbs.gfycat.com/UniqueThickGalapagosalbatross-size_restricted.gif",
			   "http://24.media.tumblr.com/9c456f389936eafa9b1f34e15aa8c28e/tumblr_mq4xj1Px811s5dbs1o1_500.gif",
			   "https://thumbs.gfycat.com/DefiniteBossyFlounder-size_restricted.gif",
			   "https://media1.tenor.com/images/2440ac6ca623910a258b8616704850f0/tenor.gif?itemid=7922565",
			   "https://media0.giphy.com/media/3qa8z4JpTTbsQ/giphy.gif",
			   "https://i.pinimg.com/originals/ec/78/5f/ec785fb9c68a789b645d9b1adeb6dd6d.gif",
			   "https://media.tenor.com/images/670ae3107bc19c6297511fcf62cc84df/tenor.gif",
			   "https://thumbs.gfycat.com/BlackandwhitePlushEeve-small.gif",
			   "http://24.media.tumblr.com/0997d9e6865c7a8fd53f65a8e3018017/tumblr_msizvuMMBa1s7s6pro1_500.gif",
			   "https://media4.giphy.com/media/14krMb54Cw2T60/giphy.gif",
			   "https://media4.giphy.com/media/ASeK6nCfqZXC8/giphy.gif",
			   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSAGI_jcb6-Xd9zoWF_MYEtyK-pmvJ50j8kA&usqp=CAU",
			   "https://media1.tenor.com/images/57f08a1c0a7999f98d4d2cc6f2a33666/tenor.gif?itemid=16660238",
			   "https://i2.wp.com/gifimage.net/wp-content/uploads/2017/09/anime-bite-gif-4.gif",
			   "https://gifimage.net/wp-content/uploads/2017/09/anime-bite-gif-3.gif",
			   "https://i.pinimg.com/originals/61/94/32/6194329007a4a09db4b5bebcc0f98b6e.gif",
			   "https://www.icegif.com/wp-content/uploads/nezuko-icegif-1.gif",
			   "https://pa1.narvii.com/5805/3c2b05492e800861834367ffdeb822ae8c12bb8b_hq.gif",
			   "https://i.pinimg.com/originals/ea/b4/55/eab45577ce6e8e8fb7e1a1b5730dec30.gif",
			   "https://www.pbh2.com/wordpress/wp-content/uploads/2013/02/19-finger-chew-wtf-anime.gif",
			   "https://media1.tenor.com/images/89f6c275fb5cdf44c7b75c92306b8d66/tenor.gif?itemid=12652308",
			   "https://i0.wp.com/fsmedia.imgix.net/47/6f/95/eb/9b55/4af0/8c26/27a7fe448a81/eren-bites-his-own-hand-in-order-to-become-a-titan.gif",
			   "https://animesher.com/orig/0/83/836/8362/animesher.com_kirara-bernstein-bite-funny-836205.gif",
			   "https://thumbs.gfycat.com/FixedJovialBoar-size_restricted.gif",
			   "http://pa1.narvii.com/5910/43955a023f1ad5646d848be9ec21cd7706bae5ca_hq.gif",
			   "https://64.media.tumblr.com/b1b7287355aedb3f0321188cb255d5d2/tumblr_p8a7oxomw61th206io3_640.gifv"
			   ]

	face = ["٩(͡๏̮͡๏)۶",
			"ಠ益ಠ",
			"ლ(́◉◞౪◟◉‵ლ)",
			"ↁ_ↁ",
			"щ(ಠ益ಠщ)",
			"o(≧o≦)o",
			"〴⋋_⋌〵",
			"щ(ಥДಥщ)",
			"(◡︿◡✿)",
			"(⋋▂⋌)",
			"ಠoಠ",
			"╚(•⌂•)╝",
			"ヾ(｀ε´)ノ",
			"(>.<)",
			"(*≧∀≦*)",
			"v(^∀^*)",
			"^-^"]

	action = [ f"{ctx.author.display_name} bites {member.display_name} ~ Ouch!",
			   f"{ctx.author.display_name} bites {member.display_name} ~ Owie!",
			   f"{ctx.author.display_name} bites {member.display_name} ~~ Kinky ;)",
			   f"{ctx.author.display_name} bites into {member.display_name} ~ adorable!",
			   f"{member.display_name} gets the chomp from {ctx.author.display_name}"]

	embed = discord.Embed(title = f"Bite chomp cronch {random.choice(face)}", description = f"{random.choice(action)}", color = 0x176cd5)
	embed.set_image(url=random.choice(bites))
	if ctx.message.author in ctx.message.mentions:
		await ctx.send("I mean to each their own I guess!")
	else:
		await ctx.send(embed=embed)

client.run("removed for safety purposes")





