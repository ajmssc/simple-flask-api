import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    TITLE = 'Bitcoin Inspector'
    YOUTUBE_URL = 'https://www.youtube.com/watch?v=sE2rKoDDk3Q'
    EMAIL_ADDRESS = 'jeanmarc.soumet@gmail.com'
    GITHUB_URL = 'http://github.com/ajmssc/'
    LINKEDIN_URL = 'https://www.linkedin.com/in/jeanmarcsoumet'
    PAGES = [
        {
            'name' : 'Home',
            'link' : '/index',
            'icon' : 'fa-home'
        },
        {
            'name' : 'Presentation Slides',
            'link' : '/presentation',
            'icon' : 'fa-slideshare'
        },
        {
            'name' : 'Historical Data',
            'link' : '/history_blocks',
            'icon' : 'fa-line-chart'
        },
        {
            'name' : 'Live Data',
            'link' : '/live',
            'icon' : 'fa-bolt'
        },
        {
            'name' : 'Wallets',
            'link' : '/wallets',
            'icon' : 'fa-money'
        },
        {
            'name' : 'Range query',
            'link' : '/wallets_timed',
            'icon' : 'fa-clock-o'
        }
    ]

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
