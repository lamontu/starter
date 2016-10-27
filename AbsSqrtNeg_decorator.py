def juedui(x):
    return abs(x)

def kaifang(F):
    def new_F(x):
        return F(x) ** 0.5
    return new_F

def xiangfan(F):
    def new_F(x):
        return -F(x)
    return new_F

func = xiangfan(kaifang(juedui))

print(func(-4))
