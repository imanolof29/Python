import discord
import random
import re

from urllib import parse, request
from discord.ext import commands
from Database import *


bot = commands.Bot(command_prefix = '!')
d = Database()
frases = []

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Info", color=discord.Color.blue())
    embed.add_field(name = "Comandos", value = "-!insertar_frase\n-!listar_frases\n-!frase_random\n-!yt")
    await ctx.send(embed=embed)

@bot.command()
async def insertar_frase(ctx, args):
    d.insertar(args)
    frases = None
    await ctx.send('Insertado')


@bot.command()
async def listar_frases(ctx):
    frases = d.leer_frases()
    await ctx.send(frases)

@bot.command()
async def frase_random(ctx):
    frases = d.leer_frases()
    num = random.randint(0, len(frases))
    await ctx.send(frases[num])
    print(len(frases)-1)

@bot.command()
async def yt(ctx, *, titulo):
    consulta = parse.urlencode({'search_query': titulo})
    contenido = request.urlopen('http://www.youtube.com/results?' + consulta)
    resultado = re.findall('href=\"\\/watch\\?v=(.{11})', contenido.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + resultado[0])

#Aqui hay que poner el token del bot
bot.run('')

