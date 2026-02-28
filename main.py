from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DebtApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="مرحباً بك في تطبيق ديوني", font_size='24sp'))
        return layout

if __name__ == '__main__':
    DebtApp().run()
