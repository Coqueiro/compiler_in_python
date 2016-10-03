from action_table import *
import analisador_escopo_tipo as scope
import analisador_lexico as lexic

def IS_SHIFT(p):
    return p>0

def IS_REDUCTION(p):
    return p<0

def RULE(p):
    return (-p)

ruleLen = [
    2,1,2,1,1,1,9,8,4,1,1,1,1,1,5,3,9,5,3,4,2,1,2,1,5,3,1,5,7,5,7,1,2,4,2,2,3,
    3,1,3,3,3,3,3,3,1,3,3,1,3,3,1,1,2,2,2,2,3,4,2,2,1,1,1,1,1,3,1,3,4,1,1,1,0
]

ruleLeft = [
    lexic.enumMap["PRG"],lexic.enumMap["P"],lexic.enumMap["LDE"],lexic.enumMap["LDE"],lexic.enumMap["DE"],lexic.enumMap["DE"],
    lexic.enumMap["DT"],lexic.enumMap["DT"],lexic.enumMap["DT"],lexic.enumMap["TP"],lexic.enumMap["TP"],lexic.enumMap["TP"],
    lexic.enumMap["TP"],lexic.enumMap["TP"],lexic.enumMap["DC"],lexic.enumMap["DC"],lexic.enumMap["DF"],lexic.enumMap["LP"],
    lexic.enumMap["LP"],lexic.enumMap["B"],lexic.enumMap["LDV"],lexic.enumMap["LDV"],lexic.enumMap["LS"],lexic.enumMap["LS"],
    lexic.enumMap["DV"],lexic.enumMap["LI"],lexic.enumMap["LI"],lexic.enumMap["S"],lexic.enumMap["S"],lexic.enumMap["S"],
    lexic.enumMap["S"],lexic.enumMap["S"],lexic.enumMap["S"],lexic.enumMap["S"],lexic.enumMap["S"],lexic.enumMap["S"],lexic.enumMap["E"],
    lexic.enumMap["E"],lexic.enumMap["E"],lexic.enumMap["L"],lexic.enumMap["L"],lexic.enumMap["L"],lexic.enumMap["L"],lexic.enumMap["L"],
    lexic.enumMap["L"],lexic.enumMap["L"],lexic.enumMap["R"],lexic.enumMap["R"],lexic.enumMap["R"],lexic.enumMap["TM"],lexic.enumMap["TM"],
    lexic.enumMap["TM"],lexic.enumMap["F"],lexic.enumMap["F"],lexic.enumMap["F"],lexic.enumMap["F"],lexic.enumMap["F"],lexic.enumMap["F"],
    lexic.enumMap["F"],lexic.enumMap["F"],lexic.enumMap["F"],lexic.enumMap["F"],lexic.enumMap["F"],lexic.enumMap["F"],
    lexic.enumMap["F"],lexic.enumMap["F"],lexic.enumMap["LE"],lexic.enumMap["LE"],lexic.enumMap["LV"],lexic.enumMap["LV"],
    lexic.enumMap["LV"],lexic.enumMap["IDD"],lexic.enumMap["IDU"],lexic.enumMap["NB"]

]

stateStack = []

def syntaxError():
    print("Syntax error: line", line)

def parse():
    global stateStack, lexic, actionTable, ruleLen, ruleLeft, scope
    q = 0
    stateStack.append(q)
    a = lexic.nextToken()
    firstPass = True
    while firstPass or (q != ACCEPT):
        print(enums[a]) #Debug
        firstPass = False
        if a in actionTable[q]:
            p = actionTable[q][a]
            if IS_SHIFT(p):
                stateStack.append(p)
                a = lexic.nextToken()
                print("NextToken:", enums[a]) #Debug
            elif IS_REDUCTION(p):
                r = RULE(p)
                print("Regra:", r) #Debug
                for i in range(ruleLen[r]):
                    stateStack.pop()
                stateStack.append(actionTable[stateStack[-1]][ruleLeft[r]])
                scope.analyze(r, lexic.getSecondaryToken(), lexic.line)
            else:
                print("Estado:", stateStack[-1]) #Debug
                syntaxError()
                break
            print("Estado:", stateStack[-1]) #Debug
            q = stateStack[-1]
        else:
            syntaxError()
            break
        print()

