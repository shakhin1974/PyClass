class Abitur:
    def __init__(self, name:str, age:int, pol:str, sr:float):
        self.__name = name
        self.__age = age
        self.__pol = pol
        self.__sr = sr
    def get_name(self):
         return  self.__name 
    def set_name(self, name):
        self.__name = name 
    def get_age(self):
        if 0 <self.__age < 45:
            return self.__age 
        else:
            return 0 
    def set_age(self, age):
        if 0 <age < 45:
            self.__age = age
        else:
            self.__age = 0
    def vivod (self):
        print("Имя :", self.__name,   "Возраст:",   self.get_age(),   "Пол: ", self.__pol )
    
    def __del__(self):
        print (self.__name,  "удален")

Ivan = Abitur("Иван", 124, 'м', 4.6)
Ivan.vivod()
Ivan.set_name("Кирилл")
Ivan.vivod()
Ivan.set_age(25)
Ivan.vivod()

