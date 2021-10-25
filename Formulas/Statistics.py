from collections import Counter
import math

def Mean(data) :
   mean = sum(data, 0)
   mean = mean / len(data)
   return mean

def Median(data) :
   if (len(data) % 2 == 0) :
      middle1 = len(data) // 2
      middle2 = middle1 - 1
      median = (data[middle1] + data[middle2]) / 2
   else :
      median = data[len(data)//2]
   return median

def Mode(data) :
   frequency = Counter(data)
   return frequency.most_common(1)

def Quartiles(data):
   if(len(data) % 2 == 0) :
      q1_1 = data[len(data) // 4 - 1]
      q1_2 = data[(len(data) // 4)]
      q1 = (q1_1 + q1_2) / 2
      q3_1 = data[len(data) - (len(data) // 4)]
      q3_2 = data[len(data) - (len(data) // 4 + 1)]
      q3 = (q3_1 + q3_2) / 2
   else :
      q1 = data[(len(data) // 4)]
      q3 = data[((len(data) // 4) * 3) - 1]
   IQR = q3 - q1
   results = [q1,Median(data),q3,IQR]
   return results
   
def OutliarsLow(data) :
   quartiles = Quartiles(data)
   low = quartiles[0] - (quartiles[3] * 1.5)
   lowOutliars = []
   for x in data :
      if (x < low) :
         lx = [x]
         lowOutliars += lx
   return lowOutliars

def OutliarsHigh(data) :
   quartiles = Quartiles(data)
   High = quartiles[2] + (quartiles[3] * 1.5)
   HighOutliars = []
   for x in data :
      if (x > High) :
         lx = [x]
         HighOutliars += lx
   return HighOutliars
   
def Variance(data, mode) : #mode 1 for sample, Mode 0 for population
   sum = 0
   mean = Mean(data)
   for x in data :
      sum += (x - mean) ** 2
   varience = round(sum / (len(data) - mode), 4)
   standardDeviation = round(math.sqrt(varience), 4)
   return [varience, standardDeviation]