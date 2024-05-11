token = ("MTIzODYzNzY3ODY0NDMwMTgzNA.GoRV5u.UdN1RROzl-ogNR-kxjt5_iuQ_8k_VEnwAf2CGg")
         
import discord

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send(f"Hi, selamat datang!.{client.user} disini, ada yang bisa saya bantu?")
    elif message.content.startswith('$bye'):
        await message.channel.send("baik, selamat tinggal!")
    else:
        await message.channel.send(message.content)

client.run("MTIzODYzNzY3ODY0NDMwMTgzNA.GoRV5u.UdN1RROzl-ogNR-kxjt5_iuQ_8k_VEnwAf2CGg")
