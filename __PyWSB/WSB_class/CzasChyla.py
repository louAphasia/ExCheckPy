class Czas:

    def __init__(self, hour_or_descr, minutes=None):
        if minutes is None:
            as_list = hour_or_descr.split()
            self._godz = int(as_list[0])
            self._minuty = int(as_list[2])
        else:
            self._godz = hour_or_descr
            self._minuty = minutes

        if self._godz > 0 and self._minuty < 0:
            raise InvalidTimeException("Hour is positive and minutes are negative")

    def to_string(self):
        return "{} godz {} min".format(self._godz, self._minuty)

    def add(self, oth):
        h = self._godz + oth._godz + int((self._minuty + oth._minuty) / 60)
        m = (self._minuty + oth._minuty) % 60
        return Czas(h, m)

    def sub(self, oth):
        h = self._godz - oth._godz
        if self._minuty - oth._minuty < 0:
            h = h - 1 - int((self._minuty - oth._minuty) / 60)
        m = (self._minuty - oth._minuty) % 60
        return Czas(h, m)

    def multiply(self, ile):
        h = self._godz * ile + int(self._minuty * ile / 60)
        m = (self._minuty * ile) % 60
        return Czas(h, m)


class InvalidTimeException(Exception):
    def __init__(self, msg):
        super().__init__(msg)