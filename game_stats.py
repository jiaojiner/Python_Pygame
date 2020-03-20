#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, settings):
        """初始化统计信息"""
        self.ai_settings = settings
        self.reset_stats()

        # # 游戏刚启动时处于活动状态
        # self.game_active = True
        # 让游戏一开始处于非活动状态
        self.game_active = False

        # 在任何情况下都不重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
