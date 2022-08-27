def singleton(class_name):
    instances = dict()
    def wrap(*args, **kwargs):
        if class_name not in instances:
            instances[class_name] = class_name(*args, **kwargs)
        return instances[class_name]
    return wrap
