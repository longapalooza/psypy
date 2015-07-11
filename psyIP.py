import math as m

# All functions expect base SI units for any arguments given
# DBT   - Dry bulb temperature          - Degrees Rankine, R
# DPT   - Dew point temperature         - Degress Rankine, R
# H     - Specific enthalpy             - British thermal unit per pound mass,
#                                         Btu/lbm
# P     - Atmospheric pressure          - Pounds force per square inch, psi
# Pw    - Water vapor partial pressure  - Pounds force per square inch, psi
# RH    - Relative humidity             - Decimal (i.e. not a percentage)
# V     - Specific volume               - Cubic feet per pound mass, ft^3/lbm
# W     - Humidity ratio                - pounds mass per pound mass, lbm/lbm
# WBT   - Wet bulb temperature          - Degrees Rankine, R

# Minimum dry bulb temperature
Min_DBT=491.67
# Maximum dry bulb temperature
Max_DBT=851.67
# Convergence tolerance
TOL=0.0000005

def __DBT_H_RH_P(H, RH, P):
    [DBTa, DBTb]=[Min_DBT, Max_DBT]
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>TOL:
        ya=__W_DBT_RH_P(DBTa, RH, P)-__W_DBT_H(DBTa, H)
        y=__W_DBT_RH_P(DBT, RH, P)-__W_DBT_H(DBT, H)
        if __is_positive(y)==__is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def __DBT_H_V_P(H, V, P):
    [DBTa, DBTb]=[Min_DBT, Max_DBT]
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>TOL:
        ya=__W_DBT_V_P(DBTa, V, P)-__W_DBT_H(DBTa, H)
        y=__W_DBT_V_P(DBT, V, P)-__W_DBT_H(DBT, H)
        if __is_positive(y)==__is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def __DBT_H_W(H, W):
    [DBTa, DBTb]=[Min_DBT, Max_DBT]
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>TOL:
        ya=W-__W_DBT_H(DBTa, H)
        y=W-__W_DBT_H(DBT, H)
        if __is_positive(y)==__is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def __DBT_H_WBT_P(H, WBT, P):
    [DBTa, DBTb]=[Min_DBT, Max_DBT]
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>TOL:
        ya=__W_DBT_WBT_P(DBTa, WBT, P)-__W_DBT_H(DBTa, H)
        y=__W_DBT_WBT_P(DBT, WBT, P)-__W_DBT_H(DBT, H)
        if __is_positive(y)==__is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def __DBT_RH_V_P(RH, V, P):
    [DBTa, DBTb]=[Min_DBT, Max_DBT]
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>TOL:
        ya=__W_DBT_RH_P(DBTa, RH, P)-__W_DBT_V_P(DBTa, V, P)
        y=__W_DBT_RH_P(DBT, RH, P)-__W_DBT_V_P(DBT, V, P)
        if __is_positive(y)==__is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def __DBT_RH_W_P(RH, W, P):
    [DBTa, DBTb]=[Min_DBT, Max_DBT]
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>TOL:
        ya=__W_DBT_RH_P(DBTa, RH, P)-W
        y=__W_DBT_RH_P(DBT, RH, P)-W
        if __is_positive(y)==__is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def __DBT_RH_WBT_P(RH, WBT, P):
    [DBTa, DBTb]=[Min_DBT, Max_DBT]
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>TOL:
        ya=__W_DBT_WBT_P(DBTa, WBT, P)-__W_DBT_RH_P(DBTa, RH, P)
        y=__W_DBT_WBT_P(DBT, WBT, P)-__W_DBT_RH_P(DBT, RH, P)
        if __is_positive(y)==__is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def __DBT_V_W_P(V, W, P):
    [DBTa, DBTb]=[Min_DBT, Max_DBT]
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>TOL:
        ya=W-__W_DBT_V_P(DBTa, V, P)
        y=W-__W_DBT_V_P(DBT, V, P)
        if __is_positive(y)==__is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def __DBT_V_WBT_P(V, WBT, P):
    [DBTa, DBTb]=[Min_DBT, Max_DBT]
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>TOL:
        ya=__W_DBT_WBT_P(DBTa, WBT, P)-__W_DBT_V_P(DBTa, V, P)
        y=__W_DBT_WBT_P(DBT, WBT, P)-__W_DBT_V_P(DBT, V, P)
        if __is_positive(y)==__is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

