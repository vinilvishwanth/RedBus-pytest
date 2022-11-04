import xlrd
from Library.config import Config

class ReadExcel:

    def read_testdata(self,sheetname):
        wb = xlrd.open_workbook(Config.testdata_path)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header = next(rows)
        data = []

        for row in rows:
            if columns == 1:
                data.append(row[0].value)
            else:
                values = ()
                for j in range(columns):
                    values += (row[j].value,)
                data.append(values)
        return data


    def read_locator(self, sheetname):
        wb = xlrd.open_workbook(Config.locators_path)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        dict_1 = {}
        for row in rows:
            dict_1[row[0].value] = (row[1].value, row[2].value)
        return dict_1
