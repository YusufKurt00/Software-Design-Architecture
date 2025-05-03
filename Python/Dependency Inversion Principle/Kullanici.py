class Kullanici:
    
    def __init__(self,isim=None,mail=None,ip=None,tel=None):
        self.isim=isim
        self.mail=mail
        self.ip=ip
        self.tel=tel
    
    def getİsim(self):
        return self.isim
    
    def setİsim(self,isim):
        self.isim=isim
        
    def getMail(self):
        return self.mail
    
    def setMail(self,mail):
        self.mail=mail
        
    def getİp(self):
        return self.ip
    
    def setİp(self,ip):
        self.ip=ip
        
    def getTel(self):
        return self.tel
    
    def setTel(self,tel):
        self.tel=tel
        