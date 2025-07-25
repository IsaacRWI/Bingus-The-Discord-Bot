import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import logging
from asyncio import sleep
from dotenv import load_dotenv
import os
from datetime import datetime

from yt_dlp import YoutubeDL

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')  # logs the status messages in discord/log for debugging

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
# sets the intents for the bot (permissions)

ydl_options = {"format" : "bestaudio" , "noplaylist" : True}
ffmpeg_options = {"options": "-vn"}
# options for ytdlp and ffmpeg that will be referenced later in the code

bot = commands.Bot(command_prefix = '!', intents=intents)  # sets up the command prefix

bingu_role = "bingu"  # name of role that the bot is aware of will be referenced later in the code

@bot.event
async def on_ready():
    """
    Once the bot is online, it prints out a line saying the bot is now online, along with which bot it is and at what
    time it was initialised.
    :return: str
    """
    print(f'bot is now online, bot: {bot.user.name}')
    print(f"Initiation time: {datetime.now( )}")
    print('-----------------------------------------')

@bot.event
async def on_member_join(member):
    """
    Sends a dm to the member that just joined the server
    :param member: the member that just joined the server
    :return: None
    """
    await member.send(f'{member.name}, bingus greets you.')

@bot.event
async def on_message(message):
    """
    If the user sends a message contain the word 'hippo', Bingus removes it and warns the user to not use that word again,
    as Bingus does not like hippos
    :param message: the message that contained the word 'hippo'
    :return: None
    """
    if message.author == bot.user:
        return

    if "hippo" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} bingus does not like hippos")

    await bot.process_commands(message)  # this needs to be here at the end for on_message functions

@bot.command()
async def aid (ctx):
    """
    A command that returns a string of the commands to reach Bingus
    :param ctx: ctx is the parameter discord.py takes that tell the bot to take in the context of the command
    :return: None
    """
    embedded_message = discord.Embed(title="The phrases to reach Bingus are as follows:", description="""!hellob:  You greets bingus warmly and will result in Bingus returning the favor.
    !pledge:  You pledge your allegiance to Bingus, becoming a servant of it, bingu.
    !escape:  You forfeit your privilege to be a servant of Bingus, you are now binguless.
    !verify:  You look up to Bingus for validation and he confirms you a real one.
    !dm:  You send Bingus a message and he replies to you in your dms.
    !reply:  You force Bingus to reply to your message regardless of whether it wants to or not.
    !poll:  You summon Bingus to ascertain the opinion of the masses, collected as cute emojis.
    !plankton:  Bingus plays the plankton meme.
    !p *:  Bingus searches youtube for * and plays it in the voice channel.""")
    await ctx.send(embed=embedded_message)


@bot.command()  # bot.commands() needs a bracket following it unlike bot.events that don't
async def hellob(ctx):  # ctx means context or the person or event that triggered the command
    """
    Makes Bingus send a greeting back at the user
    :param ctx: ctx is the parameter discord.py takes that tell the bot to take in the context of the command
    :return: None
    """
    await ctx.send(f"{ctx.author.mention} bingus greets you.")  # ctx.send sends the message in the channel it was triggered

@bot.command()
async def pledge(ctx):
    """
    Makes the bot give the user the role of 'bingu'
    :param ctx: ctx is the parameter discord.py takes that tell the bot to take in the context of the command
    :return: None
    """
    role = discord.utils.get(ctx.guild.roles, name=bingu_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} you are now a servent of bingus")
    else:
        await ctx.send(f"{ctx.author.mention} {role} role does not exist")

@bot.command()
async def escape  (ctx):
    """
    Makes the bot remove the role of 'bingu' from user
    :param ctx: ctx is the parameter discord.py takes that tell the bot to take in the context of the command
    :return: None
    """
    role = discord.utils.get(ctx.guild.roles, name=bingu_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention}, you are now free of the shackles of bingus")
    else:
        await ctx.send(f"{ctx.author.mention}, you were never granted the role of {role}")

