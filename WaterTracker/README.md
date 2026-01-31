# Water Tracker App - Hydration Check-in

A cool water drinking tracker app with a red and black tech-style design to help you develop healthy hydration habits.

## Features

- ✅ **One-tap Check-in**: Simple and quick water intake recording
- 📊 **Real-time Statistics**: Display today's water intake and goal completion
- 📝 **Record List**: Detailed display of each drinking time
- 🎯 **Health Reminders**: Smart tips on how much more water you need
- 🎨 **Cool Interface**: Red and black tech style with outstanding visual effects
- 💾 **Data Persistence**: Save data using localStorage
- 📅 **Date Display**: Real-time display of current date and day of week

## Tech Stack

- **Framework**: Apache Cordova
- **Frontend**: HTML5 + CSS3 + JavaScript
- **Platform**: Android (expandable to iOS)
- **Storage**: localStorage

## Installation and Build

### Prerequisites

1. **Node.js** (v14 or higher)
2. **Cordova CLI**
   ```bash
   npm install -g cordova
   ```

3. **Android Development Environment**:
   - Java JDK 8 or higher
   - Android SDK
   - Gradle

### Environment Setup

1. Install Android SDK:
   ```bash
   # Download Android Studio or Android SDK Command-line Tools
   # Set environment variables
   export ANDROID_HOME=$HOME/Android/Sdk
   export PATH=$PATH:$ANDROID_HOME/tools
   export PATH=$PATH:$ANDROID_HOME/platform-tools
   ```

2. Verify environment:
   ```bash
   cordova requirements
   ```

### Build Steps

1. **Navigate to project directory**:
   ```bash
   cd WaterTracker
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Add Android platform** (if not already added):
   ```bash
   cordova platform add android
   ```

4. **Build APK**:
   ```bash
   # Debug version
   cordova build android

   # Release version
   cordova build android --release
   ```

5. **Run on device**:
   ```bash
   # Connect Android device and enable USB debugging
   cordova run android
   ```

6. **Run on emulator**:
   ```bash
   cordova emulate android
   ```

### Quick Build Script

Use the provided build script for easier deployment:

```bash
./build.sh
```

### Browser Preview

For development, you can preview the app in a browser:

```bash
cd www
python3 -m http.server 8080
# Then visit http://localhost:8080 in your browser
```

## Usage

1. **Open App**: Shows current date and water statistics
2. **Check-in**: Tap the red "喝水打卡" (Water Check-in) button to record drinking
3. **View Records**: List below shows all drinking times for today
4. **View Progress**: Top section displays today's water intake and goal completion
5. **Clear Records**: Tap "清空" (Clear) button to remove all today's records

## Health Standard

- **Daily Goal**: 8 glasses of water
- **Progress Bar**: Real-time completion percentage
- **Completion Message**: Congratulations message when goal is reached

## Design

### Color Scheme
- **Primary**: Black (#000000, #0a0a0a, #1a0000)
- **Accent**: Red (#ff0000, #ff3333, #ff6666)
- **Text**: White (#ffffff) and Gray (#999999, #666666)

### Design Features
- Gradient background for tech feel
- Glow effects and shadows for visual impact
- Smooth animation transitions
- Responsive button feedback
- Custom scrollbar styling

## Data Storage

The app uses `localStorage` to store data:
- **Storage Key**: `waterTrackerData`
- **Data Structure**:
  ```json
  {
    "date": "2026-01-31",
    "records": [
      {
        "time": "09:30:15",
        "timestamp": 1738315815000
      }
    ]
  }
  ```
- **Auto Reset**: Records automatically clear on first open after midnight

## Compatibility

- **Android**: 5.0 (API 21) and above
- **Browsers**: Chrome, Firefox, Safari, Edge (modern browsers)

## Customization

### Change Daily Goal

Edit `www/js/index.js`:
```javascript
const DAILY_GOAL = 8; // Change to your desired number of glasses
```

### Change Colors

Edit `www/css/index.css` and replace color codes:
- Red: `#ff0000`, `#ff3333`, `#ff6666`
- Black: `#000000`, `#0a0a0a`, `#1a0000`

## Troubleshooting

### Build Fails
- Ensure all prerequisites are installed
- Run `cordova requirements` to check environment
- Clean and rebuild: `cordova clean && cordova build android`

### App Won't Start
- Check if USB debugging is enabled on Android device
- Verify device connection: `adb devices`
- View logs: `adb logcat`

### Data Loss
- Check if browser/app cleared cache
- localStorage data is stored in app's private directory

## Future Plans

- [ ] Custom daily goal settings
- [ ] Support different cup sizes (small, medium, large)
- [ ] Drinking reminder notifications
- [ ] Historical data statistics and charts
- [ ] Multi-language support
- [ ] iOS platform support

## License

This project is open source under the Apache License 2.0.

---

**Enjoy a healthy hydration lifestyle! 💧**
