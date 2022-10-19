import discord
from discord.ext import commands
import random
import json
import os

# Parametros : Sesion + Token
if os.path.exists(os.getcwd() + 'config.json'):
	
	with open('config.json') as f:
		configData = json.load(f)

else:
	configTemplate = {'Token':'', 'Prefix': '-'}

	with open(os.getcwd() + 'config.json', 'w+') as f:
		json.dump(configTemplate, f)

toke = configData['Token']
prefix = configData['Prefix'] 


# Commandos : Prefijo !
bot = commands.Bot(command_prefix='-')

# Iniciando Bot
@bot.event 
async def on_ready():
	print(f'Hello, I am ready Human!')

# Command : Kitty
@bot.command()
async def Kitty(ctx):
	await ctx.send('Miaauu')

# # Command : holaCat : Dime una frase
@bot.command(aliases=['holaCat'])
async def _holaCat(ctx):
	responses = ['Cuando pierdas, no pierdas la lección - Dalai Lama ',
				 'No busques los errores, busca un remedio - Henry Ford',
				 'La vida es una aventura, atrévete - Teresa de Calcuta',
				 'Cuanto más duramente trabajo, más suerte tengo - Gary Player',
				 'Tu actitud, no tu aptitud, determinará tu altitud - Zig Ziglar',
				 'Tienes que hacer las cosas que crees que no puedes hacer - Eleanor Roosevelt',
				 'Si te caíste ayer, levántate hoy - H. G. Wells',
				 'Siempre parece imposible... hasta que se hace - Nelson Mandela',
				 'Si no pierdes, no puedes disfrutar de las victorias - Rafael Nadal',
				 'No dejes que el miedo se interponga en tu camino - Babe Ruth',
				 'Haz de cada día tu obra maestra John Wooden ',
				 'No cuentes los días, haz que los días cuenten - Muhammad Ali',
				 'El mejor momento del día es ahora - Pierre Bonnard',
				 'Si la oportunidad no llama, construye una puerta - Milton Berle',
				 'Deja que cada hombre ejerza el arte que domina - Aristófanes ',
				 'El valor de una idea radica en su uso - Thomas Edison']

	await ctx.send(f'\n{random.choice(responses)}')

# cliente : Token 
bot.run(' ')