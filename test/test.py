class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singletonクラス")
        else:
            Singleton.__instance = self

#インスタンスが生成できる
class Singleton_2():
    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance

class Singleton_3():
    __instance = None

    def __init__(self):
        raise NotImplementedError("not allowed")

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance

class Singleton_4():
    __instance = None

    def __new__(cls):
        raise NotImplementedError("Cannot initialize via Constructor")

    @classmethod
    def __internal_new_(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = cls.__internal_new_()

        return cls.__instance

class Dog(object):
    def __init__(self, name):
        self.name = name

class UltraDog(Dog):
    def __init__(self, name, type):
        super(UltraDog, self).__init__(name)
        self.type = type

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def say_name(self):
        print("私の名前は" + self.name + "です．年齢は" + str(self.age) + "歳です")


if __name__ == "__main__":
    ud1 = UltraDog("taro", "akita")
    print(ud1.name)
