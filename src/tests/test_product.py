from daos.product_dao import ProductDAO
from models.product import Product
import pytest

dao = ProductDAO()


@pytest.fixture(scope="module", autouse=True)
def cleanup_after_tests():
    yield
    dao.delete_all()
    dao.close()


def test_product_insert():
    product = Product(
        None,
        name="Test Product",
        brand="aaa",
        price=9.99,
    )
    _id = dao.insert(product)
    products = dao.select_all()
    brands = [p.brand for p in products]
    assert product.brand in brands


def test_product_update():
    product = Product(
        None,
        name="Test Product",
        brand="aaa",
        price=10,
    )
    id = dao.insert(product)
    product.id = id
    product.price += 10
    dao.update(product)
    updated_product = dao.select_all()
    prices = [p.price for p in updated_product if p.id == id]
    assert product.price in prices


def test_product_delete():
    product = Product(
        None,
        name="Test Product",
        brand="aaa",
        price=10,
    )
    id = dao.insert(product)
    product.id = id
    dao.delete(id)
    products = dao.select_all()
    ids = [p.id for p in products]
    assert product.id not in ids
