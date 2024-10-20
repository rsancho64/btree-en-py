#! /usr/bin/python3

class bnodo:

    __info = None
    __de = None
    __iz = None

    def __init__(self,info = None) -> None:
        self.__info = info


    def __str__(self) -> str:
        answ = "("
        if self.__iz == None:
            answ += "(.)"
        answ += str(self.__info)
        if self.__de == None:
            answ += "(.)"
        answ += ")"
        return answ

if __name__ == "__main__":

    bn0 = bnodo()
    print(bn0)

