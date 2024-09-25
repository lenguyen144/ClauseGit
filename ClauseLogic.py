class Clause:
    def __init__(self, name, status):
        self.name = name
        self.status = status
        self.listOpera = []
    def __eq__(self, other):
        return self.name == other.name

    @staticmethod
    def phep_Hoi(a, b):
        if a == 1 and b == 1:
            return 1
        else:
            return 0

    @staticmethod
    def phep_Tuyen(a, b):
        if a == 0 and b == 0:
            return 0
        else:
            return 1

    @staticmethod
    def phep_PhuDing(a):
        if a == 0:
            return 1
        else:
            return 0

    @staticmethod
    def phep_KeoTheo(a,b):
        if a==1 and b == 0:
            return 0
        else:
            return 1

    @staticmethod
    def phep_TuongDuong(a, b):
        if a == b:
            return 1
        else:
            return 0

    @staticmethod
    def tinh(a, b, phep_Tinh):
        if phep_Tinh == "/\\":
            return Clause.phep_Hoi(a,b)
        elif phep_Tinh == "\\/":
            return Clause.phep_Tuyen(a, b)
        elif phep_Tinh == "->":
            return Clause.phep_KeoTheo(a, b)
        elif phep_Tinh == "<>":
            return Clause.phep_TuongDuong(a, b)

        
    
           