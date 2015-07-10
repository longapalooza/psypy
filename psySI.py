import convert as c
import math as m

def Pws(DBT):
    if valid_DBT(DBT):
        C8=-5.8002206*10**3
        C9=1.3914993
        C10=-4.8640239*10**-2
        C11=4.1764768*10**-5
        C12=1.4452093*10**-8
        C13=6.5459673
        return m.exp(C8/DBT+C9+C10*DBT+C11*DBT**2+C12*DBT**3+C13*m.log(DBT))

def W_DBT_RH_P(DBT,RH,P):
    if valid_DBT(DBT):
        Pws=RH*Pws(DBT)
        return 0.621945*Pws/(P-Pws)

def valid_DBT(DBT):
    if 0<DBT<200:
        return TRUE
    else:
        return FALSE
