# -*- coding: utf-8 -*-

from __future__ import print_function
import requests
from requests.compat import urljoin
import logging

logger = logging.getLogger(__name__)


class TrenitApy:

    @staticmethod
    def _call(action, *args, fmt='json'):
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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
