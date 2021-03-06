KEYDIR = './keys'

WEB_SERVER_QUERY_URL = 'http://localhost:5000/queries'
WEB_SERVER_QUERY_STATUS_URL = 'http://localhost:5000/query'
EMAIL_SENDER = 'sigurd.gartmann@ntnu.no'

QUERY_SERVER_HOST = 'localhost'
QUERY_SERVER_PORT = 50010
QUERY_SERVER_RECIPIENT = 'sigurdga@edge'

MERGE_SERVER_HOST = 'localhost'
MERGE_SERVER_PORT = 50020
MERGE_SERVER_RECIPIENT = 'sigurdga@edge'

SUMMARY_SERVER_HOST = 'localhost'
SUMMARY_SERVER_PORT = 50030
SUMMARY_SERVER_RECIPIENT = 'sigurdga@edge'

PRESENTATION_SERVER_HOST = 'localhost'
PRESENTATION_SERVER_PORT = 50040
PRESENTATION_SERVER_RECIPIENT = 'sigurdga@edge'

RECIPIENTS = {
    'hunt': 'sigurdga@edge',
    'cancer': 'sigurdga@edge',
    'death': 'sigurdga@edge'
}

# Field information should be set in registries

FIELD_INTERVALS = {
    'born': 5,
    'height': 2,
    'weight': 5,
    'bmi': 0.5
}

FIELD_REPLACEMENTS = {
    'gender': {'0': 'male',
               '1': 'female'},
    'training': {'0': 'no',
                 '1': 'one time per week',
                 '2': '2-3 times per week',
                 '3': 'a lot'},
    'smoking': {'0': 'no',
                '1': 'at parties',
                '2': 'some',
                '3': 'too much'},
    'drinking': {'0': 'never',
                 '1': 'sometimes',
                 '2': 'often',
                 '3': 'too often'},
    'genotyped': {'0': 'no',
                  '1': 'yes'},
    'cancer': {'0': 'no',
               '1': 'yes'},
    'lung_cancer': {'0': 'no',
                    '1': 'yes'},
    'bowel_cancer': {'0': 'no',
                     '1': 'yes'},
    'breast_cancer': {'0': 'no',
                      '1': 'yes'},
    'prostate_cancer': {'0': 'no',
                        '1': 'yes'}
}

# TODO: Override these when finding a file containing local config
