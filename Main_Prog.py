##                                    ..                       .x+=:.                                                                
##                                  dF                        z`    ^%                                                               
##                            u.   '88bu.                        .   <k        u.      x.    .        .u    .                        
##                 .    ...ue888b  '*88888bu        .u         .@8Ned8"  ...ue888b   .@88k  z88u    .d88B :@8c        .        .u    
##            .udR88N   888R Y888r   ^"*8888N    ud8888.     .@^%8888"   888R Y888r ~"8888 ^8888   ="8888f8888r  .udR88N    ud8888.  
##           <888'888k  888R I888>  beWE "888L :888'8888.   x88:  `)8b.  888R I888>   8888  888R     4888>'88"  <888'888k :888'8888. 
##           9888 'Y"   888R I888>  888E  888E d888 '88%"   8888N=*8888  888R I888>   8888  888R     4888> '    9888 'Y"  d888 '88%" 
##           9888       888R I888>  888E  888E 8888.+"       %8"    R88  888R I888>   8888  888R     4888>      9888      8888.+"    
##           9888      u8888cJ888   888E  888F 8888L          @8Wou 9%  u8888cJ888    8888 ,888B .  .d888L .+   9888      8888L      
##           ?8888u../  "*888*P"   .888N..888  '8888c. .+   .888888P`    "*888*P"    "8888Y 8888"   ^"8888*"    ?8888u../ '8888c. .+ 
##            "8888P'     'Y"       `"888*""    "88888%     `   ^"F        'Y"        `Y"   'YP        "Y"       "8888P'   "88888%   
##             "P'                    ""         "YP'                                                             "P'       "YP'     
##                                                                                                                                   


                                                                                                                    
##                      _           _                                                                         _        _                     _ 
##  __ _  ___  ___   __| | ___  ___(_) __ _ _   _  ___  __   _____ _ __ ___    __ _  ___  ___   ___ ___ _ __ | |_ _ __(_) __ _ _   _  ___   / |
## / _` |/ _ \/ _ \ / _` |/ _ \/ __| |/ _` | | | |/ _ \ \ \ / / _ \ '__/ __|  / _` |/ _ \/ _ \ / __/ _ \ '_ \| __| '__| |/ _` | | | |/ _ \  | |
##| (_| |  __/ (_) | (_| |  __/\__ \ | (_| | |_| |  __/  \ V /  __/ |  \__ \ | (_| |  __/ (_) | (_|  __/ | | | |_| |  | | (_| | |_| |  __/  | |
## \__, |\___|\___/ \__,_|\___||___/_|\__, |\__,_|\___|   \_/ \___|_|  |___/  \__, |\___|\___/ \___\___|_| |_|\__|_|  |_|\__, |\__,_|\___|  |_|
## |___/                                 |_|                                  |___/                                         |_|


def transformation_cor_Geodisiques_Geocentriques(Lambda,Phi,h,a,b):
    
    Lambda=degree2radians(Lambda)
    Phi=degree2radians(Phi)
    
    e=sqrt(1-(b/a)**2)
    N=a/(sqrt(1-(e*sin(Phi))**2))
    x=(N+h)*cos(Phi)*cos(Lambda)
    y=(N+h)*cos(Phi)*sin(Lambda)
    z=(N*(1-(e)**2)+h)*sin(Phi)
    
    return x,y,z

