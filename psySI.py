import math as m

# All functions expect base SI units for any arguments given
# DBT   - Dry bulb temperature          - Kelvins, K
# DPT   - Dew point temperature         - Kelvins, K
# H     - Specific enthalpy             - kiloJoules per kilogram, kJ/kg
# P     - Atmospheric pressure          - Pascals, Pa
# Pw    - Water vapor partial pressure  - Pascals, Pa
# RH    - Relative humidity             - Decimal (i.e. not a percentage)
# V     - Specific volume               - Cubic meters per kilogram, m^3/kg
# W     - Humidity ratio                - kilograms per kilograms, kg/kg
# WBT   - Wet bulb temperature          - Kelvins, K

def DBT_H_RH_P(H, RH, P):
    DBTa=273.15
    DBTb=473.15
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>0.0005:
        ya=W_DBT_RH_P(DBTa, RH, P)-W_DBT_H(DBTa, H)
        y=W_DBT_RH_P(DBT, RH, P)-W_DBT_H(DBT, H)
        if is_positive(y)==is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def DBT_H_V_P(H, V, P):
    DBTa=273.15
    DBTb=473.15
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>0.0005:
        ya=W_DBT_V_P(DBTa, V, P)-W_DBT_H(DBTa, H)
        y=W_DBT_V_P(DBT, V, P)-W_DBT_H(DBT, H)
        if is_positive(y)==is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def DBT_H_W(H, W):
    DBTa=273.15
    DBTb=473.15
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>0.0005:
        ya=W-W_DBT_H(DBTa, H)
        y=W-W_DBT_H(DBT, H)
        if is_positive(y)==is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def DBT_H_WBT_P(H, WBT, P):
    DBTa=273.15
    DBTb=473.15
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>0.0005:
        ya=W_DBT_WBT_P(DBTa, WBT, P)-W_DBT_H(DBTa, H)
        y=W_DBT_WBT_P(DBT, WBT, P)-W_DBT_H(DBT, H)
        if is_positive(y)==is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def DBT_RH_V_P(RH, V, P):
    DBTa=273.15
    DBTb=473.15
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>0.0005:
        ya=W_DBT_RH_P(DBTa, RH, P)-W_DBT_V_P(DBTa, V, P)
        y=W_DBT_RH_P(DBT, RH, P)-W_DBT_V_P(DBT, V, P)
        if is_positive(y)==is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def DBT_RH_W_P(RH, W, P):
    DBTa=273.15
    DBTb=473.15
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>0.0005:
        ya=W_DBT_RH_P(DBTa, RH, P)-W
        y=W_DBT_RH_P(DBT, RH, P)-W
        if is_positive(y)==is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def DBT_RH_WBT_P(RH, WBT, P):
    DBTa=273.15
    DBTb=473.15
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>0.0005:
        ya=W_DBT_WBT_P(DBTa, WBT, P)-W_DBT_RH_P(DBTa, RH, P)
        y=W_DBT_WBT_P(DBT, WBT, P)-W_DBT_RH_P(DBT, RH, P)
        if is_positive(y)==is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def DBT_V_W_P(V, W, P):
    DBTa=273.15
    DBTb=473.15
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>0.0005:
        ya=W-W_DBT_V_P(DBTa, V, P)
        y=W-W_DBT_V_P(DBT, V, P)
        if is_positive(y)==is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def DBT_V_WBT_P(V, WBT, P):
    DBTa=273.15
    DBTb=473.15
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>0.0005:
        ya=W_DBT_WBT_P(DBTa, WBT, P)-W_DBT_V_P(DBTa, V, P)
        y=W_DBT_WBT_P(DBT, WBT, P)-W_DBT_V_P(DBT, V, P)
        if is_positive(y)==is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def DBT_W_WBT_P(W, WBT, P):
    DBTa=273.15
    DBTb=473.15
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>0.0005:
        ya=W_DBT_WBT_P(DBTa, WBT, P)-W
        y=W_DBT_WBT_P(DBT, WBT, P)-W
        if is_positive(y)==is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

