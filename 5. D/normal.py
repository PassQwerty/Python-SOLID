import os
import sys
import time

# Dependency Inversion Principle
# Принцип инверсии зависимостей
# Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter:
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

    def logStderr(self, message):
        TerminalPrinter().write(f"{self.prefix} {message}")

    def logFile(self, message):
        FilePrinter().write(f"{self.prefix} {message}")


def main():
    logger = Logger()
    logger.logFile("Starting the program...")
    logger.logStderr("An error!")


if __name__ == '__main__':
    os.system('cls||clear')
    main()
