import analisador_lexico as lexic_func

MAX_NEST_LEVEL = 50
DF_RULE = 4
DT_ARRAY_RULE = 6
DT_STRUCT_RULE = 7
DT_RULE = 8
T_INTEGER_RULE = 9
T_CHAR_RULE = 10
T_BOOL_RULE = 11
T_STRING_RULE = 12
T_IDU_RULE = 13
DC_DC_RULE = 14
DC_LI_RULE = 15
DF_RULE = 16
LP_LP_RULE = 17
LP_IDD_RULE = 18
B_RULE = 19
DV_VAR_RULE = 24
LI_COMMA_RULE = 25
LI_IDD_RULE = 26
S_IF_RULE = 27
S_IF_ELSE_RULE = 28
S_WHILE_RULE = 29
S_DO_WHILE_RULE = 30
S_BLOCK_RULE = 31
S_E_SEMICOLON = 32
S_BREAK_RULE = 33
S_CONTINUE_RULE = 34
E_AND_RULE = 35
E_OR_RULE = 36
E_L_RULE = 37
L_LESS_THAN_RULE = 38
L_GREATER_THAN_RULE = 39
L_LESS_EQUAL_RULE = 40
L_GREATER_EQUAL_RULE = 41
L_EQUAL_EQUAL_RULE = 42
L_NOT_EQUAL_RULE = 43
L_R_RULE = 44
R_PLUS_RULE = 45
R_MINUS_RULE = 46
R_TM_RULE = 47
TM_TIMES_RULE = 48
TM_DIVIDE_RULE = 49
TM_F_RULE = 50
F_LV_RULE = 51
F_LEFT_PLUS_PLUS_RULE = 52
F_LEFT_MINUS_MINUS_RULE = 53
F_RIGHT_PLUS_PLUS_RULE = 54
F_RIGHT_MINUS_MINUS_RULE = 55
F_PARENTHESIS_E_RULE = 56
F_IDU_MC_RULE = 57
F_MINUS_F_RULE = 58
F_NOT_F_RULE = 59
F_TRUE_RULE = 60
F_FALSE_RULE = 61
F_CHR_RULE = 62
F_STR_RULE = 63
F_NUM_RULE = 64
LE_LE_RULE = 65
LE_E_RULE = 66
LV_DOT_RULE = 67
LV_SQUARE_RULE = 68
LV_IDU_RULE = 69
IDD_RULE = 70
IDU_RULE = 71
ID_RULE = 72
TRUE_RULE = 73
FALSE_RULE = 74
CHR_RULE = 75
STR_RULE = 76
NUM_RULE = 77
NB_RULE = 78
IDT_RULE = 9001

kindEnum = ['NO_KIND_DEF', 'VAR', 'PARAM', 'FUNCTION', 'FIELD', 'ARRAY_TYPE', 'STRUCT_TYPE', 'ALIAS_TYPE', 'SCALAR_TYPE', 'UNIVERSAL']
t_kind = {}

for i in range(len(kindEnum)):
    t_kind[kindEnum[i]] = i-1

def IsKindType(type):
    return type == t_kind['ARRAY_TYPE'] or type == t_kind['STRUCT_TYPE'] or type == t_kind['ALIAS_TYPE'] or type == t_kind['SCALAR_TYPE']

class Map(dict):
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]

class pobject(dict):
    nName = 0
    pNext = None
    eKind = -1
    def __init__(self, nName=0, pNext=None, eKind=-1):
        self.nName = nName
        self.pNext = pNext
        self.eKind = eKind
    Var = Map()
    Var['pType'] = None
    Var['nIndex'] = 0
    Var['nSize'] = 0    
    Param = Map()
    Param['pType'] = None
    Param['nIndex'] = 0
    Param['nSize'] = 0
    Field = Map()
    Field['pType'] = None
    Field['nIndex'] = 0
    Field['nSize'] = 0
    Function = Map()
    Function['pRetType'] = None
    Function['pParams'] = None
    Function['nIndex'] = 0
    Function['nParams'] = 0
    Function['nVars'] = 0
    Array = Map()
    Array['pElemType'] = None
    Array['nNumElems'] = 0
    Array['nSize'] = 0
    Struct = Map()
    Struct['pFields'] = None
    Struct['nSize'] = 0
    Alias = Map()
    Alias['pFields'] = None
    Alias['nSize'] = 0
    Type = Map()
    Type['pFields'] = None
    Type['nSize'] = 0

