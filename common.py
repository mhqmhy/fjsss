import sys,os
import pygame
#   公有的操作
# Music:控制游戏中的音乐
# Avatr:控制用户头像
# Cartoon:控制动画

class Music():
    def __init__(self):
        self.Path={
            'defalut':'path',
        }

    def loadMusic(self):
        pass

    def chgMusic(self):
        pass


    def turnUp(self):
        pass

    def turnDown(self):
        pass

class BackgroundMusic(Music): #继承自Music
    pass


class Avatar():

    def __init__(self):
        self.Path={
            'default':'',
        }

    def loadAvatr(self):
        pass