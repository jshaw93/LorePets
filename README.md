# LorePets
A Twitch Chat Bot that allows viewers to take on the difficult life of raising little monsters for profit.


# Requirements
Python 3.6+ with pip: https://www.python.org/downloads/

Type the corresponding commands into a command shell

dotenv:  pip install python-dotenv

twitchio: pip install twitchio

dateutil: pip install python-dateutil

# Twitch Account that is set up to be a bot:
Make an account on Twitch (for your bot) or use the one you stream with. Make it something cool like RealStreamer69 😎

Request an oauth code. You'll need to login and give the app permissions to generate it for you.  https://twitchapps.com/tmi/

oauth will look like: oauth:65cbmejgiemlnyzbq1onjhkkkk7m and be put under TMI_TOKEN

Register your app with Twitch dev and request a client-id (so you can interface with Twitch's API) https://dev.twitch.tv/console/apps/create

client-id will look like: gsgx0a285jjfwui2vqzegg4xxxxvkz

In the .env file, update the necessary information.  You can find all the necessary info by following the above steps.  The bot_nick will be the bot's twitch name, while the channel will be your channel!

# How to run
Just run the LorePets batch executable!


# Want to request features?
Email: TwitchLorePets@gmail.com


# Commands
!pet -- Displays your pet, and pet’s level, for the chat to see!

!petpay (@name) (amount) -- Give your friends some gold!

!pethelp -- Displays the link for this chat.

!gold -- Displays your current gold in the chat.

!renamepet (name) -- Allows you to rename your pet, usage is !renamepet (name).  Please be courteous with your chosen name, don’t want to get banned!

!sendpet -- Allows you to send your pet out on a farming run once an hour!

!resetpet -- Mod only command, allows moderators to reset a user’s pet timer in case they get stuck unable to use !sendpet or !petboss, as could happen if the bot goes down, or a bug happens.

!levelup (amount you’d like to spend) -- Levels up your pet for a chunk of gold.  These levels will be used.  If no amount is specified, all available levels that you have gold for will be given to you at that cost.

!selectpet (pet number) -- Select the pet you’d like to use!  In order to see what number your desired pet is, just type this command without the number argument! (!selectpet)


!petboss (nothing/boss name/time) -- You send your pet to fight various bosses in the world for increased gold return!  However, the stronger the boss, the longer your pet may have to wait between boss runs!  Using ‘!petboss time’ will allow you to see the time remaining before you can use petboss again!  In order to begin bossing, you must have a pet at level 30.

!petduel (@name) (gold) -- Request a duel with a fellow pet owner!  50/50 chance to take gold, or lose it!
