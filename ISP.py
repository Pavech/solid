from abc import abstractmethod


class Machine:
    def print(self):
        raise NotImplementedError

    def fax(self):
        raise NotImplementedError

    def scan(self):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self):
        pass

    def fax(self):
        pass

    def scan(self):
        pass


class OldPrinter(Machine):
    def print(self):
        pass  # ok

    def fax(self):
        pass  # noop

    def scan(self):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan')


###################


class Printer:
    @abstractmethod
    def print(self):
        pass


class Scan:
    @abstractmethod
    def print(self):
        pass


class Fax:
    @abstractmethod
    def print(self):
        pass


class MyPrinter(Printer):
    def print(self):
        print()
