class BaseDecorator:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        function_name = func.__name__
        if hasattr(self, function_name) and callable(getattr(self, function_name)):
            if getattr(self, function_name)():
                return func
            else:
                print(f'Permission denied for {function_name}')
        else:
            print(f'Permission check method not found for {function_name}')