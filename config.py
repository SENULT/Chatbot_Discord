import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot Configuration
TOKEN = os.getenv('DISCORD_TOKEN')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
COMMAND_PREFIX = '!'

# API Configuration
GOOGLE_PLACES_API_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
GOOGLE_PLACES_PHOTO_URL = "https://maps.googleapis.com/maps/api/place/photo"

# Cache Configuration
CACHE_TTL = 3600  # 1 hour in seconds

# Da Nang Information (Supports English and Vietnamese)
DA_NANG_INFO = {
    'overview': {
        'en': (
            'Da Nang is the fourth largest city in Vietnam, located on the coast of the East Sea at the mouth of the Han River.'
            ' It is a major port city in Central Vietnam and one of five centrally-governed municipalities.'
            ' Da Nang is situated almost equidistant from Hanoi and Ho Chi Minh City and serves as the hub for three UNESCO World Heritage sites:'
            ' the Complex of Hue Monuments, Hoi An Ancient Town, and My Son Sanctuary.'
        ),
        'vi': (
            'Đà Nẵng là thành phố lớn thứ 4 ở Việt Nam, nằm trên bờ Biển Đông có cửa sông Hàn.'
            ' Đây là một trong những thành phố cảng có vị trí chiến lược của miền Trung Việt Nam và là một trong 5 thành phố trực thuộc Trung ương.'
            ' Đà Nẵng nằm ở trung độ đất nước, trên trục giao thông Bắc – Nam và là trung tâm của 3 di sản văn hóa thế giới:'
            ' Cố đô Huế, phố cổ Hội An và thánh địa Mỹ Sơn.'
        )
    },
    'places': {
        'marble_mountains': {
            'en': 'The Marble Mountains (Ngu Hanh Son) are five limestone hills named after the five elements. They feature caves, temples, and panoramic views of Da Nang.',
            'vi': 'Ngũ Hành Sơn (hay Núi Non Nước) là quần thể gồm 5 ngọn núi đá vôi được đặt tên theo ngũ hành. Nơi đây có nhiều hang động, chùa chiền và tầm nhìn toàn cảnh Đà Nẵng.'
        },
        'dragon_bridge': {
            'en': 'The Dragon Bridge is a modern architectural marvel that spans the Han River. It breathes fire and water every weekend night.',
            'vi': 'Cầu Rồng là một biểu tượng kiến trúc hiện đại bắc qua sông Hàn. Cầu phun lửa và phun nước vào các tối cuối tuần.'
        },
        'my_khe_beach': {
            'en': 'My Khe Beach is known as one of the most beautiful beaches in Vietnam, famous for its white sand and clear water.',
            'vi': 'Biển Mỹ Khê được mệnh danh là một trong những bãi biển đẹp nhất Việt Nam, nổi tiếng với bờ cát trắng mịn và làn nước trong xanh.'
        },
        'lady_buddha': {
            'en': 'The Lady Buddha statue at Linh Ung Pagoda is the tallest Buddha statue in Vietnam, standing at 67 meters.',
            'vi': 'Tượng Phật Bà Quan Âm tại Chùa Linh Ứng là tượng Phật cao nhất Việt Nam, cao 67 mét.'
        },
        'han_market': {
            'en': 'Han Market is a traditional market offering local food, souvenirs, and a glimpse into daily life in Da Nang.',
            'vi': 'Chợ Hàn là một khu chợ truyền thống bày bán các món ăn địa phương, quà lưu niệm và mang đến cái nhìn về đời sống hàng ngày tại Đà Nẵng.'
        }
    },
    'traditions': {
        'festivals': {
            'en': 'Da Nang hosts several festivals including the International Fireworks Festival and the Quan The Am Festival.',
            'vi': 'Đà Nẵng tổ chức nhiều lễ hội như Lễ hội Pháo hoa Quốc tế và Lễ hội Quán Thế Âm.'
        },
        'cuisine': {
            'en': 'Famous local dishes include Mi Quang (turmeric noodles), Banh Xeo (savory pancakes), and fresh seafood.',
            'vi': 'Các món ăn địa phương nổi tiếng gồm Mì Quảng, Bánh Xèo và hải sản tươi sống.'
        },
        'crafts': {
            'en': 'Traditional crafts include stone carving in Non Nuoc village and fishing net making.',
            'vi': 'Các nghề thủ công truyền thống gồm điêu khắc đá Non Nước và làm lưới đánh cá.'
        }
    },
    'surroundings': {
        'hoi_an': {
            'en': 'Hoi An Ancient Town is a UNESCO World Heritage site known for its well-preserved architecture, custom tailoring, and lantern-lit streets. It\'s about 30 km south of Da Nang.',
            'vi': 'Phố cổ Hội An là Di sản Văn hóa Thế giới được UNESCO công nhận, nổi tiếng với kiến trúc cổ kính được bảo tồn tốt, nghề may đo truyền thống và những con phố đèn lồng lung linh. Nơi đây cách Đà Nẵng khoảng 30 km về phía Nam.'
        },
        'hue': {
            'en': 'Hue is the former imperial capital of Vietnam, located about 100 km north of Da Nang. It\'s famous for its historic citadel, palaces, and tombs.',
            'vi': 'Huế là cố đô xưa của Việt Nam, cách Đà Nẵng khoảng 100 km về phía Bắc. Huế nổi tiếng với Kinh thành, cung điện và lăng tẩm mang đậm dấu ấn lịch sử.'
        },
        'my_son': {
            'en': 'My Son Sanctuary is a complex of ancient Hindu temples constructed by the Champa Kingdom. It\'s a UNESCO World Heritage site located about 70 km southwest of Da Nang.',
            'vi': 'Thánh địa Mỹ Sơn là một quần thể kiến trúc đền thờ Ấn Độ giáo cổ xưa của Vương quốc Chăm Pa. Đây là Di sản Văn hóa Thế giới được UNESCO công nhận, nằm cách Đà Nẵng khoảng 70 km về phía Tây Nam.'
        }
    },
    'visiting_info': {
        'best_time_to_visit': {
            'en': 'The best time to visit Da Nang is generally from March to May and September to October. The weather is pleasant, with less rain and comfortable temperatures. The summer months (June to August) are hot and humid but popular for beach activities. The rainy season is typically from November to February.',
            'vi': 'Thời điểm tốt nhất để du lịch Đà Nẵng thường là từ tháng 3 đến tháng 5 và từ tháng 9 đến tháng 10. Thời tiết lúc này dễ chịu, ít mưa và nhiệt độ thoải mái. Các tháng mùa hè (tháng 6 đến tháng 8) nóng và ẩm nhưng thích hợp cho các hoạt động biển. Mùa mưa thường kéo dài từ tháng 11 đến tháng 2.'
        }
    },
    'messages': {
        'select_place_prompt': {
            'en': 'Please select a place in Da Nang to learn more about it:',
            'vi': 'Vui lòng chọn một địa điểm ở Đà Nẵng để tìm hiểu thêm:'
        },
        'location_field': {
            'en': 'Location',
            'vi': 'Vị trí'
        },
        'rating_field': {
            'en': 'Rating',
            'vi': 'Đánh giá'
        },
        'reviews_text': {
            'en': 'reviews',
            'vi': 'đánh giá'
        },
        'general_intro': {
            'en': 'Hello {mention}! I can help you explore Da Nang.',
            'vi': 'Xin chào {mention}! Tôi có thể giúp bạn khám phá Đà Nẵng.'
        },
        'general_topics': {
            'en': 'You can ask me about:\n• Places to visit\n• Local traditions\n• Best time to visit\n• Surrounding attractions',
            'vi': 'Bạn có thể hỏi tôi về:\n• Các địa điểm tham quan\n• Truyền thống địa phương\n• Thời điểm tốt nhất để thăm\n• Các điểm tham quan lân cận'
        },
        'use_danang_command_hint': {
            'en': 'Or use `!danang` to see a menu of popular places!',
            'vi': 'Hoặc sử dụng `!danang` để xem menu các địa điểm phổ biến!'
        },
        'ask_command_no_query': {
            'en': 'Please provide a question about Da Nang. For example: "Tell me about Dragon Bridge"',
            'vi': 'Vui lòng đặt câu hỏi về Đà Nẵng. Ví dụ: "Kể cho tôi nghe về Cầu Rồng"'
        },
        'ask_command_no_info': {
            'en': 'I couldn\'t find specific information about that. Try using {command} to see available places!',
            'vi': 'Tôi không tìm thấy thông tin cụ thể về điều đó. Hãy thử sử dụng {command} để xem các địa điểm có sẵn!'
        },
        'generic_error': {
            'en': 'Sorry, something went wrong. Please try again later.',
            'vi': 'Xin lỗi, đã xảy ra lỗi. Vui lòng thử lại sau.'
        },
        'help_message': {
            'en': 'Here are the available commands:\n\n{command_danang} - Show the interactive place selection menu\n{command_askdanang} - Ask a question about Da Nang\n{command_language} - Set your preferred language (English or Vietnamese)',
            'vi': 'Đây là các lệnh có sẵn:\n\n{command_danang} - Hiển thị menu chọn địa điểm tương tác\n{command_askdanang} - Đặt câu hỏi về Đà Nẵng\n{command_language} - Đặt ngôn ngữ ưa thích của bạn (Tiếng Anh hoặc Tiếng Việt)'
        },
        'other_related_places_surroundings': {
            'en': 'Other places you might be interested in: {items}',
            'vi': 'Các địa điểm khác bạn có thể quan tâm: {items}'
        },
        'ask_about_traditions_visiting': {
            'en': 'Would you like to know about local traditions or the best time to visit?',
            'vi': 'Bạn có muốn biết về truyền thống địa phương hoặc thời điểm tốt nhất để thăm không?'
        },
        'other_related_traditions': {
            'en': 'Other traditions you might be interested in: {items}',
            'vi': 'Các truyền thống khác bạn có thể quan tâm: {items}'
        },
        'ask_about_places_surroundings_visiting': {
            'en': 'Would you like to know about other places, surrounding attractions, or the best time to visit?',
            'vi': 'Bạn có muốn biết về các địa điểm khác, các điểm tham quan lân cận hoặc thời điểm tốt nhất để thăm không?'
        },
        'ask_about_places_traditions_surroundings_after_visiting': {
            'en': 'Would you like to know about specific places, traditions, or surrounding attractions?',
            'vi': 'Bạn có muốn biết về các địa điểm cụ thể, truyền thống hoặc các điểm tham quan lân cận không?'
        },
        'ask_about_details_after_overview': {
            'en': 'Would you like to know about specific places, traditions, surrounding attractions, or the best time to visit?',
            'vi': 'Bạn có muốn biết về các địa điểm cụ thể, truyền thống, các điểm tham quan lân cận hoặc thời điểm tốt nhất để thăm không?'
        },
        'generic_follow_up_fail': {
            'en': 'I\'m not sure what else to tell you about that. Try asking about something else!',
            'vi': 'Tôi không chắc chắn còn điều gì khác để nói về điều đó. Hãy thử hỏi về điều khác!'
        },
        'no_last_topic_follow_up': {
            'en': 'I\'m not sure what you\'d like to know more about. Try asking about a specific place or topic!',
            'vi': 'Tôi không chắc chắn bạn muốn biết thêm về điều gì. Hãy thử hỏi về một địa điểm hoặc chủ đề cụ thể!'
        }
    }
}