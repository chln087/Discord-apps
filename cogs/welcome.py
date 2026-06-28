import sqlite3
import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

#############SQL資料庫id載入##############
        conn = sqlite3.connect("data/settings.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT welcome_channel
            FROM guild_settings
            WHERE guild_id = ?
        """, (member.guild.id,))

        result = cursor.fetchone()

        conn.close()

        if result:
            welcome_channel_id = result[0]

        channel = member.guild.get_channel(welcome_channel_id)

        ##歡迎訊息發送
        await channel.send(f">>歡迎 {member.mention} 加入伺服器！:3")

        print(f"{member} 加入伺服器")

async def setup(bot): 
    await bot.add_cog(Welcome(bot))