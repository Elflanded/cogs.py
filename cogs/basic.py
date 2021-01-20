from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
      name="hello",
      aliases="Hello",
      description="Sends 'hello!' back.",
      usage="@elf#1000"
    )
    async def hello_command(self, ctx, user : discord.Member)
    await ctx.send(f"{ctx.author} says Hello to {user.mention}!")

    # !hello @elf#1000
    # @elf#100 says Hello to @elf#1000!

    # https://discordpy.readthedocs.io/en/latest/api.html#discord.Member
    



      

def setup(bot):
    bot.add_cog(Basic(bot))