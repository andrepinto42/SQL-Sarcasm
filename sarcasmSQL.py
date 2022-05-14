import ply.lex as lex

from random import seed
from random import randint
# seed random number generator
seed(1)

def sarcasm(string):
    final =""
    value = randint(0,1)
    flip = True
    if value == 0:
        flip = False

    for ch in string:
        if flip: final += ch.upper()
        else:    final += ch.lower()  
        flip = not flip
    return final




reservadas = ["ADD","ALL","ALTER","ANALYZE","AND","AS","ASC","AUTO_INCREMENT","BDB","BERKELEYDB","BETWEEN","BIGINT","BINARY","BLOB","BOTH","BTREE","BY","CASCADE","CASE","CHANGE","CHAR","CHARACTER","CHECK","COLLATE","COLUMN","COLUMNS","CONSTRAINT","CREATE","CROSS","CURRENT_DATE","CURRENT_TIME","CURRENT_TIMESTAMP","DATABASE","DATABASES","DAY_HOUR","DAY_MINUTE","DAY_SECOND","DEC","DECIMAL","DEFAULT","DELAYED","DELETE","DESC","DESCRIBE","DISTINCT","DISTINCTROW","DIV","DOUBLE","DROP","ELSE","ENCLOSED","ERRORS","ESCAPED","EXISTS","EXPLAIN","FALSE","FIELDS","FLOAT","FOR","FORCE","FOREIGN","FROM","FULLTEXT","FUNCTION","GEOMETRY","GRANT","GROUP","HASH","HAVING","HELP","HIGH_PRIORITY","HOUR_MINUTE","HOUR_SECOND","IF","IGNORE","IN","INDEX","INFILE","INNER","INNODB","INSERT","INT","INTEGER","INTERVAL","INTO","IS","JOIN","KEY","KEYS","KILL","LEADING","LEFT","LIKE","LIMIT","LINES","LOAD","LOCALTIME","LOCALTIMESTAMP","LOCK","LONG","LONGBLOB","LONGTEXT","LOW_PRIORITY","MASTER_SERVER_ID","MATCH","MEDIUMBLOB","MEDIUMINT","MEDIUMTEXT","MIDDLEINT","MINUTE_SECOND","MOD","MRG_MYISAM","NATURAL","NOT","NULL","NUMERIC","ON","OPTIMIZE","OPTION","OPTIONALLY","OR","ORDER","OUTER","OUTFILE","PRECISION","PRIMARY","PRIVILEGES","PROCEDURE","PURGE","READ","REAL","REFERENCES","REGEXP","RENAME","REPLACE","REQUIRE","RESTRICT","RETURNS","REVOKE","RIGHT","RLIKE","RTREE","SELECT","SET","SHOW","SMALLINT","SOME","SONAME","SPATIAL","SQL_BIG_RESULT","SQL_CALC_FOUND_ROWS","SQL_SMALL_RESULT","SSL","STARTING","STRAIGHT_JOIN","STRIPED","TABLE","TABLES","TERMINATED","THEN","TINYBLOB","TINYINT","TINYTEXT","TO","TRAILING","TRUE","TYPES","UNION","UNIQUE","UNLOCK","UNSIGNED","UPDATE","USAGE","USE","USER_RESOURCES","USING","VALUES","VARBINARY","VARCHAR","VARCHARACTER","VARYING","WARNINGS","WHEN","WHERE","WITH","WRITE","XOR","YEAR_MONTH","ZEROFILL"]
#-----------------------
# Parametros do Lexer 
#-----------------------
tokens =["WORD","SPACE"]

upperState = False

def t_WORD(t):
    r'\s*\w+\s+'
    if t.value.upper().strip() in reservadas:
        if upperState:
            print(t.value.upper(),end='')
        else:
            print(sarcasm(t.value),end=' ')
    else:print(t.value,end='')

def t_space(t):
    r'\s'
    print(t.value,end='')

def t_default(t):
    r'.'
    print(t.value,end='')

def t_error(t):
    pass

lexer = lex.lex()

import sys

if len(sys.argv) >= 2:
    codigo = open( sys.argv[1]).read()
else:
    codigo = sys.stdin.read()

if "-upper" in sys.argv:
    upperState = True

lexer.input(codigo)

lexer.token()