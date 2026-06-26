import json
import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        ##json id載入
        with open("data/settings.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        guild_id = str(member.guild.id)

        channel_id = data[guild_id]["welcome_channel"]

        channel = member.guild.get_channel(channel_id)

        ##歡迎訊息發送
        await channel.send(f">>歡迎 {member.mention} 加入伺服器！:3")

        print(f"{member} 加入伺服器")

async def setup(bot): 
    await bot.add_cog(Welcome(bot))