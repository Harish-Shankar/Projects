import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
from youtube_search import YoutubeSearch
import asyncio
import youtube_dl
from random import choice

youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaduio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}
ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


musicBot = commands.Bot(command_prefix='!')
status = ['Mode 1', 'Mode 2', 'Mode 3']
musicURL = []
songName = []


@musicBot.event
async def on_ready():
    change_status.start()
    print("The bot is online")


@musicBot.event
async def member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!  Ready to jam out? See `?help` command for details!')


@musicBot.command(name='intro', help='This command introduces the bot')
async def intro(ctx):
    await ctx.send('This a trial of a music bot for discord')


@musicBot.command(name='ping', help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'The ping is: {round(musicBot.latency * 1000)}ms')


@musicBot.command(name='credit', help='This returns the name of the person who made this bot')
async def credit(ctx):
    await ctx.send('This bot was made by SGFyaXNo')


@musicBot.command(name='join', help='This command makes the bot enter the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send('You are not connected to the voice channel')
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@musicBot.command(name='play', help='This command plays the specified song')
async def play(ctx):
    global musicURL, songName
    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(musicURL[0], loop=musicBot.loop)
        voice_channel.play(player, after=lambda e: print("Player error: %s" %e) if e else None)
        del(musicURL[0])
        del(songName[0])
    await ctx.send(f'**Now Playing:** {player.title}')
print('song is over')


@musicBot.command(name='pause', help='This command pauses the current song')
async def pause(ctx):
    ctx.message.guild.voice_client.pause()


@musicBot.command(name='resume', help='This command resumes the current song')
async def resume(ctx):
    ctx.message.guild.voice_client.resume()


@musicBot.command(name='stop', help='This command stops the current song')
async def stop(ctx):
    ctx.message.guild.voice_client.stop()


@musicBot.command(name='leave', help='This command makes the bot leave the channel')
async def leave(ctx):
    voice = ctx.message.guild.voice_client
    await voice.disconnect()


@musicBot.command(name='queue', help='This command adds the song to the queue')
async def queue(ctx, *, song):
    global musicURL, songName
    songName.append(song)
    musicURL.append('https://youtube.com'+(YoutubeSearch(song, max_results=1).to_dict()[0]).get('url_suffix'))
    await ctx.send(f'`{song}` added to the queue!')


@musicBot.command(name='remove', help='This command removes a song from the queue')
async def remove(ctx, number):
    global musicURL, songName
    try:
        del (musicURL[int(number-1)])
        del (songName[int(number-1)])
        await ctx.send("The que is now ", "\n".join([(str(i)+". " +item) for i, item in enumerate(songName)]))
    except IndexError:
        await ctx.send('The song could not be found in the queue')


@musicBot.command(name='view', help='This command shows the queued up songs')
async def view(ctx):
    global songName
    for i, item in enumerate(songName):
        if i == 0:
            await ctx.send("The queue is")
        await ctx.send((str(i)+". ", item))


@tasks.loop(seconds=5)
async def change_status():
    await musicBot.change_presence(activity=discord.Game(choice(status)))

print('okay')
musicBot.run('NzczNTE1NTUwODc3ODEwNjg4.X6KWfg.hGjbMB-9dY2J611wUGKfGRzkgQ8')
