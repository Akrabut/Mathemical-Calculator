####EXERCISE 1####
class date:
    #Takes a year, month and day value and creates an object that represents a date
    def __init__(self, newyear, newmonth, newday):
        self.year = newyear
        if(newmonth == 1):
            self.month = "January"
        if(newmonth == 2):
            self.month = "February"
        if(newmonth == 3):
            self.month = "March"
        if(newmonth == 4):
            self.month = "April"
        if(newmonth == 5):
            self.month = "May"
        if(newmonth == 6):
            self.month = "June"
        if(newmonth == 7):
            self.month = "July"
        if(newmonth == 8):
            self.month = "August"
        if(newmonth == 9):
            self.month = "September"
        if(newmonth == 10):
            self.month = "October"
        if(newmonth == 11):
            self.month = "November"
        if(newmonth == 12):
            self.month = "December"
        self.day = newday
    def __repr__(self):
        return 'date()'
    def __str__(self):
        return str(self.day) + " of " + str(self.month) + ", " + str(self.year)
    
class time:
    #takes an hour and a min values and creates an object that represents the time
    def __init__(self, newhour, newmin):
        self.hour = newhour
        self.min = newmin
    def __repr__(self):
        return 'time()'
    def __str__(self):
        if (self.min < 10):
            return str(self.hour) + ':' + '0' + str(self.min)
        return str(self.hour) + ':' + str(self.min)

class task:
    #A class that represents a task, makes the calendarentry code more readable
    def __init__(self, name, time1, time2):
        self.name = name
        self.time1 = time1
        self.time2 = time2

class calendarentry:
    #represents a calendar entry which may contain a list of tasks needed to be done at a certain time and ate.
    #also sorts the tasks by time
    def __init__(self, year, month, day):
        self.tasks = []
        self.index = 0
        self.day = date(year, month, day)
    def addtask(self, name, time1, time2):
        for i in range(0, self.index):
            if (time1.hour is self.tasks[i].time1.hour and time2.hour is self.tasks[i].time2.hour and time1.min is self.tasks[i].time1.min and time2.min is self.tasks[i].time2.min):
                print ("Invalid entry")
                return
        self.index += 1
        self.newtask = task(name, time1, time2)
        self.tasks.append(self.newtask)
        self.tasks = sorted(self.tasks, key = lambda task: task.time1.hour)
    def __repr__(self):
        return 'calendarentry()'
    def __str__(self):
        print("Todo list for", self.day, ":")
        for i in range(0, self.index):
            print (i+1, ".", self.tasks[i].time1, "-", self.tasks[i].time2, "-", self.tasks[i].name)
        return ""

####EXERCISE 2####
    #Functions from the presentations
def make_class(attributes, base_class=None):
    def get_value(name):
            if name in attributes:
                return attributes[name]
            elif base_class is not None:
                return base_class['get'](name)
    def set_value(name, value):
        attributes[name] = value
    def new(*args):
        return init_instance(cls, *args)
    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls

def init_instance(cls, *args):
        instance = make_instance(cls)
        init = cls['get']('__init__')
        if init:
            init(instance, *args)
        return instance

def make_instance(cls):
    attributes = {}
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
        return bind_method(value,instance)
    def set_value(name, value):
        attributes[name] = value
    instance = {'get': get_value, 'set': set_value}
    return instance

def bind_method(value, instance):
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value   

def make_date_class():
    #implementation of date class using a function
    def __init__(self, year, month, day):
        self['set']('year', year)
        self['set']('month', month)
        self['set']('day', day)
    return make_class({'__init__':__init__})

def make_calentry_class():
    #implementation of calendar class using a fuction
    def __init__(self, year, month, day):
        self['set']('year',year)
        self['set']('month',month)
        self['set']('day',day)
    def addtask(self, name, time1, time2):
        if(self['get']('tasks') == None):
            self['set']('tasks', {(time1['get']('__str__')(), time2['get']('__str__')()): name})
        else:
            tasks = {(time1['get']('__str__')(), time2['get']('__str__')()): name}
            tasks.update(self['get']('tasks'))
            self['set']('tasks', tasks)
    return make_class({'__init__':__init__, 'addtask':addtask})

