# 1
print(1)
print(2)
print("fizz")
print(4)
print("buzz")
print("fizz")
print(7)
print(8)
print("fizz")
print("buzz")
print(11)
print("fizz")
print(13)
print(14)
print("fizzbuzz")


# 2.
for x in range(1, 16):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)

        
# 3.
def solution(x):
  if x % 3 and x % 5 == 0:
    return "fizzbuzz"
  elif x % 3 == 0:
    return "fizz"
  elif x % 5 == 0:
    return "buzz"
  else:
    return x
  
answer = [solution(x) for x in list(range(1, 16)]
print(answer
      
or
      
      
answer = ["fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else x  for x in list(range(1, 16))]
answer