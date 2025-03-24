def solution(s):
    lst = []
    if len(s)%2==1:
        s=s+'_'
    for i in range(0,len(s),2):
        lst.append(s[i:i+2])
    return lst

print(solution("asdfads"))