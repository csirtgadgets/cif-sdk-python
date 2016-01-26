import os

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s[%(lineno)s] - %(message)s'

REMOTE_ADDR = 'https://localhost'
REMOTE_ADDR = os.environ.get('CIF_REMOTE_ADDR', REMOTE_ADDR)

LIMIT = 500
LIMIT = os.environ.get('CIF_LIMIT', LIMIT)

FEED_LIMIT = 50000
FEED_LIMIT = os.environ.get('CIF_FEED_LIMIT', FEED_LIMIT)

FEED_CONFIDENCE = 85
FEED_CONFIDENCE = os.environ.get('CIF_FEED_CONFIDENCE', FEED_CONFIDENCE)

WHITELIST_LIMIT = 25000
WHITELIST_LIMIT = os.environ.get('CIF_WHITELIST_LIMIT', WHITELIST_LIMIT)

WHITELIST_CONFIDENCE = os.environ.get('CIF_WHITELIST_CONFIDENCE', 25)

PROXY = os.environ.get('CIF_PROXY')

TOKEN = os.environ.get('CIF_TOKEN')

FIELDS = ['tlp', 'group', 'lasttime', 'reporttime', 'observable', 'otype', 'cc', 'asn', 'asn_desc', 'confidence', 'description',
          'tags', 'rdata', 'provider']
FIELDS = os.environ.get('CIF_FIELDS', FIELDS)

PINGS=4
