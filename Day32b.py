def email_validator(arr: list):
    valid_emails = []
    for email in arr:
        if "@" in email and email.count('@') == 1 and email[-4:] == '.com':
            if email[0] != '@':
                valid_emails.append(email)
                # checking if list with emails is empty
        elif len(valid_emails) == 0:
            return 'All emails are invalid'

    return f'The list of valid emails is: {valid_emails}'


emails = ['benchil@gmail.com', 'cost@mail.com', '@lis.com']

print(email_validator(emails))
