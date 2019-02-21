from discord.ext import commands
import discord
from discord import utils
import random
import os


def run_in(channels):
    def predicate(ctx):
        return ctx.message.channel.name in channels
    return commands.check(predicate)

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

class Togepi(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='?',
            description='''Hi! I'm Togepi!''',
            fetch_offline_members=True
        )

        self.client_id = os.environ.get('CLIENT_ID')
        self.token = os.environ.get('BOT_TOKEN')

        self.add_command(self.hello)

    async def on_ready(self):
        print(f'Ready: {self.user} (ID: {self.user.id})')

    # async def on_message(self, message):
    #     if message.author.bot:
    #         return
    #     await self.process_commands(message)

    def run(self):
        try:
            super().run(
                self.token,
                reconnect=True
            )
        finally:
            pass

    @commands.command()
    async def hello(self, ctx):
        author = ctx.author
        """says hello"""
        await ctx.message.add_reaction('❤')
        await ctx.send("Hello! {author.mention}".format(author=author))

    @commands.command()
    async def sad(self, ctx):
        author = ctx.author
        """ tells a user not to be sad """
        await ctx.send("no sad")


   

    # @cool.command(name='bot')
    # async def _bot(self, ctx):
    #     """Is the bot cool?"""
    #     await ctx.send('Yes, the bot is cool.')

    # @cool.command(name='tatum')
    # async def _tatum(self, ctx):
    #     """Is tatum cool?"""
    #     await ctx.send('Yes, tatum is cool.')


Togepi().run()