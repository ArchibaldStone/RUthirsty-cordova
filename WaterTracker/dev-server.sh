#!/bin/bash

# Water Tracker - Hot Reload Development Server
# 喝水打卡 - 热重载开发服务器

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WWW_DIR="$SCRIPT_DIR/www"
LOG_FILE="/tmp/live-server.log"
PORT=8080

echo "================================"
echo "Water Tracker - Hot Reload Server"
echo "喝水打卡 - 热重载服务器"
echo "================================"
echo ""

# Function to check if server is running
check_server() {
    if pgrep -f "live-server" > /dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to start server
start_server() {
    if check_server; then
        echo "⚠️  Server is already running!"
        echo "服务器已在运行！"
        echo ""
        show_status
        return
    fi

    echo "🚀 Starting live-server with hot reload..."
    echo "启动热重载服务器..."
    cd "$WWW_DIR"
    nohup npx live-server --port=$PORT --host=0.0.0.0 --no-browser > "$LOG_FILE" 2>&1 &

    sleep 3

    if check_server; then
        echo "✅ Server started successfully!"
        echo "服务器启动成功！"
        echo ""
        show_status
    else
        echo "❌ Failed to start server"
        echo "服务器启动失败"
        echo ""
        echo "Check log: cat $LOG_FILE"
    fi
}

# Function to stop server
stop_server() {
    if ! check_server; then
        echo "⚠️  Server is not running"
        echo "服务器未运行"
        return
    fi

    echo "🛑 Stopping live-server..."
    echo "停止服务器..."
    pkill -f "live-server"
    sleep 1

    if ! check_server; then
        echo "✅ Server stopped successfully!"
        echo "服务器已停止！"
    else
        echo "❌ Failed to stop server"
        echo "停止失败"
    fi
}

# Function to restart server
restart_server() {
    echo "🔄 Restarting server..."
    echo "重启服务器..."
    stop_server
    sleep 2
    start_server
}

# Function to show status
show_status() {
    if check_server; then
        echo "📊 Server Status / 服务器状态"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "Status:  ✅ Running"
        echo "Port:    $PORT"
        echo "URL:     http://localhost:$PORT"
        echo "Dir:     $WWW_DIR"
        echo "Log:     $LOG_FILE"
        echo "PID:     $(pgrep -f 'live-server')"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        echo "🔥 Hot reload is enabled!"
        echo "热重载已启用！"
        echo ""
        echo "💡 Edit files in www/ and browser will auto-refresh"
        echo "编辑 www/ 目录中的文件，浏览器会自动刷新"
    else
        echo "📊 Server Status / 服务器状态"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "Status:  ❌ Not Running"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    fi
}

# Function to show logs
show_logs() {
    if [ -f "$LOG_FILE" ]; then
        echo "📋 Server Logs / 服务器日志"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        tail -20 "$LOG_FILE"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        echo "💡 Follow logs: tail -f $LOG_FILE"
    else
        echo "⚠️  Log file not found: $LOG_FILE"
    fi
}

# Main menu
case "${1:-}" in
    start)
        start_server
        ;;
    stop)
        stop_server
        ;;
    restart)
        restart_server
        ;;
    status)
        show_status
        ;;
    logs)
        show_logs
        ;;
    follow)
        echo "📋 Following logs (Ctrl+C to exit)..."
        tail -f "$LOG_FILE"
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status|logs|follow}"
        echo "用法: $0 {start|stop|restart|status|logs|follow}"
        echo ""
        echo "Commands / 命令:"
        echo "  start    - Start the server / 启动服务器"
        echo "  stop     - Stop the server / 停止服务器"
        echo "  restart  - Restart the server / 重启服务器"
        echo "  status   - Show server status / 显示状态"
        echo "  logs     - Show recent logs / 显示日志"
        echo "  follow   - Follow logs in real-time / 实时跟踪日志"
        echo ""
        show_status
        exit 1
        ;;
esac
