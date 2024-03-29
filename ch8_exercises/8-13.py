def build_profile(first, last, **user_info):
    """Builds dictionary containing information about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
my_profile = build_profile('mochi', 'silly', fur='black',
                           eyes='green', behavior='super silly')
print(my_profile)