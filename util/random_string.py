import os
import random
import string

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


def randomString(lengthOfString):
    # lengthOfString = 10
    res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase +
                                 string.digits, k=lengthOfString))
    return res


# print(randomString())


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
