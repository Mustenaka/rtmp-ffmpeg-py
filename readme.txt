将项目路径添加到环境变量，将项目中的nginxnginx-1.7.11.3-Gryphon也添加到环境变量，可参考[环境变量参考.png]
第一步，首先安装vlc播放器
第二部，以管理员身份运行下cmd，并且输入nginx.exe -c conf\nginx-win-rtmp.conf     （启动RTMP-nginx服务）
第三步，运行gui.py代码，启动软件

推流地址写上rtmp://127.0.0.1:1935/live/home
文件地址选择一个在磁盘上的视频即可
帧数需要手动输入，可高可低（超过原视频帧数也没用）
解码器手动输入，默认可无
编码器手动输入，h264,libx264或者copy均可

推流之后,在vlc中打开媒体-网络串流，输入rtmp://127.0.0.1:1935/live/home
等待一小会的加载即可播放

python需要提前安装pillow库