#! /usr/bin/python3
class bnodo:

    __info = None  ## item: objeto NO instancia de bnodo.
    __de = None    ## item: un bnodo o None.
    __iz = None    ## item: un bnodo o None.

    def __init__(self, info = None) -> None:
        self.setInfo(info)

    def __str__(self) -> str:
        answ = "("

        if self.__iz: answ += str(self.__iz)
        else: answ += ". "

        answ += f" {str(self.__info)} "

        if self.__de: answ += str(self.__de)
        else: answ += " ."

        answ += ")"
        return answ

    def setInfo(self, info):
        if isinstance(info, bnodo):
            raise ValueError("bnodo.setInfo: unable inform bnodo w bnodo.")
        self.__info = info

    def getInfo(self) -> object:
        return self.__info

    def setIZ(self, bn):
        self.__iz = bn

    def getIZ(self) -> object:
        if self.__iz: return self.__iz
        # return bnodo()  # a void new one? NO
        return None

    def setDE(self, bn):
        self.__de = bn  # sea lo que sea.

    def getDE(self) -> object:
        if self.__de: return self.__de
        # return bnodo()  # a void new one? NO
        return None

def print_bnodo(unbnodo):
    print(str(unbnodo))
    print("izq: ", unbnodo.getIZ())
    print("inf: ", unbnodo.getInfo())
    print("der: ", unbnodo.getDE())
    print()


if __name__ == "__main__":

    bnR = bnodo()
    print_bnodo(bnR)

    bnR.setInfo(22)
    print_bnodo(bnR)

    try:
        bnR.setInfo(bnodo(11))    # raise ValueError
        print_bnodo(bnR)
    except ValueError:
        print("main: dato bnodo no entró como info de un bnodo")
  
    bnR.setIZ(11)
    print_bnodo(bnR)

    bnR.setDE(bnodo(33))
    print_bnodo(bnR)

    bnR.setIZ(bnodo(11))
    print_bnodo(bnR)
    
    # print(type(bnR.getDE()))
    # bn = bnR.getDE()
    # print(bn)    
    # print("iz: ", bn.getIZ())
    # print("de: ", bn.getDE())
    
    # bn.setDE(bnodo(44))
    # print(bn)    
    # print("iz: ", bn.getIZ())
    # print("de: ", bn.getDE())
    
    # print(bnR)    
    # print("iz: ", bnR.getIZ())
    # print("de: ", bnR.getDE())
    