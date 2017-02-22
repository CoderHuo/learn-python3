#!/usr/bin/env python3
# -*- coding: utf-8 -*
from enum import Enum, unique

__author__ = 'Mr.Huo'

# 常量
# month类型的枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


def main():
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)
    for day, member in Weekday.__members__.items():
        print(day, '=>', member, ',', member.value)
    print(Weekday.Wed,'=>',Weekday.Wed.value)
    print(Weekday['Tue'],'=>',Weekday['Tue'].value)
    print(Weekday(1),'=>',Weekday(1).value)


if __name__ == '__main__':
    main()
