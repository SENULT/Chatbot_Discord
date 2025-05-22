import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Da Nang information
da_nang_info = {
    'places': {
        'marble_mountains': 'The Marble Mountains (Ngu Hanh Son) are five limestone hills named after the five elements. They feature caves, temples, and panoramic views of Da Nang.',
        'dragon_bridge': 'The Dragon Bridge is a modern architectural marvel that spans the Han River. It breathes fire and water every weekend night.',
        'my_khe_beach': 'My Khe Beach is known as one of the most beautiful beaches in Vietnam, famous for its white sand and clear water.',
        'lady_buddha': 'The Lady Buddha statue at Linh Ung Pagoda is the tallest Buddha statue in Vietnam, standing at 67 meters.',
        'han_market': 'Han Market is a traditional market offering local food, souvenirs, and a glimpse into daily life in Da Nang.'
    },
    'traditions': {
        'festivals': 'Da Nang hosts several festivals including the International Fireworks Festival and the Quan The Am Festival.',
        'cuisine': 'Famous local dishes include Mi Quang (turmeric noodles), Banh Xeo (savory pancakes), and fresh seafood.',
        'crafts': 'Traditional crafts include stone carving in Non Nuoc village and fishing net making.'
    }
}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='danang')
async def da_nang(ctx, category=None, topic=None):
    """Get information about Da Nang"""
    if not category:
        await ctx.send("Please specify a category: 'places' or 'traditions'")
        return

    if category.lower() == 'places':
        if not topic:
            places_list = "\n".join([f"- {place.replace('_', ' ').title()}" for place in da_nang_info['places'].keys()])
            await ctx.send(f"Available places in Da Nang:\n{places_list}")
        elif topic.lower() in da_nang_info['places']:
            await ctx.send(da_nang_info['places'][topic.lower()])
        else:
            await ctx.send("Place not found. Use !danang places to see the list of available places.")

    elif category.lower() == 'traditions':
        if not topic:
            traditions_list = "\n".join([f"- {tradition.replace('_', ' ').title()}" for tradition in da_nang_info['traditions'].keys()])
            await ctx.send(f"Available traditions in Da Nang:\n{traditions_list}")
        elif topic.lower() in da_nang_info['traditions']:
            await ctx.send(da_nang_info['traditions'][topic.lower()])
        else:
            await ctx.send("Tradition not found. Use !danang traditions to see the list of available traditions.")
    else:
        await ctx.send("Invalid category. Use 'places' or 'traditions'")

@bot.command(name='help_danang')
async def help_danang(ctx):
    """Show help information about the bot"""
    help_text = """
**Da Nang Information Bot Commands:**

`!danang places` - List all famous places in Da Nang
`!danang places [place_name]` - Get information about a specific place
`!danang traditions` - List all traditions in Da Nang
`!danang traditions [tradition_name]` - Get information about a specific tradition

Example:
`!danang places dragon_bridge` - Get information about the Dragon Bridge
`!danang traditions cuisine` - Get information about Da Nang cuisine
"""
    await ctx.send(help_text)

# Run the bot
bot.run(TOKEN) 