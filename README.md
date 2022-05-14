# SQL-Sarcasm

Changes all the reserved keywords of a SQL File to Sarcasm

Output of a file:
```
InSeRt  InTo  `orders` vAlUeS  (3,8,'2017-12-01',1,NULL,NULL,NULL);
iNsErT  InTo  `orders` VaLuEs  (4,2,'2017-01-22',1,NULL,NULL,NULL);
```

## How to run

Normal behaviour

`python3 sarcasmSQL.py test.sql`

Convert all to Upper Case

`python3 sarcasmSQL.py test.sql -upper`

Can also read from the standart input

`cat test.sql | python3 sarcasmSQL.py`

## Why

I Felt bored 
