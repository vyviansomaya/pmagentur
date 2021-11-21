


# 1.1

def factorial(num):
    sum=1
    for i in range(1,num+1):
        sum*=i
    return sum


# Example

# input:  print(factorial(8))
# output: 40320



# 1.2

def questionsMarks(str1):
    len1=len(str1)
    flg=False
    attr1=0;
    
    if(str1.count("???")>0):
       # print(str1.count("???"))
        attr2=str1.count("???")
        for i in range(0,attr2):
            j=str1.find("???",attr1)
        #    print(" j ",j)
            attr1=j
            if(j!=0 and (j <len1-5)):
        #        print("yes 1")
                if(str1[j-1].isdigit()):
        #          print("yes 2")
                    if(str1[j+3].isdigit()):
         #               print(" yes 3",isinstance(int(str1[j-1]),int))
         #               print(" yes 5 ",int(str1[j-1]), int(str1[j+3]))
                        if((int(str1[j-1])+ int(str1[j+3]))==10):
          #                  print(" ys 4")
                            flg=True
    return flg
        

# Example

# input:  print(questionsMarks("arrb6???4xxbl5???eee5"))
# output: True



# 1.3 prime factorial 

import math

def ifprime(num):
    flg=True
    for i in range(2,math.ceil(num/2)):
        if num%i==0:
            flg=False
            break
    return flg
 
 def getPrimeNumbersTo(num):
    
    lst_prime=[]
    if(num==2):
        lst_prime.append(num)
    elif num>2:
        for i in range (2,num):
            if(ifprime(i)):
                lst_prime.append(i)
    str1="";
    str1=','.join(map(str,lst_prime))
    return str1

# Example

# input:  getPrimeNumbersTo(13)
# output: '2,3,4,5,7,11'

#1.4 binary tree
import re
def constructTree(strArr):
    node={}
    child={}
    for i in strArr:
        lst2=i.split(",")
        
            
        a=re.sub(r"[()]","",lst2[0])
        b=re.sub(r"[()]","",lst2[1])
      #  print("a", a)
      #  print("b ",b)
        if a in child.keys():
      #      print("dis1")
            return False
        else:
            child[a]=b
       #     print(child)
        if b not in node.keys():
            node[b]=[a]
        #    print(node)
        else:
            if(len(node.get(b))>=2):
         #       print("dis2")
                return False
            else:
                node.get(b).append(a)
          #      print(node)
    return True    
               
 # Example

# input:  lst1=["(1,2)","(2,4)","(5,7)","(7,2)","(9,5)"]
		  constructTree(lst1)
# output: True    