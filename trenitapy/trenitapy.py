# -*- coding: utf-8 -*-

from __future__ import print_function
import requests
from requests.compat import urljoin
import logging
import string

logger = logging.getLogger(__name__)


class TrenitApy:

    @staticmethod
    def _call(action, *args, **kwargs):
        fmt = kwargs.pop('fmt', None) or 'json'
        
        base_url = 'http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno'
        url = '/'.join((base_url, action, ) + args)
        response = requests.get(url)
        if fmt == 'json':
            data = response.json()
        else:
            data = response.text
        return data

    def andamento_treno(self, id_stazione_partenza, numero_treno):
        """
        http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/andamentoTreno/IDStazionePartenza/numeroTreno
        http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/andamentoTreno/S00228/4640
        """
        return self.__class__._call('andamentoTreno', id_stazione_partenza, numero_treno)

    def cerca_stazione(self, nome_stazione):
        return self.__class__._call('cercaStazione', nome_stazione)

    def tratte_canvas(self):
        'http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/tratteCanvas/IDStazionePartenza/numeroTreno'
        pass

    def soluzioni_viaggio(self, _from, _to, _datetime):
        """
        http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/soluzioniViaggioNew/228/458/2015-01-26T00:00:00
        """

        def clean_id(s):
            s = ''.join([x for x in s if x in string.digits])
            return s.lstrip('0')

        _from = clean_id(_from)
        _to = clean_id(_to)
        _datetime = _datetime.strftime('%Y-%m-%dT%H:%M:%S')
        return self.__class__._call('soluzioniViaggioNew', _from, _to, _datetime)

    def cerca_numero_treno(self, numero_treno):
        """Ricavare la stazione di partenza dal numero del treno:
         http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/cercaNumeroTrenoTrenoAutocomplete/numeroTreno

        Output: stringa di una o più righe esempio:
        http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/cercaNumeroTrenoTrenoAutocomplete/4600
        restituisce una riga
        4600 - ASTI|4600-S00462
        (4600 è il numero del treno, ASTI è il nome della stazione di partenza, S00462 il codice stazione
         da usare nelle chiamate ad andamentoTreno e alle altre API

        Se il numero del treno non è univoco, l'output sarà di più righe nello stesso formato:
        http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/cercaNumeroTrenoTrenoAutocomplete/88
        88 - VERONA PORTA NUOVA|88-S02430
        88 - BRESCIA|88-N00201

        :param numero_treno:
        :return:
        """
        raw_results = self.__class__._call('cercaNumeroTrenoTrenoAutocomplete', numero_treno, fmt='raw')
        results = list()
        for r in raw_results.splitlines():
            left, right = r.split('|')
            n_treno, stazione = left.split(' - ')
            n_treno, id_stazione = right.split('-')
            results.append({'numeroTreno': numero_treno, 'stazione': stazione, 'idStazione': id_stazione})
        return results


if __name__ == '__main__':
    import doctest
    doctest.testmod()
