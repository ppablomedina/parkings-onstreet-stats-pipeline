import pandas as pd


PROJECT_ID = 'bigdata-fase2'

# BigQuery
DATASET        = f'{PROJECT_ID}.parkings_datamart'
TABLE_EVENTS   = f'{DATASET}.facts'
TABLE_SUBJECTS = f'{DATASET}.subjects'
TABLE_STATES   = f'{DATASET}.states'

# Cloud Storage
BUCKET_NAME        =  'sagulpa-datalake'
PATH_DATALAKE_DOCS =  'parkings-on_street/documents'

prev      = pd.Timestamp.now() - pd.DateOffset(months  =1)
n_month   = prev.month
year      = prev.year
date      = prev.strftime("%Y%m")
full_date = prev.strftime("%Y%m%d")
w_month   = prev.month_name(locale='es_ES.UTF-8')

path_inventario   = f'{PATH_DATALAKE_DOCS}/{year}/ser.inventario-plazas'      + f'/{date}.xlsx'
path_parquimetros = f'{PATH_DATALAKE_DOCS}/{year}/flowbird.parquimetros'      + f'/{full_date}.csv'
path_elavon       = f'{PATH_DATALAKE_DOCS}/{year}/flowbird.pagos-con-tarjeta' + f'/{date}.elavon.csv'
path_caixa        = f'{PATH_DATALAKE_DOCS}/{year}/flowbird.pagos-con-tarjeta' + f'/{date}.caixa.csv'
 