text = "  Hello, Python World!  "

print(text.lower())           #   hello, python world!  
print(text.upper())           #   HELLO, PYTHON WORLD!  
print(text.title())           #   Hello, Python World!  
print(text.capitalize())      #   hello, python world!  
print(text.strip())           # Hello, Python World!
print(text.lstrip())          # Hello, Python World!  
print(text.rstrip())          #   Hello, Python World!
print(text.replace("Python", "Java"))  #   Hello, Java World!  
print(text.split())           # ['Hello,', 'Python', 'World!']
print(text.split(','))        # ['  Hello', ' Python World!  ']
print(','.join(['a', 'b']))   # a,b
print(text.find("World"))     # 16
print(text.index("World"))    # 16
print(text.count("o"))        # 3
print(text.startswith("  He"))# True
print(text.endswith("!  "))   # True
print(text.isalpha())         # False
print(text.isdigit())         # False
print(text.isalnum())         # False
print(text.isspace())         # False
print(text.swapcase())        #  HELLO, pYTHON wORLD!  
print(text.center(30, '*'))   # ****  Hello, Python World!  ****
print(text.ljust(30, '-'))    #   Hello, Python World!  -----
print(text.rjust(30, '-'))    # -----  Hello, Python World!  
print(text.zfill(30))         # 00000  Hello, Python World!  00
print(text.encode())          # b'  Hello, Python World!  '