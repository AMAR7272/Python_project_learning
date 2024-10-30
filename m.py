def cntChrs(str):
    cntChars=dict()
    for char in str:
        cnt=str.count(char)
        cntChars[char]=cnt
    print("Total number of each characters in the given string are:", cntChars)
str=input("Enter the string:")
cntChrs(str)
