from shop.views import add_like, comments_list, create_comment, product_list, product_create, product_delete, product_detail, product_update, create_category, category_list
from account import urls

urlpatterns = [
    ('products/', product_list),
    ('add-product/', product_create),
    ('delete-product/id', product_delete),
    ('product-detail/id', product_detail),
    ('product-update/id', product_update),

    ('categories/', category_list),
    ('category-create/', create_category),

    ('comments/', comments_list),
    ('add-comment/email', create_comment),

    ('add-like/email', add_like)
]
urlpatterns += urls.urlpatterns