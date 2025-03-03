# Operatos

#Arithmetic Operators
#Assignment Operators
#Relation / Comparison Operators
#Logical Operators

#Arithmetic Operators
#+, -, *, /, %, **, 

x = 10
y = 5
sum = (x+y)
print(sum)

x = 10
y = 5
sub = (x-y)
print(sub) #Ans will be 5

x = 10
y = 5
mul = (x*y)
print(mul) #Ans will be 50

x = 10
y = 5
div1 = (x/y)
print(div1) #Ans will be 

x = 10
y = 5
div2 = (x//y) #Floor Division
print(div2) #Ans will be 2.0 (It makes round figure)

x = 8
y = 8
exp = (x**y) # exponent  8^2 = 8 X 8
print(exp) #Ans will be 64


x = 20
y = 5
mod = (x%y) #remainder / modulus
print(mod)  #Ans will be 0


 
#Logical Operators
#And, Or, Not
# if else
 
# Function to check the status of K-Electric and UPS

def check_power_status(k_electric_status):
    if k_electric_status == "on":
        ups_status = "off" 
    elif k_electric_status == "off":
        ups_status = "on"
    else:
        return "Invalid status for K-Electric. Use 'on' or 'off'."
    
    return f"K-Electric is {k_electric_status}, so UPS is {ups_status}."

# Test cases
print(check_power_status("on"))   # Output: K-Electric is on, so UPS is off.
print(check_power_status("off"))  # Output: K-Electric is off, so UPS is on.







 