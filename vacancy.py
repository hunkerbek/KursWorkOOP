class Vacancy:
    def __init__(self, title, sallary_from, sallary_to):
        self._title = title
        self._sallary_from = sallary_from
        self._sallary_to = sallary_to
    def __str__(self):
        return f'{self._title} от:{self._sallary_from} до:{self._sallary_to}'


    def __repr__(self):
        return str(self)

    @property
    def title(self):
        return self._title

    @property
    def sallary_from(self):
        return self._sallary_from

    @property
    def sallary_to(self):
        return self._sallary_to


    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise Exception("Нельзя сравнивать")
        sallary_from1=self._sallary_from
        sallary_from2=other._sallary_from
        sallary_to1=self._sallary_to
        sallary_to2=other._sallary_to

        if sallary_from1 is None:
            sallary_from1=sallary_to1
        if sallary_from2 is None:
            sallary_from2=sallary_to2
        if sallary_to1 is None:
            sallary_to1=sallary_from1
        if sallary_to2 is None:
            sallary_to2=sallary_from2

        if sallary_from1 is None and sallary_to1 is None:
            return True
        if sallary_from2 is None and sallary_to2 is None:
            return False

        return sallary_from1<sallary_from2 or sallary_to1<sallary_to2



    def __le__(self, other):
        if not isinstance(other, Vacancy):
            raise Exception("Нельзя сравнивать")
        sallary_from1 = self._sallary_from
        sallary_from2 = other._sallary_from
        sallary_to1 = self._sallary_to
        sallary_to2 = other._sallary_to

        if sallary_from1 is None:
            sallary_from1 = sallary_to1
        if sallary_from2 is None:
            sallary_from2 = sallary_to2
        if sallary_to1 is None:
            sallary_to1 = sallary_from1
        if sallary_to2 is None:
            sallary_to2 = sallary_from2

        if sallary_from1 is None and sallary_to1 is None:
            return True
        if sallary_from2 is None and sallary_to2 is None:
            return False

        return sallary_from1 <= sallary_from2 and sallary_to1 <= sallary_to2


    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return False

        return self._title == other._title\
            and self._sallary_from == other._sallary_from\
            and self._sallary_to == other._sallary_to



