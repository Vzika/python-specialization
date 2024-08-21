def add(a,b):
  return(a + b)

def sub(a,b):
  return a - b

def mul(a,b):
  return a * b

def div(a,b):
  return a / b

#print(mul(2,3))
#addtion  = add
 #add(3,2)

def cal(function_name, a, b):
  if  function_name == add:
    print(function_name(a, b))
    #print("hi")
  elif  function_name == sub:
    print(function_name(a, b))
  elif  function_name == mul:
    print(function_name(a, b))
  elif  function_name == div:
    print(function_name(a, b))
  else:
    print("invalid function")
    
cal(add,2,3);
cal(sub,2,3);
cal(mul,2,3);
cal(div,2,3);

