# bot_daily
 Discord bot to scrum IT dailys 

Discord bot that sends a message every week day at the same hour.
The bot is currently set to not show in weekends and holidays.
The message contains a meeting link, and two buttons to say that you assist to the meeting (green emoji) or you don't (red emoji).
The message stays up for 15 minutes and then it gets eliminated. The data is sent to the flask server and displayed in the specified route (http://127.0.0.1:5000/asistentes).
The bot has a command !daily that sends the message manually, a command !participantes that shows who assists to the meeting, and a !cuando_daily that show when it's the next meeting. 
The bot.py file contains all the bot functioning and Discord libraries, you should check discord developers options to learn more on how to add the bot to your channel. https://discord.com/developers/docs/intro
The api.py file contains all the functioning of the flask server that is used to connect the discord to a webpage if needed, it sends in real time the participants. See the flask docs for more info https://flask.palletsprojects.com/en/2.3.x/
The main.py file puts all together and make the bot and the server run at the same time, you can run the bot and the server in different threads if you like, but I couldn't make it work.
You only have to put in console 'python main.py' and done!
You can also run the bot alone and it will work just fine, but it won't send any data, it will just display a message with a link.
The link of the meeting has to be introduced manually in the code. 
You can also change the message text and change the emojis.
In the discord docs you will also find that you have to put your own TOKEN and CHANNEL_ID, that goes into a .env file into the same folder like this:
TOKEN=yourToken
CHANNEL_ID=yourId


This is a work in progress
