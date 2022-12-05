# We have considered the following rules for username and password:

# We want to keep the usernames 'quera' and 'codecup' for ourselves. No one is allowed to join with these usernames.
# Username less than 4 characters is too short and is not allowed.
# Also, for the security of users, a user whose password is less than 6 characters or only consists of numbers is not allowed to become a member.
def check_registration_rules(**kwargs):
    accept_list = []
    for username in kwargs :
        if username != "quera" and username != "codecup" and len(username) > 3 and len(kwargs[username]) > 5 :
            if any(char.islower() for char in kwargs[username]) or any(char.isupper() for char in kwargs[username]):
                accept_list.append(username)
    return accept_list
#_________________example________________#
# print(check_registration_rules(nnno2oo2='12aD6',nnnooo='123456',ali='dad65f6s',mali='dad65f6s',username='password', sadegh='He3@lsa', quera='kLS45@l$',codecup='4982fsf3',mohamad='1112ADF565'))
#output : ['mali', 'username', 'sadegh', 'mohamad']