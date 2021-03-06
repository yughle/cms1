#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/11/20 16:29 
# filename: captcha.py
# development_tool： PyCharm

import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

numbers="".join(map(str, range(10)))
chars="".join((numbers))

def create_validete_code(size=(120, 30),
                         chars=chars,
                         mode="RGB",
                         bg_color=(255, 255, 255),
                         fg_color=(255, 0, 0),
                         font_size=18,
                         font_type="STZHONGS.TTF",
                         length=4,
                         draw_points=True,
                         point_chance=2):
    """
    :param size:图片大小，格式（高， 宽）
    :param chars:格式字符串
    :param mode:图片模式，RGB模式
    :param bg_color:背景颜色， 默认为白色
    :param fg_color:前景色，验证码颜色
    :param font_size:验证码字体大小
    :param font_type:验证码字体格式
    :param length:验证码长度
    :param draw_points:是否画干扰点
    :param point_chance:干扰点出现的概率，大小范围[0,50]
    :return:
    """
    width, height=size
    #创建图形
    img= Image.new(mode, size, bg_color)
    draw=ImageDraw.Draw(img)
    
    def get_chars():
        """生成给定长度的字符串，返回列表格式"""
        return random.sample(chars, length)
    
    def create_points():
        """绘制干扰点"""
        chance=min(50, max(0, int(point_chance)))
        for w in range(width):
            for h in range(height):
                tmp=random.randint(0, 50)
                if tmp>50-chance:
                    draw.point((w, h), fill=(0, 0, 0))
    
    def create_strs():
        c_chars=get_chars()
        strs="%s" % "".join(c_chars)
        font=ImageFont.truetype(font_type, font_size)
        font_width, font_height=font.getsize(strs)
        draw.text(((width-font_width)/3, (height-font_height)/4),
                   strs,font=font, fill=fg_color)
        return strs
    
    if draw_points:
        create_points()
    strs=create_strs()
    params=[1-float(random.randint(1, 2))/100, 0, 0, 0, 1-float(random.randint(1, 10))/100,
            float(random.randint(1, 2))/500, 0.001, float(random.randint(1, 2))/500]
    img=img.transform(size, Image.PERSPECTIVE, params)
    img=img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, strs

