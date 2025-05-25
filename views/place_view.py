import discord
from discord import ui
from typing import List
import logging
from utils.places import get_place_info

logger = logging.getLogger(__name__)

class PlaceSelect(ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Marble Mountains",
                value="marble_mountains",
                description="Five limestone hills with caves and temples"
            ),
            discord.SelectOption(
                label="Dragon Bridge",
                value="dragon_bridge",
                description="Modern architectural marvel"
            ),
            discord.SelectOption(
                label="My Khe Beach",
                value="my_khe_beach",
                description="One of Vietnam's most beautiful beaches"
            ),
            discord.SelectOption(
                label="Lady Buddha",
                value="lady_buddha",
                description="Tallest Buddha statue in Vietnam"
            ),
            discord.SelectOption(
                label="Han Market",
                value="han_market",
                description="Traditional market in Da Nang"
            )
        ]
        super().__init__(
            placeholder="Choose a place in Da Nang...",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer()
            
            place_name = self.values[0]
            place_info = await get_place_info(place_name)
            
            embed = discord.Embed(
                title=place_info['name'],
                description=place_info['description'],
                color=discord.Color.blue()
            )
            
            if place_info['photo_url']:
                embed.set_image(url=place_info['photo_url'])
            
            if place_info['maps_url']:
                embed.add_field(
                    name="Location",
                    value=f"[View on Google Maps]({place_info['maps_url']})",
                    inline=False
                )
            
            if place_info['rating']:
                embed.add_field(
                    name="Rating",
                    value=f"⭐ {place_info['rating']} ({place_info['user_ratings_total']} reviews)",
                    inline=True
                )
            
            await interaction.followup.send(embed=embed)
            
            # Add reactions
            message = await interaction.original_response()
            for emoji in ["🔥", "❤️", "😋"]:
                await message.add_reaction(emoji)
                
        except Exception as e:
            logger.error(f"Error in PlaceSelect callback: {str(e)}")
            await interaction.followup.send(
                "Sorry, there was an error processing your request. Please try again later.",
                ephemeral=True
            )

class PlaceView(ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(PlaceSelect()) 