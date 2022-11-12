с = input()
l = len(с)
l = l//2
for i in range(l):
    if с[i]!=с[-1-i]:
        print("нет")
        break
else:
    print("да")
