# https://github.com/AlexFlipnote/discord_bot.py/blob/master/utils/permissions.py


import discord

from utils import default
from discord.ext import commands

from os import environ

owners = environ.get("DEVELOPERS")


def is_owner(ctx):
    """ Checks if the author is one of the owners """
    return ctx.author.id in owners


async def check_permissions(ctx, perms, *, check=all):
    """ Checks if author has permissions to a permission """
    if ctx.author.id in owners:
        return True

    resolved = ctx.channel.permissions_for(ctx.author)
    return check(getattr(resolved, name, None) == value for name, value in perms.items())


def has_permissions(*, check=all, **perms):
    """ discord.Commands method to check if author has permissions """
    async def pred(ctx):
        return await check_permissions(ctx, perms, check=check)
    return commands.check(pred)


def can_handle(ctx, permission: str):
    """ Checks if bot has permissions or is in DMs right now """
    return isinstance(ctx.channel, discord.DMChannel) or getattr(ctx.channel.permissions_for(ctx.guild.me), permission)