@bot.command()
@commands.has_role(bingu_role)
async def verify(ctx):
    """
    The bot checks the user whether they have the role of 'bingu' and sends a confirmation if they do
    :param ctx: ctx is the parameter discord.py takes that tell the bot to take in the context of the command
    :return: None
    """
    await ctx.send(f"{ctx.author.mention}, you are a certified servent of bingus")

@verify.error
async def verify_error(ctx, error):
    """
    If the user does not have the role of 'bingu' the bot sends them confirmation that they do not have the role
    :param ctx: ctx is the parameter discord.py takes that tell the bot to take in the context of the command
    :param error: is the missing role error as the bot cannot remove a role the user does not have
    :return: None
    """
    if isinstance(error, commands.MissingRole):
        await ctx.send(f"{ctx.author.mention}, you are no true bingu")
    else:
        await ctx.send(f"error: {error}")

@bot.command()
# !dm hello world  # "hello world" would be the msg
async def dm(ctx, *, msg):
    """
    Makes the bot send you a direct message containing your message
    :param ctx: ctx is the parameter discord.py takes that tell the bot to take in the context of the command
    :param msg: will be the message you attach after the command !dm
    :return: None
    """
    await ctx.author.send(f"tf did you mean by {msg}")

@bot.command()
async def reply(ctx):
    """
    Makes the bot reply to your message in agreement
    :param ctx: ctx is the parameter discord.py takes that tell the bot to take in the context of the command
    :return: None
    """
    await ctx.reply("type shyt")

@bot.command()
async def poll(ctx, *, question):
    """
    Makes the bot create a poll which is just an embedded message with reactions as the votes
    :param ctx: ctx is the parameter discord.py takes that tell the bot to take in the context of the command
    :param question: the question you want a poll of
    :return: None
    """
    embedded_message = discord.Embed(title="make your opinions known", description=question)
    poll_message = await ctx.send(embed=embedded_message)
    await poll_message.add_reaction("😞")
    await poll_message.add_reaction("👍")

@bot.command(pass_context = True)
async def plankton (ctx):
    """
    Plays the plankton meme sound effect 'plankton-augh.mp3'
    :param ctx: ctx is the parameter discord.py takes that tell the bot to take in the context of the command
    :return: None
    """
    await ctx.send("plankton request received")
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        source = FFmpegPCMAudio('plankton-augh.mp3')
        voice = await channel.connect()
        voice.play(source)
        await sleep(4)
        await ctx.voice_client.disconnect()

    else:
        await ctx.send("You need to be in a voice channel to hear plankton")

@bot.command()
async def dc (ctx):
    """
    Disconnects the bot from the voice channel
    :param ctx: ctx is the parameter discord.py takes that tell the bot to take in the context of the command
    :return: None
    """
    if not ctx.author.voice:
        await ctx.send("monke im not even in your channel")
    else:
        await ctx.send("bye monke")
        await ctx.voice_client.disconnect()

@bot.command()
async def p (ctx, *, search):
    """
    Makes the bot go on youtube and search for a video matching your input, then play it in your voice channel
    :param ctx: ctx is the parameter discord.py takes that tell the bot to take in the context of the command
    :param search: the message you attach after command !p
    :return: None
    """
    if not ctx.author.voice:
        await ctx.send("You need to be in a voice channel to hear Bingus sing.")
    else:
        voice_channel = ctx.message.author.voice.channel
        await ctx.send("Play request received")
        async with ctx.typing():
            with YoutubeDL(ydl_options) as ydl:
                info = ydl.extract_info(f"ytsearch:{search}", download=False)
                # print(info)
                if "entries" in info:
                    info = info["entries"][0]
                url = info["url"]
                title = info["title"]
                author = info["channel"]
                channel = ctx.author.voice.channel
                await channel.connect()
                source = await discord.FFmpegOpusAudio.from_probe(url, **ffmpeg_options)
                await ctx.send(f"Now playing **{title}** by **{author}**")
                await ctx.voice_client.play(source)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)  # needs to be at the end (python sequential processing)
# client.run(bot api address)
