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
        """
        url = 'andamentoTreno/{}/{}/'.format(id_stazione_partenza, numero_treno)
        url = urljoin(base_url, url)
        response = requests.get(url)
        return response.json()
