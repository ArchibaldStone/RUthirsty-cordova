# 🔥 热重载开发环境 - Hot Reload Development

## ✅ 当前状态

**服务器**: live-server (带热重载)
**状态**: ✅ 运行中
**端口**: 8080
**访问地址**: http://localhost:8080
**进程**: 后台运行 (nohup)
**日志文件**: /tmp/live-server.log

---

## 🚀 访问应用

直接在浏览器中打开:
```
http://localhost:8080
```

---

## 🔥 热重载功能

live-server 会自动监控文件变化，当您修改以下文件时，浏览器会自动刷新:

- `www/index.html` - HTML 结构
- `www/css/index.css` - 样式文件
- `www/js/index.js` - JavaScript 逻辑
- 其他 www 目录下的文件

**无需手动刷新浏览器！**

---

## 📝 开发工作流

### 1. 修改代码
编辑任何文件，例如:
```bash
# 修改样式
vim /workspaces/RUthirsty-cordova/WaterTracker/www/css/index.css

# 修改功能
vim /workspaces/RUthirsty-cordova/WaterTracker/www/js/index.js

# 修改界面
vim /workspaces/RUthirsty-cordova/WaterTracker/www/index.html
```

### 2. 保存文件
保存后，live-server 会自动检测变化

### 3. 自动刷新
浏览器会自动刷新，显示最新内容

---

## 🔧 服务器管理

### 查看服务器状态
```bash
ps aux | grep live-server | grep -v grep
```

### 查看日志
```bash
tail -f /tmp/live-server.log
```

### 停止服务器
```bash
pkill -f "live-server"
```

### 重启服务器
```bash
# 停止
pkill -f "live-server"

# 启动
cd /workspaces/RUthirsty-cordova/WaterTracker/www
nohup npx live-server --port=8080 --host=0.0.0.0 --no-browser > /tmp/live-server.log 2>&1 &
```

---

## 📊 服务器配置

当前配置:
- **端口**: 8080
- **主机**: 0.0.0.0 (允许外部访问)
- **根目录**: /workspaces/RUthirsty-cordova/WaterTracker/www
- **浏览器**: 不自动打开 (--no-browser)
- **日志**: /tmp/live-server.log
- **运行模式**: 后台 (nohup)

---

## 🎯 开发建议

### 实时预览
1. 在浏览器中打开 http://localhost:8080
2. 打开浏览器开发者工具 (F12)
3. 修改代码并保存
4. 观察浏览器自动刷新

### 调试技巧
- 使用浏览器控制台查看 JavaScript 错误
- 使用 Elements 面板检查 HTML 结构
- 使用 Network 面板查看资源加载
- 使用 Application 面板查看 localStorage

### 移动端测试
在浏览器开发者工具中:
1. 按 F12 打开开发者工具
2. 点击设备工具栏图标 (Ctrl+Shift+M)
3. 选择移动设备模拟器
4. 测试响应式设计

---

## 🔍 常见问题

### Q: 浏览器没有自动刷新？
A: 检查:
1. live-server 是否正在运行
2. 文件是否真的保存了
3. 浏览器控制台是否有错误

### Q: 端口 8080 被占用？
A: 更改端口:
```bash
pkill -f "live-server"
cd /workspaces/RUthirsty-cordova/WaterTracker/www
nohup npx live-server --port=3000 --host=0.0.0.0 --no-browser > /tmp/live-server.log 2>&1 &
```

### Q: 如何查看实时日志？
A: 使用 tail 命令:
```bash
tail -f /tmp/live-server.log
```

### Q: 服务器崩溃了？
A: 查看日志并重启:
```bash
cat /tmp/live-server.log
# 然后重启服务器
```

---

## 📱 测试清单

使用热重载测试以下功能:

- [ ] 修改标题文字 - 自动刷新
- [ ] 修改按钮颜色 - 自动刷新
- [ ] 修改 JavaScript 逻辑 - 自动刷新
- [ ] 添加新的 CSS 样式 - 自动刷新
- [ ] 修改进度条动画 - 自动刷新

---

## 🎨 快速修改示例

### 修改主题色
编辑 `www/css/index.css`:
```css
/* 将红色改为蓝色 */
/* 搜索 #ff0000 替换为 #0066ff */
/* 搜索 #ff3333 替换为 #3399ff */
/* 搜索 #ff6666 替换为 #66ccff */
```
保存后浏览器自动刷新！

### 修改每日目标
编辑 `www/js/index.js`:
```javascript
const DAILY_GOAL = 10; // 从 8 改为 10
```
保存后浏览器自动刷新！

### 修改标题
编辑 `www/index.html`:
```html
<h1 class="app-title">
    <span class="icon">💧</span>
    健康饮水助手  <!-- 修改标题 -->
</h1>
```
保存后浏览器自动刷新！

---

## 🌟 优势

相比普通 HTTP 服务器:
- ✅ **自动刷新** - 无需手动刷新浏览器
- ✅ **实时预览** - 修改立即可见
- ✅ **提高效率** - 节省开发时间
- ✅ **文件监控** - 自动检测变化
- ✅ **开发友好** - 专为开发设计

---

## 📌 快速命令

```bash
# 查看状态
ps aux | grep live-server | grep -v grep

# 查看日志
tail -f /tmp/live-server.log

# 停止服务器
pkill -f "live-server"

# 重启服务器
cd /workspaces/RUthirsty-cordova/WaterTracker/www && \
nohup npx live-server --port=8080 --host=0.0.0.0 --no-browser > /tmp/live-server.log 2>&1 &

# 测试访问
curl -I http://localhost:8080
```

---

**当前状态**: ✅ live-server 运行中
**访问地址**: http://localhost:8080
**热重载**: ✅ 已启用
**后台运行**: ✅ 是 (nohup)

**开始开发吧！修改代码，浏览器会自动刷新！** 🔥
