class Secretive:
    def __inaccessable(self):
        print("Bet you can not see me")

    def accessable(self):
        print("The secret message is:")
        self.__inaccessable()


class Filter:

    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']


class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print("Hi, my value is ", self.value)


class TalkingCalculator(Calculator, Talker):
    pass


if __name__ == '__main__':
    # s = Secretive()
    # s.accessable()
    # s.__inaccesable()

    f = Filter()
    f.init()
    print(f.filter([1, 2, 3]))

    s = SPAMFilter()
    s.init()
    print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'SPAM', 'SPAM', 'egg']))
