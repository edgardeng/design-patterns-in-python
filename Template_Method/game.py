class Game(object):
    def initialize(self, ): pass

    def start(self, ): pass

    def end(self, ): pass

    def play(self):
        self.initialize()
        self.start()  # 开始游戏
        self.end()  # 结束游戏


class Cricket(Game):
    def initialize(self, ):
        print("Cricket Game Finished!")

    def start(self, ):
        print("Cricket Game Initialized! Start playing.")

    def end(self, ):
        print("Cricket Game Started. Enjoy the game!")


class Football(Game):
    def initialize(self, ):
        print("Football Game Finished!")

    def start(self, ):
        print("Football Game Initialized! Start playing.")

    def end(self, ):
        print("Football Game Started. Enjoy the game!")


if __name__ == "__main__":
    game = Cricket()
    game.play()
    print()
    game = Football()
    game.play()
