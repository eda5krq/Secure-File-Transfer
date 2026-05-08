from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend


def generate_rsa_keys():
    #gjeneron keys RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key, private_key.public_key()

def serialize_public_key(public_key) -> bytes:
    #kthen public key ne PEM bytes per e dergu
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

def load_public_key_from_bytes(data: bytes):
    #ngarkon public key nga PEM bytes
    return serialization.load_pem_public_key(data, backend=default_backend())