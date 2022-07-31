

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'appendAndDelete' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts following parameters:
# #  1. STRING s
# #  2. STRING t
# #  3. INTEGER k
# #

# def appendAndDelete(s, t, k):
#     # Write your code here
#     flag = 1
#     b = s
#     q = t
#     d1=""
#     if(s==t):
#         return "Yes"
#     for i in b:
#         if i not in q:
#             d1+=i
#         else:
#             b = b.replace(i,'',1)
#             q = q.replace(i,'',1)
#         #print(b,q)
#     b = s
#     q = t
#     d2 = ""
#     print(d1)
#     for i in q:
#         if i not in b:
#             d2+=i
#         else:
#             b = b.replace(i,'',1)
#             q = q.replace(i,'',1)
#        # print(b,q)
#     print(d2)
#     if(len(d1)+len(d2)==k):
#         return "Yes"
#     # if(len(d1)+len(d2)+1==k):
#     #     return "No"
#     if(k>len(d1)+len(d2)):
#         if(abs(len(d1)+len(d2)-k)%2==0):
#             return "Yes"
#         return "No"     
#     if(k<len(d1)+len(d2)):
#         return "No"     
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     t = input()

#     k = int(input().strip())

#     result = appendAndDelete(s, t, k)

#     fptr.write(result + '\n')

#     fptr.close()


import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    g = []
    mg = len(G)
    for i in G:
        l = list(i)
        g.append(l)
    ng = len(l)
    p = []
    mp = len(P)
    for i in P:
        l = list(i)
        p.append(l)
    np = len(l)
    count = 0
    flag = 0
    tot = mp*np
    for i in range(mg):
        for j in range(ng):
            count = 0
            flag = 0
            if(p[0][0]== g[i][j]):
                for k in range(mp):
                    for l in range(np):
                        if(i+k<mg and j+l<ng):
                            if(p[k][l]!=g[i+k][j+l]):
                                flag = 1
                                break
                    if(flag==1):
                        break
                if(flag==0):
                    return "YES"
    return "NO"
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        print(result)
