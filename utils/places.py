import aiohttp
import asyncio
from cachetools import TTLCache
from typing import Dict, Optional
import logging
from config import (
    GOOGLE_API_KEY,
    GOOGLE_PLACES_API_URL,
    GOOGLE_PLACES_PHOTO_URL,
    CACHE_TTL,
    DA_NANG_INFO
)

logger = logging.getLogger(__name__)

# Initialize cache
place_cache = TTLCache(maxsize=100, ttl=CACHE_TTL)

async def get_place_info(place_name: str) -> Dict:
    """
    Get information about a place in Da Nang using Google Places API with caching.
    
    Args:
        place_name (str): Name of the place to look up
        
    Returns:
        Dict: Place information including name, description, and photo URL
    """
    # Check cache first
    cache_key = f"place_{place_name}"
    if cache_key in place_cache:
        logger.info(f"Cache hit for {place_name}")
        return place_cache[cache_key]
    
    try:
        async with aiohttp.ClientSession() as session:
            # Search for the place
            params = {
                'query': f"{place_name} Da Nang Vietnam",
                'key': GOOGLE_API_KEY
            }
            
            async with session.get(GOOGLE_PLACES_API_URL, params=params) as response:
                if response.status != 200:
                    logger.error(f"API request failed with status {response.status}")
                    return get_fallback_info(place_name)
                
                data = await response.json()
                
                if data['status'] != 'OK' or not data['results']:
                    logger.warning(f"No results found for {place_name}")
                    return get_fallback_info(place_name)
                
                place = data['results'][0]
                
                # Get photo if available
                photo_url = None
                if 'photos' in place:
                    photo_reference = place['photos'][0]['photo_reference']
                    photo_url = f"{GOOGLE_PLACES_PHOTO_URL}?maxwidth=400&photoreference={photo_reference}&key={GOOGLE_API_KEY}"
                
                result = {
                    'name': place['name'],
                    'description': place.get('formatted_address', 'No description available'),
                    'maps_url': f"https://www.google.com/maps/place/?q=place_id:{place['place_id']}",
                    'photo_url': photo_url,
                    'rating': place.get('rating'),
                    'user_ratings_total': place.get('user_ratings_total')
                }
                
                # Cache the result
                place_cache[cache_key] = result
                return result
                
    except Exception as e:
        logger.error(f"Error fetching place info for {place_name}: {str(e)}")
        return get_fallback_info(place_name)

def get_fallback_info(place_name: str) -> Dict:
    """
    Get fallback information from static data when API fails.
    
    Args:
        place_name (str): Name of the place
        
    Returns:
        Dict: Basic place information
    """
    return {
        'name': place_name.replace('_', ' ').title(),
        'description': DA_NANG_INFO['places'].get(place_name, 'No description available'),
        'maps_url': None,
        'photo_url': None,
        'rating': None,
        'user_ratings_total': None
    } 