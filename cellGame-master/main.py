# -*- coding: gbk -*-

from pyheat import PyHeat
ph = PyHeat(r'D:\����\������̻���\cellGame-master\main.py')
ph.create_heatmap()
# To view the heatmap.
ph.show_heatmap()
# To output the heatmap as a file.
ph.show_heatmap(r'D:\main.png')

"""have a nice day.

@author: Khan,ChenJie
@contact:
@time: 2020/5/28 19:06
@file: cell_list.py
@desc: ������Ϸ��Game of Life��
       ��Ϸ����
            1. ��ϸ����Χ��ϸ�������С��2�������3���������������Ⱥ����Ⱦ�������������
            2. ��ϸ����Χ�����2��3��ϸ�����Լ��������������棩
            3. ��ϸ�����ո���Χ���ǡ����3��ϸ����ᵮ���µĻ�ϸ��������ֳ��
       ������������B3/S23��������������Ӧ��ϸ�������������������������͵��Զ�����
"""

from game import Game


if __name__ == '__main__':
    game = Game(1300, 800)
    game.start(1)
