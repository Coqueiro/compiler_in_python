enums = [
    "ARRAY", "BOOLEAN", "BREAK", "CHAR", "CONTINUE", "DO", "ELSE", "FALSE", "FUNCTION", "IF", "INTEGER", "OF", "STRING", "STRUCT",
    "TRUE", "TYPE", "VAR", "WHILE", "COLON", "SEMI_COLON", "COMMA", "EQUALS", "LEFT_SQUARE", "RIGHT_SQUARE", "LEFT_BRACES", 
    "RIGHT_BRACES", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "AND", "OR", "LESS_THAN", "GREATER_THAN", "LESS_OR_EQUAL", 
    "GREATER_OR_EQUAL", "NOT_EQUAL", "EQUAL_EQUAL", "PLUS", "PLUS_PLUS", "MINUS", "MINUS_MINUS", "TIMES", "DIVIDE", "DOT", "NOT",
    "CHARACTER", "NUMERAL", "STRINGVAL", "ID", "UNKNOWN", "EOF_t"
]
enumMap = {}

for i in range(len(enums)):
    enumMap[enums[i]] = i

enums_nont = [
    "PRG","P","LDE","DE","DT","TP","DC","DF","LP","B","LDV","LS","DV","LI","S",
    "E","L","R","TM","F","LE","LV","IDD","IDU","NB"
]

for i in range(len(enums_nont)):
    enumMap[enums_nont[i]] = i+enumMap["EOF_t"]

class t_const(object):
    type = 0
    cVal = ''
    nVal = 0
    sVal = ""

MAX_CONSTS = 400
vConsts = [t_const()]*MAX_CONSTS
nNumConsts = 0
nextChar = '\x20'
token = enumMap["UNKNOWN"]
secondaryToken = 0
line = 1
program = ""
pointer = 0

tokenMap = {}
tokenMap["array"] = enumMap["ARRAY"]
tokenMap["boolean"] = enumMap["BOOLEAN"]
tokenMap["break"] = enumMap["BREAK"]
tokenMap["char"] = enumMap["CHAR"]
tokenMap["continue"] = enumMap["CONTINUE"]
tokenMap["do"] = enumMap["DO"]
tokenMap["else"] = enumMap["ELSE"]
tokenMap["false"] = enumMap["FALSE"]
tokenMap["function"] = enumMap["FUNCTION"]
tokenMap["if"] = enumMap["IF"]
tokenMap["integer"] = enumMap["INTEGER"]
tokenMap["of"] = enumMap["OF"]
tokenMap["string"] = enumMap["STRING"]
tokenMap["struct"] = enumMap["STRUCT"]
tokenMap["true"] = enumMap["TRUE"]
tokenMap["type"] = enumMap["TYPE"]
tokenMap["var"] = enumMap["VAR"]
tokenMap["while"] = enumMap["WHILE"]

