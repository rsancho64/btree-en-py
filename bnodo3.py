#! /usr/bin/python3

class bnodo:

    __info = None
    __de = None
    __iz = None

    def __init__(self,info = None) -> None:
        self.__info = info


    def __str__(self) -> str:
        answ = "("

        if self.__iz: answ += str(self.__iz)
        else: answ += ". "

        answ += f" {str(self.__info)} "

        if self.__de: answ += str(self.__de)
        else: answ += " ."

        answ += ")"
        return answ

    def setIZ(self, bn):
        self.__iz = bn

    def setDE(self, bn):
        self.__de = bn

    def getIZ(self) -> object:
        if self.__iz: return self.__iz
        # return bnodo()  # a void new one? NO
        return None

    def getDE(self) -> object:
        if self.__de: return self.__de
        # return bnodo()  # a void new one? NO
        return None

if __name__ == "__main__":

    bn0 = bnodo("zero")
    print(bn0)    
    print("iz: ", bn0.getIZ())
    print("de: ", bn0.getDE())

    bnR = bnodo(22)
    print(bnR)    
    print("iz: ", bnR.getIZ())
    print("de: ", bnR.getDE())

    bnR.setIZ(bnodo(11))
    print(bnR)    
    print("iz: ", bnR.getIZ())
    print("de: ", bnR.getDE())
    
    bnR.setDE(bnodo(33))
    print(bnR)    
    print("iz: ", bnR.getIZ())
    print("de: ", bnR.getDE())
    
    print(type(bnR.getDE()))
    bn = bnR.getDE()
    print(bn)    
    print("iz: ", bn.getIZ())
    print("de: ", bn.getDE())
    
    bn.setDE(bnodo(44))
    print(bn)    
    print("iz: ", bn.getIZ())
    print("de: ", bn.getDE())
    
    print(bnR)    
    print("iz: ", bnR.getIZ())
    print("de: ", bnR.getDE())
    