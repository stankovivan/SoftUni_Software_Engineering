from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidNameError(Exception):
    pass


pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'
valid_mails = ['.com', '.bg', '.org', '.net']

email = input()
while email != "End":
    try:
        if len(findall(pattern_name, email.split("@")[0])[0]) <= 4:
            raise NameTooShortError(f"Name must be more than 4 characters")

        elif "@" not in email:
            raise MustContainAtSymbolError(f"Email must contain @")
        elif len(findall(pattern_name, email.split("@")[0])[0]) != len(email.split('@')[0]):
            raise InvalidNameError("Email name should contain only letters, numbers and underscores")

        elif findall(pattern_domain, email.split("@")[1])[0] not in valid_mails:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_mails)}")
        print(f"Email is valid")
    except IndexError:
        print(f"Invalid email")
    email = input()
