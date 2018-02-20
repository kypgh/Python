def rot13(s):
    lower = ''.join(chr(c) for c in range (97,123))
    upper = ''.join(chr(c) for c in range (65,91))
    l = lower[13:] + lower[:13]
    u = upper[13:] + upper[:13]
    output = ""
    for c in s:
        if c in lower:
                output += l[lower.find(c)]
        elif c in upper:
            output += u[upper.find(c)]
        else:
            output += c
    return output
x=raw_input("grapse ena keimeno \n")

print rot13(x)
