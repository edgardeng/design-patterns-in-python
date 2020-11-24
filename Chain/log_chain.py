from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class AbstractLogger(ABC):
    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self, l):
        self.level = l
        self.next_logger = None

    # @abstractmethod
    def set_next(self, logger: AbstractLogger) -> AbstractLogger:
        self.next_logger = logger
        return self.next_logger

    def log_message(self, level, message):
        # print('log_message', self.level, level)
        if self.level <= level:
            self.write(message)
        if self.next_logger:
            self.next_logger.log_message(level, message)

    @abstractmethod
    def write(self, request):
        pass


class ConsoleLogger(AbstractLogger):
    def __init__(self):
        super().__init__(1)  # INFO

    def write(self, message):
        print("Standard Console::Logger: " + message)


class FileLogger(AbstractLogger):
    def __init__(self):
        super().__init__(2)  # DEBUG

    def write(self, message):
        print("File::Logger: " + message)


class ErrorLogger(AbstractLogger):
    def __init__(self):
        super().__init__(3)  # ERROR

    def write(self, message):
        print("Error Console::Logger: " + message)


if __name__ == '__main__':
    logger_chain = ErrorLogger()
    logger_chain.set_next(FileLogger()).set_next(ConsoleLogger())

    logger_chain.log_message(AbstractLogger.INFO, "This is an information.");
    print()
    logger_chain.log_message(AbstractLogger.DEBUG, "This is a debug level information.");
    print()
    logger_chain.log_message(AbstractLogger.ERROR, "This is an error information.");
