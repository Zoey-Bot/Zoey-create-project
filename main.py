
ZoeyBot
/
fortnitepy
Python


Upgrade

Invite

Files







 
Preview of README.md
fortnitepy


Asynchronous library for interacting with Fortnite and EpicGames' API and XMPP services.

Note: This library is still under developement so breaking changes might happen at any time.

Some key features:

Full support for Friends.
Support for XMPP events including friend and party messages + many more.
Support for Parties.
Support for Battle Royale stats.
Documentation
https://fortnitepy.readthedocs.io/en/latest/

Installing
# windows
py -3 -m pip install -U fortnitepy

# linux
python3 -m pip install -U fortnitepy
# windows
py -3 -m pip install -U fortnitepy

# linux
python3 -m pip install -U fortnitepy
Basic usage
import fortnitepy
import json
import os
 
from fortnitepy.ext import commands
 
email = 'email@email.com'
password = 'password1'
filename = 'device_auths.json'
 
def get_device_auth_details():
    if os.path.isfile(filename):
        with open(filename, 'r') as fp:
            return json.load(fp)
    return {}
 
def store_device_auth_details(email, details):
    existing = get_device_auth_details()
    existing[email] = details
 
    with open(filename, 'w') as fp:
        json.dump(existing, fp)
 
device_auth_details = get_device_auth_details().get(email, {})
bot = commands.Bot(
    command_prefix='!',
    auth=fortnitepy.AdvancedAuth(
        email=email,
        password=password,
        prompt_authorization_code=True,
        delete_existing_device_auths=True,
        **device_auth_details
    )
)
 
@bot.event
async def event_device_auth_generate(details, email):
    store_device_auth_details(email, details)
 
@bot.event
async def event_ready():
    print('----------------')
    print('Bot ready as')
    print(bot.user.display_name)
    print(bot.user.id)
    print('----------------')
 
@bot.event
async def event_friend_request(request):
    await request.accept()
 
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')
 
bot.run()
