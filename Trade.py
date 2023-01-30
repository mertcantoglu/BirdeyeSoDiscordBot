class Trade:
    def __init__(self,time,_type,value) -> None:
        self.time = time
        self.type = _type
        self.value = value
        
    def __str__(self) -> str:
        return f"{self.time}\t{self.type}\t{self.value}"