# ASHRAE 2009 Chapter 1 Equation 39
def DPT_Pw(Pw):
    Pw=Pw/1000
    C14=6.54
    C15=14.529
    C16=0.7389
    C17=0.09486
    C18=0.4569
    a=m.log(Pw)
    return (C14+C15*a+C16*a**2+C17*a**3+C18*Pw**0.1984)+273.15

# ASHRAE 2009 Chapter 1 Equation 32
def H_DBT_W(DBT, W):
    if valid_DBT(DBT):
        DBT=DBT-273.15
        return 1.006*DBT+W*(2501+1.86*DBT)

def is_positive(x):
    if x>0:
        return True
    else:
        return False

# ASHRAE 2009 Chapter 1 Equation 22
def Pw_W_P(W, P):
    return W*P/(W+0.621945)

# ASHRAE 2009 Chapter 1 Equation 6
def Pws(DBT):
    if valid_DBT(DBT):
        C8=-5.8002206*10**3
        C9=1.3914993
        C10=-4.8640239*10**-2
        C11=4.1764768*10**-5
        C12=-1.4452093*10**-8
        C13=6.5459673
        return m.exp(C8/DBT+C9+C10*DBT+C11*DBT**2+C12*DBT**3+C13*m.log(DBT))

def state(prop1, prop1val, prop2, prop2val,P):
    if prop1==prop2:
        print("Properties must be independent.")
        return
    prop=["DBT","WBT","RH","W","V","H"]
    if prop1 not in prop or prop2 not in prop:
        print("Valid property must be given.")
        return
    prop1i=prop.index(prop1)
    prop2i=prop.index(prop2)
    if prop1i<prop2i:
        cd1=prop1
        cd1val=prop1val
        cd2=prop2
        cd2val=prop2val
    else:
        cd1=prop2
        cd1val=prop2val
        cd2=prop1
        cd2val=prop1val
    if cd1=="DBT":
        DBT=cd1val
        if cd2=="WBT":
            WBT=cd2val
            W=W_DBT_WBT_P(DBT, WBT, P)
            H=H_DBT_W(DBT, W)
            RH=RH_DBT_W_P(DBT, W, P)
            V=V_DBT_W_P(DBT, W, P)
        elif cd2=="RH":
            RH=cd2val
            W=W_DBT_RH_P(DBT, RH, P)
            H=H_DBT_W(DBT, W)
            V=V_DBT_W_P(DBT, W, P)
            WBT=WBT_DBT_W_P(DBT, W, P)
        elif cd2=="W":
            W=cd2val
            H=H_DBT_W(DBT, W)
            RH=RH_DBT_W_P(DBT, W, P)
            V=V_DBT_W_P(DBT, W, P)
            WBT=WBT_DBT_W_P(DBT, W, P)
        elif cd2=="V":
            V=cd2val
            W=W_DBT_V_P(DBT, V, P)
            H=H_DBT_W(DBT, W)
            RH=RH_DBT_W_P(DBT, W, P)
            WBT=WBT_DBT_W_P(DBT, W, P)
        elif cd2=="H":
            H=cd2val
            W=W_DBT_H(DBT, H)
            RH=RH_DBT_W_P(DBT, W, P)
            V=V_DBT_W_P(DBT, W, P)
            WBT=WBT_DBT_W_P(DBT, W, P)
    elif cd1=="WBT":
        WBT=cd1val
        if cd2=="RH":
            RH=cd2val
            DBT=DBT_RH_WBT_P(RH, WBT, P)
            W=W_DBT_RH_P(DBT, RH, P)
            H=H_DBT_W(DBT, W)
            V=V_DBT_W_P(DBT, W, P)
        elif cd2=="W":
            W=cd2val
            DBT=DBT_W_WBT_P(W, WBT, P)
            H=H_DBT_W(DBT, W)
            RH=RH_DBT_W_P(DBT, W, P)
            V=V_DBT_W_P(DBT, W, P)
        elif cd2=="V":
            V=cd2val
            DBT=DBT_V_WBT_P(V, WBT, P)
            W=W_DBT_V_P(DBT, V, P)
            H=H_DBT_W(DBT, W)
            RH=RH_DBT_W_P(DBT, W, P)
        elif cd2=="H":
            H=cd2val
            DBT=DBT_H_WBT_P(H, WBT, P)
            W=W_DBT_H(DBT, H)
            RH=RH_DBT_W_P(DBT, W, P)
            V=V_DBT_W_P(DBT, W, P)
    elif cd1=="RH":
        RH=cd1val
        if cd2=="W":
            W=cd2val
            DBT=DBT_RH_W_P(RH, W, P)
            H=H_DBT_W(DBT, W)
            V=V_DBT_W_P(DBT, W, P)
            WBT=WBT_DBT_W_P(DBT, W, P)
        elif cd2=="V":
            V=cd2val
            DBT=DBT_RH_V_P(RH, V, P)
            W=W_DBT_RH_P(DBT, RH, P)
            H=H_DBT_W(DBT, W)
            WBT=WBT_DBT_W_P(DBT, W, P)
        elif cd2=="H":
            H=cd2val
            DBT=DBT_H_RH_P(H, RH, P)
            W=W_DBT_RH_P(DBT, RH, P)
            V=V_DBT_W_P(DBT, W, P)
            WBT=WBT_DBT_W_P(DBT, W, P)
    elif cd1=="W":
        W=cd1val
        if cd2=="V":
            V=cd2val
            DBT=DBT_V_W_P(V, W, P)
            H=H_DBT_W(DBT, W)
            RH=RH_DBT_W_P(DBT, W, P)
            WBT=WBT_DBT_W_P(DBT, W, P)
        elif cd2=="H":
            H=cd2val
            DBT=DBT_H_W(H, W)
            RH=RH_DBT_W_P(DBT, W, P)
            V=V_DBT_W_P(DBT, W, P)
            WBT=WBT_DBT_W_P(DBT, W, P)
    elif cd1=="V":
        V=cd1val
        H=cd2val
        DBT=DBT_H_V_P(H, V, P)
        W=W_DBT_V_P(DBT, V, P)
        RH=RH_DBT_W_P(DBT, W, P)
        WBT=WBT_DBT_W_P(DBT, W, P)
    return [DBT, H, RH, V, W, WBT]

