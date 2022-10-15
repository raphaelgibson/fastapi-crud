class MissingParamError(Exception):
    def __init__(self, param_name: str):
        super()
        self.param_name = param_name

    def __str__(self):
        return f'{self.__class__.__name__}: Missing param: {self.param_name}'

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__
