numbers_strings = ("1" ,"2" ,"3" ,"4" ,"5")

def print_str(first, *second):
    print(first)
    print(second)

if __name__ == "__main__":
    print_str(*numbers_strings)  # 注意这里的*numbers_strings
    my_book = {"first": "小当家", "seoncd": "我是baby"}
    def my_blood(**kwargs):
        print(kwargs)
    my_blood(**my_book)  # 作为一个字典对象传入
    my_blood(**my_book)  # 一个一个的关键字参数传入

    from functools import wraps


    class logit(object):
        def __init__(self, logfile='out.log'):
            self.logfile = logfile

        def __call__(self, func):
            @wraps(func)
            def wrapped_function(*args, **kwargs):
                log_string = func.__name__ + " was called"
                print(log_string)
                # 打开logfile并写入
                with open(self.logfile, 'a') as opened_file:
                    # 现在将日志打到指定的文件
                    opened_file.write(log_string + '\n')
                # 现在，发送一个通知
                self.notify()
                return func(*args, **kwargs)

            return wrapped_function


        def notify(self):
            # logit只打日志，不做别的
            pass
