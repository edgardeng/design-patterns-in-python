from __future__ import annotations

import random
from abc import ABC, abstractmethod


class Profile(object):
    def __init__(self, pid, email):
        self.id = pid
        self.email = email


class ProfileIterator(ABC):
    @abstractmethod
    def get_next(self) -> Profile:
        pass

    @abstractmethod
    def has_more(self) -> bool:
        pass


class SocialNetwork(ABC):
    """
    The collection interface must declare a factory method for producing iterators.
    You can declare several methods if there are different kinds of iteration available in your program.
    """

    @abstractmethod
    def create_friends_iterator(self, profile_id) -> ProfileIterator:
        pass

    @abstractmethod
    def create_coworkers_iterator(self, profile_id) -> ProfileIterator:
        pass


class FacebookIterator(ProfileIterator):

    def __init__(self, pid, t):
        self.profile_id = pid
        self.type = t
        self.current_position = 0
        self.cache = [
            Profile(random.randint(1, 50), ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 8)) + '@' + self.type)
            for _ in range(5)]
        # self.cache = []
        # cache = facebook.socialGraphRequest(profileId, type)

    def get_next(self) -> Profile:
        if self.has_more():
            self.current_position += 1
            return self.cache[self.current_position - 1]

    def has_more(self) -> bool:
        return self.current_position < len(self.cache)


class Facebook(SocialNetwork):
    def create_friends_iterator(self, profile_id) -> ProfileIterator:
        return FacebookIterator(profile_id, "friends")

    def create_coworkers_iterator(self, profile_id) -> ProfileIterator:
        return FacebookIterator(profile_id, "coworkers")


class SocialSpammer(object):
    def send(self, it: ProfileIterator, message: str):
        while it.has_more():
            profile = it.get_next()
            print('send email msg: %s to %s' % (message, profile.email))


def send_spam_to_friends(network, spammer, profile):
    iterator = network.create_friends_iterator(profile.id)
    spammer.send(iterator, "Very important friend's message ")


def send_spam_to_coworkers(network, spammer, profile):
    iterator = network.create_coworkers_iterator(profile.id)
    spammer.send(iterator, "Very important coworker's message ")


if __name__ == '__main__':
    network = Facebook()
    spammer = SocialSpammer()
    profile = Profile(1, '****@gmail.com')
    send_spam_to_friends(network, spammer, profile)
    send_spam_to_coworkers(network, spammer, profile)
