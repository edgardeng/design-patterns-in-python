from __future__ import annotations
import random
from collections.abc import Iterable, Iterator
from typing import Any, List


class Profile(object):
    def __init__(self, pid, email):
        self.id = pid
        self.email = email


class FacebookIterator(Iterator):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection
        self._position = 0

    def __iter__(self) -> FacebookIterator:
        """
        The __iter__() method returns the iterator object itself
        """
        return FacebookIterator(self._collection)

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value

    def add_item(self, item: Profile):
        self._collection.append(item)


class Facebook():
    def __init__(self, p):
        self._profile = p

    def social_graph_request(self, type):
        return [Profile(random.randint(1, 50), ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 8)) + '@' + type)
                for _ in range(5)]

    def create_friends_iterator(self) -> FacebookIterator:
        return FacebookIterator(self.social_graph_request('friend'))

    def create_coworkers_iterator(self) -> FacebookIterator:
        return FacebookIterator(self.social_graph_request('coworkers'))


class SocialSpammer(object):
    def send(self, it: FacebookIterator, message: str):
        for p in it:
            print('send email msg: %s to %s' % (message, p.email))


def send_spam_to_friends(network, spammer):
    iterator = network.create_friends_iterator()
    spammer.send(iterator, "Very important friend's message from ")


def send_spam_to_coworkers(network, spammer):
    iterator = network.create_coworkers_iterator()
    spammer.send(iterator, "Very important coworker's message ")


if __name__ == '__main__':
    profile = Profile(1, '****@gmail.com')
    network = Facebook(profile)
    spammer = SocialSpammer()

    send_spam_to_friends(network, spammer)
    send_spam_to_coworkers(network, spammer)
