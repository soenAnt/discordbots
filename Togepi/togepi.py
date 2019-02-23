from discord.ext import commands
import discord
from discord import utils
import random
import os
from dotenv import load_dotenv
load_dotenv()
print(os.environ.get('BOT_TOKEN'))


def run_in(channels):
    def predicate(ctx):
        return ctx.message.channel.name in channels

    return commands.check(predicate)


class Togepi(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='?',
            description='''Hi! I'm Togepi!''',
            fetch_offline_members=True)

        self.client_id = os.environ.get('CLIENT_ID')
        self.token = os.environ.get('BOT_TOKEN')

        self.add_command(self.hello)
        self.add_command(self.sad)
        self.add_command(self.vote)

    async def on_ready(self):
        print(f'Ready: {self.user} (ID: {self.user.id})')

    def run(self):
        try:
            super().run(self.token, reconnect=True)
        finally:
            pass

    @commands.command()
    async def hello(self, ctx):
        """: says hello back!"""
        author = ctx.author
        await ctx.message.add_reaction('❤')
        await ctx.send("Hello! {author.mention}".format(author=author))

    @commands.command()
    async def vote(self, ctx):
        """: allows reaction vote!"""
        #author = ctx.author
        await ctx.message.add_reaction('😍')
        await ctx.message.add_reaction('😡')
       # await ctx.send("Hello! {author.mention}".format(author=author))

    @commands.command()
    async def sad(self, ctx):
        """: tells a user not to be sad """
        await ctx.send("no sad pls")

    async def on_message(self, message):
        # we do not want the bot to reply to itself

        if message.author.bot:
            return
        #string comprehension
        if any([sub in message.content for sub in ('im sad', 'i\'m sad')]):
            await message.add_reaction('❤')
            await message.add_reaction('😢')
            await message.channel.send(
                f'Dont be sad, {message.author.mention} !!!')

        #elif message.content.find('bye') != -1:
        elif any([sub in message.content for sub in('bye', 'Bye', 'bai', 'Bai','goodnight','gn','good night',)]):
            await message.add_reaction('😘')
            await message.channel.send(
                f'Bye Bye, {message.author.mention} !!'
            )
        
        if str(message.author) in ["Dawgears🐶#6303"]:
            await message.add_reaction('🖕') # for you, self may be client

        if str(message.author) in ["noax#0265"]:
            await message.add_reaction('🐧') # for you, self may be client

        if str(message.author) in ["Taterz#6769"]:
            await message.add_reaction(r":gasp:535632776787918858") # for you, self may be client

        await self.process_commands(message)


Togepi().run()
