import discord
from GenEmoji import emoji
from password import gen_pass
from Randoms import coin
from Randoms import dice

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('¬hola'):
        await message.channel.send("Hola!")
    elif message.content.startswith('¬emoji'):
        emoji()
    elif message.content.startswith('¬adiós'):
        await message.channel.send("Adiós!")
    elif message.content.startswith('¬lanza una moneda'):
        coin()
    elif message.content.startswith('¬tira los dados'):
        dice()
    elif message.content.startswith('¬password'):
        gen_pass()
    elif message.content.startswith('¬10') :
        await message.channel.send('Modelo de Quarks: https://es.wikipedia.org/w/index.php?title=Special:Search&search=Modelo+de+cuarks&wprov=acrw1_1')
    elif message.content.startswith('¬9') :
        await message.channel.send('Principio de exclusión de Pauli: https://es.wikipedia.org/wiki/Principio_de_exclusi%C3%B3n_de_Pauli')
    elif message.content.startswith('¬8') :
        await message.channel.send('Preón: https://es.wikipedia.org/wiki/Pre%C3%B3n')
    elif message.content.startswith('¬7') :
        await message.channel.send('Gluón: https://es.wikipedia.org/wiki/Gluon')
    elif message.content.startswith('¬6') :
        await message.channel.send('Quarks: https://es.wikipedia.org/wiki/Cuark')
    elif message.content.startswith('¬5') :
        await message.channel.send('Teorema espín-estadística: https://es.wikipedia.org/wiki/Esp%C3%ADn#Teorema_esp%C3%ADn-estad%C3%ADstica')
    elif message.content.startswith('¬4') :
        await message.channel.send('Neutrinos: https://es.wikipedia.org/wiki/Neutrino')
    elif message.content.startswith('¬3') :
        await message.channel.send('Condensado de Bose-Einstein: https://es.wikipedia.org/wiki/Condensado_de_Bose-Einstein')
    elif message.content.startswith('¬2') :
        await message.channel.send('Bosones: https://es.wikipedia.org/wiki/Bos%C3%B3n')
    elif message.content.startswith('¬1') :
        await message.channel.send('Estadística Fermi-Dirac: https://es.wikipedia.org/wiki/Estad%C3%ADstica_de_Fermi-Dirac')
    elif message.content.startswith('¬0') :
        await message.channel.send('Fermiones: https://es.wikipedia.org/wiki/Fermi%C3%B3n#:~:text=Un%20fermi%C3%B3n%20es%20uno%20de,principio%20de%20exclusi%C3%B3n%20de%20Pauli.')
    elif message.content.startswith('¬poema'):
        await message.channel.send("cae-lanion luhial")
        await message.channel.send("di mari felanua")
        await message.channel.send("kreata tu ciar")
        await message.channel.send("tu alaran di")
        await message.channel.send("dirella amauen")
        await message.channel.send("loesi an delian")
        await message.channel.send("tu nia vor ruhlan")
        await message.channel.send("Felurian thae")

        
client.run("secreto")