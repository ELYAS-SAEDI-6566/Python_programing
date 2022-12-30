# LL(k) parser
This repository implements an LL(k) parser that can construct lookup tables for standard grammar parsing and parsing a string.
# Output example
```
Enter number of rules : 4   
Enter none terminal 1 : S
S --> aBb
Enter none terminal 2 : B
B --> +C
Enter none terminal 3 : C
C --> (D)
Enter none terminal 4 : D
D --> id
_______________gramer______________
S --> aBb
B --> +C
C --> (D)
D --> id
_______________firsts______________
S = a
B = +
C = (
D = id
_______________follows______________
S = $
B = b,$
C = b,$
D = ),$

┌───┬─────┬───┬────┬─────┬───┬────┬───┐
│   │ a   │ b │ +  │ (   │ ) │ id │ $ │
├───┼─────┼───┼────┼─────┼───┼────┼───┤
│ S │ aBb │   │    │     │   │    │   │
├───┼─────┼───┼────┼─────┼───┼────┼───┤
│ B │     │   │ +C │     │   │    │   │
├───┼─────┼───┼────┼─────┼───┼────┼───┤
│ C │     │   │    │ (D) │   │    │   │
├───┼─────┼───┼────┼─────┼───┼────┼───┤
│ D │     │   │    │     │   │ id │   │
└───┴─────┴───┴────┴─────┴───┴────┴───┘ 

Enter string for parsing : a+(id)b

Successful parse 
```