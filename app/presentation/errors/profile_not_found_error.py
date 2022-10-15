class ProfileNotFoundError(Exception):
    def __str__(self):
        return f'{self.__class__.__name__}: Profile not found'

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__
