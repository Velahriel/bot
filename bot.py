import discord
from discord.ext import commands
from deep_translator import GoogleTranslator
from dotenv import load_dotenv
import yt_dlp
import asyncio
import logging
import os

# -----------------------------------------------------------
# 🔇 Désactiver les warnings yt-dlp
# -----------------------------------------------------------
logging.getLogger("yt_dlp").setLevel(logging.CRITICAL)

# Charger le fichier .env pour récupérer le TOKEN
load_dotenv()

# Intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# -----------------------
# 🦊 Paramètres du bot
# -----------------------
ROLE_AUTORISE = "Maître du jeu (MJ)"  # Nom du rôle autorisé à utiliser !renard

# -----------------------
# 📡 Événement de connexion
# -----------------------
@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

# -----------------------
# 🦊 Commande !renard
# -----------------------
@bot.command()
async def renard(ctx, *, message: str):
    """Fait parler le bot et traduit le message en anglais avec une belle mise en page."""
    # Vérifie le rôle
    role_ok = discord.utils.get(ctx.author.roles, name=ROLE_AUTORISE)
    if not role_ok:
        return  # silencieux si non autorisé

    # Supprime le message d’origine
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass

    # Traduction FR -> EN
    try:
        traduction_en = GoogleTranslator(source='fr', target='en').translate(message)
    except Exception:
        return

    # Mise en forme esthétique 
    texte = (
        "🇫🇷 **[MESSAGE EN FRANÇAIS]**\n\n"
        f"{message}\n\n"
        "───────────────────────────────\n\n"
        "🇬🇧 **[ENGLISH TRANSLATION]**\n\n"
        f"{traduction_en}"
    )

    await ctx.send(texte)

# -----------------------
# 🎵 Commande !renardyt
# -----------------------
@bot.command()
async def renardyt(ctx, *, arg: str):
    """Le bot joue un son YouTube ou stoppe la lecture (silencieux)."""
    # Supprime la commande utilisateur
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass

    # Si "stop" → déconnecte sans parler
    if arg.lower() == "stop":
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
        return

    # Vérifie que l’utilisateur est dans un salon vocal
    if ctx.author.voice is None:
        return  # silencieux si pas dans un vocal

    channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        vc = ctx.voice_client

    # yt-dlp silencieux
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
        'extract_flat': False
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(arg, download=False)
            audio_url = info['url']
    except Exception:
        if vc.is_connected():
            await vc.disconnect()
        return

    # Lecture audio via FFmpeg (silencieuse)
    ffmpeg_opts = {'options': '-vn -loglevel panic'}
    source = await discord.FFmpegOpusAudio.from_probe(audio_url, **ffmpeg_opts)
    vc.play(source)

    # Attend la fin du son
    while vc.is_playing():
        await asyncio.sleep(1)

    # Quitte après la lecture
    if vc.is_connected():
        await vc.disconnect()

# -----------------------
# 🚀 Lancement du bot
# -----------------------
bot.run(os.getenv("TOKEN"))