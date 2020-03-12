# Marcos Moreno Blanco // UB // 2019-2020

from tkinter import *   
from tkinter import ttk  
from tkinter import filedialog
from tkinter import font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib as plt
plt.use("TkAgg")
import numpy as np
import math
import os
import glob 
import sys
import urllib.request
import support


class App():

    def __init__(self):
    # inicio
        self.create_window(800,600)
        self.helv36 = font.Font(family='Helvetica', size=20, weight= 'bold')

        self.bselectfiles = Button(self.raiz, text='Seleccionar archivos', font=self.helv36, width=25, height=5, bg='gray85', command=self.selectfiles)
        self.bselectfiles.pack(side = TOP, expand = True)

        self.bexit = Button(self.raiz, text='Salir', font=self.helv36, width=25, height=5,  bg='gray85', command=quit)
        self.bexit.pack(side = TOP, expand = True)
        
        self.raiz.mainloop()
    
    def center_window(self, width, height):
    # tamaño de la pantalla
        screen_width = self.raiz.winfo_screenwidth()
        screen_height = self.raiz.winfo_screenheight()

    # calculamos donde posicionar la ventana
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.raiz.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    def create_window(self,width,height):
    # creación de la ventana
        self.raiz = Tk()
        self.center_window(width, height) # anchura x altura
        self.raiz.configure(bg = 'gray85') #color
        self.raiz.title('Programa') #título
    # imagen de fondo
        imgpath = os.getcwd()
        if os.path.isfile('fondo.png') != True:
            urllib.request.urlretrieve('https://lh3.googleusercontent.com/xmYlBRE3lEGs5cICC2Y5RHdzkeCoW4irXTDuMNZsusDcQkBgZrlWFoCJwvnd6276-i_RO_lPXVUZEjy9oQ4EoZpOStaFsXC7pJFUxGM7H_rQcEbVRHIdJPJcLefEpi7wKvjlwOVb6anxte4pLmeMAFahPJu9MsnCsQ0HTrLZrY1r_BVnuwW8WMS3XIkRzEg9Bk5RBXfRK2_HTLHm5inrAKmUH_iOyOFv59R3kPvTXkno5AqSZcYbwfrmXI32Ou3GfEP10OkbImYT-Sp_eXxZdF4JNbU50UoR0KBi7CbPSsWU1DYUYqcigtYFxxdxEeO-YMMjRz2wOXom7biMQZ59Bg45VPFuMw3ku45krRSM_U4A6F1E1g3S3-MITzXN6zX0LY4EeEsHSwuwRl-q_erdSzFhLKNcmqkcUvFPytuPDbr2HgpJ9mE92UfL8R3z4xzmMUlhV-2rxkWFT3JF7YLGVHJF3eHNJA0ohsaeQfLB-m2mSXGaaWUpBszzEfLLMtHpsC8GdLpGHMs7BHex5GsvPJOjKyQISdtHlEQWf0xWqbxGe1TGzYlHxhcI33g5wVzdPK1uqx_hg4ohRZKtPzJDVIkPzQNj-aERRBwyy6Hj8w459LHr2sMixCnoSMG0I_F3OLO7jn-3wJ9diFUtnfhkBohZ6bZWzsKikyddFQHbWknf3k7GqvUNCIzI4TMIXMXPayF3Bt2sXKiQj7-6UBNSMyb41FlUPVY8QAsHeZwavuGvEXI=w1287-h806-no', 'fondo.png')
        background_image= PhotoImage(file=imgpath + '\\fondo.png')
        background_label= Label(image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)        
        background_label.image = background_image

    def selectfiles(self):     
    # pedimos experimento que queremos analizar
        global file_path
        file_path = filedialog.askdirectory()
     #   file_path = "C:\\Users\\Marcos\\Desktop\\Pràctiques_empresa\\EXPERIMENTOS\\mu50_FFW23_p5A_1_208"
        self.functions()

    def functions(self):
    # función que nos da todas las posibilidades de análisis    
        self.raiz.destroy()
        self.create_window(800,600)

        self.btimedependant = Button(self.raiz, text='W vs t', font=self.helv36, width=30, height=5, bg='gray85', command=self.timedependant)   
        self.btimedependant.pack(side = TOP, expand = True)

        self.bsizedependant = Button(self.raiz, text='W vs L', font=self.helv36, width=30, height=5,bg='gray85', command=self.timesize)   
        self.bsizedependant.pack(side = TOP, expand = True)

        self.bspectrum = Button(self.raiz, text='Espectro de Fourier', font=self.helv36, width=30, bg='gray85', height=5, command=self.timespectrum)   
        self.bspectrum.pack(side = TOP, expand = True)

        self.raiz.update()
        self.raiz.deiconify()

    def timedependant(self):
    # función análisis de w vs t mediante el archivo file.py que calcula y permite 
    # ajustar la gráfica seleccionando un w0,t0    
        self.btimedependant.config(state="disabled", bg = 'snow')
        self.bsizedependant.config(state="disabled")
        self.bspectrum.config(state="disabled")
    # definimos vectores que se usan en file.py
        global t,w,tc,wc
        t=[]
        w=[]
        tc=[]
        wc=[]

        support.evol_w(file_path,t,w,tc,wc)
        
        self.raiz.destroy()
    # graficamos el resultado
        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        b.plot(t,w,tc,wc)
        b.set_xscale('log')
        b.set_yscale('log')

        b.set_title ("W,Wc vs t,tc", fontsize=16)
        b.set_ylabel("W,Wc", fontsize=14)
        b.set_xlabel("t,tc", fontsize=14)

        self.create_window(800,600)

        self.canvas = FigureCanvasTkAgg(f, master=self.raiz)
        self.canvas.get_tk_widget().pack(side=LEFT)
        self.canvas.draw()

        self.bsaveimages = Button(self.raiz, text='Guardar gráficos', font=self.helv36, width=20, height=3,  bg='gray85', command=self.saveimages)   
        self.bsaveimages.pack(side = TOP, expand = True)

        self.bsavedata = Button(self.raiz, text='Guardar vectores', font=self.helv36, width=20, height=3,  bg='gray85', command=self.savedata)   
        self.bsavedata.pack(side = TOP, expand = True)

        self.brepeat = Button(self.raiz, text='Seleccionar otro punto', font=self.helv36, width=20, height=3,  bg='gray85', command=self.timedependant2)   
        self.brepeat.pack(side = TOP, expand = True)

        self.banotherfunction = Button(self.raiz, text='Otras funciones', font=self.helv36, width=20, height=3,  bg='gray85', command=self.anotherfunction)
        self.banotherfunction.pack(side = TOP, expand = True)

        self.bexit = Button(self.raiz, text='Salir', font=self.helv36, width=20, height=3,  bg='gray85', command=quit)
        self.bexit.pack(side = TOP, expand = True)

    def timedependant2(self):
    # función que permite reutilizar los datos calculados y únicamente volver
    # a seleccionar w0,t0 mediante file2.py
        self.raiz.destroy()

        tc=[]
        wc=[]
        support.evol2_w(t,w,tc,wc)
    # graficamos
        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        b.plot(t,w,tc,wc)
        b.set_xscale('log')
        b.set_yscale('log')

        b.set_title ("W,Wc vs t,tc", fontsize=16)
        b.set_ylabel("W,Wc", fontsize=14)
        b.set_xlabel("t,tc", fontsize=14)

        self.create_window(800,600)

        self.canvas = FigureCanvasTkAgg(f, master=self.raiz)
        self.canvas.get_tk_widget().pack(side=LEFT)
        self.canvas.draw()

        self.bsaveimages = Button(self.raiz, text='Guardar gráficos', font=self.helv36, width=20, height=3, bg='gray85', command=self.saveimages)   
        self.bsaveimages.pack(side = TOP, expand = True)

        self.bsavedata = Button(self.raiz, text='Guardar vectores', font=self.helv36, width=20, height=3, bg='gray85', command=self.savedata)   
        self.bsavedata.pack(side = TOP, expand = True)

        self.brepeat = Button(self.raiz, text='Seleccionar otro punto', font=self.helv36, width=20, height=3, bg='gray85', command=self.timedependant2)   
        self.brepeat.pack(side = TOP, expand = True)

        self.banotherfunction = Button(self.raiz, text='Otras funciones', font=self.helv36, width=20, height=3, bg='gray85', command=self.anotherfunction)
        self.banotherfunction.pack(side = TOP, expand = True)

        self.bexit = Button(self.raiz, text='Salir', font=self.helv36, width=20, height=3, bg='gray85', command=quit)
        self.bexit.pack(side = TOP, expand = True)

    def saveimages(self):
    # función que permite guardar los gráficos creados por timedependant y timedependant2
    # elegimos dónde guardarlos
        savedir = filedialog.askdirectory(title='Seleccione dónde guardar los gráficos')

        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        b.plot(t,w,tc,wc)
        b.set_xscale('log')
        b.set_yscale('log')
        b.set_title ("W,Wc vs t,tc", fontsize=16)
        b.set_ylabel("W,Wc", fontsize=14)
        b.set_xlabel("t,tc", fontsize=14)
        f.savefig(savedir + "\\comparison.png")

        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        b.plot(t,w)
        b.set_xscale('log')
        b.set_yscale('log')
        b.set_title ("W vs t", fontsize=16)
        b.set_ylabel("W", fontsize=14)
        b.set_xlabel("t", fontsize=14)
        f.savefig(savedir + "\\W_vs_t.png")

        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        b.plot(tc,wc)
        b.set_xscale('log')
        b.set_yscale('log')
        b.set_title ("Wc vs tc", fontsize=16)
        b.set_ylabel("Wc", fontsize=14)
        b.set_xlabel("tc", fontsize=14)
        f.savefig(savedir + "\\Wc_vs_tc.png")

    def savedata(self):
    # función que permite guardar los vectores creados por timedependant y timedependant2
    # elegimos dónde guardarlos
        savedir = filedialog.askdirectory(title='Seleccione dónde guardar los datos')

        file = open(savedir+"\\w&t.dat","w")         
        file.write("t"+"\t"+"w") 
        t_len= len(t)
        for i in range(t_len):
            file.write("\n")
            file.write(str(t[i])+";"+str(w[i]))
        file.close()

        file = open(savedir+"\\wc&tc.dat","w")         
        file.write("tc"+"\t"+"wc") 
        tc_len= len(tc)
        for i in range(tc_len):
            file.write("\n")
            file.write(str(tc[i][0])+";"+str(wc[i]))
        file.close()

    def sizedependant(self):
    # funcion que estudia w en función de la size para un tiempo determinado
        self.tiempo= int(self.entry.get())
        global Lc,wc
        Lc=[]
        wc=[]

        os.chdir(file_path)
        files = sorted(glob.glob('*.dat'))
