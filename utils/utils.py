import hashlib
from datetime import datetime


def gen_random_md5():
    return hashlib.md5(str(datetime.now().timestamp()).encode()).hexdigest()



def md5(value):
    return hashlib.md5(str(value).encode()).hexdigest()