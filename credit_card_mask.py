def maskify(cc):
    if len(cc) == 0:
        return ''
    for element in cc:
        return '#'*(len(cc)-4) + cc[-4:]

print(maskify('SF$SDfgsd2eA'))
print(maskify(''))
print(maskify('12'))
print(maskify('123'))
print(maskify('1234'))
