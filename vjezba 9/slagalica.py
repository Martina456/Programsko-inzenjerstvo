class Polje():


    def __init__(self, broj = 0):
        self.__broj = broj

    def vratiBroj(self):
        return self.__broj

    @property
    def jeBroj(self):
        if self.__broj > 0:
            return True
        return False

    @property
    def jePrazno(self):
        if self.__broj <= 0:
            return True
        return False

    '''
    Implementiraj stringovnu reprezentaciju __str__() koja će vratiti:
        broj 'n' ako je broj polja n > 0
        razmak ' ' ako je broj polja = 0
    Implementiraj reprezentaciju __Repr__() koja će vratiti string kojim se stvara objekt od te klase
    '''

    def __str__(self):
        broj = self.vratiBroj()
        if broj > 0:
            return str(broj)
        elif broj == 0:
            return " "

    def __repr__(self):
        return "Polje({})".format(self.vratiBroj())