import pandas as pd
from pytrends.request import TrendReq
import time
import pandas as pd
from pytrends.request import TrendReq
import time
from geopy.geocoders import Nominatim
import geopandas as gpd
import numpy as np
import multiprocessing as mp
from time import time
import threading

def Gstrends():
    pytrends=TrendReq()
    #kw_list=['febre','tosse','garganta','hospital','dengue']
    kw_list=['febre']
    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR',gprop='')
    testef=pytrends.interest_over_time()
    del testef['isPartial']
    testef.to_excel('google_febre.xlsx')
    
    kw_list=['tosse']
    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR',gprop='')
    testef=pytrends.interest_over_time()
    del testef['isPartial']
    testef.to_excel('google_tosse.xlsx')
    
    kw_list=['garganta']
    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR',gprop='')
    testef=pytrends.interest_over_time()
    del testef['isPartial']
    testef.to_excel('google_garganta.xlsx')
    
    kw_list=['hospital']
    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR',gprop='')
    testef=pytrends.interest_over_time()
    del testef['isPartial']
    testef.to_excel('google_hospital.xlsx')
    
    kw_list=['dengue']
    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR',gprop='')
    testef=pytrends.interest_over_time()
    del testef['isPartial']
    testef.to_excel('google_dengue.xlsx')
    
    return 

def Gstrends2():
    pytrends=TrendReq()
    kw_list=['desmatamento']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR',gprop='')
    testef2=pytrends.interest_over_time()

    del testef2['isPartial']
    testef2.to_excel('google2.xlsx')
    return 

def Gstrends3():
    pytrends=TrendReq()
    kw_list=['desmatamento']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR-PA',gprop='')
    testef3=pytrends.interest_over_time()
    del testef3['isPartial']
    Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                    inc_geo_code=True)

    Regiao=pd.DataFrame(Regiao)
    Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna
    Regiao['latitude'] = [d.get('lat') for d in Regiao.coordinates]
    Regiao['longitude'] = [d.get('lng') for d in Regiao.coordinates]
    Regiao.drop(['coordinates'],inplace=True,axis=1)
    Regiao=Regiao[Regiao!=0].dropna()       
    Regiao.to_excel('Regiao_PA.xlsx')     
    return 

def Gstrends3_2():
    pytrends=TrendReq()
    kw_list=['desmatamento']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR-PR',gprop='')
    testef3=pytrends.interest_over_time()
    del testef3['isPartial']
    Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                    inc_geo_code=True)

    Regiao=pd.DataFrame(Regiao)
    Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna
    Regiao['latitude'] = [d.get('lat') for d in Regiao.coordinates]
    Regiao['longitude'] = [d.get('lng') for d in Regiao.coordinates]
    Regiao.drop(['coordinates'],inplace=True,axis=1)
    Regiao=Regiao[Regiao!=0].dropna()       
    Regiao.to_excel('Regiao_PR.xlsx')     
    return 

def Gstrends3_3():
    pytrends=TrendReq()
    kw_list=['desmatamento']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR-SP',gprop='')
    testef3=pytrends.interest_over_time()
    del testef3['isPartial']
    Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                    inc_geo_code=True)

    Regiao=pd.DataFrame(Regiao)
    Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna
    Regiao['latitude'] = [d.get('lat') for d in Regiao.coordinates]
    Regiao['longitude'] = [d.get('lng') for d in Regiao.coordinates]
    Regiao.drop(['coordinates'],inplace=True,axis=1)
    Regiao=Regiao[Regiao!=0].dropna()       
    Regiao.to_excel('Regiao_SP.xlsx')     
    return 

def Gstrends3_4():
    pytrends=TrendReq()
    kw_list=['desmatamento']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR-RS',gprop='')
    testef3=pytrends.interest_over_time()
    del testef3['isPartial']
    Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                    inc_geo_code=True)

    Regiao=pd.DataFrame(Regiao)
    Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna
    Regiao['latitude'] = [d.get('lat') for d in Regiao.coordinates]
    Regiao['longitude'] = [d.get('lng') for d in Regiao.coordinates]
    Regiao.drop(['coordinates'],inplace=True,axis=1)
    Regiao=Regiao[Regiao!=0].dropna()       
    Regiao.to_excel('Regiao_RS.xlsx')     
    return 

def Gstrends3_5():
    pytrends=TrendReq()
    kw_list=['desmatamento']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR-MG',gprop='')
    testef3=pytrends.interest_over_time()
    del testef3['isPartial']
    Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                    inc_geo_code=True)

    Regiao=pd.DataFrame(Regiao)
    Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna
    Regiao['latitude'] = [d.get('lat') for d in Regiao.coordinates]
    Regiao['longitude'] = [d.get('lng') for d in Regiao.coordinates]
    Regiao.drop(['coordinates'],inplace=True,axis=1)
    Regiao=Regiao[Regiao!=0].dropna()       
    Regiao.to_excel('Regiao_MG.xlsx')     
    return 

def Gstrends3_6():
    pytrends=TrendReq()
    kw_list=['desmatamento']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR-AM',gprop='')
    testef3=pytrends.interest_over_time()
    del testef3['isPartial']
    Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                    inc_geo_code=True)

    Regiao=pd.DataFrame(Regiao)
    Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna
    Regiao['latitude'] = [d.get('lat') for d in Regiao.coordinates]
    Regiao['longitude'] = [d.get('lng') for d in Regiao.coordinates]
    Regiao.drop(['coordinates'],inplace=True,axis=1)
    Regiao=Regiao[Regiao!=0].dropna()       
    Regiao.to_excel('Regiao_AM.xlsx')     
    return 