terminalMap = {}
terminalMap[enumMap["ARRAY"]] = "ARRAY"
terminalMap[enumMap["BOOLEAN"]] = "BOOLEAN"
terminalMap[enumMap["BREAK"]] = "BREAK"
terminalMap[enumMap["CHAR"]] = "CHAR"
terminalMap[enumMap["CONTINUE"]] = "CONTINUE"
terminalMap[enumMap["DO"]] = "DO"
terminalMap[enumMap["ELSE"]] = "ELSE"
terminalMap[enumMap["FALSE"]] = "FALSE"
terminalMap[enumMap["FUNCTION"]] = "FUNCTION"
terminalMap[enumMap["IF"]] = "IF"
terminalMap[enumMap["INTEGER"]] = "INTEGER"
terminalMap[enumMap["OF"]] = "OF"
terminalMap[enumMap["STRING"]] = "STRING"
terminalMap[enumMap["STRUCT"]] = "STRUCT"
terminalMap[enumMap["TRUE"]] = "TRUE"
terminalMap[enumMap["TYPE"]] = "TYPE"
terminalMap[enumMap["VAR"]] = "VAR"
terminalMap[enumMap["WHILE"]] = "WHILE"
terminalMap[enumMap["COLON"]] = "COLON"
terminalMap[enumMap["SEMI_COLON"]] = "SEMI_COLON"
terminalMap[enumMap["COMMA"]] = "COMMA"
terminalMap[enumMap["EQUALS"]] = "EQUALS"
terminalMap[enumMap["LEFT_SQUARE"]] = "LEFT_SQUARE"
terminalMap[enumMap["RIGHT_SQUARE"]] = "RIGHT_SQUARE"
terminalMap[enumMap["LEFT_BRACES"]] = "LEFT_BRACES"
terminalMap[enumMap["RIGHT_BRACES"]] = "RIGHT_BRACES"
terminalMap[enumMap["LEFT_PARENTHESIS"]] = "LEFT_PARENTHESIS"
terminalMap[enumMap["RIGHT_PARENTHESIS"]] = "RIGHT_PARENTHESIS"
terminalMap[enumMap["AND"]] = "AND"
terminalMap[enumMap["OR"]] = "OR"
terminalMap[enumMap["LESS_THAN"]] = "LESS_THAN"
terminalMap[enumMap["GREATER_THAN"]] = "GREATER_THAN"
terminalMap[enumMap["LESS_OR_EQUAL"]] = "LESS_OR_EQUAL"
terminalMap[enumMap["GREATER_OR_EQUAL"]] = "GREATER_OR_EQUAL"
terminalMap[enumMap["NOT_EQUAL"]] = "NOT_EQUAL"
terminalMap[enumMap["EQUAL_EQUAL"]] = "EQUAL_EQUAL"
terminalMap[enumMap["PLUS"]] = "PLUS"
terminalMap[enumMap["PLUS_PLUS"]] = "PLUS_PLUS"
terminalMap[enumMap["MINUS"]] = "MINUS"
terminalMap[enumMap["MINUS_MINUS"]] = "MINUS_MINUS"
terminalMap[enumMap["TIMES"]] = "TIMES"
terminalMap[enumMap["DIVIDE"]] = "DIVIDE"
terminalMap[enumMap["DOT"]] = "DOT"
terminalMap[enumMap["NOT"]] = "NOT"
terminalMap[enumMap["CHARACTER"]] = "CHARACTER"
terminalMap[enumMap["NUMERAL"]] = "NUMERAL"
terminalMap[enumMap["STRINGVAL"]] = "STRINGVAL"
terminalMap[enumMap["ID"]] = "ID"
terminalMap[enumMap["UNKNOWN"]] = "UNKNOWN"
terminalMap[enumMap["EOF_t"]] = "EOF_t"

def addCharConst(character):
    global vConsts, nNumConsts
    constant = t_const()
    constant.cVal = character
    vConsts[nNumConsts] = constant
    nNumConsts = nNumConsts + 1
    return nNumConsts

def addIntConst(number):
    global vConsts, nNumConsts
    constant = t_const()
    constant.nVal = number
    vConsts[nNumConsts] = constant
    nNumConsts = nNumConsts + 1
    return nNumConsts

def addStringConst(_string):
    global vConsts, nNumConsts
    constant = t_const()
    constant.sVal = _string
    vConsts[nNumConsts] = constant
    nNumConsts = nNumConsts + 1
    return nNumConsts

def getCharConst(n):
    global vConsts
    return vConsts[n].cVal

def getIntConst(n):
    global vConsts
    return vConsts[n].nVal

def getStringConst(n):
    global vConsts
    return vConsts[n].sVal

def readChar():
    try:
        global pointer, program, line
        symbol = program[pointer]
        pointer = pointer + 1
        if symbol == '\n': 
            line = line + 1
        return symbol
    except IndexError:
        return '\x03'

def getSecondaryToken():
    return secondaryToken

