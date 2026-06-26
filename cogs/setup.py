import json
import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
############斜線指令設定################
    @app_commands.command(name = "setup", description = "設定歡迎頻道及身分組",)
    @app_commands.checks.has_permissions(administrator=True)
    async def setup(
        self,
        interaction: discord.Interaction,
        welcome_channel: discord.TextChannel,
        verify_role: discord.Role,
    ):

###############獲取id#############
        guild_id = str(interaction.guild.id)
        channel_id = welcome_channel.id
        role_id = verify_role.id

        with open("data/settings.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        data[guild_id] = {
            "welcome_channel": channel_id,
            "verify_role": role_id
        }

        with open("data/settings.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    
        await interaction.response.send_message(f"設定成功！", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Setup(bot))