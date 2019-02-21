from discord.ext import commands
import discord
from discord import utils
import random
import os


def run_in(channels):
    def predicate(ctx):
        return ctx.message.channel.name in channels
    return commands.check(predicate)


class Larvitar(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='?',
            description='''An example bot''',
            fetch_offline_members=True
        )

        self.client_id = os.environ.get('CLIENT_ID')
        self.token = os.environ.get('BOT_TOKEN')

        self.add_command(self.add)
        self.add_command(self.roll)
        self.add_command(self.choose)
        self.add_command(self.repeat)
        self.add_command(self.joined)
        self.add_command(self.cool)
        self.add_command(self.role)
        self.add_command(self.roles)
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
        """says hello"""
        await ctx.send('Hello!')

    @commands.command()
    async def roles(self, ctx):
        """Get all role names in the server."""
        rolenames = [role.name for role in ctx.guild.roles]
        rolenames.remove('@everyone')
        await ctx.send(rolenames)

    @commands.command()
    async def role(self, ctx, operation: str, rolename: str, member: discord.Member = None):
        """Add or remove a role to yourself or a member."""
        try:
            user = member or ctx.message.author
            role = discord.utils.get(ctx.guild.roles, name=rolename)
            roles = ctx.guild.roles

            if role not in roles:
                await ctx.message.add_reaction('❌')
                await ctx.send(f'{rolename} is not a role on this server, bro.')
                return

            if role.permissions.administrator and user.guild_permissions.administrator is not True or member and user.id != member.id:
                await ctx.message.add_reaction('❌')
                await ctx.send('Nice try, bro.')
                return

            if operation == 'add':
                await user.add_roles(role)
            elif operation == 'remove':
                await user.remove_roles(role)

            await ctx.message.add_reaction('✅')
        except Exception as err:
            await ctx.message.add_reaction('❌')
            await ctx.send(err)

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command(
        description='For when you wanna settle the score some other way',
        aliases=['8ball']
    )
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    @commands.command()
    async def repeat(self, ctx, times: int, content='repeating...'):
        """Repeats a message multiple times."""
        for i in range(times):
            await ctx.send(content)

    @commands.command()
    async def joined(self, ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

    @commands.group(pass_context=True)
    async def cool(self, ctx, person: str):
        """Says if a user is cool.
        In reality this just checks if a subcommand is being invoked.
        """
        if ctx.invoked_subcommand is None:
            await ctx.send(f'{person} is super {"not cool" if random.randint(0,2) != 1 else "cool"}')

    # @cool.command(name='bot')
    # async def _bot(self, ctx):
    #     """Is the bot cool?"""
    #     await ctx.send('Yes, the bot is cool.')

    # @cool.command(name='tatum')
    # async def _tatum(self, ctx):
    #     """Is tatum cool?"""
    #     await ctx.send('Yes, tatum is cool.')


Larvitar().run()