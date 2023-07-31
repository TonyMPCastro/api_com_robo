import requests
import json

def verifica_urls(urls):
    urls_status = {}
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                urls_status[url] = 'online'
            else:
                urls_status[url] = 'offline'
        except:
            urls_status[url] = 'offline'
    return urls_status

# Exemplo de uso
urls = [
    "https://transparencia.cmbomjardim.ma.gov.br",
    "https://transparencia.bomprev.ma.gov.br",
    "https://transparencia.cmtuntum.ma.gov.br",
    "https://transparencia.cmguimaraes.ma.gov.br",
    "https://transparencia.olhodaguadascunhas.ma.gov.br",
    "https://transparencia.santaines.ma.gov.br",
    "https://transparencia.cmpresidentevargas.ma.gov.br",
    "https://transparencia.guimaraes.ma.gov.br",
    "https://transparencia.satubinha.ma.gov.br",
    "http://transparencia.senadoralexandrecosta.ma.gov.br",
    "https://transparencia.novaiorque.ma.gov.br",
    "https://transparencia.pacodolumiar.ma.gov.br",
    "https://transparencia.cmsatubinha.ma.gov.br",
    "https://transparencia.diariomunicipal.net.br\/transparencia",
    "https://transparencia.diariomunicipal.net.br\/transparencia\/",
    "https://transparencia.bacuri.diariomunicipal.net.br",
    "https://transparencia.cmapicumacu.ma.gov.br",
    "https://transparencia.cmarari.ma.gov.br",
    "https://transparencia.cmcentronovo.ma.gov.br",
    "https://transparencia.cmmorros.ma.gov.br",
    "https://transparencia.cmpalmeirandia.ma.gov.br",
    "https://transparencia.governadoredisonlobao.ma.gov.br",
    "https://transparencia.cmbacabal.ma.gov.br.ma.gov.br",
    "https://transparencia.cmmirinzal.ma.gov.br",
    "https://transparencia.cmturiacu.ma.gov.br",
    "https://transparencia.cmitaipava.ma.gov.br",
    "https://transparencia.cmsrdocabezerra.ma.gov.br",
    "https://transparencia.cmbernardodomearim.ma.gov.br",
    "https://transparencia.cmcoroata.ma.gov.br",
    "https://transparencia.lagodojunco.ma.gov.br",
    "https://transparencia.pedrodorosario.ma.gov.br",
    "https://transparencia.centronovo.ma.gov.br",
    "https://transparencia.cmduquebacelar.ma.gov.br",
    "https://transparencia.estreito.ma.gov.br",
    "http://transparencia.santaluzia.ma.gov.br",
    "https://transparencia.portofranco.diariomunicipal.net.br",
    "https://transparencia.cmcentraldomaranhao.ma.gov.br",
    "https://transparencia.CMBELAVISTA.ma.gov.br",
    "https://transparencia.barreirinhas.ma.gov.br",
    "https://transparencia.cmbelavista.ma.gov.br",
    "https://transparencia.cmcaxias.ma.gov.br",
    "https://transparencia.jenipapodosvieiras.ma.gov.br",
    "https://transparencia.cmgrajau.ma.gov.br",
    "https://transparencia.cmbequimao.ma.gov.br",
    "https://transparencia.cmaraioses.ma.gov.br",
    "https://transparencia.cmcoelhoneto.ma.gov.br",
    "https://transparencia.carutapera.ma.gov.br",
    "https://transparencia.saobeneditodoriopreto.ma.gov.br",
    "https://transparencia.santoamaro.ma.gov.br",
    "https://transparencia.cmportorico.ma.gov.br",
    "https://transparencia.cmbacuri.ma.gov.br",
    "https://transparencia.palmeirandia.ma.gov.br",
    "https://transparencia.morros.ma.gov.br",
    "https://transparencia.buriti.ma.gov.br",
    "https://transparencia.amapa.ma.gov.br",
    "https://transparencia.cmcururupu.ma.gov.br",
    "https://transparencia.itaipava.ma.gov.br",
    "https://transparencia.cmvitorinofreire.ma.gov.br",
    "https://transparencia.cmbomlugar.ma.gov.br",
    "http://transparencia.turiacu.ma.gov.br",
    "https://transparencia.lajeadonovo.diariomunicipal.net.br",
    "http://transparencia.tuntum.ma.gov.br",
    "https://transparencia.mataroma.ma.gov.br",
    "https://transparencia.governadorarcher.ma.gov.br",
    "https://transparencia.cururupu.ma.gov.br",
    "https://transparencia.apicumacu.ma.gov.br",
    "https://transparencia.candidomendes.ma.gov.br",
    "https://transparencia.diariomunicipal.net.br\/formosadaserranegra",
    "https://transparencia.altoalegredomaranhao.ma.gov.br",
    "http://transparencia.pindaremirim.ma.gov.br",
    "https://transparencia.saobento.ma.gov.br",
    "http://transparencia.cmclagoacu.ma.gov.br",
    "https://transparencia.centraldomaranhao.ma.gov.br",
    "http://transparencia.vitorinofreire.ma.gov.br",
    "https://transparencia.cmlagoagrandedomaranhao.ma.gov.br",
    "https://transparencia.cmpocaodepedras.ma.gov.br",
    "https://transparencia.cmpresidentesarney.ma.gov.br",
    "https://transparencia.cmlagodojunco.ma.gov.br",
    "https://transparencia.cmlagoverde.ma.gov.br",
    "https://transparencia.cmigarapegrande.ma.gov.br",
    "https://transparencia.alcantara.ma.gov.br",
    "https://transparencia.mirinzal.ma.gov.br",
    "https://transparencia.cmlagodosrodrigues.ma.gov.br",
    "https://transparencia.cmpresidentemedici.ma.gov.br",
    "https://transparencia.mirandadonorte.ma.gov.br",
    "https://transparencia.cmsaoroberto.ma.gov.br",
    "https://transparencia.saoroberto.ma.gov.br",
    "https://transparencia.cmlagodapedra.ma.gov.br",
    "http://transparencia.cmesperantinopolis.ma.gov.br",
    "http://transparencia.conceicaodolagoacu.ma.gov.br",
    "https://transparencia.presidentemedici.ma.gov.br",
    "http://transparencia.www.saoraimundododocabezerra.ma.gov.br",
    "http://transparencia.governadornunesfreire.ma.gov.br",
    "https://transparencia.cmpauloramos.ma.gov.br",
    "https://transparencia.presidentesarney.ma.gov.br",
    "https://transparencia.marajadosena.ma.gov.br",
    "https://transparencia.pocaodepedras.ma.gov.br",
    "https://transparencia.pauloramos.ma.gov.br",
    "https://transparencia.lagodosrodrigues.ma.gov.br",
    "https://transparencia.igarapegrande.ma.gov.br",
    "https://transparencia.bernardodomearim.ma.gov.br",
    "https://transparencia.esperantinopolis.ma.gov.br",
    "https://transparencia.belavista.ma.gov.br"
]

urls_status = verifica_urls(urls)

# Salva o status das URLs em um arquivo JSON
with open('urls_status.json', 'w') as f:
    json.dump(urls_status, f)

# Imprime o status de cada URL
for url, status in urls_status.items():
    print(f'{url} _______________________________ Stutus: {status}.')
