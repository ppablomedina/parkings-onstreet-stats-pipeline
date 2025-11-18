import processes.ocupacion, processes.abonados_en_banco, processes.abonados_lpa_y_qr, processes.recaudacion, processes.rincon_estadisticas, processes.abonados_y_rotacion, processes.informes_filtrados, processes.ratios
from gcp.utils import insert_events
from flask import Flask, request


def entry_point(req):
    modules = [
        processes.ocupacion,
        processes.abonados_en_banco,
        processes.recaudacion,
        processes.rincon_estadisticas,
        processes.abonados_lpa_y_qr,
        processes.informes_filtrados,
        processes.abonados_y_rotacion,
    ]
    all_events = []
    for module in modules:
        feeds = module.main()
        all_events.extend(feeds)

    insert_events(processes.ratios.main(all_events))
    return "ETL ejecutado correctamente\n", 200

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def run():
    return entry_point(request)