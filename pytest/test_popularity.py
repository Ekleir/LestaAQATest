from main import get_data_from_table
import pytest


@pytest.mark.parametrize('min_popularity', [10 ** 7,
                                            1.5 * 10 ** 7,
                                            5 * 10 ** 7,
                                            10 ** 8,
                                            5 * 10 ** 8,
                                            10 ** 9,
                                            1.5 * 10 ** 9])
def test_popularity(min_popularity):
    table_data = get_data_from_table()

    errors = []
    for row in table_data:
        if row.popularity < min_popularity:
            errors.append(
                f'{row.website} (Frontend:{row.frontend}|Backend:{row.backend} has {row.popularity}'
                f' unique visitors per month. (Expected more then {min_popularity})')

    #for better reading
    assert not errors, '\n'.join(errors)


if __name__ == '__main__':
    pytest.main()
