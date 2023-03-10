"""_summary_
"""

import logging
from datetime import datetime
import hashlib
from api.auth_features.util import ApiCrypto
import json
from decouple import config
import ast

logger = logging.getLogger(__name__)
class GeneralTokenAutorization(object):
    def validate(data):
        _token_data = None
        _is_valid, _token_data = False, None
        _bk = config('BASE_KEY', cast=str)
        _data = ApiCrypto.decrypt(base_key=_bk, encrypted_message=data)
        _data = json.loads(_data)
        _token = _data.get('token')
        _token = json.dumps(_token)
        _token = ApiCrypto.decrypt(base_key=_bk, encrypted_message=_token)
        _token = json.loads(_token)
        _token_message = _token.get('token_message')
        _token_crc = _token.get('token_crc')
        _gmi = config('GENERAL_MOBILE_ID', cast=str)
        _togt = config('TIME_OUT_GENERAL_TOKEN', cast=int)
        _d = ApiCrypto.decrypt(base_key=_bk, encrypted_message = _token_crc)
        _base_string = _gmi + _d
        _calculated_token_message = hashlib.sha256(_base_string.encode('utf-8')).hexdigest()
        if (_token_message==_calculated_token_message):
            _server_now = datetime.utcnow()
            _string_now = _server_now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            _dtf = datetime.strptime(_d, '%Y-%m-%d %H:%M:%S.%f')
            _dif = (_server_now - _dtf)
            if _dif.total_seconds() > 0 and _dif.total_seconds() <= _togt:
                _is_valid= True
                _encrypted_server_now = ApiCrypto.encrypt(base_key = _bk, string_message = _string_now)
                _base_string = _gmi + _string_now
                _new_token_message = hashlib.sha256(_base_string.encode('utf-8')).hexdigest()    
                _token_data = {
                    'token_message': _new_token_message,
                    'token_crc': _encrypted_server_now, 
                }
                _token_data = ApiCrypto.encrypt(base_key = _bk, string_message = json.dumps(_token_data))
        return _is_valid, _token_data 

class CompanyTokenAutorization(object):
    def login(data):
        _result, rd = False, None
        _bk = config('BASE_KEY', cast=str)
        _data = ApiCrypto.decrypt(base_key=_bk, encrypted_message=data)
        _data = json.loads(_data)
        _token = _data.get('token')
        _data_dict = json.loads(_data.get('data'))
        _d = _data_dict.get('d')
        _gmi = config('GENERAL_MOBILE_ID', cast=str)
        _togt = config('TIME_OUT_GENERAL_TOKEN', cast=int)
        _d = ApiCrypto.decrypt(base_key=_bk, encrypted_message = _d)
        _base_string = _gmi + _d
        n = datetime.utcnow()
        _t = hashlib.sha256(_base_string.encode('utf-8')).hexdigest()    
        if (_token==_t):
            _dtf = datetime.strptime(_d, '%Y-%m-%d %H:%M:%S.%f')
            _dif = (n - _dtf)
            if _dif.total_seconds() > 0 and _dif.total_seconds() <= _togt:
                _result, rd = True, ApiCrypto.encrypt(_bk, n.strftime('%Y-%m-%d %H:%M:%S.%f'))
        return _result, rd