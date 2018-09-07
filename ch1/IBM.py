# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:31:47 2018

@author: frien
"""

import pandas as pd
#pandas 모듈의 read_csv파일로 불러오기
x = pd.read_csv("C:/Users/frien/Documents/forfinance/ch1/ibm.csv")
#pandas 모듈의 read_table로 불러오기
x=pd.read_table("C:/Users/frien/Documents/forfinance/ch1/ibm.csv")
#웹 크롤링
url = 'http://canisius.edu/~yany/data/ibm.csv'
x = pd.read_csv(url)
#excel 통합 데이터 파일인 xlsx파일 불러오기
infile=pd.ExcelFile("C:/Users/frien/Documents/forfinance/ch1/stockReturns.xlsx")
#numpy.ndarray 타입
import numpy as np
r=0.023
pv=np.array([100,300,500])
#소수점 이하 자리 수를 지정하려면 round()함수를 사용
round(7/3,5)
#10개의 0으로 된 배열 선언
a=np.zeros(10)
#0으로 채워진 3x2 행렬
b = np.zeros((3,2),dtype=float)
#1으로 채워진 4x3 행렬
c = np.ones((4,3),float)
#0~9
d = np.array(range(10),float)
#4x4 단위행렬
e1 = np.identity(4)
e2 = np.eye(4)
#4x4, 1은 k열부터
e3 = np.eye(4,k=1)
#1부터 19까지 3의 간격으로
f = np.arange(1,20,3,float)
#2x3 행렬
g = np.array([[2,2,2],[3,3,3]])
#모두 0인 g의 크기를 가진 행렬
h=np.zeros_like(g)
#모두 1인 g의 크기를 가진 행렬
i=np.ones_like(g)
#합을 구하는 함수 sum
f.sum()
g.sum()
