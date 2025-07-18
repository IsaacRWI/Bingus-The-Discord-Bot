# Bingus the Discord Bot

## Project Outline
This is Bingus, a bot I built to learn and test out discord bot functions.  
It can do several things including play audio from youtube or file, respond to user input, and a few other things.  
I will likely continue to expand on this project as time goes on to experiment with integrating different functions into 
discord bots.

## Dependencies
Dependencies used in this project can be found in `requirements.txt`  
To install all project dependencies run the following line in the console.  
`pip install -r requirements.txt`  
In addition, FFmpeg is also required on the computer that will be running the bot in order for the voice channel related commands and run yt-dlp.  
To install FFmpeg on windows, run the following line in the cmd terminal.  
`winget install FFmpeg`  
If you're on linux good luck you'll figure it out.

## Debugging 
When the python code is running it will generate a log file titled `discord.log` and can be used for debugging purposes 
especially surrounding errors thrown by the discord extension.

## Commands
The phrases to reach Bingus are as follows:  
!hellob:  You greets bingus warmly and will result in Bingus returning the favor.  
!pledge:  You pledge your allegiance to Bingus, becoming a servant of it, bingu.  
!escape:  You forfeit your privilege to be a servant of Bingus, you are now binguless.  
!verify:  You look up to Bingus for validation and he confirms you a real one.  
!dm:  You send Bingus a message and he replies to you in your dms.  
!reply:  You force Bingus to reply to your message regardless of whether it wants to or not.  
!poll:  You summon Bingus to ascertain the opinion of the masses, collected as cute emojis.  
!plankton:  Bingus plays the plankton meme.  
!p *:  Bingus searches youtube for * and plays it in the voice channel.  
!dc: Disconnects Bingus from you voice channel.