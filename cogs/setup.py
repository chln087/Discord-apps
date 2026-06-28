import sqlite3
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
        await interaction.response.defer()
###############獲取id#############
        conn = sqlite3.connect("data/settings.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO guild_settings
            (guild_id, welcome_channel, verify_role)
            VALUES (?, ?, ?)
            """, (
                interaction.guild_id,
                welcome_channel.id,
                verify_role.id
            ))

        conn.commit()
        conn.close()

###############回應###############
        await interaction.response.send_message(f"設定成功！", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Setup(bot))
