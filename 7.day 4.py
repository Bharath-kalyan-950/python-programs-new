def countstrings(n,s):
    if n == 0:
        return 1
    count = 0
    for i in range(s, 5):
        count += countstrings(n - 1, i)
    return count
def countVowelStrings(n):
   
    return countstrings(n, 0)
n = int(input("enter the num :"))
print(countVowelStrings(n))