numberFunctions = 0
currentFunction = pobject()

pInt = pobject(-1, None, t_kind['SCALAR_TYPE'])
pChar = pobject(-1, None, t_kind['SCALAR_TYPE'])
pBool = pobject(-1, None, t_kind['SCALAR_TYPE'])
pString = pobject(-1, None, t_kind['SCALAR_TYPE'])
pUniversal = pobject(-1, None, t_kind['SCALAR_TYPE'])

labelNo = 0
def NewLabel():
    labelNo = labelNo + 1
    return labelNo

SymbolTable = [None]*MAX_NEST_LEVEL
SymbolTableLast = [None]*MAX_NEST_LEVEL
nCurrentLevel = -1

def NewBlock():
    global nCurrentLevel
    nCurrentLevel = nCurrentLevel + 1
    SymbolTable[nCurrentLevel] = None
    SymbolTableLast[nCurrentLevel] = None
    return nCurrentLevel

def EndBlock():
    global nCurrentLevel
    nCurrentLevel = nCurrentLevel - 1
    return nCurrentLevel

def Define(aName):
    global nCurrentLevel
    obj = pobject()
    obj.nName = aName
    obj.pNext = None
    if(SymbolTable[nCurrentLevel] == None):
        SymbolTable[nCurrentLevel] = obj
        SymbolTableLast[nCurrentLevel] = obj
    else:
        SymbolTable[nCurrentLevel].pNext = obj
        SymbolTableLast[nCurrentLevel] = obj
    return obj

def Search(aName):
    global nCurrentLevel
    obj = SymbolTable[nCurrentLevel]
    while obj != None:
        if obj.nName == aName:
            break
        else:
            obj = obj.pNext
    if obj == {}:
        obj = None
    return obj

def Find(aName):
    global nCurrentLevel
    i = nCurrentLevel
    obj = None
    while i >= 0:
        i = i - 1
        obj = SymbolTable[i]
        while obj != None:
            if obj.nName == aName:
                break
            else:
                obj = obj.pNext
        if obj != None:
            break
    if obj == {}:
        obj = None
    return obj

def Error(error, line):
    print(error, "line:", line)

def CheckType(t1, t2):
    if t1 == t2:
        return True
    elif t1 == pUniversal or t2 == pUniversal:
        return True
    elif t1.eKind == t_kind['UNIVERSAL'] or t2.eKind == t_kind['UNIVERSAL']:
        return True
    elif t1.eKind == t_kind['ALIAS_TYPE'] and t2.eKind != t_kind['ALIAS_TYPE']:
        return CheckType(t1.Alias.pBaseType, t2)
    elif t1.eKind != t_kind['ALIAS_TYPE'] and t2.eKind == t_kind['ALIAS_TYPE']:
        return CheckType(t1, t2.Alias.pBaseType)
    elif t1.eKind == t2.eKind:
        if t1.eKind == t_kind['ALIAS_TYPE']:
            return CheckType(t1.Alias.pBaseType, t2.Alias.pBaseType)
        elif t1.eKind == t_kind['ARRAY_TYPE']:
            if t1.Array.nNumElems == t2.Array.nNumElems:
                return CheckType(t1.Array.pElemType, t2.Array.pElemType)
        elif t1.eKind == t_kind['STRUCT_TYPE']:
            if t1.Array.nNumElems == t2.Array.nNumElems:
                return CheckType(t1.Array.pElemType, t2.Array.pElemType)
        elif t1.eKind == t_kind['SRUCT_TYPE']:
            f1 = t1.Struct.pFields
            f2 = t2.Struct.pFields
            while f1 != None and f2 != None:
                if not CheckType(f1.Field.pType, f2.Field.pType):
                    return False
            return f1 == None and f2 == None
    return False

