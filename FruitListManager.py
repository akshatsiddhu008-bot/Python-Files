l=list()
n=int(input("No.of Elements:"))
for i in range(n):
  f=input("Enter fruit:")
  l.append(f)
print("Second Element:",l[1],"Fourth Element:",l[3])
l[-1]="Mango"
print(l)
print()