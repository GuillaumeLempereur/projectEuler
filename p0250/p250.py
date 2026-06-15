#p250

lim = 250250

ssmod = [] # subset modulo: nb of subset distributed by their sum%250
for i in range(250):
    ssmod.append(0)

N = {} # numbers : mod 250
for n in range(1,lim+1):
    N[n] = 1
    m = n
    for b in reversed(bin(n)[2:-1]):
        #print(n,b, bin(n)[2:])
        m = (m * m)%250
        if b == "1":
            N[n] = (N[n] * m)%250
    if n%2 == 1:
        N[n] = (N[n] * n)%250
        #print("\t", b)
#print(N)

for k in N:
    n = N[k]
    ssmod2 = ssmod[:]

    print("n: {}".format(n))
    for i in range(250):
        m = (i + n)%250
        #print("\ti: {} > {} - {}".format(i, ssmod[i],m))
        ssmod2[m] += ssmod[i]
        ssmod2[m] = ssmod2[m]%(10**16)

    ssmod2[n%250] += 1
    ssmod = ssmod2

print("Ans:", ssmod[0])
