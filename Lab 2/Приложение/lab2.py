import math 
import random 
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker 
import numpy as np 
  
values = [0, 1, 2, 3] 
def get_bar(x): 
  ax = plt.subplot(1, 1, 1) 
  #ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1)) 
  ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) 
  ax.yaxis.set_major_locator(ticker.MultipleLocator(0.05)) 
  plt.ylim(0, 0.7) 
  #plt.xlim(-1, 3.5) 
  plt.xlabel("Сгенерированное число") 
  plt.ylabel("Вероятность выпадений") 
   
  ax.bar(np.array(values)-0.15, x, width = 0.3, label='Практическое выполнение') 
  ax.bar(np.array(values)+0.15, borders, width = 0.3, label='Теоретический расчет') 
  ax.legend()
  plt.legend()

results = {} 
borders = [0.027, 0.189, 0.441, 0.343] 

N = 10000 
for _ in range(N): 
  r = random.random() 
  for i in range(len(borders) + 1): 
    if r < sum(borders[:i]): 
      if i - 1 not in results.keys(): 
        results[i - 1] = 0 
      results[i - 1] += 1 
      break 
  
x = [] 
for key, value in sorted(list(results.items())): 
  print(key, value / N) 
  x.append(value / N) 
get_bar(x) 
  
#results = {} 
#borders = [0.008, 0.175, 0.525, 0.292] 
  
#N = 10000 
#for _ in range(N): 
  #r = random.random() 
  #for i in range(len(borders) + 1): 
    #if r < sum(borders[:i]): 
      #if i - 1 not in results.keys(): 
        #results[i - 1] = 0 
      #results[i - 1] += 1 
      #break  

#x = [] 
#for key, value in sorted(list(results.items())): 
  #print(key, value / N) 
  #x.append(value / N) 
#get_bar(x)
plt.show()