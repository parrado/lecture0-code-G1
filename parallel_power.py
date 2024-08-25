def checkPower(resistance,v,p):
    from math import sqrt
    
    totalI=0
    for j in range(len(resistance)):             
        iMax=sqrt(p/resistance[j])
        i=v/resistance[j]
        totalI+=i
        if i>iMax:
            raise ValueError(f'Current exceeded permitted  value for R{j+1}')
        
    return totalI
   
# Maximum power for each resistor
rPower=1/4

# Input voltage
vIn=5.0

# Ask user for number of resistors
nResistors=int(input('Enter the number of resistors: '))

R=[]

# For loop to ask resistance value for each resistor
for i in range(nResistors):
    R.append(float(input(f'Enter resistance for resistor {i+1}: ')))

# Function checkPower
# This function raises an error 
# if dissipated power exceeds rated power, 
# otherwise it returns total current.
# arguments:R, resistance values list 
#           vIin, input voltage
#           rPower, rated power of resistors
i=checkPower(R,vIn,rPower)

print(f'Total current in circuit is: {i*1000:.2f} mA')