# ASHRAE 2009 Chapter 1 Equation 22 and Equation 24
def RH_DBT_W_P(DBT, W, P):
    if valid_DBT(DBT):
        return W*P/((0.621945+W)*Pws(DBT))

# ASHRAE 2009 Chapter 1 Equation 28
def V_DBT_W_P(DBT, W, P):
    if valid_DBT(DBT):
        return 287.042*DBT*(1+1.607858*W)/P

# ASHRAE 2009 Chapter 1 Equation 32
def W_DBT_H(DBT, H):
    if valid_DBT(DBT):
        DBT=DBT-273.15
        return (H-1.006*DBT)/(2501+1.86*DBT)

# ASHRAE 2009 Chapter 1 Equation 22 and Equation 24
def W_DBT_RH_P(DBT, RH, P):
    if valid_DBT(DBT):
        Pw=RH*Pws(DBT)
        return 0.621945*Pw/(P-Pw)

# ASHRAE 2009 Chapter 1 Equation 28
def W_DBT_V_P(DBT, V, P):
    if valid_DBT(DBT):
        return (P*V-287.042*DBT)/(1.607858*287.042*DBT)

# ASHRAE 2009 Chapter 1 Equation 35
def W_DBT_WBT_P(DBT, WBT, P):
    if valid_DBT(DBT):
        DBT=DBT-273.15
        WBT=WBT-273.15
        return ((2501-2.326*WBT)*W_DBT_RH_P(WBT+273.15,1,P)-1.006*(DBT-WBT))/\
               (2501+1.86*DBT-4.186*WBT)

# ASHRAE 2009 Chapter 1 Equation 35
def WBT_DBT_W_P(DBT, W, P):
    if valid_DBT(DBT):
        WBTa=DPT_Pw(Pw_W_P(W, P))
        WBTb=DBT
        WBT=(WBTa+WBTb)/2
        while WBTb-WBTa>0.0005:
            Ws=W_DBT_WBT_P(DBT, WBT, P)
            if W>Ws:
                WBTa=WBT
            else:
                WBTb=WBT
            WBT=(WBTa+WBTb)/2
        return WBT

def valid_DBT(DBT):
    if 273.15<=DBT<=473.15:
        return True
    else:
        return False
