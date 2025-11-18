import pandas as pd


PROJECT_ID = 'bigdata-fase2'

# BigQuery
DATASET        = f'{PROJECT_ID}.parkings_datamart'
TABLE_EVENTS   = f'{DATASET}.facts'
TABLE_SUBJECTS = f'{DATASET}.subjects'
TABLE_STATES   = f'{DATASET}.states'

# Cloud Storage
BUCKET_NAME        =  'sagulpa-datalake'
PATH_DATALAKE_DOCS =  'parkings-off_street/documents'
PATH_OPEN_DATA     =  'parkings-off_street/open_data'

prev    = pd.Timestamp.now() - pd.DateOffset(months=1)
n_month = prev.month
year    = prev.year
date    = prev.strftime("%Y%m")
w_month = prev.month_name(locale='es_ES.UTF-8')

path_abonados_en_banco   = f'{PATH_DATALAKE_DOCS}/{year}/financiero.abonados-en-banco'      + f'/{date}.xlsx'
path_recaudacion         = f'{PATH_DATALAKE_DOCS}/{year}/financiero.recaudacion'            + f'/{date}.xls'
path_rincon_estadisticas = f'{PATH_DATALAKE_DOCS}/{year}/aparcamientos.rincon-estadisticas' + f'/{date}.xlsx'
path_informes_filtrados  = f'{PATH_DATALAKE_DOCS}/{year}/aparcamientos.informes-filtrados'  + f'/{date}.&.pdf'
path_abonos_lpa_y_qr     = f'{PATH_DATALAKE_DOCS}/{year}/sistemas.abonados-qr-lpa'          + f'/{date}.xlsx'
path_ocupacion           = f'{PATH_DATALAKE_DOCS}/{year}/sistemas.ocupacion'                + f'/{date}.xlsx'
path_ocupacion_ld        = f'{PATH_DATALAKE_DOCS}/{year}/sistemas.ocupacion-ld'             + f'/{date}.xls'
path_ocupacion_lv        = f'{PATH_DATALAKE_DOCS}/{year}/sistemas.ocupacion-lv'             + f'/{date}.xls'
path_ocupacion_sd        = f'{PATH_DATALAKE_DOCS}/{year}/sistemas.ocupacion-sd'             + f'/{date}.xls'
path_abonados            = f'{PATH_DATALAKE_DOCS}/{year}/sistemas.abonados'                 + f'/{date}.&.xlsx'
path_rotacion            = f'{PATH_DATALAKE_DOCS}/{year}/sistemas.rotacion'                 + f'/{date}.&.xlsx'
path_transparencia       = f'{PATH_OPEN_DATA}/transparency'                                 + f'/{date}.xlsx'