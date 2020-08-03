# LorePets
A Twitch Chat Bot that allows viewers to take on the difficult life of raising little monsters for profit.


# Requirements
Python 3.6+ with pip: https://www.python.org/downloads/

# Packages
Type the corresponding commands into a command shell

dotenv:  pip install python-dotenv

twitchio: pip install twitchio

dateutil: pip install python-dateutil
  

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
