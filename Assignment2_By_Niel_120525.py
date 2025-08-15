1.
create a function :
    accept 2 arg. and performs it square.
    make it store that function into the python directory and using another function call first function.
    
2.
create a function :
    accept 2 arg. and performs it square with below arg.:
    default arg
    keyword arg
    arbitary arg
    required arg.

default arg.:
==============
#default.:
def get_sqr2( ip2, ip1=10):
    x=ip1*ip2
    return x
    
output.:
=========
get_sqr2(3)
#30

output.:
=========
get_sqr2(10)
#100

keyword arg.:
==============
def get_sqr(ip1, ip2):
    x=ip1*ip2
    return x

output.:
=========
get_sqr(ip2=10,ip1=2)
#20

arbitary arg.:
===============
#Arbitrary Arguments
def get_sqr3( *ip_val):
    l=[]
    for i in ip_val:
        l.append(i*i)
    return l

output.:
=========
get_sqr3(1,2,4)
#[1, 4, 16]
    
def get_sqr4( *ip_val):
    l=[]
    for i in ip_val:
        l.append(i**2)
    return l
    
output.:
=========
get_sqr4(1,2,4)
#[1, 4, 16]
    
required arg.:
===============
#Required Arguments
def get_sqr(ip1, ip2):
    x=ip1*ip2
    return x
    
output.:
=========
get_sqr(10,2)
#20

output.:
=========
get_sqr(10) 
#ERROR  missing 1 required positional argument: 'ip2'

3.
Take a list 
l=['Hi', 'Hello', 'Bye']
print the 2nd character of each element using for loop, lambda function, list comphersion.
op: ['i', 'e', 'y']

#using for loop
=================
l=['Hi', 'Hello', 'Bye']
l2=[]
for i in l:
    l2.append(i[1])
print (l2)

output.:
=========
['i', 'e', 'y']

#using map lambda function.:
============================
l=['Hi', 'Hello', 'Bye']
l2=[]
l2=list(map(lambda x :x[1],l))
print (l2)

output.:
=========
['i', 'e', 'y']


#using filter lambda function.:
l=['Hi', 'Hello', 'Bye']
l2=[]
l2=list(filter(lambda x :len(x[1])==1,l))
print (l2)

output.:
=========
['Hi', 'Hello', 'Bye']

#using List comphersion
l=['Hi', 'Hello', 'Bye']
[i[1] for i in l ]

output.:
=========
['i', 'e', 'y']

#using List comphersion, op store into a variable and print that variable values
=================================================================================
l=['Hi', 'Hello', 'Bye']
l2=[i[1] for i in l ]
print(l2)

output.:
=========
['i', 'e', 'y']