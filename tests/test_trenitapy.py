#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_trenitapy
----------------------------------

Tests for `trenitapy` module.
"""

import unittest
from datetime import date, datetime, time, timedelta

from trenitapy.trenitapy import TrenitApy


class TestTrenitapy(unittest.TestCase):

    def setUp(self):
        self.api = TrenitApy()

    def tearDown(self):
        pass

    def test_andamento_treno(self):
        keys_expected = ['anormalita', 'binarioEffettivoArrivoCodice', 'binarioEffettivoArrivoDescrizione',
                         'binarioEffettivoArrivoTipo', 'binarioEffettivoPartenzaCodice',
                         'binarioEffettivoPartenzaDescrizione', 'binarioEffettivoPartenzaTipo',
                         'binarioProgrammatoArrivoCodice', 'binarioProgrammatoArrivoDescrizione',
                         'binarioProgrammatoPartenzaCodice', 'binarioProgrammatoPartenzaDescrizione',
                         'cambiNumero', 'categoria', 'categoriaDescrizione', 'circolante', 'codDestinazione',
                         'codOrigine', 'codiceCliente', 'compClassRitardoLine', 'compClassRitardoTxt',
                         'compDurata', 'compImgCambiNumerazione', 'compImgRitardo', 'compImgRitardo2',
                         'compInStazioneArrivo', 'compInStazionePartenza', 'compNumeroTreno',
                         'compOraUltimoRilevamento', 'compOrarioArrivo', 'compOrarioArrivoZero',
                         'compOrarioArrivoZeroEffettivo', 'compOrarioEffettivoArrivo', 'compOrarioPartenza',
                         'compOrarioPartenzaZero', 'compOrarioPartenzaZeroEffettivo', 'compOrientamento',
                         'compRitardo', 'compRitardoAndamento', 'compTipologiaTreno', 'corrispondenze',
                         'dataPartenza', 'descOrientamento', 'descrizioneVCO', 'destinazione', 'destinazioneEstera',
                         'destinazioneZero', 'esisteCorsaZero', 'fermate', 'fermateSoppresse', 'haCambiNumero',
                         'hasProvvedimenti', 'idDestinazione', 'idOrigine', 'inStazione', 'motivoRitardoPrevalente',
                         'nonPartito', 'numeroTreno', 'oraArrivoEstera', 'oraPartenzaEstera', 'oraUltimoRilevamento',
                         'orarioArrivo', 'orarioArrivoZero', 'orarioPartenza', 'orarioPartenzaZero', 'orientamento',
                         'origine', 'origineEstera', 'origineZero', 'provvedimenti', 'provvedimento', 'regione',
                         'riprogrammazione', 'ritardo', 'segnalazioni', 'servizi', 'statoTreno', 'stazioneArrivo',
                         'stazionePartenza', 'stazioneUltimoRilevamento', 'subTitle', 'tipoProdotto', 'tipoTreno',
                         'tratta', ]
        d = self.api.andamento_treno('S00228', '4640')
        keys = sorted(d.keys())
        self.assertEqual(keys_expected, keys)

    def cerca_stazione(self):
        expected = [{"id": "S09008", "nomeLungo": "FRATTAMAGGIORE", "nomeBreve": "Frattamaggiore", "label": None}]
        stazioni = self.api.cerca_stazione('frattamaggiore')
        self.assertEqual(stazioni, expected)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
