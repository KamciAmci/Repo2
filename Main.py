# lista użytkowników i haseł
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

# funkcja logowania
def login(user, password):
    if user in users and password == users[user]:
        print("Zalogowano jako", user)
    else:
        print("Błąd logowania")

# odczytanie komendy z linii poleceń
import sys
args = input("Podaj polecenie: ").split()

# wywołanie funkcji logowania z podanymi argumentami
if len(args) == 2 and args[0] == "login":
    login(args[1], input("Hasło: "))
else:
    print("Nieprawidłowe polecenie")