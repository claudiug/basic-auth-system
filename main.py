from basic import BaseDecorator

class CatDecorator(BaseDecorator):
    def make_cat_admin(self):
        return self.kwargs['cat'].is_admin

    def make_user_admin(self):
        return self.kwargs['user'].is_admin and self.kwargs['bonus'].positive


class User:
    def __init__(self, is_admin):
        self.is_admin = is_admin


class Bonus:
    def __init__(self, positive):
        self.positive = positive


user = User(is_admin=True)
bonus = Bonus(positive=True)


@CatDecorator(cat=user)
def make_cat_admin():
    print('Cat is admin')


@CatDecorator(user=user, bonus=bonus)
def make_user_admin():
    print('User is admin')


if __name__ == '__main__':
    print('Allow decorator')

    # Call the decorated function
    make_user_admin()
    make_cat_admin()
