# 🌐 Codespaces 访问指南

## ✅ 正确的访问地址

您在 GitHub Codespaces 环境中，请使用以下 URL 访问应用:

### 方法 1: 使用 Codespaces 转发 URL (推荐)

```
https://stunning-palm-tree-7v4766vx64gv3x646-8080.app.github.dev
```

### 方法 2: 通过 Codespaces 端口面板

1. 在 VS Code 中，点击底部的 **"端口"** (PORTS) 标签
2. 找到端口 **8080**
3. 点击 **"在浏览器中打开"** 图标 (地球图标)
4. 或右键点击端口 → **"在浏览器中打开"**

---

## 🔧 端口可见性设置

如果端口不可见，请设置为公开:

1. 在 **"端口"** 标签中找到端口 8080
2. 右键点击 → **"端口可见性"** → **"公开"**
3. 然后点击 **"在浏览器中打开"**

---

## 📊 服务器状态

- **状态**: ✅ 运行中
- **端口**: 8080
- **进程**: live-server (PID: 22073)
- **热重载**: ✅ 启用
- **本地测试**: ✅ 正常 (HTTP 200 OK)

---

## 🚀 快速访问

### 选项 1: 直接访问 (推荐)
点击或复制此 URL:
```
https://stunning-palm-tree-7v4766vx64gv3x646-8080.app.github.dev
```

### 选项 2: 使用 VS Code 端口面板
1. 按 `Ctrl+J` 打开面板
2. 切换到 **"端口"** 标签
3. 找到 8080 端口
4. 点击地球图标打开

### 选项 3: 使用命令面板
1. 按 `Ctrl+Shift+P`
2. 输入 "Ports: Focus on Ports View"
3. 找到 8080 端口并打开

---

## ⚠️ 注意事项

### 为什么不能用 localhost:8080？

在 Codespaces 中:
- ❌ `localhost:8080` - 只能在容器内访问
- ❌ `127.0.0.1:8080` - 只能在容器内访问
- ✅ `https://[codespace-name]-8080.app.github.dev` - 可以在浏览器中访问

### 端口转发说明

GitHub Codespaces 会自动转发端口，但您需要:
1. 使用 Codespaces 提供的 URL
2. 或通过 VS Code 的端口面板访问

---

## 🔍 故障排除

### 问题: 端口面板中没有 8080

**解决**:
```bash
# 重启服务器
cd /workspaces/RUthirsty-cordova/WaterTracker
./dev-server.sh restart
```

### 问题: 访问 URL 显示 404

**解决**:
1. 检查服务器是否运行: `./dev-server.sh status`
2. 确认端口可见性设置为 "公开"
3. 刷新浏览器

### 问题: 页面加载很慢

**原因**: Codespaces 端口转发可能有延迟
**解决**: 等待几秒钟，或刷新页面

---

## 📱 移动设备访问

如果您想在手机上访问:

1. 确保端口 8080 设置为 **"公开"**
2. 在手机浏览器中访问:
   ```
   https://stunning-palm-tree-7v4766vx64gv3x646-8080.app.github.dev
   ```

---

## 🎯 验证服务器

服务器在容器内运行正常:
```bash
# 测试命令 (在终端中运行)
curl -I http://localhost:8080

# 应该返回: HTTP/1.1 200 OK
```

---

## 💡 开发提示

### 热重载仍然有效
- 修改 `www/` 目录中的文件
- 保存后浏览器会自动刷新
- 无需重启服务器

### 查看实时日志
```bash
./dev-server.sh follow
```

### 管理服务器
```bash
./dev-server.sh status   # 查看状态
./dev-server.sh restart  # 重启
./dev-server.sh stop     # 停止
```

---

## 🌟 总结

**正确的访问方式**:

1. ✅ 使用 Codespaces URL: `https://stunning-palm-tree-7v4766vx64gv3x646-8080.app.github.dev`
2. ✅ 或通过 VS Code 端口面板打开
3. ❌ 不要使用 `localhost:8080` (只在容器内有效)

**服务器状态**: ✅ 运行正常
**热重载**: ✅ 已启用
**准备就绪**: ✅ 可以访问

---

**立即访问**: https://stunning-palm-tree-7v4766vx64gv3x646-8080.app.github.dev
