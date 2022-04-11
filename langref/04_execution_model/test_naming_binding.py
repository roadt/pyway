#!/usr/bin/env python2
# encoding: utf-8 



# scope
# A scope defines the visibility of a name within a block.
#  If a local variable is defined in a block, its scope includes that block



#If the definition occurs in a function block, the scope extends to any blocks contained within the defining one, unless a contained block introduces a different binding for the name. 
def f():
    i = 2
    def g():
        def h():
            print i
            print j
        j = i + 2
        h()
    g()

f()    


# The scope ofnames defined in a class block is limited to the class block; it does not extend to the code blocks of methods –this includes generator expressions since they are implemented using a function scope.

# thus, following will fail  (NameError of 'a')
class A:
    a = 42
    b = list(a + i for i in range(10))


#When a name is used in a code block, it is resolved using the nearest enclosing scope. The set of all such scopes visible to a code block is called the block’s environment.

# If a name is bound in a block, it is a local variable of that block.
# If a name is bound at the module level, it is a global variable. (The variables of the module code block are local and global.)
# If a variable is used in a code block but not defined there, it is a free variable.

    


#When a name is not found at all, a NameError exception is raised. If the name refers to a local variable that has not been bound, a UnboundLocalError exception is raised. UnboundLocalError is a subclass of NameError.

# The following constructs bind names: formal parameters to functions, import statements, class and function definitions (these bind the class or function name in the defining block), and targets that are identifiers if occurring in an assignment, for loop header, in the second position of an except clause header or after as in a with statement. The import statement of the form from ... import * binds all names defined in the imported module, except those beginning with an underscore. This form may only be used at the module level.



            
            
            
            