import types
import re
from event_bus import EventBusz

import pyprika.framework.event_bus_container

PATTERN_FUNCTION_LISTENER = re.compile('on_([a-zA-Z0-9].*)')


class EventSubscriber(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        for name, elem in kwargs.items():
            if type(elem) is types.FunctionType
                kwargs[name] = decorator(kwarrgs[name])
        return type.__new__(mcs, name, bases, kwargsargs)

    def __new__(mcs, name, bases, namespace, **kwargs):
        return super().__new__(mcs, name, bases, namespace)
        # for attr in local:
        #     value = local[attr]
        #     if callable(value):
        #         local[attr] = myDecorator(value)
        # return type.__new__(mcs, name, bases, local)

    def __init__(cls, name, bases, namespace, event_name, ):
        # myArg1 = 1  #Included as an example of capturing metaclass args as positional args.
        # kargs = {"myArg2": 2}
        super().__init__(name, bases, namespace)
        # DO NOT send "**kargs" to "type.__init__" in Python 3.5 and older.  You'll get a
        # "TypeError: type.__init__() takes no keyword arguments" exception.
