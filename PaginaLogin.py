from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
        # Define o layout
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = [50, 20, 50, 20]
        
        # Adiciona o ícone de perfil
        self.add_widget(Image(source='Users/aluno.sesipaulista/Documents/PagLogin_Kivy/img_icone/user_icon.png"', size_hint_y=None, height=150))

        # Adiciona o Label de Login
        self.add_widget(Label(text='Login', size_hint=(1, 0.2)))

        # Adiciona o input de email
        self.email_input = TextInput(hint_text='Email', size_hint=(1, 0.1))
        self.add_widget(self.email_input)
        
        # Adiciona o input de senha
        self.password_input = TextInput(hint_text='Senha', password=True, size_hint=(1, 0.1))
        self.add_widget(self.password_input)
        
        # Adiciona os botões de entrar e cadastrar
        self.login_button = Button(text='Entrar', size_hint=(1, 0.1), background_color=(0.5, 0, 1, 1))
        self.add_widget(self.login_button)
        
        self.register_button = Button(text='Cadastrar', size_hint=(1, 0.1), background_color=(0.5, 0, 1, 1))
        self.add_widget(self.register_button)

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()