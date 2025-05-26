# Da Nang Information Discord Bot 🤖

A feature-rich Discord bot that provides information about places and attractions in Da Nang, Vietnam. The bot uses the Google Places API to fetch real-time information and includes features like place ratings, photos, and interactive menus

## Features 🌟

### Core Features
- **Interactive Place Selection**: Dropdown menu to select popular places in Da Nang
- **Rich Information Display**: 
  - Place descriptions
  - Google Maps integration
  - Place photos
  - Ratings and reviews
  - Interactive reactions
- **Real-time Data**: Uses Google Places API for up-to-date information
- **Bilingual Support**: Full support for both English and Vietnamese languages
- **Smart Follow-up Suggestions**: Contextual recommendations for related places and topics
- **Performance Optimized**: 
  - Response caching
  - Async operations
  - Error handling
- **User-friendly**: Simple commands and intuitive interface

### Available Information Categories
- **Places**: Popular attractions like Marble Mountains, Dragon Bridge, My Khe Beach, etc.
- **Traditions**: Local festivals, cuisine, and traditional crafts
- **Surroundings**: Nearby UNESCO World Heritage sites (Hoi An, Hue, My Son)
- **Visiting Info**: Best time to visit and seasonal information

## Prerequisites 📋

- Python 3.8 or higher
- Discord Bot Token
- Google Places API Key

## Installation 🚀

1. Clone the repository:
```bash
git clone <repository-url>
cd Chatbot_Discord
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your tokens:
```env
DISCORD_TOKEN=your_discord_token_here
GOOGLE_API_KEY=your_google_api_key_here
```

## Project Structure 📁

```
Chatbot_Discord/
├── bot.py              # Main bot file
├── config.py           # Configuration and constants
├── requirements.txt    # Project dependencies
├── utils/
│   ├── logger.py      # Logging configuration
│   └── places.py      # Place information utilities
└── views/
    └── place_view.py  # Discord UI components
```

## Usage 💡

1. Start the bot:
```bash
python bot.py
```

2. Available Commands:
- `!danang` - Opens the interactive place selection menu
- `!askdanang [question]` - Ask a specific question about Da Nang
- `!language [en|vi]` - Set your preferred language (English or Vietnamese)
- `!help_danang` - Display help information

### Example Questions
- "Tell me about Dragon Bridge"
- "What's the best time to visit Da Nang?"
- "What are the local traditions?"
- "What's near Da Nang?"

## Features in Detail 🔍

### Interactive Place Selection
The bot provides a dropdown menu with popular places in Da Nang. Each place entry includes:
- Detailed description
- Location on Google Maps
- Photos (when available)
- Ratings and reviews
- Interactive reactions

### Smart Follow-up Suggestions
After providing information about a place or topic, the bot suggests related information:
- Other nearby places
- Related traditions
- Best time to visit
- Surrounding attractions

### Language Support
The bot supports both English and Vietnamese:
- Switch languages using `!language en` or `!language vi`
- All information and UI elements are available in both languages
- Automatic language detection for greetings

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Google Places API for real-time place information
- Discord.py for the Discord bot framework
- The Da Nang tourism community for information and support

## Support 💬

If you encounter any issues or have questions, please open an issue in the repository.
