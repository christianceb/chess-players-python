import csv
import os


class Parser:
    __encoding = "utf-8"

    def __init__(self, path):
        self.list = []

        if os.path.exists(path):
            with open(path, newline='', encoding=self.__encoding) as csvfile:
                reader = csv.reader(
                    csvfile,
                    quotechar='"',
                    delimiter=',',
                    quoting=csv.QUOTE_ALL,
                    skipinitialspace=True,
                    escapechar='\\'
                )

                # Skip Headers
                next(reader, None)

                self.list = list(reader)