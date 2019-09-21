import pandas as pd
from custome_exception import FileFormatError, FileWriteError, FileReadError
from constants import literatls


class FileHandler:
    @classmethod
    def read_file(cls, filename, format, mode="r"):
        """

        :param filename: valid file name
        :type filename: string
        :param format: (csv/txt)
        :type format: string
        :return: data
        :rtype: Dataframe/stream of bites depending on format
        """
        try:
            with open(filename, mode) as file:
                if format == literatls["CSV"]:
                    output = pd.read_csv(filename, header=None).fillna("")
                elif format == literatls["TXT"]:
                    output = open(filename)
                else:
                    raise FileFormatError("Wrong file format")
        except Exception:
            raise FileReadError("Error File Reading File")

        return output

    @classmethod
    def write_file(self, filename, query, result):
        """

        :param filename: valid file name
        :type filename: string
        :param query: query on which search happened
        :type query: string
        :param result: result of query
        :type result: dict
        :return:
        :rtype:
        """
        with open(filename, 'a') as file:
            try:
                file.write("Matches for:{}\n".format(query))
                if len(result) > 0:
                    for index, record in enumerate(result, 1):
                        file.write("Result {}:{},{},{},{}\n".format(index, record[literatls["LASTNAME"]],
                                                                    record[literatls["FIRSTNAME"]],
                                                                    record[literatls["STATE"]],
                                                                    record[literatls["PHONE_NUMBER"]]))
                else:
                    file.write("No Result Found\n")
            except:
                raise FileWriteError("Error While writing file")

        return