class t_attrib(dict):
    enumMapIndex = 0
    nSize = 0
    ID = Map()
    ID['obj'] = pobject()
    ID['name'] = 0
    T = Map()
    T['type'] = pobject()
    E = Map()
    E['type'] = pobject()
    L = Map()
    L['type'] = pobject()
    R = Map()
    R['type'] = pobject()
    K = Map()
    K['type'] = pobject()
    F = Map()
    F['type'] = pobject()
    LV = Map()
    LV['type'] = pobject()
    MC = Map()
    MC['type'] = pobject()
    MC['param'] = pobject()
    MC['err'] = False
    MT = Map()
    MT['label'] = 0
    ME = Map()
    ME['label'] = 0
    MW = Map()
    MW['label'] = 0
    MA = Map()
    MA['label'] = 0
    LE = Map()
    LE['type'] = pobject()
    LE['param'] = pobject()
    LE['err'] = False
    LE['n'] = 0
    LI = Map()
    LI['list'] = pobject()
    DC = Map()
    DC['list'] = pobject()
    LP = Map()
    LP['list'] = pobject()
    TRU = Map()
    TRU['type'] = pobject()
    TRU['val'] = False
    FALS = Map()
    FALS['type'] = pobject()
    FALS['val'] = False
    CHR = Map()
    CHR['type'] = pobject()
    CHR['pos'] = 0
    CHR['val'] = ''
    STR = Map()
    STR['type'] = pobject()
    STR['val'] = ''
    STR['pos'] = 0
    NUM = Map()
    NUM['type'] = pobject()
    NUM['val'] = 0
    NUM['pos'] = 0

class StackSem(object):
    stack_ = []
    def __getitem__(self, arg):
        if(len(self.stack_) >= abs(arg)):
            return self.stack_[arg]
        else:
            return t_attrib()
    def append(self, element):
        self.stack_.append(element)
    def pop(self):
        if(len(self.stack_) != 0):
            return self.stack_.pop()
        else:
            return t_attrib()

StackSem = StackSem()

identity = n = l = l1 = l2 = 0
p = t = f = pobject()
IDD = IDU = ID = T = LI = LI0 = LI1 = TRU = FALS = STR = CHR = NUM = DC = DC0 = DC1 = LP = LP0 = LP1 = E = E0 = E1 = L = L0 = L1 = R = R0 = R1 = K = K0 = K1 = F = F0 = F1 = LV = LV0 = LV1 = MC = LE = LE0 = LE1 = MT = ME = MW = t_attrib()

