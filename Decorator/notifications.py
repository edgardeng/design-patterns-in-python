"""
 装饰器 代码实例
 Decorator Code Demo
"""


class Notification():

    def send(self, msg):
        print('sending a message: ', msg)


class NotificationDecorator(Notification):

    def __init__(self, notifier: Notification):
        self._notifier = notifier

    def send(self, msg):
        self._notifier.send(msg)
        print('through a NotificationDecorator')


class SMSDecorator(NotificationDecorator):
    def send(self, msg):
        super().send(msg)
        self.sendSMS(msg)

    def sendSMS(self, msg):
        print('sending a SMS Notification:', msg)


class FacebookDecorator(NotificationDecorator):
    def send(self, msg):
        super().send(msg)
        self.sendFacebook(msg)

    def sendFacebook(self, msg):
        print('sending a Facebook Notification:', msg)


if __name__ == "__main__":
    notifier = Notification()
    print("Client: I've got a simple component:")
    notifier.send('Hello')
    print()
    sms = SMSDecorator(notifier)
    sms.send('Hello')
    print()
    facebook = FacebookDecorator(notifier)
    facebook.send('Hello')
