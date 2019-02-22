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


client = discord.Client()


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
        self.add_command(self.sad)


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
        # author = ctx.author
        """ tells a user not to be sad """
        await ctx.send("no sad")

    #async def on_message(self, message):
        # we do not want the bot to reply to itself
       # if message.author.bot:
        #    return

       # if 'im sad' in message.content:
       #     await message.channel.send(f'Dont be sad, {message.author.mention}')

        #  if message.content.contains('im sad'):
        #      msg = 'dont be sad'
        #     await client.send_message(message.channel,msg)

        #   elif message.content.startswith('!hello'):
        #       msg = 'Hello {0.author.mention}'.format(message)
        #      await client.send_message(message.channel, msg)

    # @cool.command(name='bot')
    # async def _bot(self, ctx):
    #     """Is the bot cool?"""
    #     await ctx.send('Yes, the bot is cool.')

    # @cool.command(name='tatum')
    # async def _tatum(self, ctx):
    #    lol kk oh bf not gonna like thattt """Is tatum cool?"""
    #     await ctx.send('Yes, tatum is the coolest. You damn right i am')
    #  NTQ2ODU3MjY5ODY2OTIxOTk0.D1DYHQ.Lb29wyLXs7xqW_-QzpDUOrklSWMs
    # whats venv


Togepi().run()
