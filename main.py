from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivy.utils import platform
import os

class SuperBassApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        screen = MDScreen()
        scroll = ScrollView()
        self.list_view = MDList()
        
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        
        self.update_list()
        scroll.add_widget(self.list_view)
        screen.add_widget(scroll)
        return screen

    def update_list(self):
        path = '/storage/emulated/0/Music'
        try:
            if os.path.exists(path):
                songs = [f for f in os.listdir(path) if f.endswith('.mp3')]
                for s in songs:
                    self.list_view.add_widget(OneLineListItem(text=s))
                if not songs:
                    self.list_view.add_widget(OneLineListItem(text='Folder Kosong'))
            else:
                self.list_view.add_widget(OneLineListItem(text='Path tidak ditemukan'))
        except Exception as e:
            self.list_view.add_widget(OneLineListItem(text=f'Error: {str(e)}'))

if __name__ == '__main__':
    SuperBassApp().run()
