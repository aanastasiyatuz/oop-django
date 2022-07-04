from views import product_list, product_create, product_delete, product_detail, product_update

urlpatterns = [
    ('products/', product_list),
    ('create-product/', product_create),
    ('delete-product/id', product_delete),
    ('product-detail/id', product_detail),
    ('product-update/id', product_update),
]
