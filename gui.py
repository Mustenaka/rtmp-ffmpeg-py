# 导入所需模块
from tkinter import *
import tkinter as tk
from core import ffmpeg
from PIL import Image, ImageTk

import os
import threading


class Application():
    """
    gui显示类
    """

    def __init__(self):
        """
        初始话布局
        """
        self.windows = Tk()
        # 标题设置
        self.windows.title("推流小工具")
        self.windows.geometry("410x205")  # 大小
        
        # 图片大小
        self.canvas = tk.Canvas(
            self.windows, bg='green', height=200, width=200)
        # grid布局
        self.canvas.grid(column=0, columnspan=7, row=0, rowspan=7)
        # label设置
        Label(self.windows, text="文件地址").grid(
            column=7, row=0, columnspan=1, rowspan=1)
        self.input = Entry(self.windows)
        self.input.grid(column=8, row=0, columnspan=1, rowspan=1)

        Label(self.windows, text="推流地址").grid(
            column=7, row=1, columnspan=1, rowspan=1)
        self.output = Entry(self.windows)
        self.output.grid(column=8, row=1, columnspan=1, rowspan=1)

        Label(self.windows, text="推流地址").grid(
            column=7, row=1, columnspan=1, rowspan=1)
        self.output = Entry(self.windows)
        self.output.grid(column=8, row=1, columnspan=1, rowspan=1)

        Label(self.windows, text="帧数").grid(
            column=7, row=2, columnspan=1, rowspan=1)
        self.frame_num = Entry(self.windows)
        self.frame_num.grid(column=8, row=2, columnspan=1, rowspan=1)

        Label(self.windows, text="分辨率").grid(
            column=7, row=3, columnspan=1, rowspan=1)
        self.size = Entry(self.windows)
        self.size.grid(column=8, row=3, columnspan=1, rowspan=1)

        Label(self.windows, text="解码器").grid(
            column=7, row=4, columnspan=1, rowspan=1)
        self.decoder = Entry(self.windows)
        self.decoder.grid(column=8, row=4, columnspan=1, rowspan=1)

        Label(self.windows, text="编码器").grid(
            column=7, row=5, columnspan=1, rowspan=1)
        self.encoder = Entry(self.windows)
        self.encoder.grid(column=8, row=5, columnspan=1, rowspan=1)
        self.button = Button(text="开始推流", command=self.click)
        self.button.grid(column=7, row=6, columnspan=2)

    def click(self):
        """
        监听事件 开始推流
        :return:
        """
        # 获取实体中的数据
        frame_num = int(self.frame_num.get())
        size = self.size.get()
        ff = ffmpeg(self.input.get(), self.output.get())
        ff.set_scale(size)
        ff.set_encoder(self.encoder.get())
        # 解码器可为空
        if self.decoder.get() != '':
            ff.set_decoder(self.decoder.get())
        ff.set_frame_num(frame_num)
        ff.get_image()
        # 读取显示图片
        img = Image.open('./result.jpg')
        image_file = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, image=image_file)
        # 更新canvas
        self.canvas.update()
        self.canvas.after(10000)
        # 获取ffmpeg命令
        c = ff.run()
        # 创建线程 开始推流
        threading.Thread(target=os.system, args=(c,)).start()

    def run(self):
        """
        主线程 显示窗口
        :return:
        """
        self.windows.mainloop()



if __name__ == "__main__":
    Application().run()

