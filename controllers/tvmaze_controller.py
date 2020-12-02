from api_codes import MESSAGES
import requests


class TVMazeController:

    def get_result_list(self, results, type):
        list = []
        for r in results:
            list.append({
                'name': r['show']['name'] if 'name' in r['show'] else '',
                'url': r['show']['url'] if 'url' in r['show'] else '',
                'type': type,
                'source': 'tvmaze',
                'details': {
                    'Estrenado': r['show']['premiered'] if 'premiered' in r['show'] else '',
                    'Idioma': r['show']['language'] if 'language' in r['show'] else ''
                }
            })
        return list

    def search_movie(self, url, term):
        data_dict = {
            'q': term,
        }
        r = requests.get(url, params=data_dict)
        return self.get_result_list(r.json(), 'Película')

    def search(self, term):
        result_list = []
        errors = []
        url = 'http://api.tvmaze.com/search/shows'
        try:
            r = self.search_movie(url, term)
            result_list += r
        except:
            errors.append({
                'code': '3001',
                'message': MESSAGES['3001']
            })

        return result_list, errors
