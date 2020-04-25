import xlrd

def create(file_path):
    try:
        wb = xlrd.open_workbook(file_path)
        sheet = wb.sheet_by_index(0)
    except Exception:
        return "Error: Cannot read the excel. Please make sure you have entered the correct path."

    response = []
    for i in range(1, sheet.nrows):
        value = {}
        for j in range(0,sheet.ncols):
            temp = {}
            try:
                a = str(sheet.cell_value(i, j))
                temp[sheet.cell_value(0, j)] = a
                value.update(temp)
            except Exception:
                pass
        response.append(value)

    return response