#You want to make your objects support the context-management protocol (the with statement). __enter__ & __exit__



class Connection:
    def __init__(self, address):
        self.url = address


    def __enter__(self):
        print('entering', self.url)

    def __exit__(self, exc_ty, exc_val, tb):
        print('leaving', self.url)


if __name__ == '__main__':
    with Connection('https://finxter.com') as finxter:
        # Called finxter.__enter__()
        pass
        # Called finxter.__exit__()
