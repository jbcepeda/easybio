"""_summary_
"""

import logging
from datetime import datetime
import hashlib
from api.auth_features.util import ApiCrypto, ApiToken
from api.aws_services_connect import AWSServicesConnect
import json
from decouple import config
import ast

logger = logging.getLogger(__name__)
class GeneralTokenAutorization(object):
    def validate(data, base_key, client_id, time_out):
        _is_valid = False
        try:                      
            _data = ApiCrypto.decrypt(base_key= base_key, encrypted_message=data)
            _data = json.loads(_data)
            _token = _data.get('token')
            _token = ApiCrypto.decrypt(base_key = base_key, encrypted_message=_token)
            _token = json.loads(_token)
            _token_message = _token.get('token_message')
            _token_crc = _token.get('token_crc')
            _d = ApiCrypto.decrypt(base_key=base_key, encrypted_message = _token_crc)
            _base_string = client_id + _d
            _calculated_token_message = hashlib.sha256(_base_string.encode('utf-8')).hexdigest()
            if (_token_message==_calculated_token_message):
                _server_now = datetime.utcnow()
                _dtf = datetime.strptime(_d, '%Y-%m-%d %H:%M:%S.%f')
                _dif = (_server_now - _dtf)
                if _dif.total_seconds() > 0 and _dif.total_seconds() <= time_out:
                    _is_valid= True
        except Exception as ex:
            logger.error(str(ex))
        return _is_valid

class BiometricLoginAutorization(object):
    def get_bio_data(data, base_key, client_id, time_out):
        _eid, _f = None, None
        try:
            _data = data
            _base_key = base_key
            _client_id = client_id
            _time_out = time_out
            logger.debug("_is_valid_token:{} {} {} {}".format(type(_data),type(base_key),type(client_id),type(time_out),))        
            _is_valid_token = GeneralTokenAutorization.validate(data = _data,
                                            base_key=_base_key, client_id = _client_id, time_out=_time_out) 
            logger.debug("after _is_valid_token:{}".format(type(_data)))        
            if _is_valid_token:
                _data = ApiCrypto.decrypt(base_key=base_key, encrypted_message=_data)
                _data = json.loads(_data)       
                _bio_data = _data.get('data')
                _eid = _bio_data.get('_eid')
                _f = _bio_data.get('f')
        except Exception as ex:
            logger.error(str(ex))
            
        return _eid and _f, _eid, _f

    def login(self, base_key, client_id, photo, employee_photo):
        _is_valid, _token_data,  = False, None
        try:
            if photo and employee_photo:
                _face_matches, _matches_detail = AWSServicesConnect.compare_faces(self,
                    source_base64 = photo, target_base64 = employee_photo)                
                if _face_matches:
                    _is_valid = True
                    _token_data = ApiToken.generate_token(base_key = base_key, client_id = client_id)
        except Exception as ex:
            logger.error(str(ex))
        return _is_valid, _token_data
