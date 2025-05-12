# Fire Detection and Discord Alert System 🔥 (first project)

## English

### Project Overview
This project implements a real-time fire and smoke detection system using computer vision and sends alerts to Discord when potential hazards are detected.

### Features
- Real-time fire and smoke detection using YOLOv8
- Automatic image capture when fire/smoke is detected
- Instant Discord notifications with captured images
- Configurable detection thresholds and alert settings

### Prerequisites
- Python 3.8+
- Webcam or IP camera
- Discord Bot Token
- CUDA-capable GPU (recommended for better performance)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/fire-alert-bot.git
cd fire-alert-bot
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
fire-alert-bot/
├── detect_fire.py      # Main detection script
├── fire_model.pt       # YOLO model for fire/smoke detection
├── discord_bot.py      # Discord bot implementation
├── config.py           # Configuration settings
└── requirements.txt    # Project dependencies
```

### Usage
1. Start the detection system:
```bash
python detect_fire.py
```

2. The system will:
   - Initialize the camera
   - Load the YOLO model
   - Start monitoring for fire/smoke
   - Send Discord alerts when detected

### Configuration
Edit `config.py` to customize:
- Discord bot token
- Detection confidence threshold
- Alert message format
- Camera settings

---

## Tiếng Việt

### Tổng Quan Dự Án
Dự án này triển khai hệ thống phát hiện lửa và khói thời gian thực sử dụng thị giác máy tính và gửi cảnh báo qua Discord khi phát hiện nguy hiểm.

### Tính Năng
- Phát hiện lửa và khói thời gian thực sử dụng YOLOv8
- Tự động chụp ảnh khi phát hiện lửa/khói
- Gửi thông báo tức thì qua Discord kèm ảnh chụp
- Có thể cấu hình ngưỡng phát hiện và cài đặt cảnh báo

### Yêu Cầu Hệ Thống
- Python 3.8+
- Webcam hoặc camera IP
- Token Discord Bot
- GPU hỗ trợ CUDA (khuyến nghị để tăng hiệu suất)

### Cài Đặt
1. Clone repository:
```bash
git clone https://github.com/yourusername/fire-alert-bot.git
cd fire-alert-bot
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
fire-alert-bot/
├── detect_fire.py      # Script phát hiện chính
├── fire_model.pt       # Model YOLO cho phát hiện lửa/khói
├── discord_bot.py      # Triển khai Discord bot
├── config.py           # Cài đặt cấu hình
└── requirements.txt    # Các gói phụ thuộc
```

### Sử Dụng
1. Khởi động hệ thống phát hiện:
```bash
python detect_fire.py
```

2. Hệ thống sẽ:
   - Khởi tạo camera
   - Tải model YOLO
   - Bắt đầu giám sát lửa/khói
   - Gửi cảnh báo Discord khi phát hiện

### Cấu Hình
Chỉnh sửa `config.py` để tùy chỉnh:
- Token Discord bot
- Ngưỡng tin cậy phát hiện
- Định dạng tin nhắn cảnh báo
- Cài đặt camera

## License
MIT License 