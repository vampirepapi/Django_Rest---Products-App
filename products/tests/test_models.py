from products.models import ProductItem

# @pytest.mark.django_db
def test_product_item(db):
    product_name = ProductItem.objects.create(product_name="neo")
    product_price = ProductItem.objects.create(product_price="30")
    product_quantity = ProductItem.objects.create(product_quantity = "3")
    assert product_name.product_name == "neo"
    assert product_price.product_price == "30"
    assert product_quantity.product_quantity == "3"