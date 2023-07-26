class Contact:
    def __init__(self, first_name: str = "", middle_name: str = "", last_name: str = "", birthday: str = "",
                 tel_number: str = "", email: str = "") -> None:
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self.name: str = (self.first_name + " " + self.middle_name + " " + self.last_name).replace("  ", " ")
        self._birthday = birthday
        self._tel_number = tel_number
        self._email = email

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self._first_name = value

    @property
    def middle_name(self) -> str:
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value: str) -> None:
        self._middle_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        self._last_name = value

    @property
    def tel_number(self) -> str:
        return self._tel_number

    @tel_number.setter
    def tel_number(self, value: str) -> None:
        self._tel_number = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    @property
    def birthday(self) -> str:
        return self._birthday

    @birthday.setter
    def birthday(self, value: str) -> None:
        self._birthday = value


