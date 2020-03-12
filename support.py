#librerías

import glob
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import interpolate
import math
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#función que devuelve los tiempos y w's
#outputs: w,wc,t,tc

def evol_w(file_path,t,w,tc,wc):

        os.chdir(file_path)
        files=[]
        files = sorted(glob.glob('*.dat'))
        tiempo = np.loadtxt('time.dat')

        global end
        end = len(tiempo)
        
        for i in range(end):
            t.append(tiempo[i])
        files = files[0:end]
        for file in files:
            data = np.loadtxt(file,float,'#',',')
            X = data[:,1]
            Y = data[:,0]
            len_y = len(Y)
            a=0
            h=(1/len_y)*sum(Y)
            for i in range(len_y):
                a=a+(Y[i]-h)**2
            w.append(math.sqrt((1/len_y)*a))

        plt.plot(t,w)
        plt.yscale('log')    
        plt.xscale('log')
        punto = np.asarray(plt.ginput(1,timeout=0))
        plt.close()

        for l in range(end):
            a = w[l]**2-punto[:,1]**2
            if a>=0:
                wc.append(math.sqrt(a))
                tc.append(t[l]-punto[:,0])
            else:
                pass

def evol2_w(t,w,tc,wc):

        plt.plot(t,w)
        plt.yscale('log')    
        plt.xscale('log')
        punto = np.asarray(plt.ginput(1,timeout=0))

        plt.close()

        for l in range(end):
            a = w[l]**2-punto[:,1]**2
            if a>=0:
                wc.append(math.sqrt(a))
                tc.append(t[l]-punto[:,0])
            else:
                pass
        


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
