# Scene Change Detection and Discord Alert System 📸 (Second Project)

## English

### Project Overview
This project implements a real-time scene change detection system that monitors for significant changes in a scene (such as objects being added or removed) and sends alerts to Discord when changes are detected.

### Features
- Real-time scene change detection using SSIM (Structural Similarity Index)
- Automatic image capture when significant changes are detected
- Instant Discord notifications with captured images
- Configurable change detection thresholds
- Baseline image comparison system

### Prerequisites
- Python 3.8+
- Webcam or IP camera
- Discord Bot Token
- OpenCV and scikit-image libraries

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/scene-change-bot.git
cd scene-change-bot
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
scene-change-bot/
├── scene_watcher.py    # Main scene monitoring script
├── discord_bot.py      # Discord bot implementation
├── config.py           # Configuration settings
└── baseline.jpg        # Reference image for comparison
```

### Usage
1. Set up your baseline image:
   - Place your reference image as `baseline.jpg`
   - This will be used as the initial comparison point

2. Start the monitoring system:
```bash
python scene_watcher.py
```

3. The system will:
   - Load the baseline image
   - Start monitoring the scene
   - Compare new frames with the baseline
   - Send Discord alerts when significant changes are detected

### Configuration
Edit `config.py` to customize:
- Discord bot token
- Change detection threshold (default: 0.85)
- Alert message format
- Camera settings
- Monitoring interval

---

## Tiếng Việt

### Tổng Quan Dự Án
Dự án này triển khai hệ thống phát hiện thay đổi khung cảnh thời gian thực, giám sát những thay đổi đáng kể trong khung cảnh (như đồ vật bị thêm vào hoặc mất đi) và gửi cảnh báo qua Discord khi phát hiện thay đổi.

### Tính Năng
- Phát hiện thay đổi khung cảnh thời gian thực sử dụng SSIM (Structural Similarity Index)
- Tự động chụp ảnh khi phát hiện thay đổi đáng kể
- Gửi thông báo tức thì qua Discord kèm ảnh chụp
- Có thể cấu hình ngưỡng phát hiện thay đổi
- Hệ thống so sánh với ảnh gốc

### Yêu Cầu Hệ Thống
- Python 3.8+
- Webcam hoặc camera IP
- Token Discord Bot
- Thư viện OpenCV và scikit-image

### Cài Đặt
1. Clone repository:
```bash
git clone https://github.com/yourusername/scene-change-bot.git
cd scene-change-bot
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
scene-change-bot/
├── scene_watcher.py    # Script giám sát chính
├── discord_bot.py      # Triển khai Discord bot
├── config.py           # Cài đặt cấu hình
└── baseline.jpg        # Ảnh gốc để so sánh
```

### Sử Dụng
1. Thiết lập ảnh gốc:
   - Đặt ảnh tham chiếu của bạn làm `baseline.jpg`
   - Ảnh này sẽ được sử dụng làm điểm so sánh ban đầu

2. Khởi động hệ thống giám sát:
```bash
python scene_watcher.py
```

3. Hệ thống sẽ:
   - Tải ảnh gốc
   - Bắt đầu giám sát khung cảnh
   - So sánh các frame mới với ảnh gốc
   - Gửi cảnh báo Discord khi phát hiện thay đổi đáng kể

### Cấu Hình
Chỉnh sửa `config.py` để tùy chỉnh:
- Token Discord bot
- Ngưỡng phát hiện thay đổi (mặc định: 0.85)
- Định dạng tin nhắn cảnh báo
- Cài đặt camera
- Khoảng thời gian giám sát

## License
MIT License 