class Property:
    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        self._value = value

    def __get__(self, instance, owner):
        return self._value
