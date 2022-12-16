import pytest
import nobel_prize


test_data = [('100', '1', 100), ('100', '1/3', 33.333), ('1000', '1/2', 500)]


@pytest.mark.parametrize('total_pris, andel, resultat', test_data)
def test_calculate_prize_share(total_pris, andel, resultat):
    assert nobel_prize.calculate_prize_share(total_pris, andel) == resultat
