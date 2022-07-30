import discord
from discord import message
import random
import time
import linecache
import sys
sys.path.append("Package/")
from com_eat import eat

from discord import user
from discord.client import Client
from discord.utils import get
from discord import Role
from discord.ext import commands
from discord import Client, Intents, Embed
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice,create_option

import json
import datetime
from datetime import datetime, timezone, timedelta
import time
import schedule
import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.worldometers.info/coronavirus/country/taiwan/")
soup=BeautifulSoup(response.text,"html.parser")
result=soup.find_all("div",attrs={"class":"maincounter-number"})

intents = discord.Intents().all()
client = commands.Bot(command_prefix="-", intents=intents)
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print("機器人已成功啟動!\n目前機器人：",client.user)
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(activity=discord.Streaming(name="Minecraft", url="https://www.youtube.com/watch?v=o-YBDTqX_ZU"))
time_start = time.time()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.author.bot:
        return

    if message.content == "-info":
        time_end = time.time()
        activity = "機器人已運行 "+str(int(time_end - time_start))+" 秒"
        embed=discord.Embed(title="關於機器人")
        embed.add_field(name="Version", value="3.3 Open Source", inline=True)
        embed.add_field(name="Info", value="(´･ω･`)? Open Source Version", inline=False)
        embed.add_field(name="已運行時間", value=activity, inline=False)
        embed.add_field(name="製作人員", value="竹子", inline=False)
        embed.add_field(name="協助人員", value="一顆悠閒的麻鈴糬", inline=False)
        await message.channel.send(embed=embed)

    if message.content == "-help":
        embed=discord.Embed(title="關於機器人指令", description="使用-help", color=0x1eff00)
        embed.add_field(name="-gay", value="測試你Gay的機率", inline=False)
        embed.add_field(name="-ask", value="測試事情的機率", inline=False)
        embed.add_field(name="-eat", value="讓機器人幫你選食物", inline=False)
        embed.add_field(name="-say", value="讓機器人說指定的話", inline=False)
        embed.add_field(name="-info", value="機器人詳細資訊", inline=False)
        embed.add_field(name="-snipe", value="狙擊別人刪除的訊息", inline=False)
        embed.set_footer(text="記得到指令區使用歐")
        await message.channel.send(embed=embed)

    if message.content.startswith("-gay"):
        gaytmp = message.content.split(" ",1)
        ran = random.randrange(101)
        if len(gaytmp) == 1:
            url=message.author.avatar_url
            embed=discord.Embed(title=" ", description=f"{ran}% Gay")
            embed.set_author(name=message.author,icon_url=url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title=str(gaytmp[1]), description=f"{ran}% Gay")
            await message.channel.send(embed=embed)

    if message.content.startswith("-ask"):
        asktmp = message.content.split(" ",1)
        ran = random.randrange(101)
        if len(asktmp) == 1:
            member = message.author
            embed=discord.Embed(title="Error", description="指令錯誤")
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title=str(asktmp[1]), description=f"{ran}%可能")
            await message.channel.send(embed=embed)

    if message.content == "-eat":
        await message.channel.send(eat())
  
    if message.content.startswith("-say"):
        if message.mention_everyone:
            await message.delete()
            sayerror="===警告===\n"+str(message.author)+"使用-say指令Tag everyone"
            embed=discord.Embed(description=sayerror)
            embed.set_author(name=message.author,icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
        else:
            saytmp = message.content.split(" ",1)
            await message.delete()
            await message.channel.send(str(saytmp[1]))

    if message.content.startswith("-snipe"):
        delmessage = linecache.getline("delmsg.txt", 1)
        linecache.clearcache()
        if len(delmessage) == 1:
            delmessage = "沒有文字可以狙擊"
            embed=discord.Embed(description=delmessage)
            await message.channel.send(embed=embed)
        else:
            delmessage = linecache.getline("delmsg.txt", 1)
            deltime = linecache.getline("delmsg.txt", 5)
            deluser = linecache.getline("delmsg.txt", 2)
            deluserurl = linecache.getline("delmsg.txt", 3)
            delchannel = "訊息來自 "+linecache.getline("delmsg.txt", 4)+"訊息時間:"+deltime
            embed=discord.Embed(description=delmessage)
            embed.set_author(name=deluser,icon_url=deluserurl)
            embed.set_footer(text=delchannel)
            await message.channel.send(embed=embed)

    # 身分組名稱記得更改再啟用
    # if message.mention_everyone:
    #     if message.channel.id == 863288797692035112:
    #         return
    #     else:
    #         member=message.author
    #         guild = 863269145981222942
    #         role = get(message.guild.roles, name="浸鹽 (?")
    #         await member.add_roles(role)
    #         await message.delete()
    #         sayerror="===警告===\n"+str(message.author)+" Tag everyone"
    #         embed=discord.Embed(description=sayerror)
    #         embed.set_author(name=message.author,icon_url=message.author.avatar_url)
    #         await message.channel.send(embed=embed)

    if message.content.startswith("-ping"):
        embed=discord.Embed(description=f"機器人延遲:{round(client.latency*100000)/100}ms")
        embed.set_author(name=client.user,icon_url=client.user.avatar_url)
        await message.channel.send(embed=embed)

@client.event
async def on_member_join(member):
    if member.guild.id == 863269145981222942:
        channel = client.get_channel(863269308130000896)
        embed=discord.Embed(description=f"嗨 {member.mention} 歡迎加入伺服器\n快來和大家一起聊天吧",color=0x4DFFFF)
        await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    if member.guild.id == 863269145981222942:
        channel = client.get_channel(863269308130000896)
        embed=discord.Embed(description=f"{member.mention} 離開了伺服器qwq",color=0x4DFFFF)
        await channel.send(embed=embed)

@client.event
async def on_message_delete(delmessage):
    if delmessage.guild.id == 863269145981222942:
        delmsg = delmessage.content
        delmsg = str(delmsg)
        deltimetmp = datetime.utcnow().astimezone(timezone(timedelta(hours=8)))
        deltime = str(deltimetmp).split(".",1)
        f=open("delmsg.txt","w")
        f=open("delmsg.txt","a")
        f.write(delmsg+"\n"+str(delmessage.author)+"\n"+str(delmessage.author.avatar_url)+"\n"+str(delmessage.channel)+"\n"+str(deltime[0]))
        f.close()

@slash.slash(
    name="gay",
    description="測試你Gay的機率",
    guild_ids=[863269145981222942]
)
async def _gay(ctx):
    ran = random.randrange(101)
    url=ctx.author.avatar_url
    embed=discord.Embed(title=" ", description=f"{ran}% Gay")
    embed.set_author(name=ctx.author,icon_url=url)
    await ctx.send(embed=embed)

@slash.slash(
    name="eat",
    description="讓機器人幫你選食物",
    guild_ids=[863269145981222942]
)
async def _eat(ctx):
    eat()
    await ctx.send(eat.eatran)

@slash.slash(
    name="help",
    description="關於機器人指令",
    guild_ids=[863269145981222942]
)
async def _help(ctx):
    embed=discord.Embed(title="關於機器人指令", description="使用-help", color=0x1eff00)
    embed.add_field(name="-gay", value="測試你Gay的機率", inline=False)
    embed.add_field(name="-ask", value="測試事情的機率", inline=False)
    embed.add_field(name="-eat", value="讓機器人幫你選食物", inline=False)
    embed.add_field(name="-say", value="讓機器人說指定的話", inline=False)
    embed.add_field(name="-info", value="機器人詳細資訊", inline=False)
    embed.add_field(name="-snipe", value="狙擊別人刪除的訊息", inline=False)
    embed.set_footer(text="記得到指令區使用歐")
    await ctx.send(embed=embed)

@slash.slash(
    name="snipe",
    description="狙擊別人刪除的訊息",
    guild_ids=[863269145981222942]
)
async def _snipe(ctx):
    delmessage = linecache.getline("delmsg.txt", 1)
    linecache.clearcache()
    if len(delmessage) == 1:
        delmessage = "沒有文字可以狙擊"
        embed=discord.Embed(description=delmessage)
        await ctx.send(embed=embed)
    else:
        delmessage = linecache.getline("delmsg.txt", 1)
        deltime = linecache.getline("delmsg.txt", 5)
        deluser = linecache.getline("delmsg.txt", 2)
        deluserurl = linecache.getline("delmsg.txt", 3)
        delchannel = "訊息來自 "+linecache.getline("delmsg.txt", 4)+"訊息時間:"+deltime
        embed=discord.Embed(description=delmessage)
        embed.set_author(name=deluser,icon_url=deluserurl)
        embed.set_footer(text=delchannel)
        await ctx.send(embed=embed)

@slash.slash(
    name="ping",
    description="查看機器人延遲",
    guild_ids=[863269145981222942]
)
async def _ping(ctx):
    embed=discord.Embed(description=f"機器人延遲:{round(client.latency*100000)/100}ms")
    embed.set_author(name=client.user,icon_url=client.user.avatar_url)
    await ctx.send(embed=embed)

keep_alive.keep_alive()
with open('token.json', "r", encoding = "utf8") as file:
    data = json.load(file)
client.run(data['token']) #Token在Discord Developer Bot頁面裡面
