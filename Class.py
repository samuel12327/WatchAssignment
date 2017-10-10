class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def setHour(self, value):
        self.__hour = value

    def setMinute(self, value):
        self.__minute = value

    def setSecond(self, value):
        self.__second = value

    def setTime(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def toString(self):
        if self.__hour<10:
            y = "0" + str(self.__hour)
        else:
            y = str(self.__hour)
        if self.__minute < 10:
            x = "0" + str(self.__minute)
        else:
            x = str(self.__minute)
        if self.__second < 10:
            z = "0" + str(self.__second)
        else:
            z = str(self.__second)

        print(y+":"+x+":"+z)
    def nextSecond(self):
        self.__second = self.__second + 1

    def previousSecond(self):
        self.__second = self.__second - 1
