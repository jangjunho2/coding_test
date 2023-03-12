a=list(input())
b=len(a)
for i in range(b):
    if a[i].isupper():
        a[i]=a[i].lower()

    else:
        a[i]=a[i].upper()

print("".join(a))