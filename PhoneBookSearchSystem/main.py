from phone_book import PhoneBook
from file_handler import FileHandler
import os
from constants import literatls, data_filename, query_filename, output_filename

if __name__ == '__main__':
    path = os.getcwd()

    phone_book = PhoneBook(path + data_filename)
    queries = FileHandler.read_file(path + query_filename, literatls["TXT"], "r")
    for lastname in queries.readlines():
        FileHandler.write_file(path + output_filename, lastname.rsplit()[0],
                               phone_book.search_on_last_name(lastname.rstrip()))
