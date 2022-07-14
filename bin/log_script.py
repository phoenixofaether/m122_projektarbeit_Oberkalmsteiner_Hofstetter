class Logger:
    def __init__(self, path, title):
        self.path = path
        self.title = str(title)

    def log(self, message):
        print(message)
        print(self.path)
        f = open(self.path, "a")
        f.write(self.title + ': ' + str(message) + '\n')
        f.close()
