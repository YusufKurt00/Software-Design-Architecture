from abc import ABC , abstractmethod

class ILogger(ABC):
    
    @abstractmethod
    def write(self,message: str):
        pass
    
class IConnection(ABC):
    
    @abstractmethod
    def open_connection(self):
        pass
    
    def close_connection(self):
        pass
    
class ConsoleLogger(ILogger):
    
    def  write(self,message: str):
        print(message)

class DB:
    
    def __init__(self):  
        self.list=[]
        self.check=False
        
    def gettList(self):
        
        return self.list
    
    def add_Log(self,message: str):
        
        if self.check:
            self.list.append(message)
            
    def open_db(self):
        
        print("DB ile bağlantı kuruldu")
        self.check= True
        
    def clsoe_db(self):
        
        print("DB ile bağlantı kurulamadı")
        self.check= False

class DBLogger(ILogger,IConnection):
    
    def __init__(self):
        self.data=DB()
        
    def write(self, message: str):
        self.data.add_Log(message)
        
    def open_connection(self):
        self.data.open_db()
        
    def close_connection(self):
        self.data.clsoe_db()
        
        
if __name__ =="__main__":
    
    db_logger = DBLogger()
    console_logger = ConsoleLogger()
    db_logger.write("Log 1")
    db_logger.open_connection()
    db_logger.write("Log 2")

    console_logger.write("Log 3")
    db_logger.write("Log 4")
    db_logger.close_connection()
    db_logger.write("Log 5")
    
    for message in db_logger.data.gettList():
        print(message)