def   Geodesiques_vers_geocentriques():
    
    global Mafenetre1,Valeur,Valeur2,entry3,entry4,entry5,canvas1,echelle,echelle2
    
    Mafenetre1 = Tk()
    Mafenetre1.geometry('600x685')
    Mafenetre1.title('Geodesiques_vers_geocentriques')
    Mafenetre1.iconbitmap('Ressources/favicon.ico')
    
    canvas1 = Canvas(Mafenetre1, width = 400, height = 600, relief = 'raised')
    canvas1.pack()
    
    label1 = Label(Mafenetre1, text='Transformation entre systèmes de coordonnées:\n Géodésiques vers Géocentriques')
    label1.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas1.create_window(200, 25, window=label1)

    Valeur = StringVar()
    Valeur.set(180)
    echelle = Scale(Mafenetre1,from_=-180,to=180,resolution=1,orient=HORIZONTAL,length=500,width=20,label="La longitude Lambda (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur)
    canvas1.create_window(200, 100, window=echelle)

    Valeur2 = StringVar()
    Valeur2.set(180)
    echelle2 = Scale(Mafenetre1,from_=-90,to=90,resolution=1,orient=HORIZONTAL,length=500,width=20,label="La latitude Phi (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur2)
    canvas1.create_window(200, 180, window=echelle2)

    label4 = Label(Mafenetre1, text='La hauteur ellipsoidale h (m) :')
    label4.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas1.create_window(200, 230, window=label4)

    entry3 = Entry(Mafenetre1) 
    canvas1.create_window(200, 260, window=entry3)

    label5 = Label(Mafenetre1, text='Demi-grand axe a (m) :')
    label5.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas1.create_window(200, 290, window=label5)

    entry4 = Entry(Mafenetre1) 
    canvas1.create_window(200, 320, window=entry4)

    label6 = Label(Mafenetre1, text='Demi-petit axe b (m) :')
    label6.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas1.create_window(200, 350, window=label6)

    entry5 = Entry(Mafenetre1) 
    canvas1.create_window(200, 380, window=entry5)

    Bouton2= Button(Mafenetre1, text = "Saisie manuelle (Longitude / Latitude)", command =ANGLES ,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Bouton2.pack(side=BOTTOM)

    button3 = Button(Mafenetre1,text='Transformer', command=g1et_coordonnees_geocentriques2 ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    canvas1.create_window(200, 420, window=button3)
    
    Btn = Button(Mafenetre1, text = "Consulter Google earth",command=openweb,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Btn.pack(side=BOTTOM)

    Btn2 = Button(Mafenetre1, text = "Choisissez un datum",command=ellipsoide1,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Btn2.pack(side=BOTTOM)
    
    Mafenetre1.mainloop()
    
   
def ellipsoide1():
    
    class Test:
        
      def __init__(self, tk0):
        self.var = StringVar()
        fontCombo = ("Ink Free", 16, "bold")
        self.data = ("Maupertuis (1738)","Plessis (1817)","Everest (1830)","Everest 1830 Modified (1967)","Airy (1830)","Bessel (1841)","Clarke (1866)","Clarke (1878)","Clarke (1880)","Helmert (1906)","Hayford (1910)","International (1924)","Krassovsky (1940)","WGS66 (1966)","Australian National (1966)","New International (1967)","GRS-67 (1967)","South American (1969)","WGS-72 (1972)","GRS-80 (1979)","WGS-84 (1984)","IERS (1989)","IERS (2003)")
        self.cb = Combobox(tk0, values=self.data,font = fontCombo)
        self.cb.place(x=50, y=50)
        self.b1 = Button(tk0, text="Réactualiser", command=self.select,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold')).place(x=160, y=110)

      def set_text(Entry,text):   
        Entry.delete(0,END)
        Entry.insert(0,text)
        return
    
      def select(self):
        value = self.cb.get()
        ent_a=entry4
        ent_b=entry5
        if value=="Maupertuis (1738)" :
            set_text(ent_a,6397300)
            set_text(ent_b,6363806.283)
        
        elif value=="Plessis (1817)" :
            set_text(ent_a,6376523.0)
            set_text(ent_b,6355862.9333)
        
        elif value=="Everest (1830)" :
            set_text(ent_a,6377299.365)
            set_text(ent_b,6356098.359)
        
        elif value=="Everest 1830 Modified (1967)" :
            set_text(ent_a,6377304.063)
            set_text(ent_b,6356103.0390)
        
        elif value=="Everest 1830 (1967 Definition)" :
            set_text(ent_a,6377298.556)
            set_text(ent_b,6356097.550)
        
        elif value=="Airy (1830)" :
            set_text(ent_a,6377563.396)
            set_text(ent_b,6356256.909)
        
        elif value=="Bessel (1841)" :
            set_text(ent_a,6377397.155)
            set_text(ent_b,6356078.963)
        
        elif value=="Clarke (1866)" :
            set_text(ent_a,6378206.4)
            set_text(ent_b,6356583.8)
        
        elif value=="Clarke (1878)" :
            set_text(ent_a,6378190)
            set_text(ent_b,6356456)
        
        elif value=="Clarke (1880)" :
            set_text(ent_a,6378249.145)
            set_text(ent_b,6356514.870)

        elif value=="Helmert (1906)" :
            set_text(ent_a,6378200)
            set_text(ent_b,6356818.17)
        
        elif value=="Hayford (1910)" :
            set_text(ent_a,6378388)
            set_text(ent_b,6356911.946)
        
        elif value=="International (1924)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356911.946)
        
        elif value=="Krassovsky (1940)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356863.019)
        
        elif value=="WGS66 (1966)" :
            set_text(ent_a,6378145)
            set_text(ent_b,6356759.769)
        
        elif value=="Australian National (1966)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)
        
        elif value=="New International (1967)" :
            set_text(ent_a,6378157.5)
            set_text(ent_b,6356772.2)
    
        elif value=="GRS-67 (1967)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.516)
        
        elif value=="South American (1969)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)

        elif value=="WGS-72 (1972)" :
            set_text(ent_a,6378135)
            set_text(ent_b,6356750.52)
        
        elif value=="GRS-80 (1979)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3141)
        
        elif value=="WGS-84 (1984)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3142)
        
        elif value=="IERS (1989)" :
            set_text(ent_a,6378136)
            set_text(ent_b,6356751.302)

        elif value=="IERS (2003)" :
            set_text(ent_a,6378136.6)
            set_text(ent_b,6356751.9)
        else:
            messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
            
    tk0 = Tk()
    tk0.geometry("378x170")
    tk0.title("Chose_datum")
    tk0.iconbitmap('Ressources/favicon.ico')
    tt = Test(tk0)
    tk0.mainloop()



def ANGLES():
    
    global entry1,entry2,Mafenetre1_1
    
    Mafenetre1_1 = Tk()
    Mafenetre1_1.title("Manual_angles_input")
    Mafenetre1_1.iconbitmap('Ressources/favicon.ico')

    Label1 = Label(Mafenetre1_1, text = ' Veuillez entrez la valeur des angles :',font=('Ink Free', 14 ,'bold'),fg='#005994')
    Label1.pack()

    canvas = Canvas(Mafenetre1_1, width = 400, height = 300, relief = 'raised')
    canvas.pack()
    
    label2 = Label(Mafenetre1_1, text='La longitude Lambda (°) :')
    label2.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas.create_window(200, 110, window=label2)

    entry1 = Entry(Mafenetre1_1) 
    canvas.create_window(200, 140, window=entry1)

    label3 = Label(Mafenetre1_1, text='La latitude Phi (°) :')
    label3.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas.create_window(200, 170, window=label3)

    entry2 = Entry(Mafenetre1_1) 
    canvas.create_window(200, 200, window=entry2)
    
    Bouton1 = Button(Mafenetre1_1, text = 'Réactualiser ', command =ANGLESUPDAT,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    Bouton1.pack()

    button2 = Button(Mafenetre1_1,text='Transformer', command=g1et_coordonnees_geocentriques ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    button2.pack()

    Bouton3= Button(Mafenetre1_1, text = 'show map', command = lon_lat_interval ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    Bouton3.pack(side=BOTTOM)
    
    Mafenetre1_1.mainloop()
    
def ANGLESUPDAT():
    
    global entry1,entry2,Valeur,Valeur2,echelle,echelle2
    try:
        
        echelle.set((float(entry1.get())))
        echelle2.set((float(entry2.get())))
        Valeur.set(str(float(entry1.get())))
        Valeur2.set(str(float(entry2.get())))
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
        
def g1et_coordonnees_geocentriques():
  
    global Valeur,Valeur2,entry3,entry4,entry5,canvas1,Mafenetre1,echelle,echelle2
    
    try:
        Lambda,Phi,h,a,b=float(Valeur.get()),float(Valeur2.get()),float(entry3.get()),float(entry4.get()),float(entry5.get())
        x,y,z=transformation_cor_Geodisiques_Geocentriques(Lambda,Phi,h,a,b)

        label7 = Label(Mafenetre1 ,text= 'x(m) :')
        label7.config(font=('Ink Free', 10))
        canvas1.create_window(200, 460, window=label7)
    
        label8 = Label(Mafenetre1, text= '%.5E'% Decimal(x) ,font=('Ink Free', 10, 'bold'))
        canvas1.create_window(200, 480, window=label8)

        label9 = Label(Mafenetre1 , text= 'y(m) :',font=('Ink Free', 10))
        canvas1.create_window(200, 500, window=label9)
    
        label10 = Label(Mafenetre1, text= '%.5E'% Decimal(y) ,font=('Ink Free', 10, 'bold'))
        canvas1.create_window(200, 520, window=label10)

        label11 = Label(Mafenetre1 , text= 'z(m) :',font=('Ink Free', 10))
        canvas1.create_window(200, 540, window=label11)
    
        label12 = Label(Mafenetre1, text= '%.5E'% Decimal(z) ,font=('Ink Free', 10, 'bold'))
        canvas1.create_window(200, 560, window=label12)

    except:
         messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
        


        
        

def g1et_coordonnees_geocentriques2():
  
    global Valeur,Valeur2,entry3,entry4,entry5,canvas1,Mafenetre1,echelle,echelle2
    
    try:
        Lambda,Phi,h,a,b=float(echelle.get()),float(echelle2.get()),float(entry3.get()),float(entry4.get()),float(entry5.get())
        x,y,z=transformation_cor_Geodisiques_Geocentriques(Lambda,Phi,h,a,b)

        label7 = Label(Mafenetre1 ,text= 'x(m) :')
        label7.config(font=('Ink Free', 10))
        canvas1.create_window(200, 460, window=label7)
    
        label8 = Label(Mafenetre1, text= '%.5E'% Decimal(x) ,font=('Ink Free', 10, 'bold'))
        canvas1.create_window(200, 480, window=label8)

        label9 = Label(Mafenetre1 , text= 'y(m) :',font=('Ink Free', 10))
        canvas1.create_window(200, 500, window=label9)
    
        label10 = Label(Mafenetre1, text= '%.5E'% Decimal(y) ,font=('Ink Free', 10, 'bold'))
        canvas1.create_window(200, 520, window=label10)

        label11 = Label(Mafenetre1 , text= 'z(m) :',font=('Ink Free', 10))
        canvas1.create_window(200, 540, window=label11)
    
        label12 = Label(Mafenetre1, text= '%.5E'% Decimal(z) ,font=('Ink Free', 10, 'bold'))
        canvas1.create_window(200, 560, window=label12)
    
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
        
   
       

def lon_lat_interval():
    
    global entry5_1,entry5_2
    
    Mafenetre5 = Tk()
    Mafenetre5.iconbitmap('Ressources/favicon.ico')
  
    Mafenetre5.title("lon_lat_interval")

    Label1 = Label(Mafenetre5, text = ' Veuillez entrez la valeur des esspacements :',font=('Ink Free', 14 ,'bold'),fg='#005994')
    Label1.pack()

    canvas = Canvas(Mafenetre5, width = 400, height = 300, relief = 'raised')
    canvas.pack()


    label2 = Label(Mafenetre5, text='lat_interval:')
    label2.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas.create_window(200, 110, window=label2)

    entry5_1 = Entry(Mafenetre5) 
    canvas.create_window(200, 140, window=entry5_1)

    label3 = Label(Mafenetre5, text='lon_interval:')
    label3.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas.create_window(200, 170, window=label3)

    entry5_2 = Entry(Mafenetre5) 
    canvas.create_window(200, 200, window=entry5_2)

    Bouton1 = Button(Mafenetre5, text = 'Show map', command =mapp1,bg='#3498DB',fg='#FDFEFE')
    Bouton1.pack()
    
    Bouton2 = Button(Mafenetre5, text = '?', command =openweb134_2,bg='#3498DB',fg='#FDFEFE')
    Bouton2.pack()
    
    Mafenetre5.mainloop()
  
def mapp1():
    try:
       lon=Valeur2.get()
       lat=Valeur.get()
       tooltip = 'Click me!'
       map = Map(location=[lon, lat], zoom_start=12 , tiles='Stamen Terrain')
       Marker([lon, lat], popup='<i>Mt. Hood Meadows</i>', tooltip=tooltip).add_to(map)
       map
       lat_interval = int(entry5_1.get())
       lon_interval = int(entry5_2.get())
       grid = []

       for lat in range(-90, 91, lat_interval):
    
          grid.append([[lat, -180],[lat, 180]])

       for lon in range(-180, 181, lon_interval):
    
          grid.append([[-90, lon],[90, lon]])

       for g in grid:

          PolyLine(g, color="black", weight=0.5, opacity=0.5).add_to(map)

       map.save('indexx.html')
       openweb3()
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  


##                                 _        _                                                              _           _                    ____  
##  __ _  ___  ___   ___ ___ _ __ | |_ _ __(_) __ _ _   _  ___  __   _____ _ __ ___    __ _  ___  ___   __| | ___  ___(_) __ _ _   _  ___  |___ \ 
## / _` |/ _ \/ _ \ / __/ _ \ '_ \| __| '__| |/ _` | | | |/ _ \ \ \ / / _ \ '__/ __|  / _` |/ _ \/ _ \ / _` |/ _ \/ __| |/ _` | | | |/ _ \   __) |
##| (_| |  __/ (_) | (_|  __/ | | | |_| |  | | (_| | |_| |  __/  \ V /  __/ |  \__ \ | (_| |  __/ (_) | (_| |  __/\__ \ | (_| | |_| |  __/  / __/ 
## \__, |\___|\___/ \___\___|_| |_|\__|_|  |_|\__, |\__,_|\___|   \_/ \___|_|  |___/  \__, |\___|\___/ \__,_|\___||___/_|\__, |\__,_|\___| |_____|
## |___/                                         |_|                                  |___/                                 |_|                   

def Transformation_coor_Geocentriques_Geodesiques(x,y,z,a,b,eps):
    
    e=sqrt(1-(b/a)**2)

    if x==0 and y==0 :#_cas_exceptionnel.
            Laambda='               '
            h=abs(z)-b
            if z<0:
                phi1=-pi
                phi1=phi1*180/pi
            else:
                phi1=pi
                phi1=phi1*180/pi
    else :
            if x>0:
                Laambda=atan(y/x)
            elif x<0 and y>=0 :
                Laambda=atan(y/x) + pi
            elif y<0 and x<0 :
                Laambda=atan(y/x) - pi
            elif y>0 and x==0 :
                Laambda=pi/2
            elif y<0 and x==0 :
                Laambda=-pi/2
            Laambda=Laambda*180/pi #en degree.
            h=0
            phi=atan(z/((1-e**2)*sqrt(x**2+y**2)))
            N=a/sqrt(1-(e*sin(phi))**2)
            phi1=atan((z+ N*e**2*sin(phi))/sqrt(x**2+y**2))
            N=a/sqrt(1-(e*sin(phi1))**2)
            while abs(phi1-phi)>eps :
                phi=phi1
                phi1=atan((z+ N*e**2*sin(phi))/sqrt(x**2+y**2))
                N=a/sqrt(1-(e*sin(phi1))**2)
            if phi1 == pi/2 or phi == -pi/2 :
                h=(z/sin(phi1))-N*(1-e**2)
            else:
                h=sqrt(x**2+y**2)/cos(phi1)-N
            phi1=phi1*180/pi  #en degree.    

    return Laambda,phi1,h

def  geocentriques_vers_Geodesiques():
    
    global entry1_2,entry2_2,entry3_2,entry4_2,entry5_2,canvas2,Mafenetre2,entry6_2
    
    Mafenetre2 = Tk()
    Mafenetre2.geometry('600x730')
    Mafenetre2.iconbitmap('Ressources/favicon.ico')
    Mafenetre2.title('Geocentriques_vers_Geodesiques')

    canvas2 = Canvas(Mafenetre2, width = 400, height = 650, relief = 'raised')
    canvas2.pack()

    label1= Label(Mafenetre2, text='Transformation entre coordonnees:\n Géocentriques vers Géodesiques')
    label1.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas2.create_window(200, 25, window=label1)

    label2 = Label(Mafenetre2, text='x(m) :')
    label2.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas2.create_window(200, 110, window=label2)

    entry1_2 = Entry(Mafenetre2) 
    canvas2.create_window(200, 140, window=entry1_2)

    label3 = Label(Mafenetre2, text='y(m) :')
    label3.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas2.create_window(200, 170, window=label3)

    entry2_2 = Entry(Mafenetre2) 
    canvas2.create_window(200, 200, window=entry2_2)

    label4 = Label(Mafenetre2, text='z(m) :')
    label4.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas2.create_window(200, 230, window=label4)

    entry3_2 = Entry(Mafenetre2) 
    canvas2.create_window(200, 260, window=entry3_2)

    label5 = Label(Mafenetre2, text='Demi-grand axe a (m) :')
    label5.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas2.create_window(200, 290, window=label5)

    entry4_2 = Entry(Mafenetre2) 
    canvas2.create_window(200, 320, window=entry4_2)

    label6 = Label(Mafenetre2, text='Demi-petit axe b (m) :')
    label6.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas2.create_window(200, 350, window=label6)

    entry5_2 = Entry(Mafenetre2) 
    canvas2.create_window(200, 380, window=entry5_2)

    label7 = Label(Mafenetre2, text='Epsilon :')
    label7.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas2.create_window(200, 410, window=label7)

    entry6_2 = Entry(Mafenetre2) 
    canvas2.create_window(200, 440, window=entry6_2)

    button1 = Button(Mafenetre2,text='Transformer', command = get_coordonnees_Geodesiques ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    canvas2.create_window(200, 470, window=button1)
    
    Btn = Button(Mafenetre2, text = "Consulter Google earth",command=openweb,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Btn.pack(side=BOTTOM)
    
    Btn2 = Button(Mafenetre2, text = "Choisissez un datum",command=ellipsoide,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Btn2.pack(side=BOTTOM)
 
    Mafenetre2.mainloop()




def ellipsoide():
    
    class Test:
        
      def __init__(self, tk0):
        self.var = StringVar()
        fontCombo = ("Ink Free", 16, "bold")
        self.data = ("Maupertuis (1738)","Plessis (1817)","Everest (1830)","Everest 1830 Modified (1967)","Airy (1830)","Bessel (1841)","Clarke (1866)","Clarke (1878)","Clarke (1880)","Helmert (1906)","Hayford (1910)","International (1924)","Krassovsky (1940)","WGS66 (1966)","Australian National (1966)","New International (1967)","GRS-67 (1967)","South American (1969)","WGS-72 (1972)","GRS-80 (1979)","WGS-84 (1984)","IERS (1989)","IERS (2003)")
        self.cb = Combobox(tk0, values=self.data,font = fontCombo)
        self.cb.place(x=50, y=50)
        self.b1 = Button(tk0, text="Réactualiser", command=self.select,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold')).place(x=160, y=110)

      def set_text(Entry,text):   
        Entry.delete(0,END)
        Entry.insert(0,text)
        return
    
      def select(self):
        value = self.cb.get()
        ent_a=entry4_2
        ent_b=entry5_2
        if value=="Maupertuis (1738)" :
            set_text(ent_a,6397300)
            set_text(ent_b,6363806.283)
        
        elif value=="Plessis (1817)" :
            set_text(ent_a,6376523.0)
            set_text(ent_b,6355862.9333)
        
        elif value=="Everest (1830)" :
            set_text(ent_a,6377299.365)
            set_text(ent_b,6356098.359)
        
        elif value=="Everest 1830 Modified (1967)" :
            set_text(ent_a,6377304.063)
            set_text(ent_b,6356103.0390)
        
        elif value=="Everest 1830 (1967 Definition)" :
            set_text(ent_a,6377298.556)
            set_text(ent_b,6356097.550)
        
        elif value=="Airy (1830)" :
            set_text(ent_a,6377563.396)
            set_text(ent_b,6356256.909)
        
        elif value=="Bessel (1841)" :
            set_text(ent_a,6377397.155)
            set_text(ent_b,6356078.963)
        
        elif value=="Clarke (1866)" :
            set_text(ent_a,6378206.4)
            set_text(ent_b,6356583.8)
        
        elif value=="Clarke (1878)" :
            set_text(ent_a,6378190)
            set_text(ent_b,6356456)
        
        elif value=="Clarke (1880)" :
            set_text(ent_a,6378249.145)
            set_text(ent_b,6356514.870)

        elif value=="Helmert (1906)" :
            set_text(ent_a,6378200)
            set_text(ent_b,6356818.17)
        
        elif value=="Hayford (1910)" :
            set_text(ent_a,6378388)
            set_text(ent_b,6356911.946)
        
        elif value=="International (1924)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356911.946)
        
        elif value=="Krassovsky (1940)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356863.019)
        
        elif value=="WGS66 (1966)" :
            set_text(ent_a,6378145)
            set_text(ent_b,6356759.769)
             
        elif value=="Australian National (1966)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)
        
        elif value=="New International (1967)" :
            set_text(ent_a,6378157.5)
            set_text(ent_b,6356772.2)
    
        elif value=="GRS-67 (1967)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.516)
        
        elif value=="South American (1969)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)

        elif value=="WGS-72 (1972)" :
            set_text(ent_a,6378135)
            set_text(ent_b,6356750.52)
        
        elif value=="GRS-80 (1979)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3141)
        
        elif value=="WGS-84 (1984)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3142)
        
        elif value=="IERS (1989)" :
            set_text(ent_a,6378136)
            set_text(ent_b,6356751.302)

        elif value=="IERS (2003)" :
            set_text(ent_a,6378136.6)
            set_text(ent_b,6356751.9)
        else:
          messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
    tk0 = Tk()
    tk0.geometry("378x170")
    tk0.title("Chose_ellipsoid")
    tk0.iconbitmap('Ressources/favicon.ico')
    tt = Test(tk0)
    tk0.mainloop()
    
def get_coordonnees_Geodesiques():
    
    global entry1_2,entry2_2,entry3_2,entry4_2,entry5_2,canvas2,Mafenetre2,entry6_2
    try:
        
        x,y,z,a,b,Epsilon=float(entry1_2.get()),float(entry2_2.get()),float(entry3_2.get()),float(entry4_2.get()),float(entry5_2.get()),float(entry6_2.get())
        Lambda2,Phi2,h=Transformation_coor_Geocentriques_Geodesiques(x,y,z,a,b,Epsilon)
    
        label7 = Label(Mafenetre2, text= 'La longitude Lambda (°) :',font=('Ink Free', 10))
        canvas2.create_window(200, 510, window=label7)
    
        label8 = Label(Mafenetre2, text= Lambda2 ,font=('Ink Free', 10, 'bold'))
        canvas2.create_window(200, 530, window=label8)

        label9 = Label(Mafenetre2, text= 'La latitude Phi (°) :',font=('Ink Free', 10))
        canvas2.create_window(200, 550, window=label9)

        label10 = Label(Mafenetre2, text= '%.5E'% Decimal(Phi2) ,font=('Ink Free', 10, 'bold'))
        canvas2.create_window(200, 570, window=label10)

        label11 = Label( Mafenetre2,text= 'La hauteur ellipsoidale h (m) :',font=('Ink Free', 10))
        canvas2.create_window(200, 590, window=label11)
    
        label12 = Label(Mafenetre2, text= '%.5E'% Decimal(h) ,font=('Ink Free', 10, 'bold'))
        canvas2.create_window(200, 610, window=label12)
    
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  

##                                 _        _                                                   _                                   _                         _____ 
##  __ _  ___  ___   ___ ___ _ __ | |_ _ __(_) __ _ _   _  ___  __   _____ _ __ ___    __ _ ___| |_ _ __ ___  _ __   ___  _ __ ___ (_) __ _ _   _  ___       |___ / 
## / _` |/ _ \/ _ \ / __/ _ \ '_ \| __| '__| |/ _` | | | |/ _ \ \ \ / / _ \ '__/ __|  / _` / __| __| '__/ _ \| '_ \ / _ \| '_ ` _ \| |/ _` | | | |/ _ \        |_ \ 
##| (_| |  __/ (_) | (_|  __/ | | | |_| |  | | (_| | |_| |  __/  \ V /  __/ |  \__ \ | (_| \__ \ |_| | | (_) | | | | (_) | | | | | | | (_| | |_| |  __/       ___) |
## \__, |\___|\___/ \___\___|_| |_|\__|_|  |_|\__, |\__,_|\___|   \_/ \___|_|  |___/  \__,_|___/\__|_|  \___/|_| |_|\___/|_| |_| |_|_|\__, |\__,_|\___|      |____/ 
## |___/                                         |_|                                                                                     |_|                        

def Transformation_coor_Geocentriques_Astronomique(Phi3,Lambda3,DeltaX3,DeltaY3,DeltaZ3):
  
            Phi3=degree2radians(Phi3)
            Lambda3=degree2radians(Lambda3)
            M=[0,0,0]
            a=-sin(Phi3)*cos(Lambda3)
            b=-sin(Lambda3)
            c=cos(Phi3)*sin(Lambda3)
            d=cos(Lambda3)
            e=cos(Lambda3)
            f=cos(Phi3)*sin(Lambda3)
            g=cos(Phi3)
            h=0
            i=sin(Phi3)
            V1=a*DeltaX3+e*DeltaY3+h*DeltaZ3
            V2=b*DeltaX3+e*DeltaY3+h*DeltaZ3
            V3=c*DeltaX3+f*DeltaY3+i*DeltaZ3
        
            if V2>0 :
                   if V1==0:
                       Az3=Pi/2
                   elif V1>0:
                       Az3=atan(V2/V1)
                   else :
                           Az3=atan(V2/V1)+pi
            else :
                if V1==0 :
                    Az3=-pi/2
                elif V1>0 :
                    Az3=atan(V2/V1)+pi
                else :
                    Az3=atan(V2/V1)-pi
     
            C3=sqrt(DeltaX3**2+DeltaY3**2+DeltaZ3**2)
            
            if  C3 !=0 and (V3/C3)<=1 and  (V3/C3)>=-1 :
                
                M[1]=asin((V3/C3))
                M[1]=radians2degree(M[1])
                
            else :
                M[1]='Av ne peut pas etre calculé'
            
            M[0]=Az3
            M[2]=C3
            M[0]=radians2degree(M[0])
            return M[0],M[1],M[2] #Az,Av,C

        
def   Geocentrique_vers_Astronomique():
    
    global Valeur3,Valeur4,entry3_3,entry3_4,entry3_5,canvas3,Mafenetre3,echelle3,echelle4
    
    Mafenetre3 = Tk()
    Mafenetre3.geometry('600x670')
    Mafenetre3.iconbitmap('Ressources/favicon.ico')
    Mafenetre3.title('Geocentrique_vers_Astronomique_locales')

    canvas3 = Canvas(Mafenetre3, width = 400, height = 600, relief = 'raised')
    canvas3.pack()
    
    label1 = Label(Mafenetre3, text='Transformation entre coordonnees:\n Géocentriques vers Astronomiques locales')
    label1.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas3.create_window(200, 25, window=label1)

    Valeur3 = StringVar()
    Valeur3.set(180)
    echelle3 = Scale(Mafenetre3,from_=-180,to=180,resolution=1,orient=HORIZONTAL,length=500,width=20,label="La longitude Lambda (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur3)
    canvas3.create_window(200, 100, window=echelle3)

    Valeur4 = StringVar()
    Valeur4.set(180)
    echelle4 = Scale(Mafenetre3,from_=-90,to=90,resolution=1,orient=HORIZONTAL,length=500,width=20,label="La latitude Phi (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur4)
    canvas3.create_window(200, 180, window=echelle4)

    label4 = Label(Mafenetre3, text='DeltaXpq (m) :')
    label4.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas3.create_window(200, 230, window=label4)
    entry3_3 = Entry(Mafenetre3) 
    canvas3.create_window(200, 260, window=entry3_3)

    label5 = Label(Mafenetre3, text='DeltaYpq (m) :')
    label5.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas3.create_window(200, 290, window=label5)
    entry3_4 = Entry(Mafenetre3) 
    canvas3.create_window(200, 320, window=entry3_4)

    label6 = Label(Mafenetre3, text='DeltaZpq (m) :')
    label6.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas3.create_window(200, 350, window=label6)
    entry3_5 = Entry(Mafenetre3) 
    canvas3.create_window(200, 380, window=entry3_5)

    button2 = Button(Mafenetre3,text='Transformer', command = get_coordonnees_astronomique2 ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    canvas3.create_window(200, 420, window=button2)
    
    Btn = Button(Mafenetre3, text = "Consulter Google earth",command=openweb,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Btn.pack(side=BOTTOM)
    
    Bouton7= Button(Mafenetre3, text = "Saisie manuelle (Longitude / Latitude)", command =ANGLES3 ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    Bouton7.pack(side=BOTTOM)
    
    Mafenetre3.mainloop()

def ANGLES3():
    
    global entry3_1,entry3_2,Mafenetre3_1
    
    Mafenetre3_1 = Tk()
    Mafenetre3_1.iconbitmap('Ressources/favicon.ico')
    
    Label1 = Label(Mafenetre3_1, text = ' Veuillez entrez la valeur des angles :',font=('Ink Free', 14 ,'bold'),fg='#005994')
    Label1.pack()

    canvas = Canvas(Mafenetre3_1, width = 400, height = 300, relief = 'raised')
    canvas.pack()
    
    label2 = Label(Mafenetre3_1, text='La longitude Lambda (°) :')
    label2.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 110, window=label2)
    entry3_1 = Entry(Mafenetre3_1) 
    canvas.create_window(200, 140, window=entry3_1)

    label3 = Label(Mafenetre3_1, text='La latitude Phi (°) :')
    label3.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 170, window=label3)
    entry3_2 = Entry(Mafenetre3_1) 
    canvas.create_window(200, 200, window=entry3_2)
    
    Bouton1 = Button(Mafenetre3_1, text = 'Réactualiser ', command =ANGLESUPDAT3,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    Bouton1.pack()

    button2 = Button(Mafenetre3_1,text='Transformer', command = get_coordonnees_astronomique ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    button2.pack()
    
    Bouton3= Button(Mafenetre3_1, text = 'show map', command =lon_lat_interval3,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    Bouton3.pack(side=BOTTOM)
    
    Mafenetre3_1.mainloop()

def ANGLESUPDAT3():
    
    global Lambda3,Phi3,entry3_1,entry3_2,Valeur3,Valeur4,echelle3,echelle4
    try:
        
        Lambda3,Phi3=float(entry3_1.get()),float(entry3_2.get())

        echelle3.set((float(entry3_1.get())))
        echelle4.set((float(entry3_2.get())))
        Valeur3.set(str(float(entry3_1.get())))
        Valeur4.set(str(float(entry3_2.get())))
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  

def get_coordonnees_astronomique():
  
    global Valeur3,Valeur4,entry3_3,entry3_4,entry3_5,canvas3,Mafenetre3,echelle3,echelle4
    try:
        
        Lambda3,Phi3,DeltaX3,DeltaY3,DeltaZ3=float(Valeur3.get()),float(Valeur4.get()),float(entry3_3.get()),float(entry3_4.get()),float(entry3_5.get())
        Az3,Av3,C3=Transformation_coor_Geocentriques_Astronomique(Phi3,Lambda3,DeltaX3,DeltaY3,DeltaZ3)

        label7 = Label(Mafenetre3 ,text= 'Azimut astronomique Apq (°) :')
        label7.config(font=('Ink Free', 10))
        canvas3.create_window(200, 460, window=label7)
    
        label8 = Label(Mafenetre3, text= '%.5E'% Decimal(Az3) ,font=('Ink Free', 10, 'bold'))
        canvas3.create_window(200, 480, window=label8)

        label9 = Label(Mafenetre3 , text= 'Distance entre P et Q Cpq (m):',font=('Ink Free', 10))
        canvas3.create_window(200, 500, window=label9)
    
        label10 = Label(Mafenetre3, text= '%.5E'% Decimal(C3) ,font=('Ink Free', 10, 'bold'))
        canvas3.create_window(200, 520, window=label10)

        label11 = Label(Mafenetre3 , text= 'Angle vertical Vpq (°):',font=('Ink Free', 10))
        canvas3.create_window(200, 540, window=label11)
    
        label12 = Label(Mafenetre3, text= Av3 ,font=('Ink Free', 10, 'bold'))
        canvas3.create_window(200, 560, window=label12)
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
def get_coordonnees_astronomique2():
  
    global Valeur3,Valeur4,entry3_3,entry3_4,entry3_5,canvas3,Mafenetre3,echelle3,echelle4
    try:
        
         Lambda3,Phi3,DeltaX3,DeltaY3,DeltaZ3=float(echelle3.get()),float(echelle4.get()),float(entry3_3.get()),float(entry3_4.get()),float(entry3_5.get())
    
         Az3,Av3,C3=Transformation_coor_Geocentriques_Astronomique(Phi3,Lambda3,DeltaX3,DeltaY3,DeltaZ3)

         label7 = Label(Mafenetre3 ,text= 'Azimut astronomique Apq (°) :')
         label7.config(font=('Ink Free', 10))
         canvas3.create_window(200, 460, window=label7)
    
         label8 = Label(Mafenetre3, text= '%.5E'% Decimal(Az3) ,font=('Ink Free', 10, 'bold'))
         canvas3.create_window(200, 480, window=label8)

         label9 = Label(Mafenetre3 , text= 'Distance entre P et Q Cpq (m) :',font=('Ink Free', 10))
         canvas3.create_window(200, 500, window=label9)
    
         label10 = Label(Mafenetre3, text= '%.5E'% Decimal(C3) ,font=('Ink Free', 10, 'bold'))
         canvas3.create_window(200, 520, window=label10)

         label11 = Label(Mafenetre3 , text= 'Angle vertical Vpq (°) :',font=('Ink Free', 10))
         canvas3.create_window(200, 540, window=label11)
    
         label12 = Label(Mafenetre3, text= Av3 ,font=('Ink Free', 10, 'bold'))
         canvas3.create_window(200, 560, window=label12)
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
       
        
def lon_lat_interval3():
    
    global entry6_1,entry6_2
    
    Mafenetre6 = Tk()
    Mafenetre6.iconbitmap('Ressources/favicon.ico')
  
    Mafenetre6.title("lon_lat_interval")

    Label1 = Label(Mafenetre6, text = ' Veuillez entrez la valeur des esspacements :',font=('Ink Free', 14 ,'bold'),fg='#005994')
    Label1.pack()

    canvas = Canvas(Mafenetre6, width = 400, height = 300, relief = 'raised')
    canvas.pack()


    label2 = Label(Mafenetre6, text='lat_interval:')
    label2.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas.create_window(200, 110, window=label2)

    entry6_1 = Entry(Mafenetre6) 
    canvas.create_window(200, 140, window=entry6_1)

    label3 = Label(Mafenetre6, text='lon_interval:')
    label3.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas.create_window(200, 170, window=label3)

    entry6_2 = Entry(Mafenetre6) 
    canvas.create_window(200, 200, window=entry6_2)

    Bouton1 = Button(Mafenetre6, text = 'Show map', command =mapp3,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 10, 'bold'))
    Bouton1.pack()
    
    Bouton2 = Button(Mafenetre6, text = '?', command =openweb134_2,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Bouton2.pack()

    Mafenetre6.mainloop()

def mapp3():
    try:
        lon=Valeur4.get()
        lat=Valeur3.get()
        tooltip = 'Click me!'
        map = Map(location=[lon, lat], zoom_start=12 , tiles='Stamen Terrain')
        Marker([lon, lat], popup='<i>Mt. Hood Meadows</i>', tooltip=tooltip).add_to(map)
        lat_interval = int(entry6_1.get())
        lon_interval = int(entry6_2.get())
        grid = []

        for lat in range(-90, 91, lat_interval):
    
            grid.append([[lat, -180],[lat, 180]])
   
        for lon in range(-180, 181, lon_interval):
    
            grid.append([[-90, lon],[90, lon]])

        for g in grid:
      
             PolyLine(g, color="black", weight=0.5, opacity=0.5).add_to(map)
        map
        #######
        map.save('indexx.html')
        openweb3()
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  


##           _                                   _                                                                          _        _                     _  _   
##  __ _ ___| |_ _ __ ___  _ __   ___  _ __ ___ (_) __ _ _   _  ___  __   _____ _ __ ___     __ _  ___  ___   ___ ___ _ __ | |_ _ __(_) __ _ _   _  ___   | || |  
## / _` / __| __| '__/ _ \| '_ \ / _ \| '_ ` _ \| |/ _` | | | |/ _ \ \ \ / / _ \ '__/ __|   / _` |/ _ \/ _ \ / __/ _ \ '_ \| __| '__| |/ _` | | | |/ _ \  | || |_ 
##| (_| \__ \ |_| | | (_) | | | | (_) | | | | | | | (_| | |_| |  __/  \ V /  __/ |  \__ \  | (_| |  __/ (_) | (_|  __/ | | | |_| |  | | (_| | |_| |  __/  |__   _|
## \__,_|___/\__|_|  \___/|_| |_|\___/|_| |_| |_|_|\__, |\__,_|\___|   \_/ \___|_|  |___/   \__, |\___|\___/ \___\___|_| |_|\__|_|  |_|\__, |\__,_|\___|     |_|  
##                                                    |_|                                   |___/                                         |_|                     



def Transformation_coor_Astronomique_Geocentriques(phi,Laambda,az,av,c) :
    
            phi=degree2radians(phi)
            Laambda=degree2radians(Laambda)
            az=degree2radians(az)
            av=degree2radians(av)
            
            l=[]
            v1=c*cos(av)*cos(az)
            v2=c*cos(av)*sin(az)
            v3=c*sin(av)
            a=-sin(phi)*cos(Laambda)
            b=-sin(Laambda)
            c=cos(phi)*cos(Laambda)
            d=-sin(phi)*sin(Laambda)
            e=cos(Laambda)
            f=cos(phi)*sin(Laambda)
            g=cos(phi)
            h=0
            i=sin(phi)
            x=a*v1+b*v2+c*v3
            y=d*v1+e*v2+f*v3
            z=g*v1+h*v2+i*v3
            l.append(x)
            l.append(y)
            l.append(z)
            for i in range (3):
                if abs(l[i])<1e-15 :
                    l[i]=0

            return l[0],l[1],l[2]



def   Astronomique_vers_Geocentrique():
    
    global Valeur5,Valeur6,Valeur7,Valeur8,entry4_5,canvas4,Mafenetre4,echelle5,echelle6,echelle7,echelle8
    
    Mafenetre4 = Tk()
    Mafenetre4.geometry('600x670')
    Mafenetre4.iconbitmap('Ressources/favicon.ico')
    Mafenetre4.title('Astronomique_locale_vers_Geocentrique')

    canvas4 = Canvas(Mafenetre4, width = 400, height = 600, relief = 'raised')
    canvas4.pack()
    label1 = Label(Mafenetre4, text='Transformation entre coordonnees:\n Astronomique locale vers Géocentrique')
    label1.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas4.create_window(200, 25, window=label1)

    Valeur5 = StringVar()
    Valeur5.set(180)
    echelle5 = Scale(Mafenetre4,from_=-0,to=360,resolution=1,orient=HORIZONTAL,length=500,width=20,label="La longitude Lambda (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur5)
    canvas4.create_window(200, 100, window=echelle5)

    Valeur6 = StringVar()
    Valeur6.set(180)
    echelle6 = Scale(Mafenetre4,from_=-90,to=90,resolution=1,orient=HORIZONTAL,length=500,width=20,label="La latitude Phi (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur6)
    canvas4.create_window(200, 180, window=echelle6)

    Valeur7 = StringVar()
    Valeur7.set(180)
    echelle7 = Scale(Mafenetre4,from_=-180,to=180,resolution=1,orient=HORIZONTAL,length=500,width=20,label="Azimut astronomique Apq (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur7)
    canvas4.create_window(200, 260, window=echelle7)

    Valeur8 = StringVar()
    Valeur8.set(180)
    echelle8 = Scale(Mafenetre4,from_=-180,to=180,resolution=1,orient=HORIZONTAL,length=500,width=20,label="Angle vertical Vpq (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur8)
    canvas4.create_window(200, 340, window=echelle8)

    label6 = Label(Mafenetre4, text='Distance entre P et Q Cpq (m):')
    label6.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas4.create_window(200, 390, window=label6)

    entry4_5 = Entry(Mafenetre4) 
    canvas4.create_window(200, 410, window=entry4_5)

    button2 = Button(Mafenetre4,text='Transformer', command=g4et_coordonnees_geocentrique2 ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    canvas4.create_window(200, 450, window=button2)

    Bouton7= Button(Mafenetre4, text = "Saisie manuelle (Longitude / Latitude)", command =ANGLES4 ,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Bouton7.pack(side=BOTTOM)
    
    Btn = Button(Mafenetre4, text = "Consulter Google earth",command=openweb,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Btn.pack(side=BOTTOM)
    
    Mafenetre4.mainloop()

def ANGLES4():
    
    global entry4_1,entry4_2,Mafenetre4_1,entry4_3,entry4_4
    
    Mafenetre4_1 = Tk()
    Mafenetre4_1.iconbitmap('Ressources/favicon.ico')
    
    Label1 = Label(Mafenetre4_1, text = ' Veuillez entrez la valeur des angles :',font=('Ink Free', 14 ,'bold'),fg='#005994')
    Label1.pack()

    canvas = Canvas(Mafenetre4_1, width = 400, height = 410, relief = 'raised')
    canvas.pack()

    
    label2 = Label(Mafenetre4_1, text='La longitude Lambda (°) :')
    label2.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 110, window=label2)

    entry4_1 = Entry(Mafenetre4_1) 
    canvas.create_window(200, 140, window=entry4_1)

    label3 = Label(Mafenetre4_1, text='La latitude Phi (°) :')
    label3.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 170, window=label3)

    entry4_2 = Entry(Mafenetre4_1) 
    canvas.create_window(200, 200, window=entry4_2)

    label3 = Label(Mafenetre4_1, text='Azimut astronomique Apq (°) :')
    label3.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 230, window=label3)

    entry4_3 = Entry(Mafenetre4_1) 
    canvas.create_window(200, 260, window=entry4_3)

    label3 = Label(Mafenetre4_1, text='Angle vertical Vpq (°) :')
    label3.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 290, window=label3)

    entry4_4 = Entry(Mafenetre4_1) 
    canvas.create_window(200, 310, window=entry4_4)
    
    Bouton1 = Button(Mafenetre4_1, text = 'Réactualiser', command =ANGLESUPDAT4,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    Bouton1.pack()
    
    button2 = Button(Mafenetre4_1,text='Transformer', command=g4et_coordonnees_geocentrique ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    button2.pack()
    
    Bouton3= Button(Mafenetre4_1, text = 'Show map', command =lon_lat_interval4,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    Bouton3.pack(side=BOTTOM)
    
    Mafenetre4_1.mainloop()

def ANGLESUPDAT4():
    
    global Lambda4,Phi4,entry4_2,entry4_1,entry4_3,entry4_4,Valeur5,Valeur6,Valeur7,Valeur8,echelle5,echelle6,echelle7,echelle8
    try:
        
        Lambda4,Phi4,Az,Av=float(entry4_2.get()),float(entry4_1.get()),float(entry4_3.get()),float(entry4_4.get())

        echelle5.set((float(entry4_1.get())))
        echelle6.set((float(entry4_2.get())))
        echelle7.set((float(entry4_3.get())))
        echelle8.set((float(entry4_4.get())))
        Valeur5.set(str(float(entry4_1.get())))
        Valeur6.set(str(float(entry4_2.get())))
        Valeur7.set(str(float(entry4_3.get())))
        Valeur8.set(str(float(entry4_4.get())))
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  

def g4et_coordonnees_geocentrique():
    
    global Valeur5,Valeur6,entry4_3,entry4_4,entry4_5,canvas4,Mafenetre4,echelle5,echelle6,echelle7,echelle8
    try:
        
       Lambda4,Phi4,Az4,Av4,C4=float(Valeur5.get()),float(Valeur6.get()),float(Valeur7.get()),float(Valeur8.get()),float(entry4_5.get())
    
       DeltaX4,DeltaY4,DeltaZ4=Transformation_coor_Astronomique_Geocentriques(Phi4,Lambda4,Az4,Av4,C4)

       label7 = Label(Mafenetre4 ,text= 'DeltaXpq (m) :')
       label7.config(font=('Ink Free', 10))
       canvas4.create_window(200, 490, window=label7)
    
       label8 = Label(Mafenetre4, text= '%.5E'% Decimal(DeltaX4) ,font=('Ink Free', 10, 'bold'))
       canvas4.create_window(200, 510, window=label8)

       label9 = Label(Mafenetre4 , text= 'DeltaYpq(m) :',font=('Ink Free', 10))
       canvas4.create_window(200, 530, window=label9)
    
       label10 = Label(Mafenetre4, text= '%.5E'% Decimal(DeltaY4) ,font=('Ink Free', 10, 'bold'))
       canvas4.create_window(200, 550, window=label10)

       label11 = Label(Mafenetre4 , text= 'DeltaXpq (m) :',font=('Ink Free', 10))
       canvas4.create_window(200, 570, window=label11)
    
       label12 = Label(Mafenetre4, text= '%.5E'% Decimal(DeltaZ4) ,font=('Ink Free', 10, 'bold'))
       canvas4.create_window(200, 590, window=label12)

    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
    
def g4et_coordonnees_geocentrique2():
    
    global Valeur5,Valeur6,Valeur7,Valeur8,entry4_3,entry4_4,entry4_5,canvas4,Mafenetre4,echelle5,echelle6,echelle7,echelle8
    try:
        
        Lambda4,Phi4,Az4,Av4,C4=float(echelle5.get()),float(echelle6.get()),float(echelle7.get()),float(echelle8.get()),float(entry4_5.get())
    
        DeltaX4,DeltaY4,DeltaZ4=Transformation_coor_Astronomique_Geocentriques(Phi4,Lambda4,Az4,Av4,C4)

        label7 = Label(Mafenetre4 ,text= 'DeltaXpq (m) :')
        label7.config(font=('Ink Free', 10))
        canvas4.create_window(200, 490, window=label7)
         
        label8 = Label(Mafenetre4, text= '%.5E'% Decimal(DeltaX4) ,font=('Ink Free', 10, 'bold'))
        canvas4.create_window(200, 510, window=label8)

        label9 = Label(Mafenetre4 , text= 'DeltaYpq (m) :',font=('Ink Free', 10))
        canvas4.create_window(200, 530, window=label9)
      
        label10 = Label(Mafenetre4, text= '%.5E'% Decimal(DeltaY4) ,font=('Ink Free', 10, 'bold'))
        canvas4.create_window(200, 550, window=label10)

        label11 = Label(Mafenetre4 , text= 'DeltaXpq (m) :',font=('Ink Free', 10))
        canvas4.create_window(200, 570, window=label11)
    
        label12 = Label(Mafenetre4, text= '%.5E'% Decimal(DeltaZ4) ,font=('Ink Free', 10, 'bold'))
        canvas4.create_window(200, 590, window=label12)
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  


def lon_lat_interval4():
    
    global entry7_1,entry7_2
    
    Mafenetre7 = Tk()
    Mafenetre7.iconbitmap('Ressources/favicon.ico')
  
    Mafenetre7.title("lon_lat_interval")

    Label1 = Label(Mafenetre7, text = ' Veuillez entrez la valeur des esspacements :',font=('Ink Free', 14 ,'bold'),fg='#005994')
    Label1.pack()

    canvas = Canvas(Mafenetre7, width = 400, height = 300, relief = 'raised')
    canvas.pack()

    
    label2 = Label(Mafenetre7, text='lat_interval:')
    label2.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 110, window=label2)

    entry7_1 = Entry(Mafenetre7) 
    canvas.create_window(200, 140, window=entry7_1)

    label3 = Label(Mafenetre7, text='lon_interval:')
    label3.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 170, window=label3)

    entry7_2 = Entry(Mafenetre7) 
    canvas.create_window(200, 200, window=entry7_2)

    Bouton1 = Button(Mafenetre7, text = 'Show map', command =mapp4,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Bouton1.pack()
    
    Bouton2 = Button(Mafenetre7, text = '?', command =openweb134_2,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Bouton2.pack()

    
    Mafenetre7.mainloop()
  
def mapp4():
    try:
        
         lon=Valeur6.get()
         lat=Valeur5.get()
         tooltip = 'Click me!'
         map = Map(location=[lon, lat], zoom_start=14 , tiles='Stamen Terrain')
         Marker([lon,lat], popup='<i>Mt. Hood Meadows</i>', tooltip=tooltip).add_to(map)
         map
         lat_interval = int(entry7_1.get())
         lon_interval = int(entry7_2.get())
         grid = []
  
         for lat in range(-90, 91, lat_interval):

            grid.append([[lat, -180],[lat, 180]])

         for lon in range(-180, 181, lon_interval):
            
    
            grid.append([[-90, lon],[90, lon]])

         for g in grid:        


               PolyLine(g, color="black", weight=0.5, opacity=0.5).add_to(map)
        ########
         map.save('indexx.html')
         openweb3()
        
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")


##   _____   __           _           _                    _                 _                                     __                      _        _                   
##  / ____| /_/          | |         (_)                  | |               | |                                   /_/                     | |      (_)                  
## | |  __  ___  ___   __| | ___  ___ _  __ _ _   _  ___  | | ___   ___ __ _| | ___  __   _____ _ __ ___    __ _  ___  ___   ___ ___ _ __ | |_ _ __ _  __ _ _   _  ___  
## | | |_ |/ _ \/ _ \ / _` |/ _ \/ __| |/ _` | | | |/ _ \ | |/ _ \ / __/ _` | |/ _ \ \ \ / / _ \ '__/ __|  / _` |/ _ \/ _ \ / __/ _ \ '_ \| __| '__| |/ _` | | | |/ _ \ 
## | |__| |  __/ (_) | (_| |  __/\__ \ | (_| | |_| |  __/ | | (_) | (_| (_| | |  __/  \ V /  __/ |  \__ \ | (_| |  __/ (_) | (_|  __/ | | | |_| |  | | (_| | |_| |  __/ 
##  \_____|\___|\___/ \__,_|\___||___/_|\__, |\__,_|\___| |_|\___/ \___\__,_|_|\___|   \_/ \___|_|  |___/  \__, |\___|\___/ \___\___|_| |_|\__|_|  |_|\__, |\__,_|\___| 
##                                         | |                                                              __/ |                                        | |            
##                                         |_|                                                             |___/                                         |_|           


def transformation_geodesique_locales_vers_geocentrique(lambdap,phip,alphapq,vpq,cpq):
    
    lambdap=degree2radians(lambdap)
    phip=degree2radians(phip)
    alphapq=degree2radians(alphapq)
    vpq=degree2radians(vpq)
    
    a=cpq*cos(vpq)*cos(alphapq)
    b=cpq*cos(vpq)*sin(alphapq)
    c=cpq*sin(vpq)
    
    DeltaXpq=-sin(phip)*cos(lambdap)*a-sin(lambdap)*b+c*cos(phip)*cos(lambdap)
    DeltaYpq=-sin(phip)*sin(lambdap)*a+cos(lambdap)*b+cos(phip)*sin(lambdap)*c
    DeltaZpq=cos(phip)*a+c*sin(phip)
    
    return DeltaXpq,DeltaYpq,DeltaZpq


def   geodesique_locales_vers_Geocentrique():
    
    global Valeur9,Valeur10,Valeur11,Valeur12,entry5_5,canvas5,Mafenetre8,echelle9,echelle10,echelle11,echelle12
    
    Mafenetre8 = Tk()
    Mafenetre8.geometry('600x670')
    Mafenetre8.iconbitmap('Ressources/favicon.ico')
    Mafenetre8.title('Géodésique_locales_vers_Géocentrique')

    canvas5 = Canvas(Mafenetre8, width = 400, height = 600, relief = 'raised')
    canvas5.pack()
    label1 = Label(Mafenetre8, text='Transformation entre coordonnees:\n Géodésique locales vers Géocentrique')
    label1.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas5.create_window(200, 25, window=label1)

    Valeur9 = StringVar()
    Valeur9.set(180)
    echelle9 = Scale(Mafenetre8,from_=-0,to=360,resolution=1,orient=HORIZONTAL,length=500,width=20,label="La longitude Lambdap (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur9)
    canvas5.create_window(200, 100, window=echelle9)

    Valeur10 = StringVar()
    Valeur10.set(180)
    echelle10 = Scale(Mafenetre8,from_=-90,to=90,resolution=1,orient=HORIZONTAL,length=500,width=20,label="La latitude Phip (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur10)
    canvas5.create_window(200, 180, window=echelle10)

    Valeur11 = StringVar()
    Valeur11.set(180)
    echelle11 = Scale(Mafenetre8,from_=-180,to=180,resolution=1,orient=HORIZONTAL,length=500,width=20,label="alphapq Azimut Géodésique de la section Normale directe (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur11)
    canvas5.create_window(200, 260, window=echelle11)

    Valeur12 = StringVar()
    Valeur12.set(180)
    echelle12 = Scale(Mafenetre8,from_=-180,to=180,resolution=1,orient=HORIZONTAL,length=500,width=20,label="Vpq Angle Vertical vers Q selon le plan de la section normal directe (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur12)
    canvas5.create_window(200, 340, window=echelle12)

    label6 = Label(Mafenetre8, text='Cpq Distance entre P et Q (m):')
    label6.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas5.create_window(200, 390, window=label6)

    entry5_5 = Entry(Mafenetre8) 
    canvas5.create_window(200, 410, window=entry5_5)

    button2 = Button(Mafenetre8,text='Transformer', command=g5et_coordonnees_geocentrique2 ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    canvas5.create_window(200, 450, window=button2)

    Bouton7= Button(Mafenetre8, text = "Saisie manuelle (Longitude / Latitude)", command =ANGLES5 ,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Bouton7.pack(side=BOTTOM)
    
    Btn = Button(Mafenetre8, text = "Consulter Google earth",command=openweb,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Btn.pack(side=BOTTOM)
    
    Mafenetre8.mainloop()

def ANGLES5():
    
    global entry5_1,entry5_2,Mafenetre5_1,entry5_3,entry5_4
    
    Mafenetre5_1 = Tk()
    Mafenetre5_1.iconbitmap('Ressources/favicon.ico')
    
    Label1 = Label(Mafenetre5_1, text = ' Veuillez entrez la valeur des angles :',font=('Ink Free', 14 ,'bold'),fg='#005994')
    Label1.pack()

    canvas = Canvas(Mafenetre5_1, width = 400, height = 410, relief = 'raised')
    canvas.pack()

    
    label2 = Label(Mafenetre5_1, text='La longitude Lambdap (°) :')
    label2.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 110, window=label2)

    entry5_1 = Entry(Mafenetre5_1) 
    canvas.create_window(200, 140, window=entry5_1)

    label3 = Label(Mafenetre5_1, text='La latitude Phip(°) :')
    label3.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 170, window=label3)

    entry5_2 = Entry(Mafenetre5_1) 
    canvas.create_window(200, 200, window=entry5_2)

    label3 = Label(Mafenetre5_1, text='alphapq Azimut Géodésique de la section Normale directe (°) :')
    label3.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 230, window=label3)

    entry5_3 = Entry(Mafenetre5_1) 
    canvas.create_window(200, 260, window=entry5_3)

    label3 = Label(Mafenetre5_1, text='Vpq Angle Vertical vers Q selon le plan de la section normal directe (°) :')
    label3.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 290, window=label3)

    entry5_4 = Entry(Mafenetre5_1) 
    canvas.create_window(200, 310, window=entry5_4)
    
    Bouton1 = Button(Mafenetre5_1, text = 'Réactualiser', command =ANGLESUPDAT5,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    Bouton1.pack()
    
    button2 = Button(Mafenetre5_1,text='Transformer', command=g5et_coordonnees_geocentrique ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    button2.pack()
    
    Bouton3= Button(Mafenetre5_1, text = 'Show map', command =lon_lat_interval5,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    Bouton3.pack(side=BOTTOM)
    
    Mafenetre5_1.mainloop()

def ANGLESUPDAT5():
    
    global lambdap,phip,entry5_2,entry5_1,entry5_3,entry5_4,Valeur9,Valeur10,Valeur11,Valeur12,echelle9,echelle10,echelle11,echelle12
    try:
        
        lambdap,phip,alphapq,vpq=float(entry5_2.get()),float(entry5_1.get()),float(entry5_3.get()),float(entry5_4.get())

        echelle9.set((float(entry5_1.get())))
        echelle10.set((float(entry5_2.get())))
        echelle11.set((float(entry5_3.get())))
        echelle12.set((float(entry5_4.get())))
        Valeur9.set(str(float(entry5_1.get())))
        Valeur10.set(str(float(entry5_2.get())))
        Valeur11.set(str(float(entry5_3.get())))
        Valeur12.set(str(float(entry5_4.get())))
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  

def g5et_coordonnees_geocentrique():
    
    global Valeur9,Valeur10,Valeur11,Valeur12,entry5_3,entry5_4,entry5_5,canvas5,Mafenetre8,echelle9,echelle10,echelle11,echelle12
    try:
        
       lambdap,phip,alphapq,vpq,cpq=float(Valeur9.get()),float(Valeur10.get()),float(Valeur11.get()),float(Valeur12.get()),float(entry5_5.get())
    
       DeltaX4,DeltaY4,DeltaZ4=transformation_geodesique_locales_vers_geocentrique(lambdap,phip,alphapq,vpq,cpq)

       label7 = Label(Mafenetre8 ,text= 'DeltaXpq(m) :')
       label7.config(font=('Ink Free', 10))
       canvas5.create_window(200, 490, window=label7)
    
       label8 = Label(Mafenetre8, text= '%.5E'% Decimal(DeltaX4) ,font=('Ink Free', 10, 'bold'))
       canvas5.create_window(200, 510, window=label8)

       label9 = Label(Mafenetre8 , text= 'DeltaYpq(m) :',font=('Ink Free', 10))
       canvas5.create_window(200, 530, window=label9)
    
       label10 = Label(Mafenetre8, text= '%.5E'% Decimal(DeltaY4) ,font=('Ink Free', 10, 'bold'))
       canvas5.create_window(200, 550, window=label10)

       label11 = Label(Mafenetre8 , text= 'DeltaZpq(m) :',font=('Ink Free', 10))
       canvas5.create_window(200, 570, window=label11)
    
       label12 = Label(Mafenetre8, text= '%.5E'% Decimal(DeltaZ4) ,font=('Ink Free', 10, 'bold'))
       canvas5.create_window(200, 590, window=label12)

    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
    
def g5et_coordonnees_geocentrique2():
    
    global Valeur9,Valeur10,Valeur11,Valeur12,entry5_3,entry5_4,entry5_5,canvas5,Mafenetre8,echelle9,echelle10,echelle11,echelle12
    try:
        
        lambdap,phip,alphapq,vpq,cpq=float(echelle9.get()),float(echelle10.get()),float(echelle11.get()),float(echelle12.get()),float(entry5_5.get())
    
        DeltaX4,DeltaY4,DeltaZ4=transformation_geodesique_locales_vers_geocentrique(lambdap,phip,alphapq,vpq,cpq)

        label7 = Label(Mafenetre8 ,text= 'DeltaXpq (m) :')
        label7.config(font=('Ink Free', 10))
        canvas5.create_window(200, 490, window=label7)
         
        label8 = Label(Mafenetre8, text= '%.5E'% Decimal(DeltaX4) ,font=('Ink Free', 10, 'bold'))
        canvas5.create_window(200, 510, window=label8)

        label9 = Label(Mafenetre8 , text= 'DeltaYpq (m) :',font=('Ink Free', 10))
        canvas5.create_window(200, 530, window=label9)
      
        label10 = Label(Mafenetre8, text= '%.5E'% Decimal(DeltaY4) ,font=('Ink Free', 10, 'bold'))
        canvas5.create_window(200, 550, window=label10)

        label11 = Label(Mafenetre8 , text= 'DeltaZpq (m) :',font=('Ink Free', 10))
        canvas5.create_window(200, 570, window=label11)
    
        label12 = Label(Mafenetre8, text= '%.5E'% Decimal(DeltaZ4) ,font=('Ink Free', 10, 'bold'))
        canvas5.create_window(200, 590, window=label12)
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  


def lon_lat_interval5():
    
    global entry9_1,entry9_2
    
    Mafenetre9 = Tk()
    Mafenetre9.iconbitmap('Ressources/favicon.ico')
  
    Mafenetre9.title("lon_lat_interval")

    Label1 = Label(Mafenetre9, text = ' Veuillez entrez la valeur des esspacements :',font=('Ink Free', 14 ,'bold'),fg='#005994')
    Label1.pack()

    canvas = Canvas(Mafenetre9, width = 400, height = 300, relief = 'raised')
    canvas.pack()

    
    label2 = Label(Mafenetre9, text='lat_interval:')
    label2.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 110, window=label2)

    entry9_1 = Entry(Mafenetre9) 
    canvas.create_window(200, 140, window=entry9_1)

    label3 = Label(Mafenetre9, text='lon_interval:')
    label3.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 170, window=label3)

    entry9_2 = Entry(Mafenetre9) 
    canvas.create_window(200, 200, window=entry9_2)

    Bouton1 = Button(Mafenetre9, text = 'Show map', command =mapp5,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Bouton1.pack()
    
    Bouton2 = Button(Mafenetre9, text = '?', command =openweb134_2,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Bouton2.pack()

    
    Mafenetre9.mainloop()
  
def mapp5():
         
    try:
        
         lon=Valeur10.get()
         lat=Valeur9.get()
         tooltip = 'Click me!'
         map = Map(location=[lon, lat], zoom_start=14 , tiles='Stamen Terrain')
         Marker([lon,lat], popup='<i>Mt. Hood Meadows</i>', tooltip=tooltip).add_to(map)
         map
         lat_interval = int(entry9_1.get())
         lon_interval = int(entry9_2.get())
         grid = []
  
         for lat in range(-90, 91, lat_interval):

            grid.append([[lat, -180],[lat, 180]])

         for lon in range(-180, 181, lon_interval):
            
    
            grid.append([[-90, lon],[90, lon]])

         for g in grid:        


               PolyLine(g, color="black", weight=0.5, opacity=0.5).add_to(map)
        ########
         map.save('indexx.html')
         openweb3()
        
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")



##   _____   __                      _        _                                                 __           _           _                    _                 _      
##  / ____| /_/                     | |      (_)                                               /_/          | |         (_)                  | |               | |     
## | |  __  ___  ___   ___ ___ _ __ | |_ _ __ _  __ _ _   _  ___  __   _____ _ __ ___    __ _  ___  ___   __| | ___  ___ _  __ _ _   _  ___  | | ___   ___ __ _| | ___ 
## | | |_ |/ _ \/ _ \ / __/ _ \ '_ \| __| '__| |/ _` | | | |/ _ \ \ \ / / _ \ '__/ __|  / _` |/ _ \/ _ \ / _` |/ _ \/ __| |/ _` | | | |/ _ \ | |/ _ \ / __/ _` | |/ _ \
## | |__| |  __/ (_) | (_|  __/ | | | |_| |  | | (_| | |_| |  __/  \ V /  __/ |  \__ \ | (_| |  __/ (_) | (_| |  __/\__ \ | (_| | |_| |  __/ | | (_) | (_| (_| | |  __/
##  \_____|\___|\___/ \___\___|_| |_|\__|_|  |_|\__, |\__,_|\___|   \_/ \___|_|  |___/  \__, |\___|\___/ \__,_|\___||___/_|\__, |\__,_|\___| |_|\___/ \___\__,_|_|\___|
##                                                 | |                                   __/ |                                | |                                      
##                                                 |_|                                  |___/                                 |_|                                            



def transformation_geocentriques_geodesiques_locales(lambdap,phip,DeltaXpq,DeltaYpq,DeltaZpq):
    
    M=[0,0,0]
    
    lambdap=(lambdap*pi)/180
    phip=(phip*pi)/180
    
    M[1]=sqrt(DeltaXpq**2+DeltaYpq**2+DeltaZpq**2)#cpq
    
    if M[1]==0:
        M[0]='alphapq n existe pas'
    else :
        M[0]=atan((-DeltaXpq*sin(lambdap)+DeltaYpq*cos(lambdap)/(-DeltaXpq*sin(phip)*cos(lambdap)-DeltaYpq*sin(phip)*sin(lambdap)+DeltaZpq*cos(phip))))#alphapq
        radians2degree(M[0])
    if M[1]==0 :
        M[2]='cpq=0 et vpq n existe pas '
    else :
        M[2]=(asin((1/M[1])*(DeltaXpq*cos(phip)*cos(lambdap)+DeltaYpq*cos(phip)*sin(lambdap)+DeltaZpq*sin(phip))))
        radians2degree(M[2])
    
    return M[0],radians2degree(M[1]),M[2] #(alphapq,cpq,vpq)




def   geocentriques_geodesiques_locales():
    
    global Valeur13,Valeur14,entry6_3,entry6_4,entry6_5,canvas6,Mafenetre10,echelle13,echelle14
    
    Mafenetre10 = Tk()
    Mafenetre10.geometry('600x670')
    Mafenetre10.iconbitmap('Ressources/favicon.ico')
    Mafenetre10.title('transformation_geocentriques_geodesiques_locales')

    canvas6 = Canvas(Mafenetre10, width = 400, height = 600, relief = 'raised')
    canvas6.pack()
    
    label1 = Label(Mafenetre10, text='Transformation entre coordonnees:\n Géocentrique vers Géodesique locale ')
    label1.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas6.create_window(200, 25, window=label1)

    Valeur13 = StringVar()
    Valeur13.set(180)
    echelle13 = Scale(Mafenetre10,from_=-180,to=180,resolution=1,orient=HORIZONTAL,length=500,width=20,label="La longitude Lambdap (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur13)
    canvas6.create_window(200, 100, window=echelle13)

    Valeur14 = StringVar()
    Valeur14.set(180)
    echelle14 = Scale(Mafenetre10,from_=-90,to=90,resolution=1,orient=HORIZONTAL,length=500,width=20,label="La latitude Phip (°) :",font=('Ink Free', 9 ,'bold'),fg='#005994',tickinterval=20,variable=Valeur14)
    canvas6.create_window(200, 180, window=echelle14)

    label4 = Label(Mafenetre10, text='DeltaXpq (m) :')
    label4.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas6.create_window(200, 230, window=label4)
    entry6_3 = Entry(Mafenetre10) 
    canvas6.create_window(200, 260, window=entry6_3)

    label5 = Label(Mafenetre10, text='DeltaYpq (m) :')
    label5.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas6.create_window(200, 290, window=label5)
    entry6_4 = Entry(Mafenetre10) 
    canvas6.create_window(200, 320, window=entry6_4)

    label6 = Label(Mafenetre10, text='DeltaZpq (m) :')
    label6.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas6.create_window(200, 350, window=label6)
    entry6_5 = Entry(Mafenetre10) 
    canvas6.create_window(200, 380, window=entry6_5)

    button2 = Button(Mafenetre10,text='Transformer', command = g6et_coordonnees_geodesiques_locales2 ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    canvas6.create_window(200, 420, window=button2)
    
    Btn = Button(Mafenetre10, text = "Consulter Google earth",command=openweb,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Btn.pack(side=BOTTOM)
    
    Bouton7= Button(Mafenetre10, text = "Saisie manuelle (Longitude / Latitude)", command =ANGLES6 ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    Bouton7.pack(side=BOTTOM)
    
    Mafenetre10.mainloop()

def ANGLES6():
    
    global entry6_1,entry6_2,Mafenetre6_1
    
    Mafenetre6_1 = Tk()
    Mafenetre6_1.iconbitmap('Ressources/favicon.ico')
    
    Label1 = Label(Mafenetre6_1, text = ' Veuillez entrez la valeur des angles :',font=('Ink Free', 14 ,'bold'),fg='#005994')
    Label1.pack()

    canvas = Canvas(Mafenetre6_1, width = 400, height = 300, relief = 'raised')
    canvas.pack()
    
    label2 = Label(Mafenetre6_1, text='La longitude Lambda (°) :')
    label2.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 110, window=label2)
    entry6_1 = Entry(Mafenetre6_1) 
    canvas.create_window(200, 140, window=entry6_1)

    label3 = Label(Mafenetre6_1, text='La latitude Phi (°) :')
    label3.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas.create_window(200, 170, window=label3)
    entry6_2 = Entry(Mafenetre6_1) 
    canvas.create_window(200, 200, window=entry6_2)
    
    Bouton1 = Button(Mafenetre6_1, text = 'Réactualiser ', command =ANGLESUPDAT6,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    Bouton1.pack()

    button2 = Button(Mafenetre6_1,text='Transformer', command = g6et_coordonnees_geodesiques_locales ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    button2.pack()
    
    Bouton3= Button(Mafenetre6_1, text = 'show map', command =lon_lat_interval6,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    Bouton3.pack(side=BOTTOM)
    
    Mafenetre6_1.mainloop()

def ANGLESUPDAT6():
    
    global lambdap,phip,entry6_1,entry6_2,Valeur13,Valeur14,echelle13,echelle14
    try:
        
        lambdap,phip=float(entry6_1.get()),float(entry6_2.get())

        echelle13.set((float(entry6_1.get())))
        echelle14.set((float(entry6_2.get())))
        Valeur13.set(str(float(entry6_1.get())))
        Valeur14.set(str(float(entry6_2.get())))
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  

def g6et_coordonnees_geodesiques_locales():
  
    global Valeur13,Valeur14,entry6_3,entry6_4,entry6_5,canvas6,Mafenetre10,echelle13,echelle14
    try:
        
        lambdap,phip,DeltaXpq,DeltaYpq,DeltaZpq=float(Valeur13.get()),float(Valeur14.get()),float(entry6_3.get()),float(entry6_4.get()),float(entry6_5.get())#(alphapq,cpq,vpq)
        Az3,Av3,C3=transformation_geocentriques_geodesiques_locales(lambdap,phip,DeltaXpq,DeltaYpq,DeltaZpq)

        label7 = Label(Mafenetre10 ,text= 'alphapq Azimut Géodésique de la section Normale directe (°) :')
        label7.config(font=('Ink Free', 10))
        canvas6.create_window(200, 460, window=label7)
    
        label8 = Label(Mafenetre10, text= Az3 ,font=('Ink Free', 10, 'bold'))
        canvas6.create_window(200, 480, window=label8)

        label9 = Label(Mafenetre10 , text= 'Cpq Distance entre P et Q (m) :',font=('Ink Free', 10))
        canvas6.create_window(200, 500, window=label9)
    
        label10 = Label(Mafenetre10, text= Av3 ,font=('Ink Free', 10, 'bold'))
        canvas6.create_window(200, 520, window=label10)

        label11 = Label(Mafenetre10 , text= 'Vpq Angle Vertical vers Q selon le plan de la section normal directe (°) :',font=('Ink Free', 10))
        canvas6.create_window(200, 540, window=label11)
    
        label12 = Label(Mafenetre10, text= C3 ,font=('Ink Free', 10, 'bold'))
        canvas6.create_window(200, 560, window=label12)
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")
        
def g6et_coordonnees_geodesiques_locales2():
  
    global Valeur13,Valeur14,entry6_3,entry6_4,entry6_5,canvas6,Mafenetre10,echelle13,echelle14
    try:
        
         lambdap,phip,DeltaXpq,DeltaYpq,DeltaZpq=float(echelle13.get()),float(echelle14.get()),float(entry6_3.get()),float(entry6_4.get()),float(entry6_5.get())#(alphapq,cpq,vpq)
    
         Az3,Av3,C3=transformation_geocentriques_geodesiques_locales(lambdap,phip,DeltaXpq,DeltaYpq,DeltaZpq)

         label7 = Label(Mafenetre10 ,text= 'alphapq Azimut Géodésique de la section Normale directe (°) :')
         label7.config(font=('Ink Free', 10))
         canvas6.create_window(200, 460, window=label7)
    
         label8 = Label(Mafenetre10, text= Az3 ,font=('Ink Free', 10, 'bold'))
         canvas6.create_window(200, 480, window=label8)

         label9 = Label(Mafenetre10 , text= 'Cpq Distance entre P et Q (m) :',font=('Ink Free', 10))
         canvas6.create_window(200, 500, window=label9)
    
         label10 = Label(Mafenetre10, text= Av3 ,font=('Ink Free', 10, 'bold'))
         canvas6.create_window(200, 520, window=label10)

         label11 = Label(Mafenetre10 , text= 'Vpq Angle Vertical vers Q selon le plan de la section normal directe (°) :',font=('Ink Free', 10))
         canvas6.create_window(200, 540, window=label11)
    
         label12 = Label(Mafenetre10, text= C3 ,font=('Ink Free', 10, 'bold'))
         canvas6.create_window(200, 560, window=label12)
       
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
        
def lon_lat_interval6():
    
    global entry10_1,entry10_2
    
    Mafenetre11 = Tk()
    Mafenetre11.iconbitmap('Ressources/favicon.ico')
  
    Mafenetre11.title("lon_lat_interval")

    Label1 = Label(Mafenetre11, text = ' Veuillez entrez la valeur des esspacements :',font=('Ink Free', 14 ,'bold'),fg='#005994')
    Label1.pack()

    canvas = Canvas(Mafenetre11, width = 400, height = 300, relief = 'raised')
    canvas.pack()


    label2 = Label(Mafenetre11, text='lat_interval:')
    label2.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas.create_window(200, 110, window=label2)

    entry10_1 = Entry(Mafenetre11) 
    canvas.create_window(200, 140, window=entry10_1)

    label3 = Label(Mafenetre11, text='lon_interval:')
    label3.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas.create_window(200, 170, window=label3)

    entry10_2 = Entry(Mafenetre11) 
    canvas.create_window(200, 200, window=entry10_2)

    Bouton1 = Button(Mafenetre11, text = 'Show map', command =mapp6,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 10, 'bold'))
    Bouton1.pack()
    
    Bouton2 = Button(Mafenetre11, text = '?', command =openweb134_2,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Bouton2.pack()

    Mafenetre11.mainloop()

def mapp6():
    try:
        lon=Valeur14.get()
        lat=Valeur13.get()
        tooltip = 'Click me!'
        map = Map(location=[lon, lat], zoom_start=12 , tiles='Stamen Terrain')
        Marker([lon, lat], popup='<i>Mt. Hood Meadows</i>', tooltip=tooltip).add_to(map)
        lat_interval = int(entry10_1.get())
        lon_interval = int(entry10_2.get())
        grid = []

        for lat in range(-90, 91, lat_interval):
    
            grid.append([[lat, -180],[lat, 180]])
   
        for lon in range(-180, 181, lon_interval):
    
            grid.append([[-90, lon],[90, lon]])

        for g in grid:
      
             PolyLine(g, color="black", weight=0.5, opacity=0.5).add_to(map)
        map
        #######
        map.save('indexx.html')
        openweb3()
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  

## _____                _           _                    _                 _                                            _                                   _                          _                 _           
##|  __ \              | |         (_)                  | |               | |                                          | |                                 (_)                        | |               | |          
##| |  \/ ___  ___   __| | ___  ___ _  __ _ _   _  ___  | | ___   ___ __ _| | ___  ___  __   _____ _ __ ___    __ _ ___| |_ _ __ ___  _ __   ___  _ __ ___  _  __ _ _   _  ___  ___   | | ___   ___ __ _| | ___  ___ 
##| | __ / _ \/ _ \ / _` |/ _ \/ __| |/ _` | | | |/ _ \ | |/ _ \ / __/ _` | |/ _ \/ __| \ \ / / _ \ '__/ __|  / _` / __| __| '__/ _ \| '_ \ / _ \| '_ ` _ \| |/ _` | | | |/ _ \/ __|  | |/ _ \ / __/ _` | |/ _ \/ __|
##| |_\ \  __/ (_) | (_| |  __/\__ \ | (_| | |_| |  __/ | | (_) | (_| (_| | |  __/\__ \  \ V /  __/ |  \__ \ | (_| \__ \ |_| | | (_) | | | | (_) | | | | | | | (_| | |_| |  __/\__ \  | | (_) | (_| (_| | |  __/\__ \
## \____/\___|\___/ \__,_|\___||___/_|\__, |\__,_|\___| |_|\___/ \___\__,_|_|\___||___/   \_/ \___|_|  |___/  \__,_|___/\__|_|  \___/|_| |_|\___/|_| |_| |_|_|\__, |\__,_|\___||___/  |_|\___/ \___\__,_|_|\___||___/
##                                       | |                                                                                                                     | |                                                
##                                       |_|                                                                                                                     |_|                                               
##


def transformation_Geodesique_locales_vers_astronomiques_locales(Ap,Op,lambdap,phip,rpq,spq,tpq):
     
     Ap=degree2radians(Ap)
     Op=degree2radians(Op)
     lambdap=degree2radians(lambdap)
     phip=degree2radians(phip)
     a=rpq
     b=spq
     c=tpq
     upq=a-(Ap-lambdap)*sin(Op)*b-(Op-phip)*c
     vpq=b+a*(Ap-lambdap)*sin(Op)-(Ap-lambdap)*cos(Op)
     wpq=a*(Op-phip)+(Ap-lambdap)*cos(Op)+c
     
     return radians2degree(upq),radians2degree(vpq),radians2degree(wpq)

def  Geodesique_locales_vers_astronomiques_locales():
    
    global entry1_12,entry2_12,entry3_12,entry4_12,entry5_12,canvas7,Mafenetre12,entry6_12,entry7_12
    
    Mafenetre12 = Tk()
    Mafenetre12.geometry('600x730')
    Mafenetre12.iconbitmap('Ressources/favicon.ico')
    Mafenetre12.title('Geodesique_locales_vers_astronomiques_locales')

    canvas7 = Canvas(Mafenetre12, width = 400, height = 690, relief = 'raised')
    canvas7.pack()

    label1= Label(Mafenetre12, text='Transformation entre coordonnees:\n Géodesique locales vers Astronomiques locales')
    label1.config(font=('Ink Free', 14 ,'bold'),fg='#005994')
    canvas7.create_window(200, 25, window=label1)

    label2 = Label(Mafenetre12, text='Ap longitude astronomique locale du point P (°) :')
    label2.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas7.create_window(200, 110, window=label2)

    entry1_12 = Entry(Mafenetre12) 
    canvas7.create_window(200, 140, window=entry1_12)

    label3 = Label(Mafenetre12, text='Op latitude astronomique du point P (°) :')
    label3.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas7.create_window(200, 170, window=label3)

    entry2_12 = Entry(Mafenetre12) 
    canvas7.create_window(200, 200, window=entry2_12)

    label4 = Label(Mafenetre12, text='La longitude Lambdap (°) :')
    label4.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas7.create_window(200, 230, window=label4)

    entry3_12 = Entry(Mafenetre12) 
    canvas7.create_window(200, 260, window=entry3_12)

    label5 = Label(Mafenetre12, text='La latitude Phip (°)')
    label5.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas7.create_window(200, 290, window=label5)

    entry4_12 = Entry(Mafenetre12) 
    canvas7.create_window(200, 320, window=entry4_12)

    label6 = Label(Mafenetre12, text='Rpq :')
    label6.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas7.create_window(200, 350, window=label6)

    entry5_12 = Entry(Mafenetre12) 
    canvas7.create_window(200, 380, window=entry5_12)

    label7 = Label(Mafenetre12, text='Spq ')
    label7.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas7.create_window(200, 410, window=label7)

    entry6_12 = Entry(Mafenetre12) 
    canvas7.create_window(200, 440, window=entry6_12)

    label7 = Label(Mafenetre12, text='Tpq ')
    label7.config(font=('Ink Free', 10 ,'bold'),fg='#005994')
    canvas7.create_window(200, 470, window=label7)

    entry7_12 = Entry(Mafenetre12) 
    canvas7.create_window(200, 500, window=entry7_12)

    button1 = Button(Mafenetre12,text='Transformer', command = get_coordonnees_astronomiques_locales ,bg='#3498DB',fg='#FDFEFE', font=('Ink Free', 9, 'bold'))
    canvas7.create_window(200, 530, window=button1)
    
    Btn = Button(Mafenetre12, text = "Consulter Google earth",command=openweb,bg='#3498DB',fg='#FDFEFE',font=('Ink Free', 9, 'bold'))
    Btn.pack(side=BOTTOM)
    
 
    Mafenetre12.mainloop()


    
def get_coordonnees_astronomiques_locales():
    
    global entry1_12,entry2_12,entry3_12,entry4_12,entry5_12,canvas7,Mafenetre12,entry6_12,entry7_12
    try:
        
        Ap,Op,lambdap,phip,rpq,spq,tpq=float(entry1_12.get()),float(entry2_12.get()),float(entry3_12.get()),float(entry4_12.get()),float(entry5_12.get()),float(entry6_12.get()),float(entry7_12.get())
        Lambda2,Phi2,h=transformation_Geodesique_locales_vers_astronomiques_locales(Ap,Op,lambdap,phip,rpq,spq,tpq)
    
        label7 = Label(Mafenetre12, text= 'Upq (°) :',font=('Ink Free', 10))
        canvas7.create_window(200, 570, window=label7)
    
        label8 = Label(Mafenetre12, text= '%.5E'% Decimal(Lambda2) ,font=('Ink Free', 10, 'bold'))
        canvas7.create_window(200, 590, window=label8)

        label9 = Label(Mafenetre12, text= 'Vpq Angle Vertical vers Q selon le plan de la section normal directe (°)  :',font=('Ink Free', 10))
        canvas7.create_window(200, 610, window=label9)

        label10 = Label(Mafenetre12, text= '%.5E'% Decimal(Phi2) ,font=('Ink Free', 10, 'bold'))
        canvas7.create_window(200, 630, window=label10)

        label11 = Label( Mafenetre12,text= 'Wpq (°) :',font=('Ink Free', 10))
        canvas7.create_window(200, 650, window=label11)
    
        label12 = Label(Mafenetre12, text= '%.5E'% Decimal(h) ,font=('Ink Free', 10, 'bold'))
        canvas7.create_window(200, 670, window=label12)
    
    except:
        messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  


    
##                                                                                                     _                         
##                                                                                         /\/\   __ _(_)_ __                    
##                                                                      _____ _____ _____ /    \ / _` | | '_ \ _____ _____ _____ 
##                                                                     |_____|_____|_____/ /\/\ \ (_| | | | | |_____|_____|_____|
##                                                                                       \/    \/\__,_|_|_| |_|                  


from tkinter import Tk,Canvas,Label,StringVar,Scale,HORIZONTAL,Entry,Button,BOTTOM,font,PhotoImage,END,NE,messagebox
from math import sqrt,cos,atan,pi,sin,asin
import webbrowser
from decimal import Decimal
from folium import Map,Marker,PolyLine
from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk


new = 2

url='https://www.google.com/intl/fr/earth/'

ur3='indexx.html'

ur1_2='image_illustrative.jpg'

helpurl='How to use the application.pptx'

def set_text(Entry,text):   
    Entry.delete(0,END)
    Entry.insert(0,text)
    return

def Help():
    webbrowser.open(helpurl,new=new)
    
def openweb():
    webbrowser.open(url,new=new)

def openweb3():
    webbrowser.open(ur3,new=new)

def openweb134_2():
    webbrowser.open(ur1_2,new=new)
   
def degree2radians(degree):
  # convert degrees to radians
  return degree*(pi/180)

def radians2degree(radians):
  # convert  radians to degrees
  return radians*(180/pi)

def close():
    Mafenetre0.destroy()
    root = Tk()
    l = AnimatedGIF(root, "Ressources/Earth.gif")
    l.pack()
    root.after(7000, lambda: root.destroy()) # Destroy the widget after 30 seconds
    root.overrideredirect(True)
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)-300
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)-200
 
# Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.mainloop()


    
class AnimatedGIF(Label, object):
    def __init__(self, master, path, forever=True):
        self._master = master
        self._loc = 0
        self._forever = forever

        self._is_running = False

        im = Image.open(path)
        self._frames = []
        i = 0
        try:
            while True:
                photoframe = ImageTk.PhotoImage(im.copy().convert('RGBA'))
                self._frames.append(photoframe)

                i += 1
                im.seek(i)
        except EOFError: pass
        
        self._last_index = len(self._frames) - 1

        try:
            self._delay = im.info['duration']
        except:
            self._delay = 100

        self._callback_id = None

        super(AnimatedGIF, self).__init__(master, image=self._frames[0])

    def start_animation(self, frame=None):
        if self._is_running: return

        if frame is not None:
            self._loc = 0
            self.configure(image=self._frames[frame])

        self._master.after(self._delay, self._animate_GIF)
        self._is_running = True

    def stop_animation(self):
        if not self._is_running: return

        if self._callback_id is not None:
            self.after_cancel(self._callback_id)
            self._callback_id = None

        self._is_running = False

    def _animate_GIF(self):
        self._loc += 1
        self.configure(image=self._frames[self._loc])

        if self._loc == self._last_index:
            if self._forever:
                self._loc = 0
                self._callback_id = self._master.after(self._delay, self._animate_GIF)
            else:
                self._callback_id = None
                self._is_running = False
        else:
            self._callback_id = self._master.after(self._delay, self._animate_GIF)

    def pack(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).pack(**kwargs)

    def grid(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).grid(**kwargs)
        
    def place(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).place(**kwargs)
        
    def pack_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).pack_forget(**kwargs)

    def grid_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).grid_forget(**kwargs)
        
    def place_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).place_forget(**kwargs)


root = Tk()
l = AnimatedGIF(root, "Ressources/intro.gif")
l.pack()

root.after(8000, lambda: root.destroy()) # Destroy the widget after 30 seconds
root.overrideredirect(True)
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)-300
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)-200
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))
root.mainloop()

root.mainloop()

Mafenetre0= Tk()

Mafenetre0.title('GEODESY PROJECT')
Mafenetre0.geometry('800x600')

Mafenetre0.config(background='#F7F9F9')

x1=Button(Mafenetre0)
photo1=PhotoImage(file="Ressources/close.png")
x1.config(image=photo1,width="20",height="20",activebackground="#F7F9F9",bg="#F7F9F9", bd=0,command=close)
x1.place(relx=1,x=-15, y=15, anchor=NE)

x2=Button(Mafenetre0)
photo2=PhotoImage(file="Ressources/HELP.png")
x2.config(image=photo2,width="20",height="25",activebackground="#F7F9F9",bg="#F7F9F9", bd=0,command=Help)
x2.place(relx=1,x=-50, y=15, anchor=NE)

label_title=Label(Mafenetre0,text="La Géodésie Géométrique",font=('Ink Free', 20 ,'bold'),fg='#4E95F8',bg='#F7F9F9')##,bg='#8EF0F0',fg='#6C91BB'
label_title.pack()
label_subtitle=Label(Mafenetre0,text=" Transformation entre système de coordonnées : \n Veuillez choisir la nature de la transformation :  :",font=('Ink Free',15),bg='#F7F9F9',fg='#A6ACAF')##bg='#8EF0F0',fg='#285D97'
label_subtitle.pack()

Bouton1 = Button(Mafenetre0, text = ' Géodésiques vers Géocentriques :',width=40, command = Geodesiques_vers_geocentriques,bg='#3498DB',fg='#FDFEFE')##,bg='#91ACCA'
Bouton1['font']=font.Font(family='Ink Free',size=24,weight='bold')
Bouton1.pack(expand='YES')

Bouton2 = Button(Mafenetre0, text = ' Géocentriques vers Géodésiques :',width=40, command = geocentriques_vers_Geodesiques,bg='#3498DB',fg='#FDFEFE')
Bouton2['font']=font.Font(family='Ink Free',size=24,weight='bold')
Bouton2.pack(expand='YES')

Bouton3 = Button(Mafenetre0, text = 'Géocentriques vers Astronomiques locales :',width=40 ,command = Geocentrique_vers_Astronomique,bg='#3498DB',fg='#FDFEFE')
Bouton3['font']=font.Font(family='Ink Free',size=24,weight='bold')
Bouton3.pack(expand='YES')

Bouton4 = Button(Mafenetre0, text = ' Astronomiques locales vers Géocentriques : ',width=40, command =Astronomique_vers_Geocentrique,bg='#3498DB',fg='#FDFEFE')
Bouton4['font']=font.Font(family='Ink Free',size=24,weight='bold')
Bouton4.pack(expand='YES')

Bouton5 = Button(Mafenetre0, text = ' Géodesique locale vers Géocentrique : ',width=40, command =geodesique_locales_vers_Geocentrique,bg='#3498DB',fg='#FDFEFE')
Bouton5['font']=font.Font(family='Ink Free',size=24,weight='bold')
Bouton5.pack(expand='YES')

Bouton6 = Button(Mafenetre0, text = ' Géocentrique vers Géodesique locale : ',width=40, command =geocentriques_geodesiques_locales,bg='#3498DB',fg='#FDFEFE')
Bouton6['font']=font.Font(family='Ink Free',size=24,weight='bold')
Bouton6.pack(expand='YES')

Bouton7 = Button(Mafenetre0, text = ' Géodesique locale vers Astronomiques locales: ',width=40, command =Geodesique_locales_vers_astronomiques_locales,bg='#3498DB',fg='#FDFEFE')
Bouton7['font']=font.Font(family='Ink Free',size=24,weight='bold')
Bouton7.pack(expand='YES')

Mafenetre0.overrideredirect(True)
windowWidth = Mafenetre0.winfo_reqwidth()
windowHeight = Mafenetre0.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(Mafenetre0.winfo_screenwidth()/2 - windowWidth/2)-300
positionDown = int(Mafenetre0.winfo_screenheight()/2 - windowHeight/2)-200
 
# Positions the window in the center of the page.
Mafenetre0.geometry("+{}+{}".format(positionRight, positionDown))
Mafenetre0.mainloop()



##                                                                            ╔═╗┌─┐┌─┐┌┬┐┌─┐┌─┐┬ ┬  ╔═╗┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐       
##                                                                            ║ ╦├┤ │ │ ││├┤ └─┐└┬┘  ╠═╝├┬┘│ │ │├┤ │   │        
##                                                                            ╚═╝└─┘└─┘─┴┘└─┘└─┘ ┴   ╩  ┴└─└─┘└┘└─┘└─┘ ┴        
##                                                                                                                              
##                                               _  _        _  _ ___ _        _ \ /___ _                                       
##                                              |_)/ \| ||V||_||_| _/|_|   |_||_| Y  | |_||V|                                   
##                                              |_)\_/|_|| || || |/__| |   | || | |  | | || |                                   
##                                                                                                                              
##                                               _  _    ___ __ __ _     _  __          _  __ _____ _  _                        
##                                              |_)/ \| | | (_ (_ / \| || \|_ |\|   |\||_|(_ (_  | |_)|_|                       
##                                              |_)\_/|_|_|___)__)\_/|_||_/|__| |   | || |__)__)_|_| \| |                       
##                                                                                                                              
##                                                                                                                              
##                                              |V| _ |_  _ __  _| o    |V| _  _     |  _  o __  o __  _    |V| _ |_  _ __  _| o
##                                              | |(_)| |(_||||(_| |    | |(_|(_)|_| | (_| | | | | | |(/_   | |(_)| |(_||||(_| |
##                                                                                                                              
##                                               __       _ ______ _ ___       _     _     _____    __                          
##                                              |_ |\||\||_| |  | / \ |    |  |_||_|/ \| |/   | |\||_                           
##                                              |__| || || | | _|_\_X_|_   |__| || |\_/|_|\___|_| ||__                          
##                                                                                                                              
##                                                  _        _ ___       _     _     _                                          
##                                              |V|/ \| ||_|| \ |    |  / \| ||_)|\||_|                                         
##                                              | |\_/|_|| ||_/_|_   |__\_/|_||_)| || |                                         
##                                                                                                                              
##                                                                    _     _  _     __   ___    _                              
##                                              |  |_||_||V|| \/ \| |/  |_| |    | \ __ o  _  _                                 
##                                              |__| || || ||_/\_/|_|\__| |_|_   |_/ |  | _> _>                                 
##                                                                                                                              
##                                              ╔═╗┬  ┬┌─┐┬─┐┌─┐┌─┐┌─┐┌┐┌  ┌┐ ┬ ┬  ╦═╗┌─┐┌┬┐┌─┐  ╦ ╦┌─┐┌─┐┌─┐┌─┐┬ ┬┌┐ ┬         
##                                              ║ ║└┐┌┘├┤ ├┬┘└─┐├┤ ├┤ │││  ├┴┐└┬┘  ╠╦╝├┤  ││├─┤  ╚╦╝├─┤├─┤│ ┬│ ││ │├┴┐│         
##                                              ╚═╝ └┘ └─┘┴└─└─┘└─┘└─┘┘└┘  └─┘ ┴   ╩╚═└─┘─┴┘┴ ┴   ╩ ┴ ┴┴ ┴└─┘└─┘└─┘└─┘┴         
