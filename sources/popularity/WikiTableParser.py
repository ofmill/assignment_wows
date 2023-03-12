import re
import requests

from sources.popularity.Table import Table
from lxml import etree
from lxml.html import HtmlElement


def get_table(url: str, table_name: str) -> Table:
    page_obj = __request_page(url)
    table_obj = __find_table(page_obj, table_name)
    headers = __parse_headers(table_obj)
    rows = __parse_rows(table_obj)
    return Table(headers, rows)


def __request_page(url: str) -> HtmlElement:
    response = requests.get(url)
    return etree.HTML(response.text)


def __find_table(page_obj: HtmlElement, table_name) -> HtmlElement:
    found_tables = page_obj.xpath("//table[descendant::caption[contains(text(), '{}')]]".format(table_name))
    if len(found_tables) == 0:
        raise Exception("No table found by provided name '{}'".format(table_name))
    if len(found_tables) > 1:
        raise Exception("Several tables found by provided name '{}'".format(table_name))
    return found_tables[0]


def __parse_headers(table: HtmlElement) -> dict:
    headers = dict()
    for idx, header in enumerate(table.findall(".//th")):
        if header.find("./a") is not None:
            headers[str.replace(header.find("./a").text, "\n", "")] = idx
        else:
            headers[str.replace(header.text, "\n", "")] = idx
    return headers


def __parse_rows(table_obj: HtmlElement) -> list:
    rows = []
    for row_obj in table_obj.findall(".//tr"):
        row = []
        for cell in row_obj.findall(".//td"):
            row.append(__parse_cell_as_string(cell))
        if len(row) > 0:
            rows.append(row)
    return rows


def __parse_cell_as_string(cell: HtmlElement):
    content = ""
    for text in cell.itertext():
        # skip reference links (e.g. [2])
        if not re.match("^.*(\[\d+\])|(\n).*$", text):
            content += str.replace(text, "\n", "")
    return content
