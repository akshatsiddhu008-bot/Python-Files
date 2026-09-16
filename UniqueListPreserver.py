l=list()
n=int(input("No.of Elements:"))
for i in range(n):
  f=input("Enter integer:")
  l.append(f)
for i in range(n):
  if l.count(i)>1:
    l.remove(i)
print(l)