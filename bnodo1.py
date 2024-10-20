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

if __name__ == "__main__":

    bn0 = bnodo()
    print(bn0)

    bnR = bnodo(22)
    print(bnR)
    
    bnR.setIZ(bnodo(11))
    print(bnR)    
    
    bnR.setDE(bnodo(33))    
    print(bnR)    