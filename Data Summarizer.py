from Formulas import Statistics


#ask user for data
user = input("type data set: ")
data = []
counter = 0
temp = ""
while counter < len(user) :

   while(user[counter : counter + 1].isdigit()) :
      temp += (user[counter : counter + 1])
      counter += 1
      
   data.append(int(temp))
   temp = ""
   counter += 1

   
#display data 
data.sort()
print("data length: ",len(data))
line = 0
counter = 0
for x in data :
   if (line == 10) :
      print("")
      line = 0
   print(data[counter],end = " ")
   line += 1
   counter += 1
   
   
#display satistics
print("\n\n")

print("min: ",data[0],"max: ",data[len(data)-1],"range: ",data[len(data)-1] - data[0])

print("Mean: ",Statistics.Mean(data))

print("Median: ",Statistics.Median(data))

print("(Mode, frequency): ",Statistics.Mode(data))

print(" [Q1,   Q2,   Q3,   IQR]\n",Statistics.Quartiles(data))


#display outliars
Outliars = []
for x in Statistics.OutliarsLow(data) :
   xl = [x]
   Outliars += xl
for x in Statistics.OutliarsHigh(data) :
   xl = [x]
   Outliars += xl
print("Outliars: ",Outliars)


#Cdisplay varience
print("SampleVariance standardDevaition\n",Statistics.Variance(data,1),"\nPopVariance standardDevaition\n",Statistics.Variance(data,0))