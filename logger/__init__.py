import logging
import os
import ctypes
from multiprocessing import Queue
from logging.handlers import QueueHandler

__all__ = ['ConsoleLogger', 'ConQueueLogger', 'FileLogger', 'ConFileLogger']


class ConsoleColor:
    if os.name == 'nt':
        #
        __stdInputHandle = -10
        __stdOutputHandle = -11
        __stdErrorHandle = -12
        # Windows foreGround color
        __foreGroundBLACK = 0x00  # black.
        __foreGroundDARKBLUE = 0x01  # darkBlue.
        __foreGroundDARKGREEN = 0x02  # darkGreen.
        __foreGroundDARKSKYBLUE = 0x03  # darkSkyBlue.
        __foreGroundDARKRED = 0x04  # darkRed.
        __foreGroundDARKPINK = 0x05  # darkPink.
        __foreGroundDARKYELLOW = 0x06  # darkYellow.
        __foreGroundDARKWHITE = 0x07  # darkWhite.
        __foreGroundDARKGRAY = 0x08  # darkGray.
        __foreGroundBLUE = 0x09  # blue.
        __foreGroundGREEN = 0x0a  # green.
        __foreGroundSKYBLUE = 0x0b  # skyBlue.
        __foreGroundRED = 0x0c  # red.
        __foreGroundPINK = 0x0d  # pink.
        __foreGroundYELLOW = 0x0e  # yellow.
        __foreGroundWHITE = 0x0f  # white.
        # Windows back ground color
        __backGroundDARKBLUE = 0x10  # darkBlue.
        __backGroundDARKGREEN = 0x20  # darkGreen.
        __backGroundDARKSKYBLUE = 0x30  # darkSkyBlue.
        __backGroundDARKRED = 0x40  # darkRed.
        __backGroundDARKPINK = 0x50  # darkPink.
        __backGroundDARKYELLOW = 0x60  # darkYellow.
        __backGroundDARKWHITE = 0x70  # darkWhite.
        __backGroundDARKGRAY = 0x80  # darkGray.
        __backGroundBLUE = 0x90  # blue.
        __backGroundGREEN = 0xa0  # green.
        __backGroundSKYBLUE = 0xb0  # skyBlue.
        __backGroundRED = 0xc0  # red.
        __backGroundPINK = 0xd0  # pink.
        __backGroundYELLOW = 0xe0  # yellow.
        __backGroundWHITE = 0xf0  # white.

        stdOutHandle = ctypes.windll.kernel32.GetStdHandle(__stdOutputHandle)

        @staticmethod
        def setCmdColor(color, handle=stdOutHandle):
            return ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)

        def resetCmdColor(self):
            self.setCmdColor(self.__foreGroundDARKWHITE)

        def setCmdDarkGreen(self, mode=''):
            return self.setCmdColor(self.__foreGroundGREEN)

        def setCmdBlue(self, mode=''):
            return self.setCmdColor(self.__foreGroundBLUE)

        def setCmdYellow(self, mode=''):
            return self.setCmdColor(self.__foreGroundYELLOW)

        def setCmdRed(self, mode=''):
            return self.setCmdColor(self.__foreGroundRED)

        def setCmdPurple(self, mode=''):
            return self.setCmdColor(self.__foreGroundPINK)


    else:
        # linux
        #   \033[1;31;40m
        #   \033[0m

        STYLE = {
            # foreGround color
            'fore': {
                'black': 30,
                'red': 31,
                'green': 32,
                'yellow': 33,
                'blue': 34,
                'purple': 35,
                'cyan': 36,
                'white': 37,
            },
            # backGround color
            'back': {
                'black': 40,
                'red': 41,
                'green': 42,
                'yellow': 43,
                'blue': 44,
                'purple': 45,
                'cyan': 46,
                'white': 47,
            },
            # mode
            'mode': {
                'mormal': 0,
                'bold': 1,
                'underline': 4,
                'blink': 5,
                'invert': 7,
                'hide': 8,
            },
            'default': {'end': 0, },
        }

        def setCmdColor(self, mode='', fore='', back=''):
            mode = '%s' % self.STYLE['mode'][mode] if mode in self.STYLE['mode'] else ''
            fore = '%s' % self.STYLE['fore'][fore] if fore in self.STYLE['fore'] else ''
            back = '%s' % self.STYLE['back'][back] if back in self.STYLE['back'] else ''
            style = ';'.join([s for s in [mode, fore, back] if s])
            style = '\033[%sm' % style if style else ''
            return style

        def resetCmdColor(self):
            return '\033[m'

        def setCmdDarkGreen(self, mode=''):
            return self.setCmdColor(mode=mode, fore='green')

        def setCmdBlue(self, mode=''):
            return self.setCmdColor(mode=mode, fore='blue')

        def setCmdYellow(self, mode=''):
            return self.setCmdColor(mode=mode, fore='yellow')

        def setCmdRed(self, mode=''):
            return self.setCmdColor(mode=mode, fore='red')

        def setCmdPurple(self, mode=''):
            return self.setCmdColor(mode=mode, fore='purple')


consoleColor = ConsoleColor()


