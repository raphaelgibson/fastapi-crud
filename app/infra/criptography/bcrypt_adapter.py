import bcrypt

from app.data.protocols.index import Hasher


class BcryptAdapter(Hasher):
    async def hash(self, plaintext: str) -> str:
        salt = bcrypt.gensalt()
        digest = bcrypt.hashpw(plaintext.encode('utf-8'), salt)

        return digest.decode('utf-8')
