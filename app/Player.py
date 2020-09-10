from functools import total_ordering


@total_ordering
class Player:
    def __init__(self, last, first, name, country, dob="", dod=""):
        self.last = last
        self.first = first
        self.name = name
        self.country = country
        self.dob = dob
        self.dod = dod

        # Simplify props to feed in comparators by whitelisting props
        self.__compare_props = ("last", "first", "name", "country", "dob", "dod")

    def contains(self, keywords):
        contains = False
        keywords = keywords.lower()

        for key in self.__compare_props:
            if keywords in getattr(self, key).lower():
                contains = True
                break

        return contains

    def print(self):
        text = """
Last name: {}
First name: {}
Name: {}
Country: {}
Date of birth: {}
Died: {}"""\
            .format(*self.format_props())

        print(text)

    def format_props(self):
        list = []
        for key in self.__compare_props:
            list.append(getattr(self, key) or "-")

        return list

    def __lt__(self, other):
        lt = False

        # Iterate through whitelisted props
        for key in self.__compare_props:
            value1 = getattr(self, key)
            value2 = getattr(other, key)

            if value1 == value2:
                continue
            else:
                lt = value1 < value2
                break

        return lt

    def __eq__(self, other):
        eq = True

        # Iterate through whitelisted props
        for key in self.__compare_props:
            if getattr(self, key) != getattr(other, key):
                eq = False
                break

        return eq
