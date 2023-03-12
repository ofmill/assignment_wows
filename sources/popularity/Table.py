import re


class Table:
    _headers: dict
    _rows: list

    def __init__(self, headers: dict, rows: list):
        self._headers = headers
        self._rows = rows

    def add_header(self, name, index):
        self._headers[name] = index

    def get_headers(self):
        return self._headers

    def get_size(self):
        return len(self._rows)

    def get_value(self, row_index, header) -> str:
        return self._rows[row_index][self._headers[header]]

    def get_numeric_value(self, row_index, header) -> float:
        raw_value = self.get_value(row_index, header)
        matches = re.match("(\d{1,3}([.,]{1}\d{3}){0,})", raw_value)
        if matches:
            return float(str.replace(matches[0], ",", "").replace(".", ""))
        return 0
