
x=input()
H,M=x.split()
angle=abs(0.5*(60*int(H)-11*int(M)))
if angle>=180:
    angle=abs(360-angle)

print("{:.4f}".format(angle))