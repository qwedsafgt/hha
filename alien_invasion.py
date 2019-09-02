import pygame#导入pygame
from pygame.sprite import Group#导入group类

from settings import Settings#导入settings类
from ship import Ship#导入ship类
import game_functions as gf#导入game_functions类作为gf

def run_game():#运行程序的主要函数
    # Initialize pygame, settings, and screen object.
    pygame.init()#使pygame初始化
    ai_settings = Settings()#实例化类
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))#创建背景surface
    pygame.display.set_caption("Alien Invasion")#为背景添上名字

    # Set the background color.
    bg_color = (230, 230, 230)#设置背景颜色

    # Make a ship.
    ship = Ship(ai_settings, screen)#创建一个ship对象
    # Make a group to store bullets in.
    bullets = Group()#创建GROUP实例

    # Start the main loop for the game.
    while True:#管理程序的主循环
        gf.check_events(ai_settings, screen, ship, bullets)#检测键盘的按键 #处理用户使用空格键时处理bullets
        ship.update()#使飞船图像得到更新
        gf.update_bullets(bullets)#使子弹图像得到更新
        gf.update_screen(ai_settings, screen, ship, bullets)#使更新的图像得到显示

run_game()#运行程序
