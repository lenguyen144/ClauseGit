from ClauseLogic import Clause

s = """cac phep tinh trong menh de: 
        -phep hoi: /\\
        -phep tuyen: \\/
        -phep keo theo(suy ra): ->
        -phep tuong duong: <>
        -hien tai van chua co phep phu dinh!, se cap nhat sau, xin tran trong"""
print(s)
strClause = input("ban hay nhap mot menh de: \n")
print("bang giai tri chan ly \n")
listClauses = []
listIndex = []


def printClauses(listClause):
    a = ""
    for i in listClause:
        a = a + "{0}: {1}   ".format(i.name, i.status)
    a = a + strClause + ': ' + str(standardizeClausePlus(strClause))
    print(a)

def findParentheses(index ,string):
    count = 0
    for i in range(index, len(string)):
        if string[i] == "(":
            count = count + 1
        elif string[i] == ")":
            count = count - 1
            if count == 0:
                return i


def analysisClause(clause):
    for s in clause:
        if (ord(s) >= 97) and (ord(s) <= 122):
            a = Clause(s, 2)
            if a not in listClauses:
                listClauses.append(a)

def standardizeClause(string):
    i = 0
    newList = []
    while i < len(string):
        if (ord(string[i]) >= 97) and (ord(string[i]) <= 122):
            a = Clause(string[i], 2)
            newList.append(listClauses.index(a))
        elif string[i] == "(":
            end = findParentheses(i , string)
            newList.append(standardizeClause(string[i + 1:end]))
            i = end - 1
        i = i + 1
    return newList

def standardizeClausePlus(string):
    i = 0
    logic = 2
    if (ord(string[i]) >= 97) and (ord(string[i]) <= 122):
        a = Clause(string[i], 2)
        index = listClauses.index(a)
        logic = listClauses[index].status
    elif string[i] == "(":
        end = findParentheses(i, string)
        logic = standardizeClausePlus(string[i + 1:end])
        i = end

    while i < len(string):
        if string[i:i+2] == "/\\" or string[i:i+2] == "\\/" or string[i:i+2] == "->" or string[i:i+2] == "<>":
            if  (ord(string[i+2]) >= 97) and (ord(string[i+2]) <= 122):
                a = Clause(string[i+2], 2)
                index = listClauses.index(a)
                a = listClauses[index].status
                logic = Clause.tinh(logic, a, string[i:i+2])
            elif string[i+2] == "(":
                end = findParentheses(i + 2, string)
                a = standardizeClausePlus(string[i + 3:end])
                logic = Clause.tinh(logic, a, string[i:i+2])
                i = end - 1
        i = i + 1
    return logic
               

def possibleValueProposition(count):
    if count != len(listClauses) - 1:
        listClauses[count].status = 0
        possibleValueProposition(count + 1)

        listClauses[count].status = 1
        possibleValueProposition(count + 1)
    elif count == len(listClauses) - 1:
            listClauses[count].status = 0
            printClauses(listClauses)

            listClauses[count].status = 1
            printClauses(listClauses)


if  __name__ == "__main__":
    analysisClause(strClause)
    possibleValueProposition(0)
    listIndex = standardizeClause(strClause)

     