#coding: utf-8
def my_sum(*arg):
    print ('in my_sum')
    return sum(arg)

def my_average(*arg):
    return sum(arg) / len(arg)

def dec(func):
    def in_dec(*arg): #my_sum, func wos put in cloesure
        print ('in dec arg=', arg)
        if len(arg) == 0:
           return 0
        for val in arg:
           if not isinstance(val, int):
               return 0
        return func(*arg)
    return in_dec



#dec return in_dec -> my_sum
#my_sum = in_dec(*arg)
my_sum = dec(my_sum)

print (my_sum(1, 2, 3, 4, 5))
print (my_sum(1, 2, 3, 4, 5,'6'))

#print (my_average(1, 2, 3, 4, 5))
#print (my_average())
                               
                        
