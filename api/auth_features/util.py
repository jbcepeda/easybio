import logging
from cryptography.fernet import Fernet
import base64

logger = logging.getLogger(__name__)
class ApiCrypto(object):
    def encrypt(s, m):
        em = None
        try:
            # key = Fernet.generate_key()
            # logger.debug("GENERATE KEY: {} {}".format(type(key),key))
            # dk = key.decode()
            # logger.debug("DECODE KEY: {} {}".format(type(dk),dk))

            # logger.debug("S KEY: {} tipo:{} encode:{}".format(s, type(s.encode()),s.encode()))

            f = Fernet(s.encode())
            em = f.encrypt(m.encode())
            # logger.debug("FERNET  em:{}".format(em))
        except Exception as ex:
            logger.error(str(ex))
        return em.decode()
    
    def decrypt(s,em):
        m = None
        try:
            f = Fernet(s.encode())
            m = f.decrypt(em.encode())
            logger.debug("decryt  m:{}".format(m.decode()))
        except Exception as ex:
            logger.error(str(ex))
        return m.decode()