class ConsoleLogger:
    def __init__(self, logname='streamLog', clevel=logging.DEBUG):
        self.logger = logging.getLogger(logname)
        self.logger.setLevel(logging.DEBUG)
        self.timeFormat = '%Y-%m-%d %H:%M:%S.%d'
        self.logFormat = '[%(asctime)s%(msecs)d] [%(levelname)8s] [%(name)s] %(message)s'
        self.format = logging.Formatter(self.logFormat, self.timeFormat)
        # set CMD logger
        self.sh = logging.StreamHandler()
        self.sh.setFormatter(self.format)
        self.sh.setLevel(clevel)
        if os.name == 'posix':
            self.__darkGreenFormat = consoleColor.setCmdDarkGreen() + self.logFormat + consoleColor.resetCmdColor()
            self.__blueFormat = consoleColor.setCmdBlue() + self.logFormat + consoleColor.resetCmdColor()
            self.__yellowFormat = consoleColor.setCmdYellow() + self.logFormat + consoleColor.resetCmdColor()
            self.__redFormat = consoleColor.setCmdRed() + self.logFormat + consoleColor.resetCmdColor()
            self.__purpleFormat = consoleColor.setCmdPurple() + self.logFormat + consoleColor.resetCmdColor()
        self.logger.addHandler(self.sh)

    def __setCmdGreen(self):
        if os.name == 'nt':
            consoleColor.setCmdDarkGreen()
        else:
            self.sh.setFormatter(logging.Formatter(self.__darkGreenFormat, self.timeFormat))

    def __setCmdBlue(self):
        if os.name == 'nt':
            consoleColor.setCmdBlue()
        else:
            self.sh.setFormatter(logging.Formatter(self.__blueFormat, self.timeFormat))

    def __setCmdYellow(self):
        if os.name == 'nt':
            consoleColor.setCmdYellow()
        else:
            self.sh.setFormatter(logging.Formatter(self.__yellowFormat, self.timeFormat))

    def __setCmdRed(self):
        if os.name == 'nt':
            consoleColor.setCmdRed()
        else:
            self.sh.setFormatter(logging.Formatter(self.__redFormat, self.timeFormat))

    def __setCmdPurple(self):
        if os.name == 'nt':
            consoleColor.setCmdPurple()
        else:
            self.sh.setFormatter(logging.Formatter(self.__purpleFormat, self.timeFormat))

    def __resetCmd(self):
        if os.name == 'nt':
            consoleColor.resetCmdColor()
        else:
            self.sh.setFormatter(self.format)

    def debug(self, msg, *args, **kwargs):
        self.__setCmdGreen()
        self.logger.debug(msg, *args, **kwargs)
        self.__resetCmd()

    def info(self, msg, *args, **kwargs):
        self.__setCmdBlue()
        self.logger.info(msg, *args, **kwargs)
        self.__resetCmd()

    def warning(self, msg, *args, **kwargs):
        self.__setCmdYellow()
        self.logger.warning(msg, *args, **kwargs)
        self.__resetCmd()

    def error(self, msg, *args, **kwargs):
        self.__setCmdRed()
        self.logger.error(msg, *args, **kwargs)
        self.__resetCmd()

    def critical(self, msg, *args, **kwargs):
        self.__setCmdPurple()
        self.logger.critical(msg, *args, **kwargs)
        self.__resetCmd()

    fatal = critical

    def green(self, msg, *args, **kwargs):
        self.__setCmdGreen()
        self.logger.info(msg, *args, **kwargs)
        self.__resetCmd()

    def blue(self, msg, *args, **kwargs):
        self.__setCmdBlue()
        self.logger.info(msg, *args, **kwargs)
        self.__resetCmd()

    def yellow(self, msg, *args, **kwargs):
        self.__setCmdYellow()
        self.logger.info(msg, *args, **kwargs)
        self.__resetCmd()

    def red(self, msg, *args, **kwargs):
        self.__setCmdRed()
        self.logger.info(msg, *args, **kwargs)
        self.__resetCmd()

    def purple(self, msg, *args, **kwargs):
        self.__setCmdPurple()
        self.logger.info(msg, *args, **kwargs)
        self.__resetCmd()


class ConQueueLogger(ConsoleLogger):
    def __init__(self, queue, logname='streamLog', clevel=logging.DEBUG, qlevel=logging.DEBUG):
        super().__init__(logname=logname, clevel=clevel)
        self.qh = QueueHandler(queue)
        self.qh.setFormatter(self.format)
        self.qh.setLevel(qlevel)
        self.logger.addHandler(self.qh)


class ConFileLogger(ConsoleLogger):
    def __init__(self, file, logname='streamLog', clevel=logging.DEBUG, flevel=logging.DEBUG):
        super().__init__(logname=logname, clevel=clevel)
        self.fh = logging.FileHandler(file)
        self.fh.setFormatter(self.format)
        self.fh.setLevel(flevel)
        self.logger.addHandler(self.fh)


class FileLogger:

    def __init__(self, path, logname='QueueFile', level=logging.DEBUG):
        self.logger = logging.getLogger(logname)
        self.logger.setLevel(level)
        self.timeFormat = '%Y-%m-%d %H:%M:%S.%d'
        self.logFormat = '[%(asctime)s%(msecs)d] [%(levelname)8s] [%(name)s] %(message)s'

        self.format = logging.Formatter(self.logFormat, self.timeFormat)
        self.fh = logging.FileHandler(path)
        self.fh.setFormatter(self.format)
        self.logger.addHandler(self.fh)

    def __call__(self, queue):
        while not queue.empty():
            try:
                record = queue.get(timeout=10)
                self.logger.handle(record)
            except Exception:
                import sys, traceback
                print('Whoops! Problem:', file=sys.stderr)
                traceback.print_exc(file=sys.stderr)


if __name__ == '__main__':
    queue = Queue()
    logyyx = ConFileLogger('yxy.log')
    logyyx.debug('debug')
    logyyx.info('info')
    logyyx.warning('warning')
    logyyx.error('error')
    logyyx.critical('critical')
    logyyx.critical(123)
    logyyx.info('info' + str(123) + 'aaaaaa')

    logyyx.red('hahahahah')
    FileLogger('yyx.log')(queue)
