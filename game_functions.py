import sys#导入sys模块

import pygame#导入pygame模块

from bullet import Bullet#导入BULLET类

def check_keydown_events(event, ai_settings, screen, ship, bullets):#用来响应用户按下左右按键
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:#判断用户是否按下右键
        ship.moving_right = True#如果是返回TRue
    elif event.key == pygame.K_LEFT:#判断用户是否按下左键
        ship.moving_left = True#如果是返回FALSE
    elif event.key == pygame.K_SPACE:#判断是否按下空格键
        fire_bullet(ai_settings, screen, ship, bullets)#如果按下空格键，就创建一个新的子弹，并把它存入编组

def check_keyup_events(event, ship):#响应松开
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:#判断用户是否松开右键
        ship.moving_right = False#如果是就返回错
    elif event.key == pygame.K_LEFT:#判断用户是否松开左键
        ship.moving_left = False#如果是就返回错

def check_events(ai_settings, screen, ship, bullets):#对键盘作出反应
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():#处理不同的键盘反应
        if event.type == pygame.QUIT:#如果按键是停止
            sys.exit()#就退出游戏
        elif event.type == pygame.KEYDOWN:#判段是否按下
            check_keydown_events(event, ai_settings, screen, ship, bullets)#如果是就运行关于按下键盘的函数
        elif event.type == pygame.KEYUP:#判断是否松开
            check_keyup_events(event, ship)#如果是就运行松开键盘的函数

def fire_bullet(ai_settings, screen, ship, bullets):#使子弹发射的函数
    """Fire a bullet, if limit not reached yet."""
    # Create a new bullet, add to bullets group.
    if len(bullets) < ai_settings.bullets_allowed:#限制子弹的发射数量
        new_bullet = Bullet(ai_settings, screen, ship)#创建新的子弹
        bullets.add(new_bullet)#把建造的子弹添加到元组里

def update_screen(ai_settings, screen, ship, bullets):#更新屏幕的函数
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)#添加背景色

    # Redraw all bullets, behind ship and aliens.
    for bullet in bullets.sprites():#把编组里的子弹全都进行绘制
        bullet.draw_bullet()
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()#更新屏幕

def update_bullets(bullets):
    """Update position of bullets, and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()#更新子弹的位置

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():#删除多余的子弹
        if bullet.rect.bottom <= 0:#判断子弹是否超出边界
            bullets.remove(bullet)#删除以超出的子弹
