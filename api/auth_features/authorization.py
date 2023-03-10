"""_summary_
"""

import logging
from datetime import datetime
import hashlib
from api.auth_features.util import ApiCrypto
import json
from decouple import config

logger = logging.getLogger(__name__)
class GeneralTokenAutorization(object):
    def validate(data):
        _s = config('BASE_KEY', cast=str)
        _data = ApiCrypto.decrypt(s=_s, em = data)
        _data = json.loads(_data)
        t = _data.get('t')
        d = _data.get('d')

        _result, rd = False, None
        _gmk = config('GENERAL_MOBILE_KEY', cast=str)
        _togt = config('TIME_OUT_GENERAL_TOKEN', cast=int)
        _d = ApiCrypto.decrypt(s=_s, em = d)
        _base_string = _gmk + _d
        n = datetime.utcnow()
        _t = hashlib.sha256(_base_string.encode('utf-8')).hexdigest()    
        if (t==_t):
            _dtf = datetime.strptime(_d, '%Y-%m-%d %H:%M:%S.%f')
            _dif = (n - _dtf)
            if _dif.total_seconds() > 0 and _dif.total_seconds() <= _togt:
                _result, rd = True, ApiCrypto.encrypt(_s, n.strftime('%Y-%m-%d %H:%M:%S.%f'))
        return _result, rd

class CompanyTokenAutorization(object):
    def login(dt, d):
        _result = False
        _gmk = config('GENERAL_MOBILE_KEY', cast=str)
        _togt = config('TIME_OUT_GENERAL_TOKEN', cast=str)
        _d = d
        _base_string = _gmk + _d
        n = datetime.utcnow()
        _t = hashlib.sha256(_base_string.encode('utf-8')).hexdigest()    
        if (t==_t):
            eid,f
            _dtf = datetime.strptime(_d, '%Y-%m-%d %H:%M:%S.%f')
            _dif = (n - _dtf)
            if _dif.total_seconds() > 0 and _dif.total_seconds() <= _togt:
                _result = True
        return _result, n.strftime('%Y-%m-%d %H:%M:%S.%f')