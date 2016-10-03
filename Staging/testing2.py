class Map(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
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

class t_attrib(dict):
    def __getattr__(self, attr):
        return self.get(attr)
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__
    
    
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

IDD = IDU = ID = T = LI = LI0 = LI1 = TRU = FALS = STR = CHR = NUM = DC = DC0 = DC1 = LP = LP0 = LP1 = E = E0 = E1 = L = L0 = L1 = R = R0 = R1 = K = K0 = K1 = F = F0 = F1 = LV = LV0 = LV1 = MC = LE = LE0 = LE1 = MT = ME = MW = t_attrib()

identity = 1
IDU.ID.name = identity
print(IDU.ID.name)