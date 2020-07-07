import os

'''
本模块为ffmpeg模块
'''


class ffmpeg:
    """
    ffmpeg推流类
    """
    def __init__(self, input, output):
        """
        初始化函数
        :param input: 文件地址
        :param output: 推流地址
        """
        self.input = input
        self.output = output
        self.decoder =None
    def set_frame_num(self, num=20):
        """
        设置帧率
        :param num: 默认20
        :return:
        """
        self.frame_num = num

    def set_scale(self, size):
        """
        设置 输入视频大小
        :param size: '200x100'
        :return:
        """
        self.scale =size

    def set_encoder(self, encoder='h264'):
        """
        设置编码器
        :param encoder: ffmpeg支持
        :return:
        """
        self.encoder = encoder

    def set_decoder(self, decoder):
        """
        设置解码器
        :param decoder: ffmpeg支持
        :return:
        """
        self.decoder = decoder
    def get_image(self):
        """
        获取视频第1秒的图像并保存200x200大小的result.jpg
        :return:
        """
        os.popen("ffmpeg -i {} -y -f mjpeg -ss 3 -t 1 -s 400x400 result.jpg".format(self.input))
    def run(self):
        """
        解析参数
        :return:
        """
        # 编码器为空
        if self.decoder ==None:
            # ffmpeg参数
            commond ="ffmpeg -re -i {0} -s {1} -acodec aac -f flv -vcodec {2} -r {3} {4}".format(self.input,self.scale,
                                                                                 self.encoder,self.frame_num, self.output)
        else:

            commond = "ffmpeg -re -i {0} -s {1} -vcodec {2} -acodec aac -f flv -vcodec {3} -r {4} {5}".format(self.input,self.scale,self.decoder,
                                                                                 self.encoder,self.frame_num, self.output)
        # 返回命令参数
        return commond
