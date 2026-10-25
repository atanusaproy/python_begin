from abc import ABC, abstractmethod



# Abstract class

class INotification(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

    def logging(self, message):
        print(f"Logging notification: {message}")


class EmailNotification(INotification):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")


class SMSNotification(INotification):
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")


class SlackNotification(INotification):
    def send_notification(self, message):
        print(f"Sending Slack notification: {message}")


def send_notification(notification: INotification, message: str):
    notification.logging(message)
    notification.send_notification(message)


# Usage
email_notification = EmailNotification()
send_notification(email_notification, "Hello, this is an email notification.")

sms_notification = SMSNotification()
send_notification(sms_notification, "Hello, this is an SMS notification.")

slack_notification = SlackNotification()
send_notification(slack_notification, "Hello, this is a Slack notification.")

# __del__ : This method is called when you use the del statement on an object. It should perform any necessary cleanup before the object is destroyed.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __del__(self):
        print(f"Car object {self.make} {self.model} is being destroyed.")


car = Car("Toyota", "Camry")
new_car = Car("Honda", "Civic")
del car

car.model # This will raise an AttributeError
new_car.model # This will work fine




