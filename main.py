from wordle_bot import WordleBot
from wordle_interface import WordleInterface


if __name__ == '__main__':
    interface = WordleInterface()
    bot = WordleBot(interface)
    bot.start()
