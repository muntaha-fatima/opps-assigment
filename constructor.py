
# **** ____________________ Assigment 13______________***


class logger:
    def __init__(self):
        print('object banai gy - constructer - called!')

    def __del__(self):
        print('object destory ho gaya - destructer - called!')

log = logger()

del log