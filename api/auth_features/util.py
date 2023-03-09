from cryptography import fernet

class ApiCrypto(object):
    def crypt(s, m):
        f = Fernet(s)
        em = f.encrypt(m)
        return em
    
    def decrypt(s,em):
        f = Fernet(s)
        m = f.decrypt(em)
        return m                