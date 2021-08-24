# blivechat GUI

用于 [blivechat]( https://github.com/xfgryujk/blivechat ) 的图形界面。

有朋友在搞 Vtuber， blivechat 类似的项目能通过自定义 CSS 的方式在 OBS 上添加一个非常好看的聊天栏。但是想要在桌面端看到弹幕的话得要再开一个浏览器页面，十分不方便。于是就想写一个背景透明的浮窗浏览器。  
挺喜欢自带服务端的 blibechat， 但是启动后的 Console 窗口不仅丑，还容易误操作，所以就花了点时间写了个UI。 
但是写完了 [xfgryujk]( https://github.com/xfgryujk ) 觉得这个 [PR]( https://github.com/xfgryujk/blivechat/pull/50 ) 太大，只能独立出来，于是就有了这个项目。

## 特性

* 添加了控制台图形窗口；
* 添加了托盘图标，控制台关闭自动缩小到托盘窗口~~防手滑~~；
* 添加网页悬浮窗，可以当成桌面弹幕姬来用：
  * 可以配置屏蔽，就像 bilivechat 自动弹窗的管理页面一样；
  * 可以添加自定义 CSS；
  * CSS 设置的不透明度会正常生效；
  * 可调整页面位置、大小和缩放；
* 没有改动 blivechat 原有的代码，维护成本低；
* blivechat 原先的命令行参数会正常生效。

## 使用方法

> 理论上来说，只要启动时 `--host` 和 `--port` 配置合理，网络的其他计算机能通过这个端口连接进来，那也是可以像 blivechat 那样搭成服务器供别人使用。但既然打算去搭建服务器了，[Docker]( https://github.com/xfgryujk/blivechat#%E5%9B%9Bdocker%E8%87%AA%E5%BB%BA%E6%9C%8D%E5%8A%A1%E5%99%A8 )不香嘛？

### 一、发布版

1. 下载[发布版]( https://github.com/sileence114/blivechatGUI/releases )（仅提供x64 Windows版）
2. 双击 blivechatGUI.exe 运行，也可以像 blivechat 那样添加命令行参数。
  ```bat
  blivechatGUI.exe --host 127.0.0.1 --port 12450
  ```

### 二、源代码版

0. 由于使用了git子模块，clone时需要加上`--recursive`参数：
  > blivechatGUI 包含了 blivechat， blivechat 包含了 blivedm。
  ```bat
  git clone --recursive https://github.com/sileence114/blivechatGUI.git
  ```
  如果已经clone，拉子模块的方法：
  ```bat
  git submodule update --init --recursive
  ```
1. 安装依赖（Python 3.6+）：
  ```bat
  pip install -r requirements.txt
  ```
2. 将 blivechat 的代码提取到项目根目录：
  > 由于 blivechat 中并没有将模块文件夹定义为包，所以 blivechatGUI 的文件需要与 blivechat 的入口文件在同一个目录中。
  ```bat
  python extract.py
  ```
3. 编译前端（需要安装Node.js）：
  ```bat
  cd frontend
  npm i
  npm run build
  ```
4. 运行  
如果想要看 Console 窗口， 请将下面命令中的 `pythonw` 替换为 `python`。
  ```bat
  pythonw gui.py
  ```
或者可以指定host和端口号：
  ```bat
  pythonw gui.py --host 127.0.0.1 --port 12450
  ```

## 启动命令行参数

blivechatGUI 支持 blivechat 的所有命令行参数：

* `--host 127.0.0.1` 设置监听地址为 127.0.0.1
* `--port 12450` 设置监听端口为 12450
* `--debug` Debug 模式，将显示更多的信息

此外，可以参考 [Chromium 命令行开关]( https://peter.sh/experiments/chromium-command-line-switches/ )，添加需要的参数用以修改浮窗浏览器。  
下面这些参数已被默认添加：  

* `--disable-web-security` 禁用网页安全机制：跨域
* `--allow-insecure-websocket-from-https-origin` 允许https页面访问不加密的websocket： https页面使用ws消息链连接

下面的参数在 Debug 模式自动添加：

* `--remote-debugging-port=9222` 设置 DevTools 远程调试端口为 9222

## CSS 代码段

若有需要，可以将下面的 CSS 复制下来，记事本中粘贴，保存为后缀名为 `.css` 的文件，在“悬浮窗设置”-“额外的CSS”中添加。

* 背景透明
若没有自定义 CSS，悬浮窗的背景为白色属于正常现象，添加这段 CSS 可变透明。这段代码会覆盖其他 CSS 的背景色设置，添加了其他 CSS 时慎用。
  ```css
  body{
    background-color: transparent !important;
  }
  yt-live-chat-renderer {
    background-color: transparent !important;
  }
  ```
* 显示虚线边框
  ```css
  body{
    border: dotted;
  }
  ```

## PyInstaller 打包

0. 按照[前文所述]( https://github.com/sileence114/blivechatGUI#%E4%BA%8C%E6%BA%90%E4%BB%A3%E7%A0%81%E7%89%88 )，安装源代码版，确保其正常运行
1. 安装 PyInstaller，过程略
2. cd 到项目根目录，打包
 ```bat
 pyinstaller -D -w -i frontend\dist\favicon.ico -n blivechatGUI --add-data=".\data\*;.\data" --add-data=".\frontend\dist;.\frontend\dist" --add-data=".\log;.\log" gui.py
 ```
3. 项目中出现了 `dist` 文件夹，将文件夹 `dist\blivechatGUI\PyQt5\Qt` 与 `dist\blivechatGUI\PyQt5\Qt5` 合并（合并后文件夹为 `Qt5`）。 
