#!/usr/bin/env python3

import functools

def decoDbg(funk):
    """ Print function signature and return value """
    @functools.wraps(funk)
    def wrapper(*args, **kwargs):
        arguments = [repr(a) for a in args]
        kw_args = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(arguments + kw_args)
        print(f"Calling {funk.__name__}({signature})")
        value = funk(*args, **kwargs)
        print(f"{funk.__name__} returned {value!r}")
        if value is not None:
            return value
    return wrapper

def logFnCall(funk):
    """ Logs function calls with arguments """
    @functools.wraps(funk)
    def wrapper(*args, **kwargs):
        arguments = [repr(a) for a in args]
        kw_args = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(arguments + kw_args)
        with open('callLog.txt', mode ='a') as loger:
            loger.write(f"Calling {funk.__name__}({signature})\n")
        return funk(*args, **kwargs)
    return wrapper


def applyOP(opFunk):
    """ Wraps operation function for every article in inventory yml file """
    def wrapper(*args, **kwargs):
        import yaml
        from swacc import filters

        with open(kwargs['ymlfile'], mode='r') as file:
            ymlparsed = yaml.load(file, Loader=yaml.FullLoader)
            for yt in filters.gen_dict_extract(ymlparsed['all'], kwargs['location']):
                for ft in filters.getdictkids(yt, kwargs['location']):
                    # opFunk(*args, **kwargs)
                    opFunk(name=ft[0], ip=ft[1], *args, **kwargs)
    return wrapper
