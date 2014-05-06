import os
"""
   Test if a file or directory exists.
   #param string
   #return bool
"""
  
def doesPathExist(path):
    if os.path.exists(path) is True:
      return True
    else: 
	  return False

"""
   Converts argument to a string.
   #param variable
   #return string 
"""
def ToString(var):
    return str(var)                
