from processing.clean import clean_price, clean_stock


def test_clean_price_english():
    assert clean_price("620,000 تومان") == 620000


def test_clean_stock_available():
    assert clean_stock("موجود") == 1

def test_clean_price_persian():
    assert clean_price("۲۲۰,۰۰۰ تومان") == 220000

def test_clean_stock_unavailable():
    assert clean_stock("ناموجود") == 0