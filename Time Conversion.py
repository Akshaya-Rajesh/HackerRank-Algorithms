def timeconversion(s):
    if(s[8]=='A'):
        if(s[:2]=='12'):
            return("00"+s[2:8])
        else:
            return(s[0:8])
    else:
        if(s[:2]=='12'):
            return(s[0:8])
        else:
            return(str(int(s[:2])+12)+s[2:8])

s=input()
print(timeconversion(s))
