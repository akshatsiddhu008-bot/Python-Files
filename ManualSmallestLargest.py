l=list()
n=int(input("No.of Elements:"))
for i in range(n):
  f=input("Enter integer:")
  l.append(f)
m=l[0]
for i in range(n):
  if l[i]>m:
    m=l[i]
print("Largest element:",m)
s=l[0]
for i in range(n):
  if l[i]<s:
    s=l[i]
print("smallest element:",s)