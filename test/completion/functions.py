
def array(first_param):
    #? ['first_param']
    first_param
    return list()

#? []
array.first_param
#? []
array.first_param.
func = array
#? []
func.first_param

#? ['append']
array().append

#? ['array']
arr


def inputs(param):
    return param

#? ['append']
inputs(list).append

def variable_middle():
    var = 3
    return var

#? ['real']
variable_middle().real

def variable_rename(param):
    var = param
    return var

#? ['imag']
variable_rename(1).imag

# -----------------
# double execution
# -----------------
def double_exe(param):
    return param

#? ['upper']
variable_rename(double_exe)("").upper

# -> shouldn't work (and throw no error)
#? []
variable_rename(list())().
#? []
variable_rename(1)().

# -----------------
# recursion (should ignore)
# -----------------
def recursion(a, b):
    if a:
        return b
    else:
        return recursion(a+".", b+1)

#? int() float()
recursion("a", 1.0)

# -----------------
# keyword arguments
# -----------------

def func(a=1, b=''):
    return a, b

exe = func(b=list, a=tuple)
#? []
exe[0].real
#? ['index']
exe[0].index

#? ['append']
exe[1].append

# -----------------
# closures
# -----------------
def a():
    l = 3
    def func_b():
        #? ['real']
        l.real
        l = ''
    #? ['func_b']
    func_b
    #? ['real']
    l.real

# -----------------
# *args
# -----------------

def args_func(*args):
    return args

exe = args_func(1, "")
#? ['real']
exe[0].real
#? []
exe[0].upper

#? []
exe[1].real
#? ['upper']
exe[1].upper

lis = [1,""]
exe2 = args_func(lis)[0]

#? []
exe2[1].real
#? ['upper']
exe2[1].upper

exe3 = args_func([1,""])[0]

##? []
exe3[1].real
##? ['upper']
exe3[1].upper

def args_func(arg1, *args):
    return arg1, args

exe = args_func(1, "", list)
#? ['real']
exe[0].real
#? []
exe[0].upper

#? []
exe[1].real
#? ['index']
exe[1].index

#? []
exe[1][1].upper
#? ['append']
exe[1][1].append

# -----------------
# ** kwargs
# -----------------
def kwargs_func(**kwargs):
    return kwargs

exe = kwargs_func(a=3,b=4)
#? ['items']
exe.items

# -----------------
# *args / ** kwargs
# -----------------

def fu(a=1, b="", *args, **kwargs):
    return a, b, args, kwargs

exe = fu(list, 1, "", c=set, d="")

#? ['append']
exe[0].append
#? ['real']
exe[1].real
#? ['index']
exe[2].index
#? ['upper']
exe[2][0].upper
#? ['items']
exe[3].items
#? ['union']
exe[3]['c'].union
#? []
exe[3]['c'].upper

# -----------------
# decorators
# -----------------

def decorator(func):
    def wrapper(*args):
        return func(1, *args)
    return wrapper

@decorator
def decorated(a,b):
    return a,b

exe = decorated(set, '')

#? []
exe[0].union
#? ['union']
exe[1].union

#? ['real']
exe[0].real
#? []
exe[1].real

# more complicated with args/kwargs
def dec(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@dec
def fu(a, b, c, *args, **kwargs):
    return a, b, c, args, kwargs

exe = fu(list, c=set, b=3, d='')

#? ['append']
exe[0].append
#? ['real']
exe[1].real
#? ['union']
exe[2].union

#? []
exe[4]['d'].union
#? ['upper']
exe[4]['d'].upper


exe = fu(list, set, 3, '', d='')

#? ['upper']
exe[3][0].upper
#? []
exe[3][0].real


# -----------------
# generators
# -----------------

def gen():
    yield 1
    yield ""

gen_exe = gen()
#? ['upper']
next(gen_exe).upper
#? ['real']
next(gen_exe).real
#? int() str()
next(gen_exe)
