import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        self.screen = screen#调入背景screen
        self.ai_settings = ai_settings#引入settings类

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('images/ship.bmp')#使这个bmp图像转换为surface
        self.rect = self.image.get_rect()#获取飞船rect属性
        self.screen_rect = screen.get_rect()#获取背景的rect属性

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx#将飞船图像置于中央
        self.rect.bottom = self.screen_rect.bottom#将飞船图像置于底部

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)#在飞船的属性centrex中存储小数值

        # Movement flags.
        self.moving_right = False#用户没有按键盘时设置为false
        self.moving_left = False

    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:#使飞船图像不至于触及矩形边缘
            self.center += self.ai_settings.ship_speed_factor#使用户每按一次右键就移动1.5单位
        if self.moving_left and self.rect.left > 0#使飞船边缘不触及右边屏幕
            self.center -= self.ai_settings.ship_speed_factor#使用户每按一次左键就移动1.5单位

        # Update rect object from self.center.
        self.rect.centerx = self.center#根据self.centre更新rect对象

    def blitme(self):#将飞船绘制到屏幕上
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
