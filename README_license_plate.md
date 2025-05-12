# License Plate Recognition and Discord Alert System 🚗 (third Project)

## English

### Project Overview
This project implements a real-time license plate recognition system that monitors vehicles, identifies their license plates, and sends alerts to Discord when unauthorized vehicles are detected.

### Features
- Real-time license plate detection and recognition
- Automatic image capture of vehicles
- Instant Discord notifications with captured images and plate numbers
- Whitelist-based authorization system
- Configurable detection thresholds and alert settings

### Prerequisites
- Python 3.8+
- Webcam or IP camera
- Discord Bot Token
- OpenCV and EasyOCR libraries
- Sufficient lighting for clear plate capture

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/license-alert-bot.git
cd license-alert-bot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Configure your Discord bot:
   - Create a new Discord application at https://discord.com/developers/applications
   - Create a bot and get the token
   - Add the token to `config.py`

### Project Structure
```
license-alert-bot/
├── license_recognizer.py    # Main license plate detection script
├── whitelist.json          # Authorized license plates database
├── discord_bot.py          # Discord bot implementation
├── config.py               # Configuration settings
└── captured_frames/        # Directory for storing detected plates
```

### Usage
1. Set up your whitelist:
   - Edit `whitelist.json` to add authorized license plates
   - Format: JSON array of plate numbers

2. Start the monitoring system:
```bash
python license_recognizer.py
```

3. The system will:
   - Initialize the camera
   - Start monitoring for vehicles
   - Detect and read license plates
   - Compare with whitelist
   - Send Discord alerts for unauthorized vehicles

### Configuration
Edit `config.py` to customize:
- Discord bot token
- Detection confidence threshold
- Alert message format
- Camera settings
- Recognition language settings
- Storage settings for captured frames

---

## Tiếng Việt

### Tổng Quan Dự Án
Dự án này triển khai hệ thống nhận diện biển số xe thời gian thực, giám sát phương tiện, xác định biển số và gửi cảnh báo qua Discord khi phát hiện xe không được phép.

### Tính Năng
- Nhận diện và đọc biển số xe thời gian thực
- Tự động chụp ảnh phương tiện
- Gửi thông báo tức thì qua Discord kèm ảnh và số biển
- Hệ thống phân quyền dựa trên danh sách trắng
- Có thể cấu hình ngưỡng phát hiện và cài đặt cảnh báo

### Yêu Cầu Hệ Thống
- Python 3.8+
- Webcam hoặc camera IP
- Token Discord Bot
- Thư viện OpenCV và EasyOCR
- Điều kiện ánh sáng đủ để chụp rõ biển số

### Cài Đặt
1. Clone repository:
```bash
git clone https://github.com/yourusername/license-alert-bot.git
cd license-alert-bot
```

2. Cài đặt các gói cần thiết:
```bash
pip install -r requirements.txt
```

3. Cấu hình Discord bot:
   - Tạo ứng dụng Discord mới tại https://discord.com/developers/applications
   - Tạo bot và lấy token
   - Thêm token vào `config.py`

### Cấu Trúc Dự Án
```
license-alert-bot/
├── license_recognizer.py    # Script nhận diện biển số chính
├── whitelist.json          # Cơ sở dữ liệu biển số được phép
├── discord_bot.py          # Triển khai Discord bot
├── config.py               # Cài đặt cấu hình
└── captured_frames/        # Thư mục lưu ảnh biển số đã chụp
```

### Sử Dụng
1. Thiết lập danh sách trắng:
   - Chỉnh sửa `whitelist.json` để thêm các biển số được phép
   - Định dạng: Mảng JSON các số biển

2. Khởi động hệ thống giám sát:
```bash
python license_recognizer.py
```

3. Hệ thống sẽ:
   - Khởi tạo camera
   - Bắt đầu giám sát phương tiện
   - Phát hiện và đọc biển số
   - So sánh với danh sách trắng
   - Gửi cảnh báo Discord cho xe không được phép

### Cấu Hình
Chỉnh sửa `config.py` để tùy chỉnh:
- Token Discord bot
- Ngưỡng tin cậy phát hiện
- Định dạng tin nhắn cảnh báo
- Cài đặt camera
- Cài đặt ngôn ngữ nhận diện
- Cài đặt lưu trữ ảnh đã chụp

## License
MIT License 