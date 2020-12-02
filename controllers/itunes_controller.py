from api_codes import MESSAGES
import requests


class ITunesController:

    def get_result_list(self, results, type):
        list = []
        for r in results:
            list.append({
                'name': r['trackName'] if 'trackName' in r else '',
                'autor': r['artistName'] if 'artistName' in r else '',
                'album': r['collectionName'] if 'collectionName' in r else '',
                'url': r['trackViewUrl'] if 'trackViewUrl' in r else '',
                'type': type,
                'source': 'itunes'
            })
        return list

    def search_music(self, url, term):
        data_dict = {
            'term': term,
            'media': 'music'
        }
        r = requests.get(url, params=data_dict)
        result = self.get_result_list(r.json()['results'], 'Música')
        return result

    def search_movie(self, url, term):
        data_dict = {
            'term': term,
            'media': 'movie'
        }
        r = requests.get(url, params=data_dict)
        return self.get_result_list(r.json()['results'], 'Película')

    def search(self, term):
        result_list = []
        errors = []
        url = 'https://itunes.apple.com/search'
        try:
            r = self.search_music(url, term)
            result_list += r
            result_list += self.search_movie(url, term)
        except:
            errors.append({
                'code': '2001',
                'message': MESSAGES['2001']
            })

        return result_list, errors
