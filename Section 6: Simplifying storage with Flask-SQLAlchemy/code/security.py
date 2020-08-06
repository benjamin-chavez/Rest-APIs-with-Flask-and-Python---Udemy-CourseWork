from werkzeug.security import safe_str_cmp
from user import User

# We don't need the following code once we have the
# sqlite database

# users = [
#     User(1, 'bob', 'asdf')
# ]

# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    # user = username_mapping.get(username, None)
    user = User.find_by_username(username)  # with new User method
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    # return userid_mapping.get(user_id, None)
    return User.find_by_id(user_id)
