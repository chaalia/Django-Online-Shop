from django.test import TestCase
from selenium import webdriver
from cart.forms import CartAddProductForm
import hashlib
from .models import Product, Category

# class FunctionalTestCase(TestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Firefox()

# def test_is_there_home_page(self):
#     self.browser.get("http://127.0.0.1:8000/en")
#     # text = self.browser.find_element_by_id("text")
#     # print(text)
#     # text.send_keys("hello")
#     # self.browser.find_element_by_name('submit').click()
#     # self.assertIn('install', self.browser.page_source)
#     c = self.browser.page_source.find('install')
#     print(c)
#     assert c
#
# def tearDown(self):
#     self.browser.quit()


class unitTestCase(TestCase):

    def test_home_homepage(self):
        response = self.client.get('/en/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/products/list.html')

    def test_cart_form(self):
        form = CartAddProductForm(data={'quantity':15})
        self.assertTrue(form.is_valid())

    def test_hash_text(self):
        hashtext = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', hashtext)


    def test_prod(self):
        product = Product()
        category = Category()
        category.name = "tsts"
        category.save()
        product.category = category
        product.name = "test"
        product.slug = "test"
        product.price = "150"
        product.save()
        return product

    def test_product_object(self):
        product = self.test_prod()
        test_prod = Product.objects.get(name="test")
        self.assertEqual(product.name, str(test_prod))

    def test_viewing_cart(self):
        # product = self.test_prod()
        response = self.client.get("/en/cart/")
        self.assertEqual(response.status_code, 200)

