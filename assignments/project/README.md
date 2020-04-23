# Insult me!

___
[![eabalwi class GitHub Repo](https://github.com/eabaldwi/biosystems-analytics-2020)](https://github.com/eabaldwi/biosystems-analytics-2020)

You're going to make a silly insult generator today!  
Write a program titled insulter.py that takes a text file of space separated adjectives, a text file of space separated nouns, and an optional number of adjectives to use with the default being one and maximum being 5. While the user may select multiple adjectives, only one noun will ever be printed. A standard adjectives.txt and nouns.txt will be provided, but if you decide to use your own, please use the same format!

##### Necessary arguments:
  - _adjectives_
  - _nouns_
  - _-num_ or _--numadjs_

## Outputs
When run with no inputs, the program should print a brief usage:
```
insert usage picture
```
Or a longer usage for the -h or --help flags:
```
insert long usage picture
```
The program should reject _adjectives_ and _nouns_ inputs that are not files. 
```
rejection picture
```

Without an optional _-num_ or _--numadjs_ statement the program should output an insult with one adjective and one noun:
```
single each argue pic
```

With an optional _-num_ or _--numadjs_ statement the program should output as many adjectives as requested, up to 5:
```
five adjs one noun pic
```

So with an _--numadjs_ of 3 the program will output:
```
You {adjlist} {nouns}!
```
### Tips and recommendations

```
Create an empty list and join the number of adjectives selected
```

```
Use a for loop or conditional statement to determine the number of  adjectives to be printed with a noun
```
## Tests:
A passable testing suite looks like this:
```
Test suite
```
*exists  
*usage  
*missings adjs  
*missing nouns  
*no numadjs  
*good input 1  
*good input 2  
*good input 3  
*good input 4  
*good input 5  

