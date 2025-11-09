# 🦊 BOT RENARD — GUIDE D’INSTALLATION ET DE LANCEMENT LOCAL

## 🐍 1️⃣ INSTALLER PYTHON

1. Télécharge Python ici :  
   👉 https://www.python.org/downloads/

2. Pendant l’installation, **coche la case :**
   Add Python to PATH

3. Une fois installé, vérifie que Python fonctionne (dans la console cmd.exe) tape:
   py --version
   ou :
   python --version
---

## 🎵 3️⃣ INSTALLER FFMPEG

1. Télécharge FFmpeg ici :  
   👉 https://www.gyan.dev/ffmpeg/builds/

2. Télécharge le fichier :  
   ffmpeg-release-essentials.zip
   
---

## ⚙️ 4️⃣ AJOUTER FFMPEG DANS LES VARIABLES D’ENVIRONNEMENT

1. Appuie sur Windows + R
2. Tape :
   sysdm.cpl
3. Clique sur “Avancé”
4. Clique sur “Variables d’environnement…”
5. Dans la section “Variables système”, sélectionne la ligne “Path”
6. Clique sur “Modifier” → “Nouveau”
7. Colle le chemin :
   C:\ffmpeg\bin
   (ou le chemin exact vers ton dossier `bin` selon l’endroit où tu as installé FFmpeg)
8. Clique sur OK partout pour enregistrer

## 📦 2️⃣ INSTALLER LES DÉPENDANCES NÉCESSAIRES

Dans la console tape

py -m pip install discord.py[voice] yt-dlp deep-translator python-dotenv ffmpeg-python

---

## 🔑 6️⃣ CONFIGURER LE TOKEN DU BOT

Crée un fichier nommé `.env` dans le même dossier que `bot.py`,  
et ajoute dedans :

TOKEN=ton_token_discord_ici

👉 Le token se récupère sur le portail :  
https://discord.com/developers/applications


## 🚀 7️⃣ LANCER LE BOT

Si tout est correct, tu verras :
✅ Connecté en tant que Petit Renard Gentil#xxxx

## 💬 COMMANDES DISPONIBLES

| Commande | Description |
|-----------|-------------|
| !renard <message> | Envoie ton message bilingue fr / en |
| !renardyt <lien_youtube> | Joue le son d’une vidéo YouTube 🎵 |
| !renardyt stop | Arrête le son et quitte le vocal 🔇 |
