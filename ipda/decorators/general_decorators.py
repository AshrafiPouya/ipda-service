import gc

def del_and_collect(attribute_name):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)  
            if hasattr(self, attribute_name):
                delattr(self, attribute_name)
                gc.collect()
            return result
        return wrapper
    return decorator
