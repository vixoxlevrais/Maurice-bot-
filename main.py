import discord
from discord.utils import get
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Maurice bot !!")
default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

# détecter quand le bot est pret ("allumé")

@bot.event
async def on_ready():
    print("Ready !")

@bot.command()
async def cc(ctx):
    await ctx.send("TG !!")

@bot.command()
async def list(ctx):
    await ctx.send("commande 1 : !cc"
                 "  commande 2 : ( !packmc ) lien vert le site de pack de vixox "
                 "  commande 3 : ( !github ) lien vert le git hub du bot "
                 "  commande 4 : ( !chinese ) transforme le mots que vous voulez en stile chinois "
                 "  commande 5 : ( !activité ) savoir se que vou voulez faire "
                 "  commande 6 : ( !servinfo ) info sur le serve "
                 "  commande 7 : ( !Maurice ) marche avec et sans majuscule "
                      )

@bot.command()
async def packmc(ctx):
    await ctx.send("le sit de pack et :https://ton-pack-mc.000webhostapp.com de vixox !")

@bot.command()
async def github(ctx):
 await ctx.send("le git hub du pack et https://github.com/vixoxlevrais?tab=repositories !")

@bot.command()
async def Maurice(ctx):
    await ctx.send("Bonjour je m'appel Maurice jai aites crée par 👹 vixox 👹  et 🦈 frouzer 🦈 je suis la pour vous aide dans votre serveur discord modifier moi comme vous voulez les bggg 😎 !")

@bot.command()
async def maurice(ctx):
        await ctx.send(
            "Bonjour je m'appel Maurice jai aites crée par 👹 vixox 👹  et 🦈 frouzer 🦈 je suis la pour vous aide dans votre serveur discord modifier moi comme vous voulez les bggg 😎 !")

@bot.command()
async def chinese(ctx, *text):
    chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
        chineseText.append(" ")
    await ctx.send("".join(chineseText))

@bot.command()
async def activité (ctx):
    await ctx.send("Envoyez le l'activité  que vous voulez faire  ")

    def checkMessage(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    try:
        recette = await bot.wait_for("message", timeout = 20, check = checkMessage)
    except:
        await ctx.send("Veuillez réitérer la commande.")
        return
    message = await ctx.send(f"La préparation de {recette.content} va commencer. Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
    await message.add_reaction("✅")
    await message.add_reaction("❌")


    def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

    try:
        reaction, user = await bot.wait_for("reaction_add", timeout = 20, check = checkEmoji)
        if reaction.emoji == "✅":
            await ctx.send("l'activité a démarré.")
        else:
            await ctx.send("L'activité a bien été annulé.")
    except:
        await ctx.send(":'activiter a bien été annulé.")

@bot.command()
async def servinfo(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur {serverName} contient {numberOfPerson} personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
    await ctx.send(message)

@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name  # recupere l'emoji
    canal = payload.channel_id  # recupere le numero du canal
    message = payload.message_id  # recupere le numero du messae

    bob_role = get(bot.get_guild(payload.guild_id).roles, name="bob")
    membre = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id)

    # verifier si l'emoji qu'on a ajoutée est "bob"
    if canal == 897183332872380436 and message == 897185381424975882 and emoji == "bob":
        print("Grade ajouter  !")
        await membre.remove_roles(bob_role)
        await membre.send("cc pour avoir tout les comandes fais !list sur le serve !")

@bot.event
async def on_raw_reaction_remove(payload):

    emoji = payload.emoji.name  # recupere l'emoji
    canal = payload.channel_id  # recupere le numero du canal
    message = payload.message_id # recupere le numero du messae

    bob_role = get(bot.get_guild(payload.guild_id).roles, name="bob")
    membre = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id)

    # verifier si l'emoji qu'on a ajoutée est "bob"
    if canal == 897183332872380436 and message == 897185381424975882 and emoji == "bob":
        print("Grade supprimé !")
        await membre.remove_roles(bob_role)
        await membre.send("tu a déjà eu les info tu les re veux re mais bob !")

bot.run("ODk3MDgwMDEzODQ3OTM3MDM1.YWQc3g.zlB_xkIQn7m3MkZi4y39vXceI8w")
