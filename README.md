# SmartOmmyoji

> 为了解放双手，特意学了python，虽然已经有很多大佬写了类似的脚本，但自己主要是利用这个项目学习python，所以有很多被注释的代码片段和注释啥的（大部分代码都可以删除，其实100行左右就能实现），写完之后，基本了解了opencv的目标检测方法和一些图像处理的方法，以及图像处理的一些原理，包括期间还看了神经网络和深度学习的一些知识（虽然没用上，不过以后可以用在砸百鬼上）

### 依赖库
- Gooey
- pywin32
- opencv-python
- numpy

### 使用
- 先安装python3.7,再安装上述依赖库
- 管理员身份运行 smart_onmyoji_gooey_ui.py
- 使用模板匹配时，不要调分辨率，如果要调分辨率，需要重新截图，放到/img目录的对应文件夹下面
- 支持电脑后台点击，但好像应该不支持安卓模拟器（比如网易UU），~~不过可以用scrcpy或qtscrcpy手机投屏连电脑，需要重新截图（opencv的模板匹配有点坑，大小方向一改变就匹配不到了。。。。）~~
- 支持手机USB连接电脑，需要打开手机调试模式，使用 安卓-ADB 模式时，可以使用特征点匹配方式，不过有点慢，要不就重新截图替换/img目录下的全部图片
- 特征点匹配方法适用于一个页面没有多个相同的待检测目标，而且待检测目标与周围差异比较大的情况，否则会不准确（就使用模板匹配方法）
- 原理是定时截图，然后找到图片坐标，然后随机延迟并点击附近随机坐标
- 除了阴阳师，也可以其他点点点的游戏，比如连手机抢微信红包啥的~
- 只要每天不刷满300次，理论上不会收到鬼使黑的信

### 计划
- [x] 支持abd模式，电脑连手机自动截图，
- [x] 支持切换选择匹配模式，特征点匹配（自适应分辨率，不用重新截图，但速度慢，而且不准确）、模板匹配（速度更快，更精确）
- [x] 加载图片时记录所有图片的特征信息，优化识别速度
- [x] 支持压缩图片以提升脚本识别速度，默认为1，不压缩
- [x] 所有图片转灰度图，并保存在内存里，识别速度快多了
- [ ] 使用QT5重构UI界面
- [ ] 增加超时停止脚本的功能
- [ ] 优化百鬼夜行的选式神和砸豆子逻辑
- [ ] 模拟真实点击（某时间一顿猛戳，每隔一段时间随机等待30秒到5分钟）
- [ ] 增加御灵、地域鬼王、逢魔、秘闻副本等场景
