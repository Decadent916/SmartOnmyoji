### 基础环境依赖

python 3.7+ （测试时使用的python 3.12.3）  [安装地址](https://www.python.org/downloads/windows/)

#### 安装第三方依赖

第一种方法： 手动依次执行安装

```bash
pip install pywin32
pip install opencv-python
pip install PyQt5
pip install PyAutoGUI
pip install pillow
```

第二种方法：按照requirements.txt记录的依赖一次性安装

```bash
pip install -r requirements.txt
```


### 运行

第一种方法：每次运行时启动python程序

```bash
python smart_onmyoji_start.py
```

第二种方法：将程序打包为exe安装包，安装为客户端使用（失效，安装后无法启动）

```bash
# 安装 pyinstaller 
pip install -U pyinstaller
# 打包为安装包
pyinstaller --distpath Release/ -w -i logo.ico --clean .\smart_onmyoji_start.py
```