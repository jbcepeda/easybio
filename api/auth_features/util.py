import logging
from cryptography.fernet import Fernet
import base64
from decouple import config
from datetime import datetime
import hashlib
import json

logger = logging.getLogger(__name__)
class ApiCrypto(object):
    def encrypt(base_key, string_message):
        encrypted_message = None
        try:
            # logger.debug("encrypt  em:{}".format(string_message))
            _f = Fernet(base_key)
            encrypted_message = _f.encrypt(string_message.encode())
        except Exception as ex:
            logger.error(str(ex))
        return encrypted_message.decode()
    
    def decrypt(base_key, encrypted_message):
        string_message = None
        try:
            f = Fernet(base_key.encode())
            string_message = f.decrypt(encrypted_message.encode())
            # logger.debug("decryt  m:{}".format(string_message.decode()))
        except Exception as ex:
            logger.error(str(ex))
        return string_message.decode()
class ApiToken(object):
    def generate_token(base_key, client_id):
        _server_now = datetime.utcnow()
        _string_now = _server_now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        _encrypted_server_now = ApiCrypto.encrypt(base_key = base_key, string_message = _string_now)
        _base_string = client_id + _string_now
        _new_token_message = hashlib.sha256(_base_string.encode('utf-8')).hexdigest()    
        _token_data = {
            'token_message': _new_token_message,
            'token_crc': _encrypted_server_now, 
        }
        _token_data = ApiCrypto.encrypt(base_key = base_key, string_message = json.dumps(_token_data))
        return _token_data 
