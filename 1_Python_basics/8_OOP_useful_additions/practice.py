# class MyClass:
#
#     def m_1(self, p_1):
#         print(f'{self.m_2(p_1)}')
#
#     @staticmethod
#     def m_2(p_2):
#         print(f'{p_2 ** 2}')
#
#
# my_class = MyClass()
# my_class.m_1(55)


# class MyClass:
#
#     def m_1(self, p_1):
#         return f'{p_1 ** 2}'
#
#     @staticmethod
#     def m_2(p_1):
#         print(f'{MyClass().m_1(p_1)}')
#
#
# my_class = MyClass()
# my_class.m_2(55)

# class MyClass:
#
#     def __init__(self, num):
#         self.num = num
#
#     def m_1(self, p_1):
#         return f'{p_1 ** 2}'
#
#     @staticmethod
#     def m_2():
#         print(f'{MyClass(33).num}')


class MyClass:

    def __init__(self, num):
        self.num = num

    def m_1(self, p_1):
        return f'{p_1 ** 2}'

    @staticmethod
    def m_2():
        return f'{MyClass(33).num}'

    # @classmethod
    # def m_3(cls, num):
    #     print(cls(4).m_1(6))

    @classmethod
    def m_3(cls, num):
        print(cls(4).num)


my_class = MyClass(56)
my_class.m_3(45)
MyClass.m_3(45)
