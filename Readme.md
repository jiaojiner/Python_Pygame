### 使用Python的Pygame模块实现简单小游戏
#### 环境安装
在python3.x中安装：

1、需要执行两个步骤：安装pygame依赖的库；下载并安装pygame。

2、执行下面的命令来安装pygame依赖的库
```
sudo apt-get install python3-dev mercurial
sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev﻿​
```
如果需要启用Pygame的一些高级功能，如添加声音的功能，可安装下面这些额外的库：
```
sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcodec-dev
sudo apt-get install python-numpy
```
 ﻿​   
 4、接下来，执行下面的命令来安装pygame：

 
```
pip3 -i https://pypi.douban.com/simple/ install pygame
```

5、安装完成后通过输入：
```
python3
import pygame
```
没有反应则表示导入成功。