def login(base, user, password):  # O(1) т.к. обращается с конкретными данными на проверку их
    try:
        if base[user]["password"] == password:
            if base[user]["activ"] == True:
                rez = f"hellow {user}"
            else:
                rez = f"Hellow {user}, please activate you accaunt"
        else:
            rez = "Your passworn is incorrect"
    except:
        rez = "Your Login is incorrect"
    return rez


def login2(base, user, password):  # O(n log n)
    for i in base:
        if i == user:
            if base[i]["password"] == password and base[i]["activ"] == True:
                rez = f"hellow {user}"
            elif base[i]["password"] == password and base[i]["activ"] == False:
                rez = f"Hellow {user}, please activate you accaunt"
            else:
                rez = "Your passworn is incorrect"
        else:
            rez = "Login incorrect"
    return rez


base = {
    "admin": {"password": "123321", "activ": True},
    "user": {"password": "123", "activ": False}
}

user = 'user'
password = '123'

print(login2(base, user, password))
