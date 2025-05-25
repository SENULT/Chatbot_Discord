import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests
from discord import ui
import json
import logging
from config import TOKEN, COMMAND_PREFIX, DA_NANG_INFO
from views.place_view import PlaceView
from utils.logger import setup_logger
from utils.places import get_place_info
import random # Import random for thank you responses

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Set up logging
logger = setup_logger('danang_bot')

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

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

class PlaceSelect(ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Marble Mountains", value="marble_mountains", description="Five limestone hills with caves and temples"),
            discord.SelectOption(label="Dragon Bridge", value="dragon_bridge", description="Modern architectural marvel"),
            discord.SelectOption(label="My Khe Beach", value="my_khe_beach", description="One of Vietnam's most beautiful beaches"),
            discord.SelectOption(label="Lady Buddha", value="lady_buddha", description="Tallest Buddha statue in Vietnam"),
            discord.SelectOption(label="Han Market", value="han_market", description="Traditional market in Da Nang")
        ]
        super().__init__(placeholder="Choose a place in Da Nang...", options=options)

    async def callback(self, interaction: discord.Interaction):
        place_name = self.values[0]
        place_info = await get_place_info(place_name)
        
        embed = discord.Embed(
            title=place_info['name'],
            description=place_info['description'],
            color=discord.Color.blue()
        )
        
        if 'photo_url' in place_info:
            embed.set_image(url=place_info['photo_url'])
        
        if 'maps_url' in place_info:
            embed.add_field(name="Location", value=f"[View on Google Maps]({place_info['maps_url']})")
        
        await interaction.response.send_message(embed=embed)
        
        # Add reactions
        message = await interaction.original_response()
        for emoji in ["🔥", "❤️", "😋"]:
            await message.add_reaction(emoji)