def analyze(rule, name, line):
    print('rule:', rule, 'name:', name, 'line:', line)
    global identity, n, l, l1, l2
    global p, t, f
    global IDD, IDU, ID, T, LI, LI0, LI1, TRU, FALS, STR, CHR, NUM, DC, DC0, DC1, LP, LP0, LP1, E, E0, E1, L, L0, L1, R, R0, R1, K, K0, K1, F, F0, F1, LV, LV0, LV1, MC, LE, LE0, LE1, MT, ME, MW

    if rule == IDD_RULE:
        identity = name
        IDD.nont = IDD
        IDD.ID.name = identity
        p = Search(name)
        if p != None:
            Error("Variable was already declared!", line)
        else:
            p = Define(name)
        p.eKind = t_kind['NO_KIND_DEF']
        IDD.ID.obj = p
        StackSem.append(IDD)
    elif rule == IDU_RULE:
        identity = name
        IDU.nont = IDU 
        IDU.ID.name = identity
        p = Find(name)
        if(p == None):
            Error("Declaring variable!", line)
            p = Define(name)
        IDU.ID.obj = p
        StackSem.append(IDU)
    elif rule == ID_RULE:
        ID.nont = ID 
        identity = name
        ID.ID.name = identity
        ID.ID.obj = None
        StackSem.append(ID)
    elif rule == IDT_RULE:
        do_nothing = True
    elif rule == NB_RULE:
        NewBlock()
    elif rule == DT_RULE:
        do_nothing = True
    elif rule == DF_RULE:
        EndBlock()
    elif rule == T_INTEGER_RULE: 
        T.T.type = pInt
        T.enumMapIndex = T
        T.nSize = 1
        StackSem.append(T)
    elif rule == T_CHAR_RULE:
        T.T.type = pChar
        T.enumMapIndex = T
        T.nSize = 1
        StackSem.append(T)
    elif rule == T_BOOL_RULE:
        T.T.type = pBool
        T.nont = T
        T.nSize = 1
        StackSem.append(T)
    elif rule == T_STRING_RULE:
        T.T.type = pString
        T.nont = T
        T.nSize = 1
        StackSem.append(T)
    elif rule == T_IDU_RULE:
        IDU = StackSem.pop()
        p = IDU.ID.obj
        if IsKindType(p.eKind) or p.eKind == t_kind['UNIVERSAL']:
            T.T.type = p
            if p.eKind == t_kind['ALIAS_TYPE']:
                T.nSize = p.Alias.nSize
            elif p.eKind == t_kind['ARRAY_TYPE']:
                T.nSize = p.Array.nSize
            elif p.eKind == t_kind['STRUCT_TYPE']:
                T.nSize = p.Struct.nSize
        else:
            T.T.type = pUniversal
            T.nSize = 0
            Error('different type expected', line)
        T.nont = T
        StackSem.append(T)
    elif rule == LI_IDD_RULE:
        IDD = StackSem[-1]
        LI.LI.list = IDD.ID.obj
        LI.nont = LI
        StackSem.pop()
        StackSem.append(LI)
    elif rule == LI_COMMA_RULE:
        IDD = StackSem.pop()
        LI1 = StackSem.pop()
        LI0.LI.list = LI1.LI.list
        LI0.nont = LI
        StackSem.append(LI0)
    elif rule == DV_VAR_RULE:
        T = StackSem.pop()
        t = T.T.type
        LI = StackSem.pop()
        p = LI.LI.list
        n = currentFunction.Function.nVars
        while p != None and p.eKind == t_kind['NO_KIND_DEF']:
            p.eKind = t_kind['VAR']
            p.Var.pType = t
            p.Var.nSize = T.nSize
            p.Var.nIndex = n
            n = n + T.nSize
            p = p.pNext
        currentFunction.Function.nVars = n
    elif rule == TRUE_RULE:
        TRU.nont = TRU
        TRU.TRU.val = True
        TRU.TRU.type = pBool
        StackSem.append(TRU)
    elif rule == FALSE_RULE:
        FALS.nont = FALS
        FALS.FALS.val = False
        FALS.FALS.type = pBool
        StackSem.append(FALS)
    elif rule == CHR_RULE:
        CHR.nont = CHR
        CHR.CHR.type = pChar
        CHR.CHR.pos = name 
        CHR.CHR.val = lexic_func.getCharConst(name)
        StackSem.append(CHR)
    elif rule == STR_RULE:
        STR.nont = STR
        STR.STR.type = pString
        STR.STR.pos = name
        STR.STR.val = lexic_func.getStringConst(name)
        StackSem.append(STR)
    elif rule ==  NUM_RULE:
        NUM.nont = NUM
        NUM.NUM.type = pInt
        NUM.NUM.pos = name
        NUM.NUM.val = lexic_func.getIntConst(name)
        StackSem.append(NUM)
    elif rule == DT_ARRAY_RULE:
        T = StackSem.pop()
        NUM = StackSem.pop()
        IDD = StackSem.pop()
        p = IDD.ID.obj
        n = NUM.NUM.val
        t = T.T.type
        p.eKind = t_kind['ARRAY_TYPE']
        p.Array.nNumElems = n
        p.Array.pElemType = t
        p.Array.nSize = n*T.nSize
    elif rule == DC_LI_RULE:
        T = StackSem.pop()
        LI = StackSem.pop()
        p = LI.LI.list
        t = T.T.type
        n = 0
        while p != None and p.eKind == t_kind['NO_KIND_DEF']:
            p.eKind = t_kind['FIELD']
            p.Field.pType = t
            p.Field.nSize = T.nSize
            p.Field.nIndex = n
            n = n + T.nSize
            p = p.pNext
        DC.DC.list = LI.LI.list
        DC.nSize = n
        DC.nont = DC
        StackSem.append(DC)
    elif rule == DF_RULE:
        EndBlock()
    elif rule == DC_DC_RULE:
        T = StackSem.pop()
        LI = StackSem.pop()
        DC1 = StackSem.pop()
        p = LI.LI.list
        t = T.T.type
        n = DC1.nSize
        while p != None and p.eKind == t_kind['NO_KIND_DEF']:
            p.eKind = t_kind['FIELD']
            p.Field.pType = t
            p.Field.nIndex = n
            p.Field.nSize = T.nSize
            n =  n + T.nSize
            p = p.pNext
        DC0.DC.list = DC1.DC.list
        DC0.nSize = n
        DC0.nont = DC 
        StackSem.append(DC0)
    elif rule == DT_STRUCT_RULE:
        DC = StackSem.pop()
        IDD = StackSem.pop()
        p = IDD.ID.obj
        p.eKind = t_kind['STRUCT_TYPE']
        p.Struct.pFields = DC.DC.list
        p.Struct.nSize = DC.nSize
        EndBlock()
    elif rule == LP_IDD_RULE:
        T = StackSem.pop()
        IDD = StackSem.pop()
        p = IDD.ID.obj
        t = T.T.type
        p.eKind = t_kind['PARAM']
        p.Param.pType = t
        p.Param.nIndex = 0
        p.Param.nSize = T.nSize
        LP.LP.list = p
        LP.nSize = T.nSize
        LP.nont = LP
        StackSem.append(LP)
    elif rule == B_RULE:
        MF = StackSem[-3]
        IDD = StackSem[-7]
        p = IDD.ID.obj
        p.Function.pRetType = T.T.type
        p.Function.pParams = LP.LP.list
        p.Function.nParams = LP.nSize
        p.Function.nVars = LP.nSize
    elif rule == LP_LP_RULE:
        T = StackSem.pop()
        IDD = StackSem.pop()
        LP1 = StackSem.pop()
        p = IDD.ID.obj
        t = T.T.type
        n = LP1.nSize
        p.eKind = t_kind['PARAM']
        p.Param.pType = t
        p.Param.nIndex = n
        p.Param.nSize = T.nSize
        LP0.LP.list = LP1.LP.list
        LP0.nSize = n + T.nSize
        LP0.nont = LP 
        StackSem.append(LP0)
    elif rule == DF_RULE:
        EndBlock()
    elif rule == S_BLOCK_RULE:
        EndBlock()
    elif rule == S_E_SEMICOLON:
        E = StackSem.pop()
    elif rule == S_IF_RULE:
        MT = StackSem.pop()
        E = StackSem.pop()
        t = E.E.type
        if not CheckType(t, pBool):
            Error('bool type expected', line)
    elif rule == S_IF_ELSE_RULE:
        ME = StackSem.pop()
        MT = StackSem.pop()
        E =  StackSem.pop()
        l = ME.ME.label
        t = E.E.type
        if not CheckType(t,pBool):
            Error('bool type expected', line)
    elif rule == S_WHILE_RULE:
        MT = StackSem.pop()
        E = StackSem.pop()
        MW = StackSem.pop()
        l1 = MW.MW.label
        l2 = MT.MT.label
        t = E.E.type
        if not CheckType(t, pBool):
            Error('bool type expected', line)
    elif rule == S_DO_WHILE_RULE:
        E = StackStem.pop()
        MW = StackSem.pop()
        l = MW.MW.label
        t = E.E.type
        if not CheckType(t,pBool):
            Error('bool type expected', line)
    elif rule == S_BREAK_RULE:
        do_nothing = True
    elif rule == S_CONTINUE_RULE:
        do_nothing = True
    elif rule == E_AND_RULE:
        L = StackSem.pop()
        E1 = StackSem.pop()
        if not CheckType(E1.E.type, pBool):
            Error('bool type expected', line)
        if not CheckType(L.L.type, pBool):
            Error('bool type expected', line)
        E0.E.type = pBool
        E0.nont = E
        StackSem.append(E0)
    elif rule == E_OR_RULE:
        L = StackSem.pop()
        E1 = StackSem.pop()
        if not CheckType(E1.E.type, pBool):
            Error('bool type expected', line)
        if not CheckType(L.L.type, pBool):
            Error('bool type expected', line)
        E0.E.type = pBool
        E0.nont = E
        StackSem.append(E0)
    elif rule == E_L_RULE:
        L = StackSem.pop()
        E.E.type = L.L.type
        E.nont = E
        StackSem.append(E)
    elif rule == L_LESS_THAN_RULE:
        R = StackSem.pop()
        L1 = StackSem.pop()
        if not CheckType(L1.L.type, R.R.type):
            Error('type mismatched', line)
        L0.L.type = pBool
        L0.nont = L
        StackSem.append(L0)
    elif rule == L_GREATER_THAN_RULE:
        R = StackSem.pop()
        L1 = StackSem.pop()
        if not CheckType(L1.L.type, R.R.type):
            Error('type mismatched', line)
        L0.L.type = pBool
        L0.nont = L
        StackSem.append(L0)
    elif rule == L_LESS_EQUAL_RULE:
        R = StackSem.pop()
        L1 = StackSem.pop()
        if not CheckType(L1.L.type, R.R.type):
            Error('type mismatched', line)
        L0.L.type = pBool
        L0.nont = L
        StackSem.append(L0)
    elif rule == L_GREATER_EQUAL_RULE:
        R = StackSem.pop()
        L1 = StackSem.pop()
        if not CheckType(L1.L.type, R.R.type):
            Error('type mismatched', line)
        L0.L.type = pBool
        L0.nont = L
        StackSem.append(L0)
    elif rule == L_EQUAL_EQUAL_RULE:
        R = StackSem.pop()
        L1 = StackSem.pop()
        if not CheckType(L1.L.type, R.R.type):
            Error('type mismatched', line)
        L0.L.type = pBool
        L0.nont = L
        StackSem.append(L0)
    elif rule == L_NOT_EQUAL_RULE:
        R = StackSem.pop()
        L1 = StackSem.pop()
        if not CheckType(L1.L.type, R.R.type):
            Error('type mismatched', line)
        L0.L.type = pBool
        L0.nont = L
        StackSem.append(L0)
    elif rule == L_R_RULE:
        R = StackSem.pop()
        L.L.type = R.R.type
        L.nont = L
        StackSem.append(L)
    elif rule == R_PLUS_RULE:
        K = StackSem.pop()
        R1 = StackSem.pop()
        if not CheckType(R1.R.type, K.K.type):
            Error('type mismatched', line)
        if not CheckType(R1.R.type, pInt) and not CheckType(R1.R.type, pString):
            Error('invalid type', line)
        R0.R.type = R1.R.type
        R0.nont = R
        StackSem.append(R0)
    elif rule == R_MINUS_RULE:         
        K = StackSem.pop()
        R1 = StackSem.pop()
        if not CheckType(R1.R.type, K.K.type):
            Error('type mismatched', line)
        if not CheckType(R1.R.type, pInt) and not CheckType(R1.R.type, pString):
            Error('invalid type', line)
        R0.R.type = R1.R.type
        R0.nont = R
        StackSem.append(R0)
    elif rule == R_TM_RULE:
        K = StackSem.pop()
        R.R.type = K.K.type
        R.nont = R
        StackSem.append(R)
    elif rule == TM_TIMES_RULE:
        F = StackSem.pop()
        K1 = StackSem.pop()
        if not CheckType(K1.K.type, F.F.type):
            Error('type mismatched', line)
        if not CheckType(K1.K.type, pInt):
            Error('invalid type', line)
        K0.K.type = K1.K.type
        K0.nont = K
        StackSem.append(K0)
    elif rule == TM_DIVIDE_RULE:
        F = StackSem.pop()
        K1 = StackSem.pop()
        if not CheckType(K1.K.type, F.F.type):
            Error('type mismatched', line)
        if not CheckTYpe(K1.K.type, pInt):
            Error('invalid type', line)
        K0.K.type = K1.K.type
        K0.nont = K
        StackSem.append(K0)
    elif rule == TM_F_RULE:
        F = StackSem.pop()
        K.K.type = F.F.type
        K.nont = K
        StackSem.append(K)
    elif rule == F_LV_RULE:
        LV = StackSem.pop()
        n = LV.LV.type.Type.nSize
        F.F.type = LV.LV.type
        F.nont = F
        StackSem.append(F)
    elif rule == F_LEFT_PLUS_PLUS_RULE:
        LV = StackSem.pop()
        t = LV.LV.type
        if not CheckType(t,pInt):
            Error('invalid type', line)
        F.F.type = pInt
        F.nont = F
        StackSem.append(F)
    elif rule == F_LEFT_MINUS_MINUS_RULE:
        LV = StackSem.pop()
        t = LV.LV.type
        if not CheckType(t,pInt):
            Error('invalid type', line)
        F.F.type = LV.LV.type
        F.nont = F
        StackSem.append(F)
    elif rule == F_RIGHT_PLUS_PLUS_RULE:
        LV = StackSem.pop()
        t = LV.LV.type
        if not CheckType(t,pInt):
            Error('invalid type', line)
        F.F.type = LV.LV.type
        F.nont = F
        StackSem.append(F)
    elif rule == F_RIGHT_MINUS_MINUS_RULE:
        LV = StackSem.pop()
        t = LV.LV.type
        if not CheckType(t,pInt):
            Error('invalid type', line)
        F.F.type = t
        F.nont = F
        StackSem.append(F)
    elif rule == F_PARENTHESIS_E_RULE:
        E = StackSem.pop()
        F.F.type = E.E.type
        F.nont = F
        StackSem.append(F)
    elif rule == F_MINUS_F_RULE:
        F1 = StackSem.pop()
        t = F1.F.type
        if not CheckType(t,pInt):
            Error('invalid type', line)
        F0.F.type = t
        F0.nont = F
        StackSem.append(F0)
    elif rule == F_NOT_F_RULE:
        F1 = StackSem.pop()
        t = F1.F.type
        if not CheckType(t,pBool):
            Error('invalid type', line)
        F0.F.type = t
        F0.nont = F
        StackSem.append(F0)
    elif rule == F_TRUE_RULE:
        TRU = StackSem.pop()
        F.F.type = pBool
        F.nont = F
        StackSem.append(F)
    elif rule == F_FALSE_RULE:
        FALS = StackSem.pop()
        F.F.type = pBool
        F.nont = F
        StackSem.append(F)
    elif rule == F_CHR_RULE:
        CHR = StackSem.pop()
        F.F.type = pChar
        F.nont = F
        StackSem.append(F)
        n = name
    elif rule == F_STR_RULE:
        SRT = StackSem.pop()
        F.F.type = pString
        F.nont = F
        StackSem.append(F)
    elif rule == F_NUM_RULE:
        STR = StackSem.pop()
        F.F.type = pInt
        F.nont = F
        StackSem.append(F)
        n = name
    elif rule == LV_DOT_RULE:
        ID = StackSem.pop()
        LV1 = StackSem.pop()
        t = LV1.LV.type
        if t.eKind != t_kind['STRUCT_TYPE']:
            if t.eKind != t_kind['UNIVERSAL']:
                Error('kind is not struct', line)
            LV0.LV.type = pUniversal
        else:
            p = t.Struct.pFields
            while p != None:
                if p.nName == ID.ID.name:
                    break
                p = p.pNext
            if p != None:
                Error('field not declared', line)
            else:
                LV0.LV.type = p.Field.pType
                LV0.LV.type.Type.nSize = p.Field.nSize
        LV0.nont = LV
        StackSem.append(LV0)
    elif rule == LV_SQUARE_RULE:
        E = StackSem.pop()
        LV1 = StackSem.pop()
        t = LV1.LV.type
        if not CheckType(t,pString):
            LV0.LV.type = pChar
        elif t.eKind != t_kind['ARRAY_TYPE']:
            if t.eKind != t_kind['UNIVERSAL']:
                Error('kind is not array', line)
        else:
            LV0.LV.type = t.Array.pElemType
            n = t.Array.pElemType.Struct.nSize
        if not CheckType(E.E.type, pInt):
            Error('invalid type of index', line)
        LV0.nont = LV
        StackSem.append(LV0)
    elif rule == LV_IDU_RULE:
        IDU = StackSem.pop()
        p = IDU.ID.obj
        if p.eKind != t_kind['VAR'] and p.eKind != t_kind['PARAM']:
            if p.eKind != t_kind['UNIVERSAL']:
                Error('variable can''t be declared with this kind', line)
            LV.LV.type = pUniversal
        else:
            LV.LV.type = p.Var.pType
            LV.LV.type.Type.nSize = p.Var.nSize
        LV.nont = LV
        StackSem.append(LV)
    elif rule == LE_E_RULE:
        E = StackSem.pop()
        MC = StackSem.pop()
        LE.LE.param = None
        LE.LE.err = MC.MC.err
        n = 1
        if not MC.MC.err:
            p = MC.MC.param
            if p == None:
                Error('too many arguments', line)
                LE.LE.err = True
            else:
                if not CheckType(p.Param.pType, E.E.type):
                    Erro('wrong parameter type')
                LE.LE.param = p.pNext
                LE.LE.n = n + 1
        LE.nont = lE 
        StackSem.append(LE)
    elif rule == LE_LE_RULE:
        E = StackSem.pop()
        LE1 = StackSem.pop()
        LE0.LE.param = None
        LE0.LE.err = L1.LE.err
        n = LE1.LE.n
        if not LE1.LE.err:
            p = LE1.LE.param
            if p == None:
                Error('too many arguments', line)
                LE0.LE.err = True
            else:
                if not CheckType(p.Param.pType, E.E.type):
                    Error('wrong parameter type', line)
                LE0.LE.param = p.pNext
                LE0.LE.n = n+1
        LE0.nont = LE 
        StackSem.append(LE0)
    elif rule == F_IDU_MC_RULE:
        LE = StackSem.pop()
        MC = StackSem.pop()
        IDU = StackSem.pop()
        f = IDU.ID.obj
        F.F.type = MC.MC.type
        if not LE.lE.err:
            if LE.LE.n-1 < f.Function.nParams and LE.LE.n != 0:
                Error('need more arguments', line)
            elif LE.LE.n-1 > f.Function.nParams:
                Error('too many arguments', line)
        F.nont = F
        StackSem.append(F)
    else:
        do_nothing = True
    
        

        