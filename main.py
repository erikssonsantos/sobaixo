from kivymd.app import MDApp
from kivy.core.window import Window
from dataclasses import dataclass
from kivy.uix.boxlayout import BoxLayout


@dataclass
class Config:
    MIN_HEIGHT: int = 350
    MIN_WIDTH: int = 400
    height: int = 450
    width: int = 500
    MAX_HEIGHT: int = 600
    MAX_WIDTH: int = 500
    LAST_HEIGHT: int = 1
    LAST_WIDTH: int = 1
    ROLLED_HEIGHT: int = 50
    ROLLED_WIDTH: int = LAST_WIDTH

    borderless_status: bool = False
    rolled: bool = False
    fullscreen: bool = False
    title: str = "Só Baixo"


class MixinRootWidget(object):

    def alert(self):
        print("alert MixinRootwidget")


class RootWidget(BoxLayout, MixinRootWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _trigger_layout(self, *args, **kwargs):
        super(RootWidget, self).do_layout()
        
        width, height = Window.size

        if not Config.rolled:

            if width > Config.MAX_WIDTH:
                Window.size = Config.MAX_WIDTH, Window.size[1]
            if height > Config.MAX_HEIGHT:
                Window.size = Window.size[0], Config.MAX_HEIGHT

            if width < Config.MIN_WIDTH:
                Window.size = Config.MIN_WIDTH, Window.size[1]
            if height < Config.MIN_HEIGHT:
                Window.size = Window.size[0], Config.MIN_HEIGHT

            Config.LAST_HEIGHT  =   height
            Config.LAST_WIDTH   =   width
            
        else:

            if width > Config.ROLLED_WIDTH:
                Window.size = Config.ROLLED_WIDTH, Window.size[1]
            if height > Config.ROLLED_HEIGHT:
                Window.size = Window.size[0], Config.ROLLED_HEIGHT


class MixinMain(object):
    
    def first_load(self):
        
        Window.borderless = Config.borderless_status
        self.title = Config.title
        self.icon = r'icon.ico'
        if Config.fullscreen:
            Window.fullscreen = True
        else: 
            Window.fullscreen = False
        
        # print(dir(Window))


class MainApp(MDApp, MixinMain):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return RootWidget()

    def on_start(self, *args, **kwargs):
        super(MainApp, self)

        self.first_load()


if __name__ == '__main__':
    MainApp().run()
