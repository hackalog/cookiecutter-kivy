from kivy.app import App
from kivy.lang import Builder


kv = Builder.load_string("""
#:kivy {{cookiecutter.minimum_kivy_version}}

Button:
    text: 'Hello World'
""")


class {{cookiecutter.class_name}}App(App):
    """Basic kivy app
    """

    def build(self):
        self.root = kv
        return self.root
