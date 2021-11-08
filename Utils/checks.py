from discord.ext import commands

def can_mute(**perms):
    def predicate(ctx):
        if ctx.author.guild_permissions.mute_members:
            return True
        else:
            return False
    return commands.check(predicate)

def can_kick(**perms):
    def predicate(ctx):
        if ctx.author.guild_permissions.kick_members:
            return True
        else:
            return False
    return commands.check(predicate)

def can_ban(**perms):
    def predicate(ctx):
        if ctx.author.guild_permissions.ban_members:
            return True
        else:
            return False
    return commands.check(predicate)

def can_managemsg(**perms):
    def predicate(ctx):
        if ctx.author.guild_permissions.manage_messages:
            return True
        else:
            return False
    return commands.check(predicate)

def can_manageguild(**perms):
    def predicate(ctx):
        if ctx.author.guild_permissions.manage_guild:
            return True
        else:
            return False
    return commands.check(predicate)

def is_admin(**perms):
    def predicate(ctx):
        if ctx.author.guild_permissions.administrator:
            return True
        else:
            return False
    return commands.check(predicate)
