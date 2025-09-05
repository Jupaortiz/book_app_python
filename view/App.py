from domain.Friend import Friend
from repository.FriendRepository import FriendRepository
from service.FriendService import FriendService


class App:


    def __init__(self):
        self.friendRepository = FriendRepository()
        self.friendService = FriendService()
        self.friend = Friend()

    def run_app(self):
        print("Presione 1 para iniciar ")

    def menu_friend(self):
        print("Menú Amigo")