"""_summary_
"""

import logging
from django.conf import settings
from datetime import datetime
import hashlib


logger = logging.getLogger(__name__)

def valida_token_general(t, d):
    _result = False
    _gmk = settings.GENERAL_MOBILE_KEY
    _togt = settings.TIME_OUT_GENERAL_TOKEN
    _d = d
    _base_string = _gmk + _d
    _t = hashlib.sha256(_base_string.encode('utf-8')).hexdigest()    
    if (t==_t):
        _dt = datetime.strptime(_d, '%Y-%m-%d %H:%M:%S.%f')
        n = datetime.utcnow()
        _dif = (n - _dt)
        if _dif.total_seconds() > 0 and _dif.total_seconds() <= _togt:
            _result = True
    return _result