#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
python的下划线
"""
__author__ = 'Mr.Huo'


class A():
    # 私有变量会被
    __name = 'private name'

    def __init__(self):
        self._private = 'private'
        self.__name = 'haha'

    def _internal_use(self):
        print(self.__name)
        pass

    def __method_name(self):
        pass


class B(A):
    def __method_name(self):
        pass


def main():
    # 单下划线 "_"
    # 1：在解释器中：'_'代表交互式解释器会话中上一条执行语句的结果
    # 2：作为一个名称：'_'作为不会在后面用到的临时性的名称使用(概念上的，但是实际上还是可以跟普通的临时变量一样)
    for _ in range(10):
        print(_)
    # 3：国际化：'_' 被用作函数，它通常用于实现国际化和本地化字符串之间翻译查找的函数名称,2、3不能同时存在
    # 没明白... 后续再看
    """
    from django.utils.translation import ugettext as _
    from django.http import HttpResponse
    def my_view(request):
        output = _("Welcome to my site.")
        return HttpResponse(output)
    """
    # 名称前的单下划线，指定该名称属性为“私有”，不能被from <模块/包名> import * 导入，
    # 除非模块或包中的“__all__”列表显式地包含了它们
    # 但是import a_module 这样导入模块，仍然可以用 a_module._some_var 这样的形式访问到这样的对象
    # _private_name = 'private_name'
    A()._internal_use()
    B()._internal_use()
    B()._A__name = 'HAHA'
    print(B()._A__name)
    B()._internal_use()
    A().__class__._A__name = 'HAHA'
    print(B()._A__name)
    B()._internal_use()

    # 名称前的双下划线'__' __spam 这种形式（至少两个前导下划线，最多一个后续下划线）的任何标识符
    # 将会被“_classname__spam”这种形式原文取代，在这里“classname”是去掉前导下划线的当前类名
    # (非虚方法)
    print(dir(A()))
    print(dir(B()))

    # 名称前后都有双下划线'__'，系统定义名字 如 __class__ __dir__ __init__ __all__,有特殊用法

    """
    名称前的下划线只是一种约定，只对于类的私有成员做了改名处理，其他的没有保护机制，实际还是可以访问他们
    """


if __name__ == '__main__':
    main()