def make_time_class():
    #implementation of time class using a function
    def __init__(self, hour, min):
        self['set']('hour', hour)
        self['set']('min', min)
    def __str__(self):
        if (self['get']('min') < 10):
            return str(self['get']('hour')) + ':' + '0' + str(self['get']('min'))
        return str(self['get']('hour')) + ':' + str(self['get']('min'))
    return make_class({'__init__':__init__, '__str__':__str__})

####EXERCISE 3####
rates={('dollar','nis'):3.82,('euro','nis'):4.07, ('nis', 'dollar'): 0.26, ('euro', 'dollar'): 0.93, ('dollar', 'euro'):1.06, ('nis', 'euro'): 0.24}
class shekel:
    #represents shekel currency, can calculate the addition of two values
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value) + 'nis'
    def __repr__(self):
        return 'shekel' + '(' + str(self.value) + ')'
    def __add__(self, other):
        return self.amount() + other.amount()
    def amount(self):
        return self.value
    
class dollar:
    #represents dollar currency, can calculate the addition of two values and convert to shekel
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value) + '$'
    def __repr__(self):
        return 'dollar' + '(' + str(self.value) + ')'
    def __add__(self, other):
        return self.amount() + other.amount()
    def amount(self):
        return self.value * rates['dollar', 'nis']

class euro:
    #represents euro currency, can calculate the addition of two values and convert to shekel
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value) + 'eu'
    def __repr__(self):
        return 'euro' + '(' + str(self.value) + ')'
    def __add__(self, other):
        return self.amount() + other.amount()
    def amount(self):
        return self.value * rates['euro', 'nis']

def add(coin1, coin2):
    #the required addition function
    return coin1.amount() + coin2.amount()

####EXERCISE 4####
def add_shekel(c1, c2):
    #addition of shekel and other currency, result is respresented in shekels
    return 'shekel('+str(c1.amount() + c2.amount())+')'
def sub_shekel(c1, c2):
    #subtractioon of shekel and other currency, result is respresented in shekels
    return 'shekel('+str(c1.amount() - c2.amount())+')'

def add_dollar(c1, c2):
    #addition of dollar and other currency, result is respresented in dollars
    if (type(c2) == shekel):
        return 'dollar(' + str(c1.value + c2.value * rates['dollar', 'nis']) + ')'
    if (type(c2) == dollar):
        return 'dollar(' + str(c1.value + c2.value) + ')'
    if (type(c2) == euro):
        return 'dollar(' + str(c1.value + c2.value * rates['euro', 'dollar']) + ')'
    
def sub_dollar(c1, c2):
    #subtraction of dollar and other currency, result is respresented in dollars
    if (type(c2) == shekel):
        return 'dollar(' + str(c1.value - c2.value * rates['dollar', 'nis']) + ')'
    if (type(c2) == dollar):
        return 'dollar(' + str(c1.value - c2.value) + ')'
    if (type(c2) == euro):
        return 'dollar(' + str(c1.value - c2.value * rates['euro', 'dollar']) + ')'

def add_euro(c1, c2):
    #addition of euros and other currency, result is respresented in euros
    if (type(c2) == shekel):
        return 'euro(' + str(c1.value + c2.value * rates['nis', 'euro']) + ')'
    if (type(c2) == dollar):
        return 'euro(' + str(c1.value + c2.value * rates['dollar', 'euro']) + ')'
    if (type(c2) == euro):
        return 'euro(' + str(c1.value + c2.value) + ')'
 
def sub_euro(c1, c2):
    #subtraction of euros and other currency, result is respresented in euros
    if (type(c2) == shekel):
        return 'euro(' + str(c1.value - c2.value * rates['nis', 'euro']) + ')'
    if (type(c2) == dollar):
        return 'euro(' + str(c1.value - c2.value * rates['dollar', 'euro']) + ')'
    if (type(c2) == euro):
        return 'euro(' + str(c1.value - c2.value) + ')'       

