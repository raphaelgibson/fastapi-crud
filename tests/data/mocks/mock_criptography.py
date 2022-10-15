from uuid import uuid4

from app.data.protocols.index import Hasher


class HasherSpy(Hasher):
    digest = str(uuid4())
    plaintext: str

    async def hash(self, plaintext: str) -> str:
        self.plaintext = plaintext

        return self.digest
