import string


# static methods are methods that can be called without instantiating a class
# useful for helper functions that are stored in a class
class StringHelper:
    @staticmethod
    def remove_punctuations(text: str):
        punctuations = string.punctuation

        translation_table = str.maketrans("", "", punctuations)

        return text.translate(translation_table)


class Authenticator:
    # class property is shared across all instances
    password = "12345"

    # as a convention we use 'cls' instead of 'self' in class method
    # class method is able to make changes across all class instances
    # we dont need to instantiate a class to call class method
    # useful to create singleton (1 single instance across the whole app)
    @classmethod
    def set_password(cls, new_password: str):
        cls.password = new_password

    @classmethod
    def get_password(cls):
        return cls.password


if __name__ == "__main__":

    with_punctuation = "Crazy said: Let's have some food!"
    
    no_punctuation = StringHelper.remove_punctuations(with_punctuation)

    print(no_punctuation)

    auth1 = Authenticator()

    auth2 = Authenticator()

    print(auth1.get_password())

    auth2.set_password('heyyoo')

    print(auth2.get_password())

    print(auth1.get_password())

    # we can call class methods without instantiating
    Authenticator.set_password('abc')
    print(auth1.get_password())