#       data = np.loadtxt(files[tiempo])
        data = np.loadtxt(files[self.tiempo],float,'#',',')
        X = data[:,1]
        Y = data[:,0]
        len_y=len(Y)
        step=10
        for i in range(1,len_y): 
            YNEW = []       
            wi = []
            k = len_y-i
            p=0
            while (p+k)<=len_y:
                YNEW.append(Y[p:p+k])
                p=step+p
            len_YNEW=len(YNEW)
            for s in range(len_YNEW):
                a=0
                h=(1/k)*sum(YNEW[s])
                for j in range(k):
                    a=a+(YNEW[s][j]-h)**2    
                wi.append(math.sqrt((1/k)*a))
            wc.append(sum(wi)/len_YNEW)
            Lc.append(k)
        len_wc=len(wc)
        wo=[]
        for u in range(len_wc):
            wo.append(math.sqrt(abs(wc[u]**2-min(wc)**2)))
        
        self.raiz.destroy()

        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        b.plot(Lc,wc)
        b.set_xscale('log')
        b.set_yscale('log')

        b.set_title ("wc vs Lc", fontsize=16)
        b.set_ylabel("wc", fontsize=14)
        b.set_xlabel("Lc", fontsize=14)

        self.create_window(800,600)

        self.canvas = FigureCanvasTkAgg(f, master=self.raiz)
        self.canvas.get_tk_widget().pack(side=LEFT)
        self.canvas.draw()

        self.bsaveimagessize = Button(self.raiz, text='Guardar gráfico', font=self.helv36, width=20, height=3, bg='gray85', command=self.saveimagessize)   
        self.bsaveimagessize.pack(side = TOP, expand = True)

        self.bsavedatasize = Button(self.raiz, text='Guardar vectores', font=self.helv36, width=20, height=3, bg='gray85', command=self.savedatasize)   
        self.bsavedatasize.pack(side = TOP, expand = True)

        self.brepeatsize = Button(self.raiz, text='Introducir otro tiempo', font=self.helv36, width=20, height=3, bg='gray85', command=self.timesize)   
        self.brepeatsize.pack(side = TOP, expand = True)

        self.banotherfunction = Button(self.raiz, text='Otras funciones', font=self.helv36, width=20, height=3, bg='gray85', command=self.anotherfunction)
        self.banotherfunction.pack(side = TOP, expand = True)

        self.bexit = Button(self.raiz, text='Salir', font=self.helv36, width=20, height=3, bg='gray85', command=quit)
        self.bexit.pack(side = TOP, expand = True)
        
    def saveimagessize(self):
    # función que permite guardar los gráficos creados por sizedependant
    # elegimos dónde guardarlos
        savedir = filedialog.askdirectory(title='Seleccione dónde guardar los gráficos')

        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        b.plot(Lc,wc)
        b.set_xscale('log')
        b.set_yscale('log')
        b.set_title ("wc vs Lc", fontsize=16)
        b.set_ylabel("wc", fontsize=14)
        b.set_xlabel("Lc", fontsize=14)
        f.savefig(savedir + "\\sizedependant.png")
    
    def savedatasize(self):
    # función que permite guardar los vectores creados por funcion size
    # elegimos dónde guardarlos
        savedir = filedialog.askdirectory(title='Seleccione dónde guardar los datos')

        file = open(savedir+"\\wc&Lc.dat","w")         
        file.write("Lc"+"\t"+"wc") 
        Lc_len= len(Lc)
        for i in range(Lc_len):
            file.write("\n")
            file.write(str(Lc[i])+";"+str(wc[i]))
        file.close()

    def timesize(self):
    # funcion que pide un tiempo para estudiar w en función de la size para un t determinado
        self.raiz.destroy()
        self.create_window(300,300)

        self.entry = Entry(self.raiz, font=self.helv36)
        # Posicionarla en la size.
        self.entry.place(relx=0.5,rely=0.5, anchor = CENTER)
        button = Button(self.raiz, text='Enviar tiempo', font=self.helv36, width=20, height=3, bg='gray85', command=self.sizedependant)
        button.pack(side=BOTTOM)   


    def timespectrum(self):
    # función que pide un tiempo para estudiar el espectro de los datos
        self.raiz.destroy()
        self.create_window(300,300)

        self.entry = Entry(self.raiz, font=self.helv36)
        # Posicionarla en la ventana
        self.entry.place(relx=0.5,rely=0.5, anchor = CENTER)
        button = Button(self.raiz, text='Enviar tiempo', font=self.helv36, width=20, height=3, bg='gray85', command=self.spectrum)
        button.pack(side=BOTTOM)

    def spectrum(self):
    # función que con el tiempo dado realiza una fft de una correción de las Y y la representa en 
    # función de q
        self.tiempo= int(self.entry.get())
        self.raiz.destroy()
        end = 2207

        global S,q,x

        hc=[]
        os.chdir(file_path)
        files = sorted(glob.glob('*.dat'))
        files = files[0:end]
        h = np.loadtxt(files[self.tiempo],float,'#',',')[:,0]
        x = np.loadtxt(files[self.tiempo],float,'#',',')[:,1]
        len_h=len(h)
        for i in range(len_h-1):
            hc.append(h[i]-((h[len_h-1]-h[0])/len_h)*x[i]-h[0])
        #hmedia = np.mean(h)
        q = (1/(x[1]-x[0]))*(1/(x[-1]))*np.arange(0,x[-1]/2)    
        Y = np.fft.fft(hc)
        #Yc = np.fft.fft(h-hmedia)
        S = np.abs(Y)
        #Sc = np.abs(Yc)
        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        b.plot(q,S[0:int(x[-1]/2)])
        b.set_xscale('log')
        b.set_yscale('log')

        b.set_title ("S vs q", fontsize=16)
        b.set_ylabel("S", fontsize=14)
        b.set_xlabel("q", fontsize=14)

        self.create_window(800,600)

        self.canvas = FigureCanvasTkAgg(f, master=self.raiz)
        self.canvas.get_tk_widget().pack(side=LEFT)
        self.canvas.draw()

        self.bsaveimagesfourier = Button(self.raiz, text='Guardar gráfico', font=self.helv36, width=20, height=3, bg='gray85', command=self.saveimagesspectrum)   
        self.bsaveimagesfourier.pack(side = TOP, expand = True)

        self.bsavedatafourier = Button(self.raiz, text='Guardar vectores', font=self.helv36, width=20, height=3, bg='gray85', command=self.savedataspectrum)   
        self.bsavedatafourier.pack(side = TOP, expand = True)

        self.brepeatfourier = Button(self.raiz, text='Introducir otro tiempo', font=self.helv36, width=20, height=3, bg='gray85', command=self.timespectrum)   
        self.brepeatfourier.pack(side = TOP, expand = True)

        self.banotherfunction = Button(self.raiz, text='Otras funciones', font=self.helv36, width=20, height=3, bg='gray85', command=self.anotherfunction)
        self.banotherfunction.pack(side = TOP, expand = True)

        self.bexit = Button(self.raiz, text='Salir', font=self.helv36, width=20, height=3, bg='gray85', command=quit)
        self.bexit.pack(side = TOP, expand = True)

    def saveimagesspectrum(self):
    # función que permite guardar los gráficos creados por gettiempo
    # elegimos dónde guardarlos
        savedir = filedialog.askdirectory(title='Seleccione dónde guardar los gráficos')

        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        b.plot(q,S[0:int(x[-1]/2)])
        b.set_xscale('log')
        b.set_yscale('log')
        b.set_title ("S vs q", fontsize=16)
        b.set_ylabel("S", fontsize=14)
        b.set_xlabel("q", fontsize=14)        
        f.savefig(savedir + "\\spectrum.png")

    def savedataspectrum(self):
    # función que permite guardar los vectores creados por gettiempo
    # elegimos dónde guardarlos
        savedir = filedialog.askdirectory(title='Seleccione dónde guardar los datos')

        file = open(savedir+"\\S&q.dat","w")         
        file.write("S"+"\t"+"q") 
        q_len= len(q)
        for i in range(q_len):
            file.write("\n")
            file.write(str(q[i])+";"+str(S[i]))
        file.close()

    def anotherfunction(self):
    # función que nos asiste cuando acabemos de utilizar una de las otras funciones
    # y nos permite elegir entre cargar otro experimento o seguir con el que estábamos analizando
        self.raiz.destroy()
        self.create_window(800,600)

        self.bsamefiles = Button(self.raiz, text='Conservar archivos', font=self.helv36, width=25, height=5, bg='gray85', command=self.functions)
        self.bsamefiles.pack(side = TOP, expand = True)

        self.bchangefiles = Button(self.raiz, text='Otro experimento', font=self.helv36, width=25, height=5, bg='gray85', command=self.selectfiles)
        self.bchangefiles.pack(side = TOP, expand = True)

programa = App()
programa