import datetime
class Logger:
    def __init__(self):
        self.file = open('logs.txt', 'a')
    def printe(self,error):
        date = datetime.datetime.now().strftime("%H:%M:%S %m/%d/%Y")
        print(error)
        self.file.write(f"{date} Error: {error}\n")
        self.file.flush()
    def close(self):
        self.file.close()