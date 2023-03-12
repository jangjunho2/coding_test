from string import ascii_lowercase
alpha=list(ascii_lowercase)
# # print(alpha)
# print(list(ascii_lowercase))

x=input()

for i in alpha:
    print(x.find(i))