from django.conf import settings
# パスワードのハッシュ値を計算
from django.contrib.auth.hashers import check_password, make_password
# デフォルトのUserModel場合、下記を利用
# from django.contrib.auth import User
# Customユーザーの場合、Userオブジェクトを読み込ませる
from django.contrib.auth import get_user_model
User = get_user_model()

class AuthBackend:
    def authenticate(self, request, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        # パスワードはハッシュ値を比較して検証する
        encode = make_password(settings.ADMIN_PASSWORD)
        pwd_valid = check_password(password, encode)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None