def __DBT_W_WBT_P(W, WBT, P):
    [DBTa, DBTb]=[Min_DBT, Max_DBT]
    DBT=(DBTa+DBTb)/2
    while DBTb-DBTa>TOL:
        ya=__W_DBT_WBT_P(DBTa, WBT, P)-W
        y=__W_DBT_WBT_P(DBT, WBT, P)-W
        if __is_positive(y)==__is_positive(ya):
            DBTa=DBT
        else:
            DBTb=DBT
        DBT=(DBTa+DBTb)/2
    return DBT

# ASHRAE 2009 Chapter 1 Equation 39
def __DPT_Pw(Pw):
    Pw=Pw
    C14=100.45
    C15=33.193
    C16=2.319
    C17=0.17074
    C18=1.2063
    a=m.log(Pw)
    return (C14+C15*a+C16*a**2+C17*a**3+C18*Pw**0.1984)+459.67

# ASHRAE 2009 Chapter 1 Equation 32
def __H_DBT_W(DBT, W):
    if __valid_DBT(DBT):
        DBT=DBT-459.67
        return 0.240*DBT+W*(1061+0.444*DBT)

def __is_positive(x):
    if x>0:
        return True
    else:
        return False

# ASHRAE 2009 Chapter 1 Equation 22
def __Pw_W_P(W, P):
    return W*P/(W+0.621945)

# ASHRAE 2009 Chapter 1 Equation 6
def __Pws(DBT):
    if __valid_DBT(DBT):
        C8=-1.0440397*10**4
        C9=-1.1294650*10**1
        C10=-2.7022355*10**-2
        C11=1.2890360*10**-5
        C12=-2.4780681*10**-9
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
            W=__W_DBT_WBT_P(DBT, WBT, P)
            H=__H_DBT_W(DBT, W)
            RH=__RH_DBT_W_P(DBT, W, P)
            V=__V_DBT_W_P(DBT, W, P)
        elif cd2=="RH":
            RH=cd2val
            W=__W_DBT_RH_P(DBT, RH, P)
            H=__H_DBT_W(DBT, W)
            V=__V_DBT_W_P(DBT, W, P)
            WBT=__WBT_DBT_W_P(DBT, W, P)
        elif cd2=="W":
            W=cd2val
            H=__H_DBT_W(DBT, W)
            RH=__RH_DBT_W_P(DBT, W, P)
            V=__V_DBT_W_P(DBT, W, P)
            WBT=__WBT_DBT_W_P(DBT, W, P)
        elif cd2=="V":
            V=cd2val
            W=__W_DBT_V_P(DBT, V, P)
            H=__H_DBT_W(DBT, W)
            RH=__RH_DBT_W_P(DBT, W, P)
            WBT=__WBT_DBT_W_P(DBT, W, P)
        elif cd2=="H":
            H=cd2val
            W=__W_DBT_H(DBT, H)
            RH=__RH_DBT_W_P(DBT, W, P)
            V=__V_DBT_W_P(DBT, W, P)
            WBT=__WBT_DBT_W_P(DBT, W, P)
    elif cd1=="WBT":
        WBT=cd1val
        if cd2=="RH":
            RH=cd2val
            DBT=__DBT_RH_WBT_P(RH, WBT, P)
            W=__W_DBT_RH_P(DBT, RH, P)
            H=__H_DBT_W(DBT, W)
            V=__V_DBT_W_P(DBT, W, P)
        elif cd2=="W":
            W=cd2val
            DBT=__DBT_W_WBT_P(W, WBT, P)
            H=__H_DBT_W(DBT, W)
            RH=__RH_DBT_W_P(DBT, W, P)
            V=__V_DBT_W_P(DBT, W, P)
        elif cd2=="V":
            V=cd2val
            DBT=__DBT_V_WBT_P(V, WBT, P)
            W=__W_DBT_V_P(DBT, V, P)
            H=__H_DBT_W(DBT, W)
            RH=__RH_DBT_W_P(DBT, W, P)
        elif cd2=="H":
            H=cd2val
            DBT=__DBT_H_WBT_P(H, WBT, P)
            W=__W_DBT_H(DBT, H)
            RH=__RH_DBT_W_P(DBT, W, P)
            V=__V_DBT_W_P(DBT, W, P)
    elif cd1=="RH":
        RH=cd1val
        if cd2=="W":
            W=cd2val
            DBT=__DBT_RH_W_P(RH, W, P)
            H=__H_DBT_W(DBT, W)
            V=__V_DBT_W_P(DBT, W, P)
            WBT=__WBT_DBT_W_P(DBT, W, P)
        elif cd2=="V":
            V=cd2val
            DBT=__DBT_RH_V_P(RH, V, P)
            W=__W_DBT_RH_P(DBT, RH, P)
            H=__H_DBT_W(DBT, W)
            WBT=__WBT_DBT_W_P(DBT, W, P)
        elif cd2=="H":
            H=cd2val
            DBT=__DBT_H_RH_P(H, RH, P)
            W=__W_DBT_RH_P(DBT, RH, P)
            V=__V_DBT_W_P(DBT, W, P)
            WBT=__WBT_DBT_W_P(DBT, W, P)
    elif cd1=="W":
        W=cd1val
        if cd2=="V":
            V=cd2val
            DBT=__DBT_V_W_P(V, W, P)
            H=__H_DBT_W(DBT, W)
            RH=__RH_DBT_W_P(DBT, W, P)
            WBT=__WBT_DBT_W_P(DBT, W, P)
        elif cd2=="H":
            H=cd2val
            DBT=__DBT_H_W(H, W)
            RH=__RH_DBT_W_P(DBT, W, P)
            V=__V_DBT_W_P(DBT, W, P)
            WBT=__WBT_DBT_W_P(DBT, W, P)
    elif cd1=="V":
        V=cd1val
        H=cd2val
        DBT=__DBT_H_V_P(H, V, P)
        W=__W_DBT_V_P(DBT, V, P)
        RH=__RH_DBT_W_P(DBT, W, P)
        WBT=__WBT_DBT_W_P(DBT, W, P)
    return [DBT, H, RH, V, W, WBT]

