input_data = open("input.txt","r")
data = input_data.read()
data = int(data)
a= data**2
a= str(a)
output_data = open("output.txt","w")
output_data.write(a)
input_data.close()
output_data.close()