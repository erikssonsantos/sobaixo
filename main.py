#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':

    __author__ = 'Eriksson Santos'
    __version__ = '0.0.1'
    __last_modification__ = '2023.08.25'

    # 
    #   PSEUDO-PROTOTIPO/"MAPA" DE CLASSES E FUNÇÕES
    #
    # @dataclass class Config
    # class MixinRootWidget(object)
    # class RootWidget(BoxLayout, MixinRootWidget)
    # class MixinMain(object)
    # class MainApp(MDApp, MixinMain)
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 


    from kivymd.app import MDApp
    from kivy.core.window import Window
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.uix.toolbar.toolbar import MDTopAppBar
    from kivymd.uix.screen import MDScreen
    from kivymd.uix.screenmanager import MDScreenManager
    from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
    from kivymd.uix.label.label import MDLabel
    from kivymd.uix.textfield.textfield import MDTextFieldRect
    from kivymd.color_definitions import colors
    from kivy.graphics import Color, Rectangle
    from dataclasses import dataclass


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


    class MixinMyLabel(object):
        ...

    class MyLabel(MDLabel, MDTextFieldRect, MixinMyLabel):
        ...


    class MixinMDTopAppBar0(object):
        ...

    class MDTopAppBar0(MDTopAppBar, MixinMDTopAppBar0):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.title = "Só Baixo"
            # self.anchor_title = "center"
            self.right_action_items = [
                ["white-balance-sunny", lambda x : app.switch_theme_style(), "tooltip text","overflow text", (1, 1, 1, 1),],
                ["dots-vertical", None, "tooltip text","overflow text", (1, 1, 1, 1),],
            ]

    
    class MixinScreenAddDownload(object):
        ...

    class ScreenAddDownload(MDScreen, MixinScreenAddDownload):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.name = "screen_add_download"


    class MixinScreenListDownloads(object):
        # opção para background: 
        def tamanho(self,x,y):
            self.size=(Window.width, Window.height)
    
        # opção para background:
        def draw_background(self, x, y):
            self.canvas.before.add(Rectangle(size=Window.size))

    class ScreenListDownloads(MDScreen, MixinScreenListDownloads):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.name = "screen_list_downloads"
            # self.md_bg_color = colors["BlueGray"]["50"]  # opção para background
            self.test_text = MyLabel()
            self.test_text.adaptive_size = True
            self.test_text.pos_hint = {"center_x": .5, "center_y": .5}
            self.test_text.text = "blá blá blá blá blá blá blá"
            self.test_text.allow_selection = True
            self.test_text.allow_copy = True
            self.test_text.padding = ("4dp", "4dp")
            # self.test_text.theme_text_color = "Custom"
            # self.test_text.text_color = self.test_text.theme_cls.text_color
            
            self.add_widget(self.test_text)

            # opção para background:
            # self.canvas.before.add(Color(rgba=[1,1,0,5]))
            # self.canvas.before.add(Rectangle(size=Window.size))
            # self.bind(size = self.draw_background)
            

    class MixinScreenDetailDownload(object):
        ...

    class ScreenDetailDownload(MDScreen, MixinScreenDetailDownload):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.name = "screen_detail_download"


    class MixinScreenAbout(object):
        ...

    class ScreenAbout(MDScreen, MixinScreenAbout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.name = "screen_about"


    class MixinScreenManagerCenter(object):
        ...

    class ScreenManagerCenter(MDScreenManager, MixinScreenManagerCenter):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            
            self.screen_add_download = ScreenAddDownload()
            self.screen_list_downloads = ScreenListDownloads()
            self.screen_detail_download = ScreenDetailDownload()
            self.screen_about = ScreenAbout()

            self.add_widget(self.screen_add_download)
            self.add_widget(self.screen_list_downloads)
            self.add_widget(self.screen_detail_download)
            self.add_widget(self.screen_about)
            
            self.current = 'screen_list_downloads'



    class MixinMDBottomNavigation0(object):
        ...

    class MDBottomNavigation0(MDBottomNavigation, MixinMDBottomNavigation0):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.bottom_navigation_add_download = MDBottomNavigationItem(
                        MDLabel(
                            text='Mail',
                            halign='center',
                        ),
                        name='screen 1',
                        text='Mail',
                        icon='gmail',
                        badge_icon="numeric-10",
            )

            self.bottom_navigation_list_downloads = MDBottomNavigationItem(
                        MDLabel(
                            text='Twitter',
                            halign='center',
                        ),
                        name='screen 1',
                        text='Twitter',
                        icon='twitter',
                        badge_icon="numeric-10",
            )

            self.add_widget(self.bottom_navigation_add_download)
            self.add_widget(self.bottom_navigation_list_downloads)



    class MixinRootWidget(object):

        def alert(self):
            print("alert MixinRootwidget")

    class RootWidget(MDBoxLayout, MixinRootWidget):

        

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.orientation = "vertical"

            self.topbar = MDTopAppBar0()
            self.screen_manager_center = ScreenManagerCenter()
            self.bottombar = MDBottomNavigation0()

            self.add_widget(self.topbar)
            self.add_widget(self.screen_manager_center)
            self.add_widget(self.bottombar)

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

            global app
            app = MDApp.get_running_app()
            
            # print(dir(Window))


    class MainApp(MDApp, MixinMain):



        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            

        def build(self):
            """self.theme_cls.theme_style_switch_animation = True
            self.theme_cls.theme_style_switch_animation_duration = 0.8
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"""
            return RootWidget()

        def switch_theme_style(self):
            ...
            """self.theme_cls.primary_palette = (
                "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
            )
            self.theme_cls.theme_style = (
                "Dark" if self.theme_cls.theme_style == "Light" else "Light"
            )"""

        def on_start(self, *args, **kwargs):
            super(MainApp, self)

            self.first_load()


    MainApp().run()
