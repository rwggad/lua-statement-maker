from abc import ABCMeta, abstractmethod


class LuaCtxBase():
    __metaclass__ = ABCMeta
    BASE_INDENT = 4

    @abstractmethod
    def append(self):
        pass

    @abstractmethod
    def extend(self):
        pass

    @abstractmethod
    def make_stmt(self):
        pass
