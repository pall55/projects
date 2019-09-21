import pandas as pd
from us import states
from constants import lastnames, literatls
from file_handler import FileHandler


class PhoneBook:

    def __init__(self, filename):
        """

        :param filename:
        :type filename: string
        """
        raw_book = FileHandler.read_file(filename, literatls["CSV"])
        self.book = self.assemble_book(raw_book)

    def assemble_book(self, raw_book):
        """

        :param raw_book: datafrme with data
        :type raw_book: pandas dataframe
        :return: dictionary of records with phone_number as key
        :rtype: dict
        """
        book_dictionary = dict()
        for row in raw_book.itertuples():
            temp_list = [literatls["FIRSTNAME"], literatls["LASTNAME"], literatls["STATE"]]
            for elem in row[1:]:
                if elem == "":
                    continue
                temp_split = elem.split(" ")
                num = [i for i in list(elem) if i.isdigit()]
                if len(num) == 10:
                    number = "".join(num)
                elif len(num) > 0:
                    number = "".join(num) + "_Invalid"
                elif elem in [e.name for e in states.STATES]:
                    temp_list[2] = elem
                elif len(temp_split) == 2:
                    temp_list[0:2] = temp_split[0:2]
                elif elem in lastnames:
                    temp_list[1] = elem
                else:
                    temp_list[0] = elem
            book_dictionary[number] = temp_list

        return book_dictionary

    def search_on_last_name(self, last_name):
        """

        :param last_name: search query
        :type last_name: string
        :return: dictionary of filtered records
        :rtype: dict
        """

        temp_df = pd.DataFrame(self.book).T.reset_index()
        temp_df.columns = [literatls["PHONE_NUMBER"], literatls["FIRSTNAME"], literatls["LASTNAME"], literatls["STATE"]]
        temp_df["lowercase"] = temp_df[literatls["LASTNAME"]].str.lower()
        temp_df = temp_df[temp_df["lowercase"] == last_name.lower()]
        temp_df.drop(["lowercase"], inplace=True, axis=1)
        return temp_df.sort_values(literatls["FIRSTNAME"]).to_dict(orient='record')
