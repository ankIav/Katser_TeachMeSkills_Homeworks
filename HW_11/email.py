from class_email import Email, WrongFormat, emails_list


print(f'E-mail Database start:{emails_list}')

# input cycle
while True:
    try:
        field = Email(input('Enter an e-mail:\n'))
    except WrongFormat as err:
        print(err)
        continue
    break


print(field.list())

# just try to use sub method and watch how it works.
print(field.sub('ya.ru|ya.com|yandex.ru|yandex.com', 'ya.ru', str(field)))
