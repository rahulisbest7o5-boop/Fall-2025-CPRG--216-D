'''header'''
def square(x):
    ''' body'''
    y=x**2   
    return y
'''
number = 3
y = square(number)

print(y)
print(square.__doc__)

def new_func():
    def my_max(x, y):
        if x>y:
           m= x
        else:
            m=y
        return m


    def my_min(p,q):
        if p<q:
         n=p
        else:
         n=q
        return n
    number = 4
    n = my_min(number)
    print(n)
    return my_max,my_min
print(new_func(my_max(5 ,9)))



def read_file(file):
  fid = open(file,'r')
  text = fid.readline()
  return text

msg = read_file ('ty')
print(msg)
'''




# varible length


global_var = 1

def print_local_global():
   global inside_global
   inside_global = 4
   local_var = 3
   print(inside_global)
   print(local_var)
   print(global_var)


print_local_global()
print(inside_global)
print(local_var)
print(global_var)
print_local_global()








