import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
from shapely import wkt

direccion_del_archivo = 'calles_de_medellin_con_acoso.csv'

mapa_de_medellin = pd.read_csv(direccion_del_archivo, sep=";")
