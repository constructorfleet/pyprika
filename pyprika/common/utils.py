import inspect


def auto_init():
    """Automatically set __init__ parameters to class attributes"""
    frame = inspect.currentframe(1)
    params = frame.f_locals
    self = params['self']
    param_names = frame.f_code.co_varnames[1:]  # ignore self
    for name in param_names:
        setattr(self, name, params[name])
