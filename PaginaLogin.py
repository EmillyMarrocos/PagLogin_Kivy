from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.5, 0, 0.5, 1)

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Layout
        self.orientation = 'vertical'

        #Labels
        self.add_widget(Label(text='Login', size_hint=(1, 0.5)))

        #Inputs
        self.email_input = TextInput(hint_text='Email', size_hint=(1, 0.5))
        self.add_widget(self.email_input)

        self.password_input = TextInput(hint_text='Senha', password= True, size_hint=(1, 0.5))
        self.add_widget(self.password_input)

        #Buttons
        self.login_button = Button(text='Entrar', on_press= self.login, size_hint=(1, 0.5))
        self.add_widget(self.login_button)

        self.register_button = Button(text='Cadastrar', on_press=self.register, size_hint=(1, 0.5))
        self.add_widget(self.register_button)

    def login(self, instance):
        #Implementar a lógica de Login
        email = self.email_input.text
        senha = self.password_input.text
        print('Email: ', email, 'Senha: ', senha)

    def register(self, instance):
        #Implementar a lógica de Cadastro
        print('Usuário cadastrado com sucesso!')

class LoginApp(App): 
    def build(self):
        return LoginScreen()
    
if __name__ == '__main__':
    LoginApp().run()