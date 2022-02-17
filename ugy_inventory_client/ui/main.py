from kivy.app import App
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from ugy_inventory_client.lib.auth import Auth, Credential
from ugy_inventory_client.lib.exceptions import AuthenticationError
from ugy_inventory_client.ui.spinners import IconButton

Window.size = (350, 550)


# Login Window
class Login(BoxLayout):
    def __init__(self, _parent, **kwargs):
        super().__init__(**kwargs)
        self._parent = _parent

    def main_page(self):
        self._parent.main_window()

    def login(self):
        password = self.ids.txt_password.text
        username = self.ids.txt_username.text

        # validate input
        if not all([password, username]):
            self.ids.lbl_login_status.text = "Username and password required"
            return

        server = "http://localhost:5000"
        cred = Credential(username, password)
        auth = Auth(server, cred)

        try:
            auth.authenticate()
        except AuthenticationError:
            self.ids.lbl_login_status.text = "Authentication Error"

        if auth.token:
            self.main_page()


# main form
class MainForm(BoxLayout):
    def __init__(self, _parent, **kwargs):
        super().__init__(**kwargs)
        self._parent = _parent

    def removeinventry(self):
        self._parent.remove_form()

    def add_inventry(self):
        self._parent.add_new_form()


# remove inventry form
class RemoveForm(BoxLayout):
    def __init__(self, _parent, **kwargs):
        super().__init__(**kwargs)
        self._parent = _parent

        self.dropdown = DropDown()

        for index in range(10):
            btn = Button(text="Value %d" % index, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        self.mainbutton = IconButton()
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, "text", x))

        self.add_spinner()

    def add_spinner(self):
        sparea = self.ids.spinner_box
        sparea.add_widget(self.mainbutton)

    def call_mainpage(self):
        self._parent.main_window()


# add inventry form
class AddNew(BoxLayout):
    def __init__(self, _parent, **kwargs):
        super().__init__(**kwargs)
        self._parent = _parent

    def call_mainpage(self):
        self._parent.main_window()


# Main app code
class Main(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_box = self.ids.main_box
        self.login_form()

    # load Login window
    def login_form(self):
        self.main_box.clear_widgets()
        self.login = vars(self).get("login", Login(self))
        self.main_box.add_widget(self.login)

    # load graph window
    def main_window(self):
        self.main_box.clear_widgets()
        self.mainform = vars(self).get("mainform", MainForm(self))
        self.main_box.add_widget(self.mainform)

    # load remove_form
    def remove_form(self):
        self.main_box.clear_widgets()
        self.remove_form = vars(self).get("remove_form", RemoveForm(self))
        self.main_box.add_widget(self.remove_form)

    # load add new inventry form
    def add_new_form(self):
        self.main_box.clear_widgets()
        self.add_form = vars(self).get("add_form", AddNew(self))
        self.main_box.add_widget(self.add_form)


class MainApp(App):
    def build(self):
        return Main()


def main():

    mp = MainApp()
    mp.run()


if __name__ == "__main__":
    main()
