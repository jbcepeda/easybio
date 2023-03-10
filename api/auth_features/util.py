import logging
from cryptography.fernet import Fernet
import base64

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