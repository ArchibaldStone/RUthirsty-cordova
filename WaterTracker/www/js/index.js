// Water Tracker App - Main JavaScript

// Constants
const DAILY_GOAL = 8; // 8 glasses per day
const STORAGE_KEY = 'waterTrackerData';

// App State
let waterRecords = [];
let todayDate = '';

// Wait for Cordova to be ready
document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady() {
    console.log('Running cordova-' + cordova.platformId + '@' + cordova.version);
    initApp();
}

// Initialize the app
function initApp() {
    updateDate();
    loadData();
    updateUI();
    setupEventListeners();
}

// Update date display
function updateDate() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const weekdays = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
    const weekday = weekdays[now.getDay()];

    todayDate = `${year}-${month}-${day}`;
    document.getElementById('dateDisplay').textContent = `${year}年${month}月${day}日 ${weekday}`;
}

// Load data from localStorage
function loadData() {
    try {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored) {
            const data = JSON.parse(stored);

            // Check if data is from today
            if (data.date === todayDate) {
                waterRecords = data.records || [];
            } else {
                // New day, reset records
                waterRecords = [];
                saveData();
            }
        }
    } catch (error) {
        console.error('Error loading data:', error);
        waterRecords = [];
    }
}

// Save data to localStorage
function saveData() {
    try {
        const data = {
            date: todayDate,
            records: waterRecords
        };
        localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    } catch (error) {
        console.error('Error saving data:', error);
    }
}

// Setup event listeners
function setupEventListeners() {
    document.getElementById('checkinBtn').addEventListener('click', addWaterRecord);
    document.getElementById('clearBtn').addEventListener('click', clearRecords);
}

// Add a water drinking record
function addWaterRecord() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    const timeString = `${hours}:${minutes}:${seconds}`;

    waterRecords.push({
        time: timeString,
        timestamp: now.getTime()
    });

    saveData();
    updateUI();

    // Add button animation feedback
    const btn = document.getElementById('checkinBtn');
    btn.style.transform = 'scale(0.95)';
    setTimeout(() => {
        btn.style.transform = 'scale(1)';
    }, 200);
}

// Clear all records
function clearRecords() {
    if (waterRecords.length === 0) {
        return;
    }

    if (confirm('确定要清空今日所有记录吗？')) {
        waterRecords = [];
        saveData();
        updateUI();
    }
}

// Update UI
function updateUI() {
    updateStats();
    updateRecordsList();
}

// Update statistics
function updateStats() {
    const count = waterRecords.length;
    const completionRate = Math.min(Math.round((count / DAILY_GOAL) * 100), 100);

    document.getElementById('todayCount').textContent = count;
    document.getElementById('completionRate').textContent = completionRate;
}

// Update records list
function updateRecordsList() {
    const recordsList = document.getElementById('recordsList');

    if (waterRecords.length === 0) {
        recordsList.innerHTML = '<div class="empty-state">暂无记录，开始喝水吧！</div>';
        return;
    }

    // Sort records by timestamp (newest first)
    const sortedRecords = [...waterRecords].sort((a, b) => b.timestamp - a.timestamp);

    let html = '';
    sortedRecords.forEach((record, index) => {
        html += `
            <div class="record-item">
                <div class="record-time">${record.time}</div>
                <div class="record-icon">💧</div>
            </div>
        `;
    });

    recordsList.innerHTML = html;
}

// If Cordova is not available (testing in browser), initialize directly
if (typeof cordova === 'undefined') {
    console.log('Running in browser mode');
    setTimeout(initApp, 100);
}
