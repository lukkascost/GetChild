import matplotlib.pyplot as plt
import numpy as np
import collections as cl
valors = np.zeros((11,999))
archives = [100,200,300,400,500,600,700,800,900,1000,1100]
for h,i in enumerate(archives):
        arquivo = open("Samples/Measurements/One_To_One/Suspend_6dbm/{:04d}cm.txt".format((i)))
        #print "Samples/Measurements/One_To_One/Suspend/{:04d}cm.txt".format((i))
        for j,k in enumerate(arquivo):
                if j == 999: break
                valors[h,j] = int(k)
        arquivo.close()      
modas = []
for h,i in enumerate(valors):
        #print "Counter for line {:d}: {}".format(h,cl.Counter(i))
        modas.append(cl.Counter(i))
        
toPlot = np.zeros((11,100))
for h in range(11):
        for j in range(100):
                toPlot[h,j] = modas[h][j+1]
        
x  = [c for c in range(1,101)]
valors = []
for i,j in enumerate(toPlot):
        media = 0
        Stri = "OCORRENCIAS EM {:02d}m: \t".format(i+1)
        stri2 = "QUANTIDADE EM {:02d}m: \t".format(i+1)
        for k,l in enumerate(j):
                if l!= 0:
                        Stri+="{:03d}\t".format(-k)
                        stri2+="{:03d}\t".format(int(l))
                        media += (-k)*l
        print Stri
        print stri2
        valors.append(media/1200)
for i,j in enumerate(valors):
        print "{:03.04f}".format(j)
print valors


        
        
rank = 5
for i in range(11):
        temp = np.argpartition(-toPlot[i], rank)
        result_args = temp[:rank]        
        plt.plot(x,toPlot[i],label = "RSSI MODA {:02d}m".format(i+1))
        print "{} mais recorrentes de {:02d}m: {}\t Media: {}\t StdDev: {}".format(rank,i+1,result_args,np.average(result_args), np.std(result_args))
plt.grid(True)
plt.legend()
plt.show()
