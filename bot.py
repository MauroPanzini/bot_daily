
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
import datetime
import holidays
load_dotenv()

TOKEN = os.getenv('TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

emoji_green = '✅'
emoji_red = '❌'

asistentes = []

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.command()
async def daily(ctx):
    embed = discord.Embed(title='Daily Tecnología', description='⏰ 10:15\n\n🔗 [Link de la Meet](a) \n\n🤨 ¿Quién viene?', color=0x279D2E)
    message = await ctx.send(embed=embed)
    await message.add_reaction(emoji_green)
    await message.add_reaction(emoji_red)

@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    if channel.id == CHANNEL_ID and reaction.message.author == bot.user:
        if reaction.emoji == emoji_green:
            asistentes.append(user)
            print(f'{user.name} asistirá a la daily.')
        elif reaction.emoji == emoji_red:
            asistentes.remove(user)
            print(f'{user.name} no asistirá a la daily.')
        await asyncio.sleep(900)  # Esperar 15 minutos
        await reaction.message.clear_reactions()  # Eliminar todas las reacciones del mensaje
        asistentes.clear()

@bot.command()
async def participantes(ctx):
    asistentes_nombres = ', '.join([user.name for user in asistentes])
    await ctx.send(f'Asistentes actuales: {asistentes_nombres}')

def obtener_asistentes():
    lista_asistentes = ', '.join([user.name for user in asistentes])
    return lista_asistentes

async def daily_command():
    channel = bot.get_channel(CHANNEL_ID)
    embed = discord.Embed(title='Daily Tecnología', description='⏰ 10:15\n\n🔗 [Link de la Meet](a) \n\n🤨 ¿Quién viene?', color=0x279D2E)
    message = await channel.send(embed=embed)
    await message.add_reaction(emoji_green)
    await message.add_reaction(emoji_red)

def member_to_dict(member):
    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
    member_dict = {
        'id': member.id,
        'name': member.name,
        'discriminator': member.discriminator,
        'avatar_url': str(avatar_url)
    }
    return member_dict


def es_dia_laborable(fecha):
    # Obtener los días feriados en Argentina para el año actual
    feriados_ar = holidays.Argentina(years=datetime.date.today().year)

    # Verificar si la fecha es un día feriado o fin de semana
    if fecha.weekday() >= 5 or fecha in feriados_ar:
        return False
    return True

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    await bot.loop.create_task(schedule_daily())

async def schedule_daily():
    while True:
        now = datetime.datetime.now()
        if es_dia_laborable(now.date()):
            target_time = now.replace(hour=10, minute=0, second=0, microsecond=0)
            if now > target_time:
                target_time += datetime.timedelta(days=1)  # Ejecutar al día siguiente si ya pasó la hora objetivo hoy
            time_to_wait = (target_time - now).total_seconds()
            await asyncio.sleep(time_to_wait)
            await daily_command()
        else:
            # Esperar hasta el próximo día laborable
            next_weekday = now + datetime.timedelta(days=1)
            while not es_dia_laborable(next_weekday.date()):
                next_weekday += datetime.timedelta(days=1)
            time_to_wait = (next_weekday - now).total_seconds()
            await asyncio.sleep(time_to_wait)

@bot.command()
async def cuando_daily(ctx):
    now = datetime.datetime.now()
    if es_dia_laborable(now.date()):
        target_time = now.replace(hour=10, minute=0, second=0, microsecond=0)
        if now > target_time:
            target_time += datetime.timedelta(days=1)  # Ejecutar al día siguiente si ya pasó la hora objetivo hoy
    else:
        # Obtener el próximo día laborable
        next_weekday = now + datetime.timedelta(days=1)
        while not es_dia_laborable(next_weekday.date()):
            next_weekday += datetime.timedelta(days=1)
        target_time = next_weekday.replace(hour=10, minute=0, second=0, microsecond=0)

    # Enviar un mensaje con la fecha y hora de la siguiente reunión
    await ctx.send(f"La próxima reunión está programada para el día {target_time.strftime('%Y-%m-%d')} a las {target_time.strftime('%H:%M')} (hora de Argentina).")

def run_bot():
    bot.run(TOKEN)




