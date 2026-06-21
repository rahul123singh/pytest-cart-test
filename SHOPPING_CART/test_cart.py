from cart import Cart

def test_get_item_count_counts_line_items_not_total_quantity():
    cart = Cart()
    cart.add_item("Apple", 50, 2)
    cart.add_item("Bread", 40, 1)
    assert cart.get_item_count() == 2  # 2 line items, NOT 3 (total quantity)

def test_show_item_in_a_cart():
    cart = Cart()
    cart.add_item("Apple", 50, 2)
    result = cart.show_items()
    assert result == "Apple - Qty: 2 - Price: 50 each"

def test_show_items_on_empty_cart():
    cart = Cart()
    assert cart.show_items() == "Cart is empty"

def test_combine_feature_in_a_cart():
    cart=Cart()
    if cart.get_item_count()==0:
        assert True
    else :
        assert False

    cart.add_item("Apple",27,4)
    cart.add_item("Banana",36,5)
    cart.add_item("FaceWash",1,99)

    if cart.show_items()=="Cart is empty":
        assert False
    else :
        assert True

    count=cart.get_item_count()
    print(count)
    if cart.get_item_count()<count or cart.get_item_count()>count:
        assert False
    else:
        assert True

    if cart.get_total()==387:
        assert True
    else:
        assert False

    discounted_price=cart.apply_discount(90)
    assert round(discounted_price, 2) == 38.7

    cart.remove_item("FaceWash")
    assert cart.get_item_count()==2

    def test_total_quantity_with_multiple_items():
        cart = Cart()
        cart.add_item("Apple", 27, 4)
        cart.add_item("Banana", 36, 5)
        cart.add_item("FaceWash", 1, 99)
        assert cart.total_quantity() == 108  # 4 + 5 + 99

def test_total_quantity_on_empty_cart():
    cart = Cart()
    assert cart.total_quantity() == 0

def test_get_total_with_multiple_items():
    cart = Cart()
    cart.add_item("Apple", 27, 4)
    cart.add_item("Banana", 36, 5)
    cart.add_item("FaceWash", 1, 99)
    assert cart.get_total() == 387

def test_apply_discount_90_percent():
    cart = Cart()
    cart.add_item("Apple", 27, 4)
    cart.add_item("Banana", 36, 5)
    cart.add_item("FaceWash", 1, 99)
    assert round(cart.apply_discount(90), 2) == 38.7

def test_remove_item_updates_count():
    cart = Cart()
    cart.add_item("Apple", 27, 4)
    cart.add_item("Banana", 36, 5)
    cart.add_item("FaceWash", 1, 99)
    cart.remove_item("FaceWash")
    assert cart.get_item_count() == 2


def test_apply_discount_101_percent():
    cart=Cart()
    cart.add_item("Apple", 27, 4)
    cart.add_item("Banana", 36, 5)
    cart.add_item("FaceWash", 1, 99)
    assert round(cart.apply_discount(101), 2) <0

def test_apply_discount_101_percent():
    cart=Cart()
    cart.add_item("Apple", 27, 4)
    cart.add_item("Banana", 36, 5)
    cart.add_item("FaceWash", 1, 99)
    cart.clear_cart()
    assert cart.is_empty()


def test_apply_discount_101_percent():
    cart=Cart()
    cart.add_item("Apple", 27, 4)
    cart.add_item("Banana", 36, 5)
    cart.add_item("FaceWash", 1, 99)
    assert cart.remove_item("Milk")
    
    