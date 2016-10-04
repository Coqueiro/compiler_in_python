	//P -> LDE
    P = 1,
	//LDE -> LDE DE
	LDE,
	//LDE -> DE
	LDE_TAIL,
	//DE -> DF
	DE_FUNC,
	//DE -> DT
	DE_TYPE,
	//DT -> type IDD = array [ NT_NUM ] of TP
	DT_ARRAY,
	//DT -> type IDD = struct NB { DC }
	DT_STRUCT,
	//DT -> type IDD = TP
	DT_SIMP,
	//TP -> integer
	TYPE_INT,
	//TP -> char
	TYPE_CHR,
	//TP->boolean
	TYPE_BOL,
	//TP -> string
	TYPE_STR,
	//TP -> IDU
	TYPE_IDU,
	//DC -> DC ; LI : TP
	DC,
	//DC -> LI : TP
	DC_TAIL,
	//DF -> function IDD NB ( LP ) : TP B
	DF,
	//LP -> LP , IDD : TP
	LP,
	//LP -> IDD : TP
	LP_TAIL,
	//B -> { LDV LS }
	B,
	//LDV -> LDV DV
	LDV,
	//LDV -> DV
	LDV_TAIL,
	//LS -> LS S
	LS,
	//LS -> S
	LS_TAIL,
	//DV -> var LI : TP ;
	DV,
	//LI -> LI , IDD
	LI,
	//LI -> IDD
	LI_TAIL,
	//S -> if ( E ) S
	IF,
	//S -> if ( E ) S else S
	IF_ELSE,
	//S -> while ( E ) S
	WHILE,
	//S -> do S while ( E ) ;
	DO_WHILE,
	//S -> B
	S_B,
	//S -> LV = E ;
	S_LV,
	//S -> break ;
	BREAK,
	//S -> continue ;
	CONTINUE,
	//E -> E and L
	AND,
	//E -> E or L
	OR,
	//E -> L
	L,
	//L -> L lt R
	COMP_LT,
	//L -> L gt R
	COMP_GT,
	//L -> L le R
	COMP_LE,
	//L -> L ge R
	COMP_GE,
	//L -> L eq R
	COMP_EQ,
	//L -> L ne R
	COMP_NEQ,
	//L -> R
	R,
	//R -> R + TM
	PLUS,
	//R -> R - TM
	MINUS,
	//R -> TM
	TM,
	//TM -> TM * F
	TIMES,
	//TM -> TM / F
	DIVIDE,
	//TM -> F
	F,
	//F -> LV
	LV,
	//F -> inc LV
	INC_PRE,
	//F -> dec LV
	DEC_PRE,
	//F -> LV inc
	INC_POS,
	//F -> LV dec
	DEC_POS,
	//F -> ( E )
	PARENTH,
	//F -> IDU ( LE )
	IDU_PARENTH,
	//F -> - F
	NEG,
	//F -> not F
	NOT,
	//F -> NT_TRUE
	NT_TRUE,
	//F -> NT_FALSE
	NT_FALSE,
	//F -> NT_CHR
	NT_CHR,
	//F -> NT_STR
	NT_STR,
	//F -> NT_NUM
	NT_NUM,
	//LE -> LE , E
	LE,
	//LE -> E
	LE_TAIL,
	//LV -> LV dot ID
	DOT,
	//LV -> LV [ E ]
	LV_E,
	//LV -> IDU
	IDU,
	//IDD -> id
	IDD_ID,
	//IDU -> id
	IDU_ID,
	//ID -> id
	ID,
	//NT_TRUE -> true
	TRUE,
	//NT_FALSE -> false
	FALSE,
	//NT_CHR -> charval
	CHAR,
	//NT_STR -> stringval
	STRING,
	//NT_NUM -> numeral
	NUMERAL,
	//NB leva a nada!
	NB,