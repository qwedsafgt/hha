import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):#Bullet类继承导入的Sprite
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object, at the ship's current position."""
        super(Bullet, self).__init__()#在飞船所处的位置创建一个子弹对象
        self.screen = screen#

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)#设置子弹对象的位置，长度，宽度。利用RECT类创建一个矩形
        self.rect.centerx = ship.rect.centerx#设置子弹的x坐标
        self.rect.top = ship.rect.top#设置子弹的y坐标，使子弹看起来像从飞船顶部射出

        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)#把子弹的y坐标储存为小数值，以便精确处理

        self.color = ai_settings.bullet_color#储存子弹的颜色
        self.speed_factor = ai_settings.bullet_speed_factor#储存子弹的速度

    def update(self):#更新表示子弹移动的小数值
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor#改变子弹的横坐标
        # Update the rect position.
        self.rect.y = self.y#把rect的值换为y的值

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)#绘制子弹
