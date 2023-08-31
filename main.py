import discord
import random
import json
import os

intents = discord.Intents.default()
intents.message_content = True
intents.message_attachments = True

client = discord.Client(intents=intents)

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))
quips_file_path = os.path.join(script_directory, "quips.json")

with open(quips_file_path, "r") as quips_file:
    quips_data = json.load(quips_file)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.attachments) > 0:
        attachment = message.attachments[0]
        if attachment.url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            score = random.randint(1, 10)
            selected_quip = random.choice(quips_data["quips"])
            response = f"Score: {score}/10\n{selected_quip}"
            await message.channel.send(response)

# Run the bot
client.run('MTE0Njc0Mzg3MDA0MjkzMTIwMA.GhGmRY.KlZ9TvYZCk99YavFb2EPgboCtBUz93QA0g_u20')
