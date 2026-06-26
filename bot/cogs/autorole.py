import json
from discord.ext import commands

class Autorole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        ##json id載入
        with open("data/settings.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        guild_id = str(member.guild.id)

        role_id = data[guild_id]["verify_role"]

        role = member.guild.get_role(role_id)
        

        ##身分組給予
        await member.add_roles(role)

        print(f"已給予 {member} {role} 身分組")

async def setup(bot):
    await bot.add_cog(Autorole(bot))