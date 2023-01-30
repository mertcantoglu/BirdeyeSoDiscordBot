class Trade:
    def __init__(self,time,_type,value) -> None:
        self.time = time
        self.type = _type
        self.value = value
        self.numberOfEmoji = self.calcEmoji()
        
    def __str__(self) -> str:
        return f"{self.time}\t{self.type}\t{self.value}\t{self.numberOfEmoji}"
    
    def calcEmoji(self):
        return int(float(self.value.split(">")[1].split("$")[0].replace(",",""))/10)