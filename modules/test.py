import os


def run():
    print('[*] In Evil Module 1')
    files = os.listdir('.')
    return str(files)
