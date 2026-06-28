import sqlite3
from discord.ext import commands

class Autorole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
##################SQL資料庫id載入####################
        conn = sqlite3.connect("data/settings.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT verify_role
            FROM guild_settings
            WHERE guild_id = ?
        """, (member.guild.id,))

        result = cursor.fetchone()

        conn.close()

        if result:
            verify_role_id = result[0]

        role = member.guild.get_role(verify_role_id)

        ##身分組給予
        await member.add_roles(role)

        print(f"已給予 {member} {role} 身分組")

async def setup(bot):
    await bot.add_cog(Autorole(bot))