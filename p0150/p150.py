# Online Python - IDE, Editor, Compiler, Interpreter

lim = 1000
py = [
[[0]* i for i in range(1,lim+5)],
[[0]* i for i in range(1,lim+5)],
[[0]* i for i in range(1,lim+5)],
[[0]* i for i in range(1,lim+5)]
]

t = 0
for i in range(lim):
    for j in range(i+1):
        t = (615949*t+797807)%(2**20)
        py[1][i][j] = t - 2**19

"""
for i in range(lim):
    t = ""
    for j in range(i+1):
        t += str(py[0][i][j])+ "\t"
    print(t)
"""

c = 0
miny = 10
for d in reversed(range(1,lim)):
    for i in range(d):
        for j in range(i+1):
            py[c%4][i][j] = py[(c+1)%4][i][j] + py[(c+1)%4][i+1][j] + py[(c+1)%4][i+1][j+1] - py[(c+2)%4][i+1][j] - py[(c+2)%4][i+1][j+1] - py[(c+2)%4][i+2][j+1] + py[(c+3)%4][i+2][j+1]
            
            miny = min(miny, py[c%4][i][j])
    """
    for i in range(d):
        t = ""
        for j in range(i+1):
            t += str(py[c%4][i][j])+"\t"
        print(t)
    """
    c -= 1
    #print("-"*20)
    
    print("Minimum is: " + str(miny))