class PlaceView(ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(PlaceSelect())

async def get_place_info(place_name):
    # Google Places API endpoint
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': f"{place_name} Da Nang Vietnam",
        'key': GOOGLE_API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data['status'] == 'OK' and data['results']:
            place = data['results'][0]
            
            # Get photo if available
            photo_url = None
            if 'photos' in place:
                photo_reference = place['photos'][0]['photo_reference']
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={GOOGLE_API_KEY}"
            
            return {
                'name': place['name'],
                'description': place.get('formatted_address', 'No description available'),
                'maps_url': f"https://www.google.com/maps/place/?q=place_id:{place['place_id']}",
                'photo_url': photo_url
            }
    except Exception as e:
        print(f"Error fetching place info: {e}")
    
    # Fallback to static data if API fails
    return {
        'name': place_name.replace('_', ' ').title(),
        'description': da_nang_info['places'].get(place_name, 'No description available'),
        'maps_url': None,
        'photo_url': None
    }

# Dictionary to store last topic per user and their preferred language
user_last_topic = {}
user_language = {}

# Helper function to find topic in query
def find_topic_in_query(query):
    """Helper to find a matching topic key and category in the query."""
    query_words = query.split()
    for category, items in DA_NANG_INFO.items():
        for key in items.keys():
            # Check for exact key match or key with underscores replaced by spaces (English)
            if key in query_words or key.replace('_', ' ') in query:
                return key, category
            # Add checks for Vietnamese keywords if needed in the future
            # For now, rely on English keyword matching
    return None, None

# Helper function to get localized text
def get_localized_text(user_id, key, category=None, default_text="Information not available."):
    """
    Retrieves localized text for a given key, category, and user ID.
    Defaults to English if user preference is not set or translation is missing.
    """
    lang = user_language.get(user_id, 'en') # Default to English
    
    if category and category in DA_NANG_INFO and key in DA_NANG_INFO[category]:
        if lang in DA_NANG_INFO[category][key]:
            return DA_NANG_INFO[category][key][lang]
        elif 'en' in DA_NANG_INFO[category][key]:
            return DA_NANG_INFO[category][key]['en'] # Fallback to English if preferred lang missing
            
    elif category is None and key in DA_NANG_INFO:
         if lang in DA_NANG_INFO[key]:
             return DA_NANG_INFO[key][lang]
         elif 'en' in DA_NANG_INFO[key]:
            return DA_NANG_INFO[key]['en'] # Fallback to English for overview etc.

    return default_text # Return default if key or category not found

@bot.event
async def on_ready():
    """Called when the bot is ready and connected to Discord."""
    logger.info(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        logger.info(f"Synced {len(synced)} command(s)")
    except Exception as e:
        logger.error(f"Failed to sync commands: {str(e)}")

@bot.event
async def on_error(event, *args, **kwargs):
    """Global error handler for the bot."""
    logger.error(f"Error in {event}: {str(args[0])}")

@bot.event
async def on_message(message):
    """
    Processes every message to respond to greetings and Da Nang related questions directly.
    """
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
        
    # Process commands first
    await bot.process_commands(message)
    
    # Process messages that don't start with the command prefix
    if not message.content.startswith(COMMAND_PREFIX):
        user_id = message.author.id
        query = message.content.lower()
        
        # --- Handle Greetings ---
        greeting_phrases = ['hi', 'hello', 'hey', 'yo', 'sup', '안녕', 'xin chào'] 
        if any(query.startswith(phrase) for phrase in greeting_phrases):
            await message.channel.send(f"Hello {message.author.mention}! How can I help you explore Da Nang today? You can ask me about places, traditions, or use `!danang` for a menu!")
            logger.info(f"Responded to greeting from {message.author.name}")
            return # Stop processing if it's a greeting

        # --- Handle Thanks and Well Wishes ---
        thank_you_phrases = ['thank you', 'thanks', 'have a nice day', 'good day', 'cheers', 'you can take a rest now'] # Added more phrases
        if any(phrase in query for phrase in thank_you_phrases):
            responses = [
                f"You're welcome, {message.author.mention}! Happy to help you discover Da Nang!",
                "Anytime! Enjoy your day!",
                "Glad I could help! Have a wonderful day!",
                "Thank you! Wishing you a great day as well!",
                "Thanks for the kind words! I'm always here if you need anything else about Da Nang!"
            ]
            await message.channel.send(random.choice(responses))
            logger.info(f"Responded to thank you/well wish from {message.author.name}")
            return # Stop processing after responding

        
        # --- Handle Da Nang Queries ---
        # Simple check if the message is likely a question about Da Nang or general info
        danang_keywords = ['da nang', 'danang', 'place', 'tradition', 'cuisine', 'festival', 'beach', 'bridge', 'mountain', 'market', 'buddha', 'thing', 'what', 'where', 'tell', 'show', 'info', 'about', 'know', 'visit', 'see', 'eat', 'around', 'nearby', 'surrounding', 'time to visit', 'season', 'weather', 'when to go', 'overview', 'general info', 'information'] 
        is_potential_danang_query = any(keyword in query for keyword in danang_keywords)

        # Only proceed if it seems like a potential Da Nang query or if it's a likely follow-up
        follow_up_phrases = ["anything else", "tell me more", "more info", "other", "next"]
        is_follow_up = any(phrase in query for phrase in follow_up_phrases)
        
        if is_potential_danang_query or (is_follow_up and user_id in user_last_topic and user_last_topic[user_id]):

            logger.info(f"Attempting to respond to non-command message: {query}")
            
            found_info_key = None
            found_info_category = None
            response_text = None
            
            if is_follow_up:
                # Handle follow-up based on last topic
                 if user_id in user_last_topic and user_last_topic[user_id]:
                    last_topic_key = user_last_topic[user_id]
                    last_topic_category = None
                    # Find the category of the last topic
                    for cat, items in DA_NANG_INFO.items():
                         if last_topic_key in items or last_topic_key == cat: # Check if last topic was a category itself (like overview)
                            last_topic_category = cat
                            break

                    if last_topic_category:
                         logger.info(f"Handling follow-up for last topic: {last_topic_key} ({last_topic_category})\n")
                         
                         # Get translated topic name for the response
                         last_topic_name = get_localized_text(user_id, last_topic_key, last_topic_category) # This might return the description, need just the name
                         # Simple way to get a name - try to look up in places/traditions or use the key
                         display_topic_name = last_topic_key.replace('_', ' ').title()
                         if last_topic_category in ['places', 'traditions', 'surroundings'] and last_topic_key in DA_NANG_INFO[last_topic_category]:
                              # Use English name from config for consistency in suggestions for now
                             if 'en' in DA_NANG_INFO[last_topic_category][last_topic_key]:
                                display_topic_name = DA_NANG_INFO[last_topic_category][last_topic_key]['en'].split('.')[0] # Get first sentence as a name proxy
                             else:
                                 display_topic_name = last_topic_key.replace('_', ' ').title()
                         elif last_topic_category == 'overview':
                              display_topic_name = get_localized_text(user_id, 'overview').split('.')[0] # Use first sentence of overview
                         elif last_topic_category == 'visiting_info':
                              display_topic_name = get_localized_text(user_id, 'best_time_to_visit').split('.')[0] # Use first sentence of visiting info


                         follow_up_response_parts = []

                         if last_topic_category in ['places', 'surroundings']:
                             # Suggest other places/surroundings and traditions/visiting info
                             other_places_surroundings = [get_localized_text(user_id, k, last_topic_category).split('.')[0] for k in DA_NANG_INFO[last_topic_category].keys() if k != last_topic_key]
                             if other_places_surroundings:
                                 follow_up_response_parts.append(get_localized_text(user_id, 'other_related_places_surroundings', 'messages').format(topic=display_topic_name, items=', '.join(other_places_surroundings)))
                             follow_up_response_parts.append(get_localized_text(user_id, 'ask_about_traditions_visiting', 'messages'))

                         elif last_topic_category == 'traditions':
                              # Suggest other traditions and places/surroundings/visiting info
                             other_traditions = [get_localized_text(user_id, k, last_topic_category).split('.')[0] for k in DA_NANG_INFO[last_topic_category].keys() if k != last_topic_key]
                             if other_traditions:
                                 follow_up_response_parts.append(get_localized_text(user_id, 'other_related_traditions', 'messages').format(topic=display_topic_name, items=', '.join(other_traditions)))
                             follow_up_response_parts.append(get_localized_text(user_id, 'ask_about_places_surroundings_visiting', 'messages'))

                         elif last_topic_category == 'visiting_info':
                             # Suggest places, traditions, surroundings
                              follow_up_response_parts.append(get_localized_text(user_id, 'ask_about_places_traditions_surroundings_after_visiting', 'messages').format(topic=display_topic_name))

                         elif last_topic_category == 'overview':
                              # Suggest asking about places, traditions, surroundings, visiting info
                               follow_up_response_parts.append(get_localized_text(user_id, 'ask_about_details_after_overview', 'messages').format(topic=display_topic_name))

                         # Combine parts into a response
                         if follow_up_response_parts:
                             response_text = ".\n\n".join(follow_up_response_parts)
                             # Embeds are not ideal for purely text responses, send as plain message
                             await message.channel.send(response_text)
                             logger.info(f"Responded to follow-up for {last_topic_key} with suggestions.")
                             # Don't update last topic for generic follow-up suggestions
                             return
                         else:
                              await message.channel.send(get_localized_text(user_id, 'generic_follow_up_fail', 'messages'))
                              user_last_topic[user_id] = None # Clear last topic if follow-up failed
                              return

                    if not response_text:
                        # Fallback if last topic category not found (shouldn't happen with current logic)
                        await message.channel.send(get_localized_text(user_id, 'generic_follow_up_fail', 'messages'))
                        user_last_topic[user_id] = None # Clear last topic
                        return

                 else:
                    await message.channel.send(get_localized_text(user_id, 'no_last_topic_follow_up', 'messages'))
                    user_last_topic[user_id] = None # Clear last topic
                    return

            else:
                # Process the new query for a specific topic or general info
                topic_key, category = find_topic_in_query(query)

                if topic_key:
                    if category == 'places':
                        try:
                            place_info = await get_place_info(topic_key)
                             # Use localized name for the embed title if available, otherwise fallback to English key title
                            embed_title = get_localized_text(user_id, topic_key, category).split('.')[0] if get_localized_text(user_id, topic_key, category) != "Information not available." else topic_key.replace('_', ' ').title()

                            embed = discord.Embed(
                                title=embed_title,
                                description=get_localized_text(user_id, topic_key, category),
                                color=discord.Color.green()
                            )
                            if place_info and place_info['photo_url']:
                                embed.set_image(url=place_info['photo_url'])
                            if place_info and place_info['maps_url']:
                                embed.add_field(
                                    name=get_localized_text(user_id, 'location_field', 'messages'),
                                    value=f"[View on Google Maps]({place_info['maps_url']})",
                                    inline=False
                                )
                            
                            # Safely add rating field if available from API
                            if place_info and 'rating' in place_info and place_info['rating'] is not None:
                                 rating_value = place_info['rating']
                                 user_ratings_total = place_info.get('user_ratings_total')
                                 rating_field_value = f"⭐ {rating_value}"
                                 if user_ratings_total is not None:
                                      rating_field_value += f" ({user_ratings_total} {get_localized_text(user_id, 'reviews_text', 'messages')})"
                                 
                                 embed.add_field(
                                    name=get_localized_text(user_id, 'rating_field', 'messages'),
                                    value=rating_field_value,
                                    inline=True
                                )

                            await message.channel.send(embed=embed)
                            logger.info(f"Responded to message '{query}' with place info for '{topic_key}'")
                            user_last_topic[user_id] = topic_key # Store the last topic
                            return # Stop processing after responding
                        except Exception as e:
                            logger.error(f"Error fetching place info for '{topic_key}' in on_message: {str(e)}")
                            # Fallback to static data if API call fails
                            response_text = get_localized_text(user_id, topic_key, category)
                            title = get_localized_text(user_id, topic_key, category).split('.')[0] if response_text != "Information not available." else topic_key.replace('_', ' ').title()
                            # Don't return here, proceed to send static info embed
                    # Handle other categories
                    elif category in ['traditions', 'surroundings', 'visiting_info', 'overview']:
                         response_text = get_localized_text(user_id, topic_key, category)
                         title = get_localized_text(user_id, topic_key, category).split('.')[0] if response_text != "Information not available." else topic_key.replace('_', ' ').title()
                         # Don't return here, proceed to send info embed

            # Send the embed for static/fallback info if response_text is set but hasn't been sent
            if response_text:
                 embed = discord.Embed(
                    title=title,
                    description=response_text,
                    color=discord.Color.orange()
                 )
                 await message.channel.send(embed=embed)
                 logger.info(f"Responded to message '{query}' with info for '{topic_key or title}'")
                 if topic_key: user_last_topic[user_id] = topic_key # Store the last topic if a specific topic was found
                 return # Stop processing after responding

            else:
                # No specific topic found, provide a general hint or fallback
                # Avoid being too chatty with generic responses for now, unless it's a follow-up that couldn't be handled
                if not is_follow_up:
                    # Optional: Add a fallback response for general Da Nang mentions not matching a specific topic
                    general_response = ( get_localized_text(user_id, 'general_intro', 'messages').format(mention=message.author.mention) +
                        "\n\n" + get_localized_text(user_id, 'general_topics', 'messages') +
                        "\n\n" + get_localized_text(user_id, 'use_danang_command_hint', 'messages')
                    )
                    await message.channel.send(general_response)
                    logger.info(f"Responded to general Da Nang query: {query}")
                    return # Stop processing after responding

        # If not a potential Da Nang query, a handled follow-up, or a greeting/thank you, do nothing.

@bot.command(name='language')
async def set_language(ctx, lang_code=None):
    """Sets the preferred language for bot responses (e.g., !language vi)."""
    user_id = ctx.author.id
    supported_languages = ['en', 'vi'] # Define supported languages

    if lang_code is None:
        current_lang = user_language.get(user_id, 'en')
        await ctx.send(f"Your current language preference is: {current_lang}. Supported languages are: {', '.join(supported_languages)}.")
        return

    if lang_code.lower() in supported_languages:
        user_language[user_id] = lang_code.lower()
        confirmation_message = {
            'en': f"Language set to English.",
            'vi': f"Đã đặt ngôn ngữ sang Tiếng Việt."
        }
        await ctx.send(confirmation_message.get(lang_code.lower(), confirmation_message['en']))
        logger.info(f"User {ctx.author.name} set language to {lang_code.lower()}")
    else:
        await ctx.send(f"Invalid language code. Supported languages are: {', '.join(supported_languages)}.")


@bot.command(name='danang')
async def da_nang(ctx):
    """Show the Da Nang places dropdown menu"""
    try:
        view = PlaceView()
        await ctx.send(get_localized_text(ctx.author.id, 'select_place_prompt', 'messages'), view=view)
    except Exception as e:
        logger.error(f"Error in da_nang command: {str(e)}")
        await ctx.send(get_localized_text(ctx.author.id, 'generic_error', 'messages'))

@bot.command(name='askdanang')
async def ask_danang(ctx, *args):
    """
    Ask a question about Da Nang.
    Example: !askdanang Tell me about Dragon Bridge
    """
    user_id = ctx.author.id
    query = " ".join(args).lower()
    
    if not query:
        await ctx.send(get_localized_text(user_id, 'ask_command_no_query', 'messages'))
        return

    # Simple keyword matching for this command
    topic_key, category = find_topic_in_query(query)
    found_info = None
    title = None

    if topic_key:
        if category == 'places':
            try:
                place_info = await get_place_info(topic_key)
                 # Use localized name for the embed title if available, otherwise fallback to English key title
                embed_title = get_localized_text(user_id, topic_key, category).split('.')[0] if get_localized_text(user_id, topic_key, category) != "Information not available." else topic_key.replace('_', ' ').title()

                embed = discord.Embed(
                    title=embed_title,
                    description=get_localized_text(user_id, topic_key, category),
                    color=discord.Color.green() 
                )
                if place_info and place_info['photo_url']:
                    embed.set_image(url=place_info['photo_url'])
                if place_info and place_info['maps_url']:
                    embed.add_field(
                        name=get_localized_text(user_id, 'location_field', 'messages'),
                        value=f"[View on Google Maps]({place_info['maps_url']})",
                        inline=False
                    )
                
                rating = place_info.get('rating')
                user_ratings_total = place_info.get('user_ratings_total')
                if rating is not None and user_ratings_total is not None:
                                 embed.add_field(
                                    name=get_localized_text(user_id, 'rating_field', 'messages'),
                                    value=f"⭐ {rating} ({user_ratings_total} {get_localized_text(user_id, 'reviews_text', 'messages')})",
                                    inline=True
                                )
                elif rating is not None:
                                 embed.add_field(
                                    name=get_localized_text(user_id, 'rating_field', 'messages'),
                                    value=f"⭐ {rating}",
                                    inline=True
                                )

                await ctx.send(embed=embed)
                logger.info(f"Responded to !askdanang '{query}' with place info for '{topic_key}'")
                user_last_topic[user_id] = topic_key # Store the last topic
                return
            except Exception as e:
                logger.error(f"Error fetching place info for '{topic_key}' in askdanang command: {str(e)}")
                # Fallback to static data if API call fails
                found_info = get_localized_text(user_id, topic_key, category)
                title = get_localized_text(user_id, topic_key, category).split('.')[0] if found_info != "Information not available." else topic_key.replace('_', ' ').title()

        # Handle other categories for askdanang command
        elif category in ['traditions', 'surroundings', 'visiting_info', 'overview']:
             found_info = get_localized_text(user_id, topic_key, category)
             title = get_localized_text(user_id, topic_key, category).split('.')[0] if found_info != "Information not available." else topic_key.replace('_', ' ').title()

    if found_info:
        embed = discord.Embed(
            title=title,
            description=found_info,
            color=discord.Color.orange() 
        )
        await ctx.send(embed=embed)
        logger.info(f"Responded to !askdanang '{query}' with info for '{topic_key or title}'")
        if topic_key: user_last_topic[user_id] = topic_key # Store the last topic if a specific topic was found
    else:
        await ctx.send(get_localized_text(user_id, 'ask_command_no_info', 'messages').format(command='`!danang`'))
        logger.warning(f"No info found for !askdanang query: '{query}'")
        user_last_topic[user_id] = None # Clear last topic if query wasn't understood

@bot.command(name='help_danang')
async def help_danang(ctx):
    """Show help information about the bot"""
    user_id = ctx.author.id
    help_text = get_localized_text(user_id, 'help_message', 'messages').format(
        command_danang = '`!danang`',
        command_askdanang = '`!askdanang [your question]`',
        command_language = '`!language [en|vi]`'
    )
    try:
        await ctx.send(help_text)
    except Exception as e:
        logger.error(f"Error in help_danang command: {str(e)}")
        await ctx.send(get_localized_text(user_id, 'generic_error', 'messages'))

def main():
    """Main function to run the bot."""
    try:
        bot.run(TOKEN) 
    except Exception as e:
        logger.error(f"Failed to start bot: {str(e)}")

if __name__ == "__main__":
    main() 