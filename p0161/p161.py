#161

#A0 1 2 3 4 5

# round 1:
#               1 2  3  4  5
# env = {(1, 1, 1, 1, 1): 1}
env = {(1, 1, 1, 1, 1): 1}

for i in range(1,16):
    nexenv = {}
    print("Round: {}".format(i))
    for e in env:
        k = list(e)
        print("env: {}".format(e))
        for p in range(len(k)-1):
            if k[p] == 0:
                continue
            n = k[:]
            n[p] = k[p] - 1
            for q in range(p+1, len(k)):
                n[q] = k[q] + 1
            n[-1] -= 1
            n = tuple(n)
            if n in nexenv:
                nexenv[n] += env[e]
            else:
                nexenv[n] = env[e]
            print(n)
        if k[-1] > 0:
            n = k[:]
            n[-1] -= 1
            n = tuple(n)
            if n in nexenv:
                nexenv[n] += env[e]
            else:
                nexenv[n] = env[e]
            print(n)
            
    env = nexenv
    print()