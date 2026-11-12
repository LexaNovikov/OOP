class Mixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))
    def __repr__(self) -> str:
        attributes = ", ".join(repr(v) for v in self.__dict__.values())
        return f"{self.__class__.__name__}({attributes})"