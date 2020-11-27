from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    def notify(self, sender: object, event: str):
        pass


class Component(object):
    def __init__(self, dialog: Mediator):
        self._dialog = dialog

    def click(self):
        self._dialog.notify(self, "click")

    def keypress(self):
        self._dialog.notify(self, "keypress")


class Button(Component):
    pass


class Textbox(Component):
    pass


class Checkbox(Component):
    def __init__(self, dialog: Mediator):
        self.checked = False
        super().__init__(dialog)

    def check(self):
        self.checked = not self.checked
        self._dialog.notify(self, "check")


class AuthenticationDialog(Mediator):
    """

    The concrete mediator class. The intertwined web of
    connections between individual components has been untangled
    and moved into the mediator.
    """

    def __init__(self, t=None):
        self.title = t

    def setComponent(self, btn=None, chbox=None):
        self.login_btn = btn
        self.login_register_check_box = chbox

    # private field title: string
    # private field loginOrRegisterChkBx: Checkbox
    # private field loginUsername, loginPassword: Textbox
    # private field registrationUsername, registrationPassword,
    # registrationEmail: Textbox
    # private field okBtn, cancelBtn: Button

    def notify(self, sender, event):
        if sender == self.login_register_check_box and event == "check":
            if sender.checked:
                print('I wanna Log in')
                self.title = "Log in"
                # # 1. Show login form components.
                # # 2. Hide registration form components.
            else:
                print('I wanna Register')
                self.title = "Register"
            # 1. Show registration form components.
            # 2. Hide login form components

        if sender == self.login_btn and event == "click":
            if self.login_register_check_box.checked:
                print('I am login')
                # Try to find a user using login credentials.
                # if (!found)
                # Show an error message above the login
                # field.
            else:
                print('I am register')
                # 1. Create a user account using data from the
                # registration fields.
                # 2. Log that user in.
                # ...


if __name__ == "__main__":
    dialog = AuthenticationDialog()
    login_btn = Button(dialog)
    login_register_check_box = Checkbox(dialog)

    dialog.setComponent(login_btn, login_register_check_box)
    login_register_check_box.check()
    login_btn.click()

    login_register_check_box.check()
    login_btn.click()
