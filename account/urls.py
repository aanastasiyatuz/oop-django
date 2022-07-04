from .views import register, users_list, login, logout, user_profile

urlpatterns = [
    ('register/', register),
    ('users-list/', users_list),
    ('login/email', login),
    ('logout/email', logout),
    ('profile/email', user_profile)
]