# ASHRAE 2009 Chapter 1 Equation 22 and Equation 24
def __RH_DBT_W_P(DBT, W, P):
    if __valid_DBT(DBT):
        return W*P/((0.621945+W)*__Pws(DBT))

# ASHRAE 2009 Chapter 1 Equation 28
def __V_DBT_W_P(DBT, W, P):
    if __valid_DBT(DBT):
        return 0.370486*DBT*(1+1.607858*W)/P

# ASHRAE 2009 Chapter 1 Equation 32
def __W_DBT_H(DBT, H):
    if __valid_DBT(DBT):
        DBT=DBT-459.67
        return (H-0.240*DBT)/(1061+0.444*DBT)

# ASHRAE 2009 Chapter 1 Equation 22 and Equation 24
def __W_DBT_RH_P(DBT, RH, P):
    if __valid_DBT(DBT):
        Pw=RH*__Pws(DBT)
        return 0.621945*Pw/(P-Pw)

# ASHRAE 2009 Chapter 1 Equation 28
def __W_DBT_V_P(DBT, V, P):
    if __valid_DBT(DBT):
        return (P*V-0.370486*DBT)/(1.607858*0.370486*DBT)

# ASHRAE 2009 Chapter 1 Equation 35
def __W_DBT_WBT_P(DBT, WBT, P):
    if __valid_DBT(DBT):
        DBT=DBT-459.67
        WBT=WBT-459.67
        return ((1093-0.556*WBT)*__W_DBT_RH_P(WBT+459.67,1,P)-0.240*(DBT-WBT))/\
               (1093+0.444*DBT-WBT)

# ASHRAE 2009 Chapter 1 Equation 35
def __WBT_DBT_W_P(DBT, W, P):
    if __valid_DBT(DBT):
        WBTa=__DPT_Pw(__Pw_W_P(W, P))
        WBTb=DBT
        WBT=(WBTa+WBTb)/2
        while WBTb-WBTa>TOL:
            Ws=__W_DBT_WBT_P(DBT, WBT, P)
            if W>Ws:
                WBTa=WBT
            else:
                WBTb=WBT
            WBT=(WBTa+WBTb)/2
        return WBT

def __valid_DBT(DBT):
    if Min_DBT<=DBT<=Max_DBT:
        return True
    else:
        return False
