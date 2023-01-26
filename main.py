import nextcord, requests, datetime, logging
from nextcord.ext import commands

logger = logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TESTING_GUILD_ID = 123456789 # Replace with your guild ID

bot = commands.Bot()
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print(f'{bot.user} logged in at ' + current_time)



@bot.slash_command(description="Check the current server Ip", guild_ids=[TESTING_GUILD_ID], dm_permission=True)
async def ip(interaction: nextcord.Interaction):
    ip = requests.get('http://ip.42.pl/raw').text
    await interaction.send("**Current Ip: **" + ip)
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Command /ip was used at ' + current_time)


@bot.slash_command(description="Get a list of commands", guild_ids=[TESTING_GUILD_ID], dm_permission=True)
async def help(interaction: nextcord.Interaction):
    await interaction.send("**List Of Commands** \n /help - this menu \n /ip - get the current server ip \n /status - "
                           "get the bots current status")
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Command /help was used at " + current_time)

@bot.slash_command(description="Check the bots status", guild_ids=[TESTING_GUILD_ID], dm_permission=True)
async def status(interaction: nextcord.Interaction):
    await interaction.send("**Bot Status** \n :green_circle: Online and good to go")
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Command /status was used at " + current_time)


bot.run('') # Input your bot token here
