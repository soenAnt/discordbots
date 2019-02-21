# Work with Python 3.6
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = "NTQ2ODU3MjY5ODY2OTIxOTk0.D0vYeA.MqQ3OPBGxxf_0r2xRzM9Y8yUbQU"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'Absolutely NOT',
        'It is not looking likely',
        'Nah uh',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'I think so!',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello') or message.content.startswith('?hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('im sad') or message.content.startswith('Im sad') or message.content.startswith("I'm sad"):
        msg = 'Dont be sad {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    elif message.content.startswith('bye') or message.content.startswith('Bye') or message.content.startswith('bai'):
        msg = 'Bye! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)



async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)