# -*- coding: gbk -*-

"""have a nice day.

@author: Khan,ChenJie
@contact:
@time: 2020/5/15 15:34
@file: game.py
@desc: ��Ϸ���������
"""



import sys
import pygame
from cell_list import CellList


GRAY = (119, 136, 153)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
WHITE = (255, 255, 255)

# ��ʼ��gameģ��
pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load("north.mp3")    # ��������
# pygame.mixer.music.set_volume(0.2)      # ��������Ϊ0.2
# pygame.mixer.music.play()               # ��������
pygame.display.set_caption("������Ϸ")


class Game:
    """Game.

    ��Ϸ���������
    """

    screen = None

    def __init__(self, width, height):
        """���캯��.

        @param width: screen���
        @param height: screen�߶�
        """
        self.screen = None
        self.num = 0
        # ��Ļ���
        self.width = width
        self.height = height
        #  ������Ļ
        self.set_height_width(width, height)
        self.str_start = True
        self.set_screen_color(GRAY)
        # ʱ��
        self.clock = pygame.time.Clock()
        # ƽ�����
        self.balance = 1

    def set_height_width(self, width, height):
        """���ý���Ĵ����С.

        @param width: screen���
        @param height: screen�߶�
        @return: None
        """
        self.screen = pygame.display.set_mode([width, height])

    def set_screen_color(self, color):
        """���ñ�����ɫ.
        
        @param color: rgb��ʽ����ɫ��ʾcolor
        @return: None
        """
        self.screen.fill(color)

    def set_time(self, times):
        """���ý���ˢ��ʱ��.

        @param times: ʱ����
        @return: None
        """
        self.clock.tick(times)  # ÿ��ѭ��1��


    def set_cell_num(self, num):
        """������������ɱ߳��������������ݸ�cell_list����2ά����.

        @param num: ��������ı߳�
        @return: None
        """
        self.cell_list = CellList(int(num))
        self.cell_list.set_example()

    def draw_cell(self):
        """���Ƶ�ǰ״̬�������ڵ�ϸ��,0-����,1-���.

        @return: None
        """
        # x y  �� ��
        cell_list = self.cell_list.get_cell_list()
        length = int(600 / self.num+1)
        for i in range(1, self.num+1):
            for j in range(1, self.num+1):
                if cell_list[i][j] == 1:
                    pygame.draw.rect(self.screen, BLACK,
                                     [i*(length+1)+10, j*(length+1)+10, length, length])
                else:
                    pygame.draw.rect(self.screen, WHITE,
                                     [i*(length+1)+10, j*(length+1)+10, length, length])

    def draw_text(self, dd_num, flag=False):
        """���ƽ����ϵ����������Ϣ.

        @param dd_num: ��������
        @param flag: �Ƿ�ﵽƽ��״̬��Ĭ��ΪFalse
        @return: ���ص�ǰ״̬flag
        """
        # ��������
        text_font = pygame.font.Font(r"C:\Windows\Fonts\STHUPO.TTF", 30)
        # True = �����
        # (255,255,255) = ʹ�ð�ɫ����
        # ����ֵtext_surface = ����Ҫ���Ƶ����ֱ���
        text_surface = text_font.render("��ǰ���������� "+str(dd_num), True, (255, 255, 255))
        str_balance = "" if not flag else str(self.balance)
        text_surface3 = text_font.render("ƽ������� " + str_balance, True, (255, 255, 255))
        self.screen.blit(text_surface3, (1000, 250))

        str_flag = "��" if flag else "��"
        text_surface2 = text_font.render("ƽ��״̬�� " + str_flag, True, (255, 255, 255))

        # ����������(900,200)λ��
        self.screen.blit(text_surface, (1000, 200))
        self.screen.blit(text_surface2, (1000, 300))

        pygame.draw.rect(self.screen, BLUE, [1140, 100, 150, 80])
        self.screen.blit(text_font.render("����߳���"+str(self.num), True,
                                          (255, 255, 255)), (1000, 125))
        pygame.draw.rect(self.screen, BLUE, [1070, 400, 150, 80])
        start = "��ʼ" if self.str_start else "��ͣ"
        self.screen.blit(text_font.render(start, True, (255, 255, 255)), (1110, 425))

        pygame.draw.rect(self.screen, BLUE, [1070, 500, 150, 80])
        self.screen.blit(text_font.render("���¿�ʼ", True, (255, 255, 255)), (1080, 525))

        return flag

    @staticmethod
    def get_mouse():
        """��������������.

        @return: ���������λ�õ�����
        """
        location_x, location_y = pygame.mouse.get_pos()
        return location_x, location_y

    def pre_start(self):
        """��ʼ������,����������.

        @return: None
        """
        num = "0"
        location_x = 0
        location_y = 0
        while True:
            self.screen.fill(GRAY)
            self.draw_text(0, False)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    location_x, location_y = self.get_mouse()
                #  �رմ���
                if event.type == pygame.QUIT:
                    sys.exit()
                # ��������
                elif event.type == pygame.KEYDOWN and \
                        (1070 <= location_x <= 1290) and (100 <= location_y <= 180):
                    key_num = int(event.key) - 48
                    print(key_num)
                    if 0 <= key_num <= 9:
                        num = num + str(key_num)
                        print(num)
                    elif key_num == -40 and len(num) > 0:
                        num = num[0:-1]
                    self.num = num
            if 1070 <= location_x <= 1220 and 400 <= location_y <= 480:
                self.num = int(num)
                if self.num >= 980 or self.num <= 0:
                    continue
                self.set_cell_num(num)
                self.str_start = False
                break

            pygame.display.flip()

    def start(self, time):
        """��ʼ��Ϸ��ͬʱ��������.

        @param time: ����ˢ��ʱ��
        @return: None
        """
        self.pre_start()
        round_times = 1
        self.balance = 1
        pre_list = None
        after_list = None
        while True:
            for event in pygame.event.get():
                #  �رմ���
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    location_x, location_y = self.get_mouse()
                    if (1070 <= location_x <= 1220) and (400 <= location_y <= 480):
                        self.str_start = not self.str_start
                    if (1070 <= location_x <= 1220) and (500 <= location_y <= 580):
                        self.screen.fill(GRAY)
                        pygame.display.flip()
                        round_times = 1
                        self.balance = 0
                        self.str_start = True
                        self.pre_start()
                        break
            # print(self.str_start)
            self.screen.fill(GRAY)
            # ����ˢ��ʱ��
            self.set_time(time)
            # 1.��ȡϸ��״̬
            self.draw_cell()
            if not self.str_start:
                pre_list = self.cell_list.get_cell_list()
                # 2.����ϸ��
                self.cell_list.change_life()
                after_list = self.cell_list.get_cell_list()
            # �ж��Ƿ񵽴�ƽ��״̬
            if pre_list == after_list:
                flag = True
            else:
                flag = False
            self.balance = self.balance if flag else  self.balance + 1
            print("balance:"+str(self.balance))
            # ���Ƶ�������
            if self.draw_text(round_times, flag):
                pygame.display.flip()
                self.str_start = True

            round_times = round_times if self.str_start else round_times+1
            print("round_times:" + str(round_times))
            # ������Ļ
            pygame.display.flip()
