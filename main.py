##資料庫載入
import os
import asyncio
import discord
from discord.ext import commands

from config import TOKEN


##權限要求
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix = "%", intents=intents)

##載入程式檔案
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

##卸載程式檔案
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension} done.")

##重新載入程式檔案
@bot.command(name="reload")
async def reload_extension(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded {extension} done.")

##自動載入cog檔案
async def load_extensions():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{file[:-3]}")
                print(f"成功載入 {file}")
            except Exception as e:
                print(f"{file}載入失敗")
                print(e)


async def main():
    async with bot:
        await bot.start(TOKEN)

##############初始化執行################
@bot.event
async def setup_hook():
    await load_extensions()
    slash = await bot.tree.sync()
    print("已完成初始化")

##啟動時資訊
@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.CustomActivity(
            name="哦哦哦愛 有你的將來"
        )
    )
    print(f"目前登入身分 --> {bot.user}")
    print(f"已載入 {len(slash)} 個斜線指令")

@bot.tree.command(name="test")
async def test(interaction: discord.Interaction):
    print("TEST HIT")
    await interaction.response.send_message("OK")


if __name__ == "__main__":
    asyncio.run(main())
