from abc import  ABC, abstractmethod

class Car(ABC):
    
    def __init__(self):
        self.acceleretaion=0
        self.velocity=0
    
    @abstractmethod
    def power(self):
        pass
    
    def run(self):
        self.velocity+=self.acceleretaion
    
    def getVelocity(self):
        return self.velocity
    
    def getAcceleretaion(self):
        return self.acceleretaion
    
    
class BoostCar(ABC):
    
    @abstractmethod
    def Boost(self):
        pass
    
    
class AirCondition(ABC):
    
    @abstractmethod
    def Open(self):
        pass
    
    
    
class Ferrari(Car,BoostCar,AirCondition):
    
    def power(self):
        self.acceleretaion = 10
        
    def Boost(self):
        self.velocity *= 2
        
    def Open(self):
        self.acceleretaion *= 0.9
      
        
class Mercedes(Car,BoostCar):
    
    def power(self):
        self.acceleretaion = 7
        
    def Boost(self):
        self.velocity *= 2
     
        
class Tofas(Car,AirCondition):
    
    def power(self):
        self.acceleretaion = 5
        
    def Open(self):
        self.acceleretaion *= 0.9
     
        
def main():
    
    ferrari = Ferrari()
    mercedes = Mercedes()
    tofas = Tofas()
    
    ferrari.power()
    mercedes.power()
    tofas.power()
    
    print("\n****** Ferrari ******")
    print("İlk Hız:",ferrari.getVelocity())
    
    ferrari.run()
    print("Hızlandıktan sonra:",ferrari.getVelocity())
    
    ferrari.Boost()
    ferrari.run()
    print("Turbodan sonra:",ferrari.getVelocity())
    
    ferrari.Open()
    ferrari.run()
    print("Klimadan sonra:",ferrari.getVelocity())
    
    
    
    print("\n****** Mercedes ******")
    print("İlk Hız:",mercedes.getVelocity())
    
    mercedes.run()
    print("Hızlandıktan sonra:",mercedes.getVelocity())
    
    mercedes.Boost()
    mercedes.run()
    print("Turbodan sonra:",mercedes.getVelocity())
    
    
    
    print("\n****** Tofas ******")
    print("İlk Hız:",tofas.getVelocity())
    tofas.run()
    print("Hızlandıktan sonra:",tofas.getVelocity())
    tofas.Open()
    tofas.run()
    print("Klimadan sonra:",tofas.getVelocity())
    

if  __name__ == "__main__":
    main()