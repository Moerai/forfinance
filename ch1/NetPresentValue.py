# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 01:23:57 2018

@author: frien
"""
def npv_f(rate,cashflows):
    total = 0.0
    for i in range(0, len(cashflows)):
        total += cashflows[i]/(1+rate)**i
    return total

r=0.035
cashflows=[-100,-30,10,40,50,45,20]
npv_f(r,cashflows)
#14.158224763725372

def npv_Excel(rate, cashflows):
    total=0.0
    for i , cashflow in enumerate(cashflows):
        total +=cashflow/(1+rate)**(i+1)
    return total
npv_Excel(r,cashflows[1:7])+cashflows[0]
#14.158224763725372
