import mouse
import discord

pos = "Neutral"

client = discord.Client()

pos = ['']
mode = [False]
cameras = {'1a': [971, 347], '1b': [965, 409], '1c': [933, 484], '5': [866, 425], '3': [894, 575], '2a': [
    990, 598], '2b': [980, 636], '4a': [1098, 598], '4b': [1077, 644], '7': [1197, 421], '6': [1185, 560]}

allow = False


mouse.move(776, 407, absolute=True, duration=0)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('left'):
        if(mode[0] == False):
            pos[0] = 'left'
        await message.channel.send('Looking left')
        mouse.drag(637, 432, 150, 432, absolute=True, duration=0)

    if message.content.startswith('right'):
        if(mode[0] == False):
            pos[0] = 'right'
        await message.channel.send('Looking right')
        mouse.drag(637, 432, 1385, 432, absolute=True, duration=0)

    if message.content.startswith('pos'):
        await message.channel.send(mouse.get_position())

    if message.content.startswith('flip'):
        await message.channel.send('Flipping camera')
        mouse.drag(637, 432, 637, 669, absolute=True, duration=0.1)
        mouse.drag(637, 432, 637, 432, absolute=True, duration=1)
        mouse.drag(637, 432, 637, 669, absolute=True, duration=0.1)

    if message.content.startswith('light'):
        await message.channel.send('Using lights')
        if(pos[0] == "right"):
            mouse.move(1216, 467, absolute=True, duration=0)
            mouse.click('left')
            mouse.move(1216, 467, absolute=True, duration=0.5)
            mouse.click('left')
        elif(pos[0] == "left"):
            mouse.move(45, 445, absolute=True, duration=0)
            mouse.click('left')
            mouse.move(45, 445, absolute=True, duration=0.5)
            mouse.click('left')

    if message.content.startswith('door'):
        await message.channel.send('Using door')
        if (pos[0] == "right"):
            mouse.move(1219, 356, absolute=True, duration=0)
            mouse.click('left')
        elif(pos[0] == "left"):
            mouse.move(55, 321, absolute=True, duration=0)
            mouse.click('left')

    if message.content.lower().startswith('camera'):
        await message.channel.send('Using camera')
        mouse.drag(637, 432, 637, 669, absolute=True, duration=0.1)
        if(mode[0] == False):
            mode[0] = True
        else:
            mode[0] = False

    if message.content in cameras:
        await message.channel.send('Opening camera ' + message.content)
        mouse.move(cameras[message.content][0],
                   cameras[message.content][1], absolute=True, duration=0)
        mouse.click('left')
        mouse.move(558, 669, absolute=True, duration=0)

    if message.content.startswith('start'):
        await message.channel.send('Welcome to Chat plays FNAF. Good luck!')
        pos[0] = ''
        allow = True
        mouse.move(637, 432, absolute=True, duration=0)

    if message.content.startswith('stop'):
        await message.channel.send('Bye Chat!')
        allow = False
        mouse.move(767, 431, absolute=True, duration=0)

    if message.content.startswith('help'):
        await message.channel.send(pos[0])

client.run('')
