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
        """says hello"""
        author = ctx.author
        await ctx.message.add_reaction('❤')
        await ctx.send("Hello! {author.mention}".format(author=author))

    @commands.command()
    async def vote(self, ctx):
        """says vote"""
        author = ctx.author
        await ctx.message.add_reaction('❤')
        await ctx.send("Hello! {author.mention}".format(author=author))

    @commands.command()
    async def sad(self, ctx):
        """ tells a user not to be sad """
        await ctx.send("no sad")

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


Togepi().run()
