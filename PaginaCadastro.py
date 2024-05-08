from PaginaLogin import TelaLogin
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from PaginaLogin import TelaLogin

class TelaCadastro(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
        self.orientation= "vertical"
        self.padding= [50, 20]
        self.spacing= 10

        Window.clearcolor= (0.8, 0.6, 0.9, 1)

        self.add_widget(Label(text='C A D A S T R O', font_size=30, bold=True, color=(0, 0, 0, 1)))


        self.name_input= TextInput(hint_text='Digite o seu nome...', multiline=False, size_hint=(None, None), size=(900, 70))
        self.email_input= TextInput(hint_text='Digite o seu e-mail...',password=False,multiline=False, size_hint=(None, None), size=(900, 70))
        self.username_input= TextInput(hint_text='Digite o seu usuário...', multiline=False, size_hint=(None, None), size=(900, 70))
        self.number_input= TextInput(hint_text='Digite o seu número de telefone...', multiline=False, size_hint=(None, None), size=(900, 70))
        self.password_input= TextInput(hint_text='Digite a sua senha...', multiline=True, size_hint=(None, None), size=(900, 70))
        self.add_widget(self.name_input)
        self.add_widget(self.password_input)
        self.add_widget(self.email_input)
        self.add_widget(self.number_input)
        self.add_widget(self.username_input)

        self.buttons_layout= BoxLayout(padding=[0, 10], spacing=10)
        self.signup_button= Button(text='Cadastrar', color=(0, 0, 0.1, 1), size_hint=(None,None), size=(900, 50),background_color =(100, 100, 100, 100))
        self.buttons_layout.add_widget(self.signup_button)
        self.add_widget(self.buttons_layout)

    def cadastro(self,instance):
        username = self.username_input.text
        password= self.password_input.text
        print('Username:', username)
        print('Password:', password)

class MyApp(App):
    def build(self):
        return TelaCadastro()
    
if __name__ == '__main__':
    MyApp().run()