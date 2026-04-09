from eapp.dao import load_products
from test.test_base import test_app, sample_products, test_session


def test_all(sample_products):
    actual_products = load_products()
    assert len(actual_products) == len(sample_products)

def test_paging(test_app, sample_products):
    actual_products=load_products(page=1)
    assert len(actual_products) == test_app.config['PAGE_SIZE']
    actual_products=load_products(page=3)
    assert len(actual_products)==1

def test_products_with_kw(sample_products):
    actual_products=load_products(kw='iPhone')

    assert len(actual_products)==3
