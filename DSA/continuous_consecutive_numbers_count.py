arr = [5, 6, 7,4,38,9,10,11,22,23]
current_count=1
max_count=1
start=0
results=[]
for i in range(1,len(arr)):
    if arr[i]==arr[i-1]+1:
        current_count+=1
    else:
        start=i
        current_count=1
    if max_count<current_count:
        max_count=current_count
        results=[arr[start:start+max_count]]
    elif current_count==max_count:
        results.append(arr[start:start+max_count])
        
print(max_count,results)


# import pyvisa

# rm = pyvisa.ResourceManager()
# inst = rm.open_resource('TCPIP0::169.254.54.47::inst0::INSTR')   
# n                                                                                                            
# print(inst.query('*IDN?'))