def Gstrends4():
    pytrends=TrendReq()
    kw_list=['queimadas']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR-SP',gprop='')
    testef3=pytrends.interest_over_time()
    del testef3['isPartial']
    Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                    inc_geo_code=True)

    Regiao=pd.DataFrame(Regiao)
    Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna
    Regiao['latitude'] = [d.get('lat') for d in Regiao.coordinates]
    Regiao['longitude'] = [d.get('lng') for d in Regiao.coordinates]
    Regiao.drop(['coordinates'],inplace=True,axis=1)
    Regiao=Regiao[Regiao!=0].dropna()   
    Regiao.to_excel('Queimada_SP.xlsx')           
    return 

def Gstrends5():
    pytrends=TrendReq()
    kw_list=['queimadas']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR-RJ',gprop='')
    testef3=pytrends.interest_over_time()
    del testef3['isPartial']
    Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                    inc_geo_code=True)

    Regiao=pd.DataFrame(Regiao)
    Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna
    Regiao['latitude'] = [d.get('lat') for d in Regiao.coordinates]
    Regiao['longitude'] = [d.get('lng') for d in Regiao.coordinates]
    Regiao.drop(['coordinates'],inplace=True,axis=1)
    Regiao=Regiao[Regiao!=0].dropna()     
    Regiao.to_excel('Queimada_RJ.xlsx')       
    return Regiao

def Gstrends6():
    pytrends=TrendReq()
    kw_list=['queimadas']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR-AM',gprop='')
    testef3=pytrends.interest_over_time()
    del testef3['isPartial']
    Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                    inc_geo_code=True)

    Regiao=pd.DataFrame(Regiao)
    Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna
    Regiao['latitude'] = [d.get('lat') for d in Regiao.coordinates]
    Regiao['longitude'] = [d.get('lng') for d in Regiao.coordinates]
    Regiao.drop(['coordinates'],inplace=True,axis=1)
    Regiao=Regiao[Regiao!=0].dropna()     
    Regiao.to_excel('Queimada_AM.xlsx')       
    return Regiao

def Gstrends7():
    pytrends=TrendReq()
    kw_list=['queimadas']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR-PA',gprop='')
    testef3=pytrends.interest_over_time()
    del testef3['isPartial']
    Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                    inc_geo_code=True)

    Regiao=pd.DataFrame(Regiao)
    Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna
    Regiao['latitude'] = [d.get('lat') for d in Regiao.coordinates]
    Regiao['longitude'] = [d.get('lng') for d in Regiao.coordinates]
    Regiao.drop(['coordinates'],inplace=True,axis=1)
    Regiao=Regiao[Regiao!=0].dropna()     
    Regiao.to_excel('Queimada_PA.xlsx')       
    return Regiao

def Gstrends8():
    pytrends=TrendReq()
    kw_list=['queimadas']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR-MT',gprop='')
    testef3=pytrends.interest_over_time()
    del testef3['isPartial']
    Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                    inc_geo_code=True)

    Regiao=pd.DataFrame(Regiao)
    Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna
    Regiao['latitude'] = [d.get('lat') for d in Regiao.coordinates]
    Regiao['longitude'] = [d.get('lng') for d in Regiao.coordinates]
    Regiao.drop(['coordinates'],inplace=True,axis=1)
    Regiao=Regiao[Regiao!=0].dropna()     
    Regiao.to_excel('Queimada_MT.xlsx')       
    return Regiao

def Gstrends9():
    pytrends=TrendReq()
    kw_list=['queimadas']

    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='BR-TO',gprop='')
    testef3=pytrends.interest_over_time()
    del testef3['isPartial']
    Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                    inc_geo_code=True)

    Regiao=pd.DataFrame(Regiao)
    Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna
    Regiao['latitude'] = [d.get('lat') for d in Regiao.coordinates]
    Regiao['longitude'] = [d.get('lng') for d in Regiao.coordinates]
    Regiao.drop(['coordinates'],inplace=True,axis=1)
    Regiao=Regiao[Regiao!=0].dropna()     
    Regiao.to_excel('Queimada_TO.xlsx')       
    return Regiao
 
def Ligar(): 
###################### motor ligado em computacao paralela ############# 
        results = threading.Thread(target=Gstrends)
        results.start()
        results = threading.Thread(target=Gstrends2)
        results.start()
        results = threading.Thread(target=Gstrends3)
        results.start()
        results = threading.Thread(target=Gstrends3_2)
        results.start()
        results = threading.Thread(target=Gstrends3_3) 
        results.start()
        results = threading.Thread(target=Gstrends3_4)  
        results.start()
        results = threading.Thread(target=Gstrends3_5)           
        results.start()
        results = threading.Thread(target=Gstrends3_6)           
        results.start()
        results = threading.Thread(target=Gstrends4)
        results.start()
        results = threading.Thread(target=Gstrends5)
        results.start()
        results = threading.Thread(target=Gstrends6)
        results.start()
        results = threading.Thread(target=Gstrends7)
        results.start()
        results = threading.Thread(target=Gstrends8)
        results.start()   
        results = threading.Thread(target=Gstrends9)
        results.start()   
        results.join()

