import pandas as pd
import geopandas
import matplotlib.pyplot as fig
import seaborn as sns
import matplotlib.dates as mdates
from geopy.geocoders import Nominatim
from pytrends.request import TrendReq #precisa instalar essa biblioteca 
                                      #usando pip install
import geopandas as gpd
import pandas as pd
from geopy.geocoders import Nominatim
import numpy as np


#++++++++++++++++++++++ conexao com o servidor ++++++++++++++++++++++++++++
pytrends=TrendReq(hl='en-US', tz=360)
#++++++++++++++++++++++ lista com palavra-chave +++++++++++++++++++++++++++
kw_list=['desmatamento']
#++++++++++++++++++++++ lista de legenda para o grafico
leg=[kw_list[0]]
pytrends.build_payload(kw_list, timeframe='now 1-d',geo='BR-PA',gprop='')
#pytrends.build_payload(kw_list, timeframe='today 5-y',geo='BR',gprop='')

teste=pytrends.interest_over_time()

Regiao = pytrends.interest_by_region=pytrends.interest_by_region(resolution='DMA',
                                                                inc_geo_code=True)

figura=fig.figure()
ax1=fig.subplot(111)
fig.title('GoogleTrends -Palavra chave')

ax1.plot( teste[kw_list[0]] , '-b' )
#ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))

fig.setp(ax1.get_xticklabels(), rotation=45)
fig.legend(leg)

Regiao=Regiao[kw_list[0]].sort_values(ascending=False)
print(Regiao)
Regiao=pd.DataFrame(Regiao)
Regiao=Regiao[Regiao!=0].dropna()   #### apaga as cidades com valor nulo
Regiao.reset_index(inplace=True)  ### muda o indice (nome da cidade) p/ coluna

############### Localizacao no Mapa #############################

geolocator=Nominatim(timeout=10)

Regiao['Latitude']=''
Regiao['Longitude']=''

                   
for i in range(len(Regiao)):
          try:
                      x = geolocator.geocode(Regiao['geoName'][i])
                      Regiao['Latitude'][i]=x.latitude
                      Regiao['Longitude'][i]=x.longitude
          except:
                      pass           

Regiao.replace('', np.nan, inplace=True)
Regiao.dropna(inplace=True)   
        
Regiao = Regiao.drop(Regiao[(Regiao['Latitude'] > 5)
                 | (Regiao['Latitude'] < -10) 
                 | (Regiao['Longitude'] > -40)].index)             

Regiao.to_excel('Regiao_PA.xlsx')

rg=pd.read_excel('Regiao_PA.xlsx')

gdf = geopandas.GeoDataFrame(rg, 
        geometry=geopandas.points_from_xy(rg.Longitude, rg.Latitude))

Mundo = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

# Regiao restrita ao estado #######################
df=gpd.read_file('BR_UF_2022.shp')
sp = df[df['SIGLA_UF'] == 'PA'].reset_index(drop=True)
ax = sp.plot()


############  extrai os pontos do centroide do mapa para o dataframe ####
gdf["x"] = gdf.centroid.map(lambda p: p.x)
gdf["y"] = gdf.centroid.map(lambda p: p.y)
###########################################################################
############ Grafico de bolhas conforme o volume do google trends ####

ax2=sns.scatterplot(data=gdf,x='x',y='y',hue=kw_list[0],
                size=kw_list[0],sizes=(50,300),palette='rocket_r',ax=ax)

#++++++++++++++++++++++ nomes das ciaddes no mapa ++++++++++++++++++++++++
cidades=[ax2.text(x0,y0,nome,fontsize=12) for x0,y0,nome in zip( gdf['x'], gdf['y'], gdf['geoName'] ) ]
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

fig.show()



