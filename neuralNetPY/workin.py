from scipy.special import kolmogorov

def KolmogorovComplexity(s):
    for i in range(1, 10000):
        for p in range(i):
            if eval(p) == s:
                return i

print(KolmogorovComplexity('0'))
