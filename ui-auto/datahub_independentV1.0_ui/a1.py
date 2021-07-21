class T1:
    def __init__(self, id):
        self.id = id

    @property
    def text(self):
        return self.id

if __name__ == '__main__':
    a = T1('123')
    print(a.text())



