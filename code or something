import discord
from discord.ext import commands
import random
import asyncio
import os

# lalalalalala
intents = discord.Intents.default()
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
    
    await ctx.send(f"{ctx.author.mention} received 100 rechoins for a productive day in the mines!")

@bot.command(name='say')
async def say(ctx, *, text: str):
    await ctx.send(text)

@bot.command(name='celeste')
async def celeste(ctx):
    await ctx.send(file=discord.File('https://youtu.be/uZQAWvDwRAM?si=QZIs397u3QX6KL6G'))

@bot.command(name='gamble')
async def gamble(ctx, amount: int):
    user_id = ctx.author.id
    balance = user_data.get(user_id, 0)

    if amount > balance:
        user_data[user_id] = 0
        await ctx.send("nuh uh 3:")
        return

    # actual gambling shiz
    win_amount = random.randint(1, 1000)
    user_data[user_id] -= amount
    user_data[user_id] += win_amount
    await ctx.send(f"you gambled {amount} rechoins and won {win_amount} rechoins! :3")

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
    await ctx.send(file=discord.File('https://media.discordapp.net/attachments/1042918809826230315/1303097617982689340/Untitled1626_20241103161250.png?ex=672a83ba&is=6729323a&hm=3225ec733ea1c7600b4d268da80fbe3eeec40f42e3daf6524afd5ef6c06791af&=&format=webp&quality=lossless&width=678&height=407'))

@bot.command(name='yuri')
async def lesbians(ctx):
    images = ['https://media.discordapp.net/attachments/1042918809826230315/1303105775832403998/39efbc272908f020d9e1b1286f3c662735657b86d65e3d32e6eb4a6259916916.upload.jpg?ex=672a8b53&is=672939d3&hm=36dc63dbe7f5129eb8276cb0ee19d8c7d9c1af82381916b9982b25283233fd80&=&format=webp&width=475&height=627', 'https://media.discordapp.net/attachments/1042918809826230315/1303105768819658763/f3a4b9f5e947b187598c066f0e1adbf33c9eb7f0b43eb21644337125d8abe155.upload.jpg?ex=672a8b51&is=672939d1&hm=61ca4c800b38afb412f98ea9c3e67dbb5d73b48993680a4d9ef6e394d22a78aa&=&format=webp&width=382&height=627', 'https://media.discordapp.net/attachments/1042918809826230315/1303105758824497305/webpublic-d6fcba9f-a402-4d1b-837c-08e464ea6b47.png?ex=672a8b4f&is=672939cf&hm=4fac2fc9cd6a7f5cf65dd66561a7f35b6794bcd7a5872d069deede82f3bf166e&=&format=webp&quality=lossless&width=627&height=627', 'https://media.discordapp.net/attachments/1042918809826230315/1303105750369046579/f99f2312c2e7d42e38766d1d03d8d5dbaa1ce52851ab6b7c47ff1cd7dfe42912.upload.jpg?ex=672a8b4d&is=672939cd&hm=64317fe6e2f1c7bee1515cc981d06266abca6d3d85c250d8ec6a02e297eeee84&=&format=webp&width=360&height=626', 'https://media.discordapp.net/attachments/1042918809826230315/1303105738297573436/636397e1e94322372be0e35e09d68eacbddb32d4ea5b4591c962029ed6ebb52a.upload.jpg?ex=672a8b4a&is=672939ca&hm=f0eedbf0233e7537fedde3848ad0303c55cab288d0b37d923275761e169c8a09&=&format=webp&width=655&height=627',
              'https://media.discordapp.net/attachments/1042918809826230315/1303105731360325694/f123b25e200b041526b4d12a7014a0a04f5df28d5dc6b854110a90427c55cf8a.upload.jpg?ex=672a8b48&is=672939c8&hm=0400201173959e32f3caf16a463bd006dd7f3667d1ab36c9daec2c9584b6ad15&=&format=webp&width=1115&height=627', 'https://media.discordapp.net/attachments/1042918809826230315/1303105719733850153/webpublic-3aeb127b-45d9-4feb-9c2a-17cc917337e7.png?ex=672a8b46&is=672939c6&hm=e8cb94699f284c2b79ce2bafc58fe1555937ed4a936eb627baf418424d22df71&=&format=webp&quality=lossless&width=448&height=627', 'https://media.discordapp.net/attachments/1042918809826230315/1303105697390788698/webpublic-4a3db310-c046-408a-88da-7909c75b090d.png?ex=672a8b40&is=672939c0&hm=4ceb647353f6e736386a30922e63c759614536d67e703ce4dafeecfbc7f00081&=&format=webp&quality=lossless&width=886&height=627', 'https://media.discordapp.net/attachments/1042918809826230315/1303105690130317363/b8e6df056bc66ea5.jpg?ex=672a8b3f&is=672939bf&hm=3a40ec3d9ba00bb5224b0d3d948aa34007b502140cbffe3a174b2f92975c7dca&=&format=webp&width=847&height=627', 'https://media.discordapp.net/attachments/1042918809826230315/1303105681146118226/103044521_p1.png?ex=672a8b3c&is=672939bc&hm=8680e5ffbd9c4d1b0d5982c3e87c277af4fc80b08a5de86318dbabfe38164e64&=&format=webp&quality=lossless&width=959&height=627']
    chosen_image = random.choice(images)
    await ctx.send(file=discord.File(chosen_image))

@bot.command(name='coins')
async def coins(ctx):
    user_id = ctx.author.id
    balance = user_data.get(user_id, 0)
    await ctx.send(f"{ctx.author.mention}, you have {balance} rechoins")

# run rechie.OS
TOKEN = 'YOUR_BOT_TOKEN'
bot.run(TOKEN)

# everyone thank chatgpt since i just cleaned up the code a lil and added the links i doubt any of this actually works
