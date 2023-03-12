import pytest
import sources.popularity.WikiTableParser as WikiTableParser

page_url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"

table_name = "Programming languages used in most popular websites"

column_header = "Popularity"

threshold_values = [10 ** 7,
                    1.5 * 10 ** 7,
                    5 * 10 ** 7,
                    10 ** 8,
                    10 ** 9,
                    1.5 * 10 ** 9]

error_template = "{} (Frontend:{}|Backend:{}) has {} unique visitors per month. (Expected more than {})"


@pytest.mark.parametrize("threshold", threshold_values)
def test_popularity_with_threshold(threshold):
    table = WikiTableParser.get_table(page_url, table_name)

    errors = []
    for i in range(table.get_size()):
        popularity = table.get_numeric_value(i, column_header)
        if popularity < threshold:
            errors.append(error_template
                          .format(table.get_value(i, "Websites"),
                                  table.get_value(i, "Front-end"),
                                  table.get_value(i, "Back-end"),
                                  popularity,
                                  threshold))
    if len(errors) > 0:
        print("\n")
        for error in errors:
            print(error)
        assert len(errors) == 0
