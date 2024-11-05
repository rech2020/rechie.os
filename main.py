import discord
from discord.ext import commands
import random
import asyncio
import os

# lalalalalala
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='rechie!', intents=intents)

# user database simulation
user_data = {}

# cooldown
work_cooldowns = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='work')
async def work(ctx):
    user_id = ctx.author.id
    # check 4 cooldown
    if user_id in work_cooldowns:
        await ctx.send("you can only work once a day idiot")
        return

    # update balance
    user_data[user_id] = user_data.get(user_id, 0) + 100
    work_cooldowns[user_id] = True
    
    # 24h cooldown
    await asyncio.sleep(86400)  # 24 hours in seconds
    del work_cooldowns[user_id]
    
    await ctx.send(f"{ctx.author.mention} received 100 proglet coins for a productive day in the mines!")

@bot.command(name='say')
async def say(ctx, *, text: str):
    await ctx.send(text)

@bot.command(name='celeste')
async def celeste(ctx):
    await ctx.send(file=discord.File('https://youtu.be/uZQAWvDwRAM'))

@bot.command(name='gamble')
async def gamble(ctx, amount: int):
    user_id = ctx.author.id
    balance = user_data.get(user_id, 0)

    if amount > balance:
        user_data[user_id] = 0
        await ctx.send("you dont have that amount of coins 3:")
        return

    # actual gambling shiz
    win_amount = random.randint(1, 1000)
    user_data[user_id] -= amount
    user_data[user_id] += win_amount
    await ctx.send(f"you gambled {amount} proglet coins and won {win_amount} proglet coins! :3")

@bot.command(name='clicker')
async def click(ctx):
    counter = 0
    message = await ctx.send("click the button")

    button = discord.ui.Button(label="click me!!!", style=discord.ButtonStyle.primary)

    async def button_callback(interaction):
        nonlocal counter
        counter += 1
        await interaction.response.edit_message(content=f"you've clicked {counter} times :3")

    button.callback = button_callback
    view = discord.ui.View()
    view.add_item(button)
    await message.edit(view=view)

@bot.command(name='flag')
async def flag(ctx):
    await ctx.send(file=discord.File('https://media.discordapp.net/attachments/1042918809826230315/1303097617982689340/Untitled1626_20241103161250.png'))

@bot.command(name='yuri')
async def lesbians(ctx):
    # god this was awful why did he put everything into one line
    images = [
        'https://media.discordapp.net/attachments/1042918809826230315/1303105775832403998/39efbc272908f020d9e1b1286f3c662735657b86d65e3d32e6eb4a6259916916.upload.jpg', 
        'https://media.discordapp.net/attachments/1042918809826230315/1303105768819658763/f3a4b9f5e947b187598c066f0e1adbf33c9eb7f0b43eb21644337125d8abe155.upload.jpg',
        'https://media.discordapp.net/attachments/1042918809826230315/1303105758824497305/webpublic-d6fcba9f-a402-4d1b-837c-08e464ea6b47.png',
        'https://media.discordapp.net/attachments/1042918809826230315/1303105750369046579/f99f2312c2e7d42e38766d1d03d8d5dbaa1ce52851ab6b7c47ff1cd7dfe42912.upload.jpg',
        'https://media.discordapp.net/attachments/1042918809826230315/1303105738297573436/636397e1e94322372be0e35e09d68eacbddb32d4ea5b4591c962029ed6ebb52a.upload.jpg',
        'https://media.discordapp.net/attachments/1042918809826230315/1303105731360325694/f123b25e200b041526b4d12a7014a0a04f5df28d5dc6b854110a90427c55cf8a.upload.jpg',
        'https://media.discordapp.net/attachments/1042918809826230315/1303105719733850153/webpublic-3aeb127b-45d9-4feb-9c2a-17cc917337e7.png',
        'https://media.discordapp.net/attachments/1042918809826230315/1303105697390788698/webpublic-4a3db310-c046-408a-88da-7909c75b090d.png', 
        'https://media.discordapp.net/attachments/1042918809826230315/1303105690130317363/b8e6df056bc66ea5.jpg', 
        'https://media.discordapp.net/attachments/1042918809826230315/1303105681146118226/103044521_p1.png'
        ]
    chosen_image = random.choice(images)
    await ctx.send(file=discord.File(chosen_image))

@bot.command(name='coins')
async def coins(ctx):
    user_id = ctx.author.id
    balance = user_data.get(user_id, 0)
    await ctx.send(f"{ctx.author.mention}, you have {balance} proglet coins")

# run rechie.OS
bot.run(open("token.txt").read())

"""
this is the message from rechie
im fixing the code that meo and chatgpt made
anyways uhh rechions are now proglet coins
"""