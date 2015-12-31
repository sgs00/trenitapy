# -*- coding: utf-8 -*-

from __future__ import print_function
import requests
from requests.compat import urljoin
import logging

logger = logging.getLogger(__name__)
base_url = 'http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/'


class TrenitApy:

    def andamento_treno(self, id_stazione_partenza, numero_treno):
        """
        http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/andamentoTreno/IDStazionePartenza/numeroTreno
        http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/andamentoTreno/S00228/4640

        >>> e = ['anormalita', 'binarioEffettivoArrivoCodice', 'binarioEffettivoArrivoDescrizione',\
                 'binarioEffettivoArrivoTipo', 'binarioEffettivoPartenzaCodice',\
                 'binarioEffettivoPartenzaDescrizione', 'binarioEffettivoPartenzaTipo',\
                 'binarioProgrammatoArrivoCodice', 'binarioProgrammatoArrivoDescrizione',\
                 'binarioProgrammatoPartenzaCodice', 'binarioProgrammatoPartenzaDescrizione',\
                 'cambiNumero', 'categoria', 'categoriaDescrizione', 'circolante', 'codDestinazione',\
                 'codOrigine', 'codiceCliente', 'compClassRitardoLine', 'compClassRitardoTxt',\
                 'compDurata', 'compImgCambiNumerazione', 'compImgRitardo', 'compImgRitardo2',\
                 'compInStazioneArrivo', 'compInStazionePartenza', 'compNumeroTreno',\
                 'compOraUltimoRilevamento', 'compOrarioArrivo', 'compOrarioArrivoZero',\
                 'compOrarioArrivoZeroEffettivo', 'compOrarioEffettivoArrivo', 'compOrarioPartenza',\
                 'compOrarioPartenzaZero', 'compOrarioPartenzaZeroEffettivo', 'compOrientamento',\
                 'compRitardo', 'compRitardoAndamento', 'compTipologiaTreno', 'corrispondenze',\
                 'dataPartenza', 'descOrientamento', 'descrizioneVCO', 'destinazione', 'destinazioneEstera',\
                 'destinazioneZero', 'esisteCorsaZero', 'fermate', 'fermateSoppresse', 'haCambiNumero',\
                 'hasProvvedimenti', 'idDestinazione', 'idOrigine', 'inStazione', 'motivoRitardoPrevalente',\
                 'nonPartito', 'numeroTreno', 'oraArrivoEstera', 'oraPartenzaEstera', 'oraUltimoRilevamento',\
                 'orarioArrivo', 'orarioArrivoZero', 'orarioPartenza', 'orarioPartenzaZero', 'orientamento',\
                 'origine', 'origineEstera', 'origineZero', 'provvedimenti', 'provvedimento', 'regione',\
                 'riprogrammazione', 'ritardo', 'segnalazioni', 'servizi', 'statoTreno', 'stazioneArrivo',\
                 'stazionePartenza', 'stazioneUltimoRilevamento', 'subTitle', 'tipoProdotto', 'tipoTreno',\
                 'tratta', ]
        >>> d = TrenitApy().andamento_treno('S00228', '4640')
        >>> k = d.keys()
        >>> sorted(k) == e
        True
        """
        url = 'andamentoTreno/{}/{}/'.format(id_stazione_partenza, numero_treno)
        url = urljoin(base_url, url)
        response = requests.get(url)
        return response.json()

    def cerca_stazione(self, nome_stazione):
        """
        >>> r = TrenitApy().cerca_stazione('frattamaggiore')
        >>> r == [{"id": "S09008", "nomeLungo": "FRATTAMAGGIORE", "nomeBreve": "Frattamaggiore", "label": None}]
        True
        """
        url = 'cercaStazione/{}/'.format(nome_stazione)
        url = urljoin(base_url, url)
        response = requests.get(url)
        return response.json()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
