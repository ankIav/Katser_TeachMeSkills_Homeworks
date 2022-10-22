import re


# Exception raised for wrong format inputted
class WrongFormat(Exception):
    """If condition True raise matched exception
    """

    def __init__(self, email, msg='E-mail is not correct!'):
        self.msg = msg
        self.email = email
        super().__init__(self.msg)

    def __str__(self): return f'{self.email} -> {self.msg}'


# correct form to validate username
regex = re.compile(
    r'([A-Za-z0-9]+[.!#%&`*+/=?^_{|}''-])*[A-Za-z0-9]'  # username
    r'+(@(([A-Za-z0-9]+-)*[A-Za-z0-9]){,63})'           # hostname
    r'+(\.[A-Z|a-z]{2,6})+'                             # .domain type
)

# simple Database of taken e-mails
emails_list = [
    'example@example.com', 'yandex@yandex.ru', 'ya@ya.com', 'gmail@gmail.com'
]

# simple Database of correct hosts
valid_hosts = [
    'gmail.com', 'ya.ru', 'ya.com', 'yandex.ru', 'yandex.com', 'mail.ru'
]


# Description of class Email and ist methods
class Email:
    """Base class to check email"""

    # a hidden method to check correct input
    def __valid_email(self) -> bool:
        return True if re.fullmatch(regex, self.email) else False

    # a hidden method to check correct host
    def __valid_host(self) -> bool:
        return True if self.host in valid_hosts else False

    # a hidden method to check free e-mail
    def __free_email(self) -> bool:
        pattern = 'ya.ru|ya.com|yandex.ru|yandex.com'
        if (
                re.sub(pattern, 'ya.ru', self.email)
                in [re.sub(pattern, 'ya.ru', email) for email in emails_list]):
            return False
        else:
            return True

    def __init__(self, email):
        """Initializing attributes of class Email
        :param email:
        """
        self.email = email
        if self.__valid_email():
            self.host = self.email.split('@')[1]
        else:
            raise WrongFormat(self.email)

        if not self.__valid_host():
            raise WrongFormat(self.email, f'Wrong host {self.host}')

        if not self.__free_email():
            raise WrongFormat(self.email, 'This e-mail is already taken!')

    # base method to return string email
    def __str__(self): return self.email

    # method to get username from full email address
    def username(self) -> str:
        return self.email.split('@')[0]

    # method to get host name
    def hostname(self) -> str:
        return self.host.split('.')[0]

    # method to get host name
    def domain_type(self) -> str:
        return self.host.split('.')[1]

    # method to replace a host to our host
    @staticmethod
    def sub(pattern, repl, string) -> str:
        return re.sub(pattern, repl, string)

    # method to return new email list
    def list(self) -> list:
        """
        :return: email list with new added email at the end
        """
        emails_list.append(self.email)
        return emails_list
