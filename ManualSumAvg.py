n=list()
o=int(input("No.of Elements:"))
for i in range(o):
  p=int(input("Enter Integer:"))
  n.append(p)
s=0
for i in range(o):
  s+=n[i]
print("Sum is:",s,"Average is:",s/o)