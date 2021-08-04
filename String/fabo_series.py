#!/usr/bin/env python3
#memoziation for fabo series
memo=[0,1]
def fabo_series(num):
    if num<=0:
        return -1
    if num<=len(memo):
        return memo[num-1]
    else:
        temp=fabo_series(num-1)+fabo_series(num-2)
        memo.append(temp)
        return temp

print("Fabo:"+str(fabo_series(8)))
