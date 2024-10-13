input_data = open('input.txt' , 'r')
data = input_data.read()
data = data.split()
x1 = int(data[0])
y1 = int(data[1])
x2 = int(data[2])
y2 = int(data[3])
ax1= int(data[4])
ay1 = int(data [5])
if x2 == x1:
    b = int(ax1) -int(ax1) - int(ax1)
    out = str(b) + ' '
    out = str(out +  str(ay1))
    output = open('output.txt', 'w')
    output.write(str(out))
elif y2 == y1:
    b = int(ay1) - int(ay1) -int(ay1)
    out = ' ' + str(b)
    out = str(str(ax1) + out)   
    output = open('output.txt', 'w')
    output.write(str(out))


input_data.close()
output.close()
