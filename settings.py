class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200#设置屏幕的宽度
        self.screen_height = 800#设置屏幕的高度
        self.bg_color = (230, 230, 230)#设置屏幕的背景色

        # Ship settings.
        self.ship_speed_factor = 1.5#设置移动的单位长度

        # Bullet settings.
        self.bullet_speed_factor = 1#设置子弹的移动单位
        self.bullet_width = 3#设置子弹的宽度
        self.bullet_height = 15#设置子弹的高度
        self.bullet_color = 60, 60, 60#设置子弹的颜色
        self.bullets_allowed = 3#允许存储的子弹的最大数量
