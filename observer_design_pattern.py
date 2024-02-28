class YoutubeChannel:
    def __init__(self, name) -> None:
        """
        Constructor for YoutubeChannel.

        Args:
            name (str): Name of the YouTube channel.
        """
        self.name = name  # Name of the YouTube channel
        self.subscribers = []  # List to store subscribers of the channel
    
    def subscribe(self, sub):
        """
        Method to subscribe a user to the channel.

        Args:
            sub (YoutubeSubscriber): Subscriber object to be added to the subscribers list.
        """
        self.subscribers.append(sub)
    
    def notify(self, event):
        """
        Method to notify subscribers about an event.

        Args:
            event (str): Description of the event.
        """
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)

from abc import ABC, abstractmethod
class YoutubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self, channel, event):
        """Abstract method to send notification to the subscriber."""
        pass

class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name) -> None:
        """
        Constructor for YoutubeUser.

        Args:
            name (str): Name of the YouTube user.
        """
        self.name = name

    def sendNotification(self, channel, event):
        """
        Method to send notification to the user.

        Args:
            channel (str): Name of the YouTube channel sending the notification.
            event (str): Description of the event.
        """
        print(f"User {self.name} received notification from {channel}: {event}")


# Creating a YouTube channel
channel = YoutubeChannel("Channel")

# Subscribing users to the channel
channel.subscribe(YoutubeUser("sub1"))
channel.subscribe(YoutubeUser("sub2"))
channel.subscribe(YoutubeUser("sub3"))

# Notifying subscribers about a new video release
channel.notify("A new video released")
