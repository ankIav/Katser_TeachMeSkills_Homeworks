### Task # 1:

---
***RU***:Сделать генератор геометрической прогрессии.

***EN***:Make a geometric progression generator.

---
## Result:
This program uses:
- the _yield_ statement in a hidden class static method **__yield** to populate a list of progression elements.
- hidden static method **__sum** with a _recursion_ to find the sum of elements of a progression in a given range.
- empty input is equivalent to the default value = 1.
-     b(1) - start element of GP
      q - factor GP
      c - count of elements GP
      n - N element of GP to find
- the class method decorator is implemented, but it is compensated at the input stage, so always True.
---
### Task 3*:
_**RU**_:Правила валидации е-мэйлов "**username@hostname**":
**username** может в себе содержать:
- латиницу
- цифры
- знаки .!#%&`*+/=?^_{|}''-
- *знаки выше, за исключением первого и последнего, которые не могут повторяться.

**hostname** состоит из нескольких компонентов, разделенных точкой и не превышающих 63 символа. Компоненты, в свою очередь, состоят из латинских цифр и дефисов, причем дефисы не могут быть в начале или конце компонента.

_**EN**_:Rules for e-mail validation "**username@hostname**":
**username** may contain:
- Latin
- numbers
- characters .!#%&`*+/=?^_{|}''-
  - *characters above, except for the first and last, which cannot be repeated.

**hostname** consists of several components, separated by a dot, and does not exceed 63 characters. Components, in turn, consist of Latin numerals and hyphens, and hyphens cannot be at the beginning or end of a component.

---
## Result:
This program uses:
-  _**re**_ library for regex string and it looks so:


    regex = re.compile(
    r'([A-Za-z0-9]+[.!#%&`*+/=?^_{|}''-])*[A-Za-z0-9]'  # username
    r'+(@(([A-Za-z0-9]+-)*[A-Za-z0-9]){,63})'           # hostname
    r'+(\.[A-Z|a-z]{2,6})+'                             # .domain type
    )

- Class Email can return _username_, _hostname_ and _domain type_ apart with methods **username**, **hostname** and **domain_type** respectively. 
- Also in **_email.py_** you can use you oun pattern to return email with changed host with **sub** method.
- get updated list of e-mails with method **list**.

To example I created valid e-mail list:
    
    emails_list = [
    'example@example.com', 'yandex@yandex.ru', 'ya@ya.com', 'gmail@gmail.com'
    ]
and hosts:

    valid_hosts = [
    'gmail.com', 'ya.ru', 'ya.com', 'yandex.ru', 'yandex.com', 'mail.ru'
    ]
I made my own Error **WrongFormat**, which raises with my 3 validations:
- if e-mail does not match with regex pattern in hidden method **__valid_email**:
     
      def __valid_email(self) -> bool:
          return True if re.fullmatch(regex, self.email) else False
- if host supported in list _valid_hosts_ with a hidden method **__valid_host**:

      def __valid_host(self) -> bool:
          return True if self.host in valid_hosts else False
- for example host _ya.ru_ is equal _ya.ru_, _ya.com_, _yandex.ru_ and _yandex.com_ and if usernames the same then this will raise error:

        def __free_email(self) -> bool:
            pattern = 'ya.ru|ya.com|yandex.ru|yandex.com'
            if (
                re.sub(pattern, 'ya.ru', self.email)
                in [re.sub(pattern, 'ya.ru', email) for email in emails_list]):
            return False
            else:
                return True
### All validations check in **init** magic method:


        if self.__valid_email():
            self.host = self.email.split('@')[1]
        else:
            raise WrongFormat(self.email)

        if not self.__valid_host():
            raise WrongFormat(self.email, f'Wrong host {self.host}')

        if not self.__free_email():
            raise WrongFormat(self.email, 'This e-mail is already taken!')