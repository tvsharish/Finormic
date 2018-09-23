
def threesum(num,tar):
    num=sorted(num)
    sum0=num[0]+num[1]+num[2]
    for i in range(0,len(num)-2):
        j=i+1
        k=len(num)-1
        while j<k:
            if (tar==sum0):
                return sum0
            if(abs(sum0)>abs(num[i]+num[j]+num[k])):
               sum0=num[i]+num[j]+num[k]
            if (num[i]+num[j]+num[k]>tar):
                k=k-1
            else:
                j=j+1
    return sum0
                    


