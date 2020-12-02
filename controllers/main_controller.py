from controllers.itunes_controller import ITunesController
from api_codes import MESSAGES

ITUNES_CONTROLLER = ITunesController()


class MainController:

    def search(self, data):
        response = {
            'errors': [],
            'results': [],
            'message': ''
        }

        term = data['term'] if 'term' in data else ''

        if term == '':
            response['errors'].append({
                'code': '1001',
                'message': MESSAGES['1001']
            })
        else:
            # iTunes search
            itunes_res, itunes_errors = ITUNES_CONTROLLER.search(term)
            response['results'] += itunes_res
            response['errors'] += itunes_errors

            #
        # Sorting alphabetically
        if len(response['results']) > 0:
            response['results'] = sorted(response['results'], key=lambda k: k['name'])
        response['ok'] = len(response['errors']) < 1

        return response