def nextToken():
    global nextChar, enumMap, secondaryToken
    #loop do estado inicial para pular os separadores
    while nextChar.isspace():
        nextChar = readChar()   

    if nextChar.isalpha():
        text = ""
        firstPass = True
        while firstPass or (nextChar.isalnum() or nextChar == '_'):
            firstPass = False
            text += nextChar
            nextChar = readChar()
        token = searchKeyWord(text)
        if(token == enumMap["ID"]):
            secondaryToken = searchName(text)

    elif nextChar.isdigit():
        numeral = ""
        firstPass = True
        while firstPass or nextChar.isdigit():
            firstPass = False
            numeral += nextChar
            nextChar = readChar()
        token = enumMap["NUMERAL"]
        secondaryToken = addIntConst(int(numeral))

    elif nextChar == "\"":
        text = "\""
        nextChar = readChar()
        while nextChar != "\"":
            text += nextChar
            nextChar = readChar()
        text += "\""
        token = enumMap["STRING"]   
        secondaryToken = addStringConst(text) 
        nextChar = readChar()

    else:
        text = nextChar
        if nextChar == "\\":
            nextChar = readChar()
            token = enumMap["CHARACTER"]
            secondaryToken = addCharConst(nextChar)
            nextChar = readChar()
            nextChar = readChar()
        elif nextChar == ":":
            nextChar = readChar()
            token = enumMap["COLON"]
        elif nextChar == ";":
            nextChar = readChar()
            token = enumMap["SEMI_COLON"]
        elif nextChar == ",":
            nextChar = readChar()
            token = enumMap["COMMA"]
        elif nextChar == "[":
            nextChar = readChar()
            token = enumMap["LEFT_SQUARE"]
        elif nextChar == "]":
            nextChar = readChar()
            token = enumMap["RIGHT_SQUARE"]
        elif nextChar == "{":
            nextChar = readChar()
            token = enumMap["LEFT_BRACES"]
        elif nextChar == "}":
            nextChar = readChar()
            token = enumMap["RIGHT_BRACES"]
        elif nextChar == "(":
            nextChar = readChar()
            token = enumMap["LEFT_PARENTHESIS"]
        elif nextChar == ")":
            nextChar = readChar()
            token = enumMap["RIGHT_PARENTHESIS"]
        elif nextChar == "&":
            nextChar = readChar()
            if nextChar == "&":
                text += nextChar
                token = enumMap["AND"]
                nextChar = readChar()
            else:
                token = enumMap["UNKNOWN"]
        elif nextChar == "|":
            nextChar = readChar()
            if nextChar == "|":
                text += nextChar
                token = enumMap["OR"]
                nextChar = readChar()
            else:
                token = enumMap["UNKNOWN"]
        elif nextChar == "=":
            nextChar = readChar()
            if nextChar == "=":
                text += nextChar
                token = enumMap["EQUAL_EQUAL"]
                nextChar = readChar()
            else:
                token = enumMap["EQUALS"]
        elif nextChar == "<":
            nextChar = readChar()
            if nextChar == "=":
                text += nextChar
                token = enumMap["LESS_OR_EQUAL"]
                nextChar = readChar()
            else:
                token = enumMap["LESS_THAN"]
        elif nextChar == ">":
            nextChar = readChar()
            if nextChar == "=":
                text += nextChar
                token = enumMap["GREATER_OR_EQUAL"]
                nextChar = readChar()
            else:
                token = enumMap["GREATER_THAN"]
        elif nextChar == "!":
            nextChar = readChar()
            if nextChar == "=":
                text += nextChar
                token = enumMap["NOT_EQUAL"]
                nextChar = readChar()
            else:
                token = enumMap["NOT"]
        elif nextChar == "+":
            nextChar = readChar()
            if nextChar == "+":
                text += nextChar
                token = enumMap["PLUS_PLUS"]
                nextChar = readChar()
            else:
                token = enumMap["PLUS"]
        elif nextChar == "-":
            nextChar = readChar()
            if nextChar == '-':
                text += nextChar
                token = enumMap["MINUS_MINUS"]
                nextChar = readChar()
            else:
                token = enumMap["MINUS"]
        elif nextChar == "*":
            nextChar = readChar()
            token = enumMap["TIMES"]
        elif nextChar == "/":
            nextChar = readChar()
            token = enumMap["DIVIDE"]
        elif nextChar == ".":
            nextChar = readChar()
            token = enumMap["DOT"]
        elif nextChar == '\x03':
            token = enumMap["EOF_t"]
        else:
            token = enumMap["UNKNOWN"]
            print("Lexical error!")    
    return token

def searchKeyWord(key):
    if key in tokenMap:
        return tokenMap[key]
    else:
        return enumMap["ID"]

secondaryTokenId = 0
secondaryTokenMap = {}

def searchName(key):
    global secondaryTokenId
    if key in secondaryTokenMap:
        return secondaryTokenMap[key]
    else:
        secondaryTokenMap[key] = secondaryTokenId
        secondaryTokenId = secondaryTokenId + 1
        return secondaryTokenId