#dispatch on type method
dispatch = {('add', (shekel, shekel)): add_shekel, ('add', (shekel, dollar)): add_shekel, ('add', (shekel, euro)): add_shekel,
                   ('add', (dollar, shekel)): add_dollar, ('add', (dollar, dollar)): add_dollar, ('add', (dollar, euro)): add_dollar,
                    ('add', (euro, shekel)): add_euro, ('add', (euro, dollar)): add_euro, ('add', (euro, euro)): add_euro,
                    ('sub', (shekel, shekel)): sub_shekel, ('sub', (shekel, dollar)): sub_shekel, ('sub', (shekel, euro)): sub_shekel,
                   ('sub', (dollar, shekel)): sub_dollar, ('sub', (dollar, dollar)): sub_dollar, ('sub', (dollar, euro)): sub_dollar,
                    ('sub', (euro, shekel)): sub_euro, ('sub', (euro, dollar)): sub_euro, ('sub', (euro, euro)): sub_euro}

def apply(op, c1, c2):
    #the apply functioon
    return dispatch[op, (type(c1), type(c2))](c1, c2)

####EXERCISE 5####

coercions = {('dollar', 'nis'): dollar.amount, ('euro', 'nis'): euro.amount}
    #the coercion dictionary
def coerce_apply(op, c1, c2):
    #returns the result in shekels
    if (op == 'add'):
        return 'Shekel(' + str(c1.amount() + c2.amount()) + ')'
    if (op == 'sub'):
        return 'Shekel(' + str(c1.amount() - c2.amount()) + ')'

####EXERCISE 6####
def get_reverse_map_iterator(s, g = lambda x: x):
    #gets a sequence and a nameless function or just a sequence.
    #if input is 'next', either returns g applied on s[i] if g exists, or return s[i] otherwise.
    i = len(s)
    def has_more():
        nonlocal i
        if (i == 0):
            return False
        else: return True
    def next():
    #The edited Next function
        nonlocal i 
        try:
            i -= 1
            if (i < 0):
                raise IndexError
            print(g(s[i]))
        except IndexError:
            print("no more items")
            return
        except (ZeroDivisionError, ArithmeticError, ValueError, TypeError):
            return next()
    return {'next': next, 'has_more': has_more}

####EXERCISE 7####

from functools import reduce
from operator import mul,add

class Exp(object):
     def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands
        
     def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

     def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)

def calc_eval(exp):
    #Evaluate a Calculator expression.
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)

def calc_apply(operator, args):
    #Apply the named operator to a list of args.
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer/denom
    #The required additions.
    if operator in ('pow', '^'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly two arguements')
        return args[0]**args[1]
    if operator in ('sqrt', 'V'):
        if len(args) != 1:
            raise TypeError(operator + ' requires exactly one arguement')
        if (args[0] < 0): 
            raise ValueError(operator + ' math domain error')
        return args[0]**0.5

def read_eval_print_loop():
    #Run a read-eval-print loop for calculator.
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError,ValueError,ArithmeticError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return

def calc_parse(line):
    #Parse a line of calculator input and return an expression tree.
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree

def tokenize(line):
    spaced = line.replace('(',' ( ').replace(')',' ) ').replace(',', ' , ')
    return spaced.strip().split()

def analyze(tokens):
    #Create a tree of nested lists from a sequence of tokens.
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected ' + token)

def analyze_operands(tokens):
    #Read a list of comma-separated operands.
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands

def analyze_token(token):
    #Return the value of token if it can be analyzed as a number, or token.
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token
        except ArithmeticError as e:
            return e

known_operators = ['add', 'sub', 'mul', 'div', 'pow','sqrt','+', '-', '*', '/','^','V']

def assert_non_empty(tokens):
    #Raise an exception if tokens is empty.
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')

read_eval_print_loop()