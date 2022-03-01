chave = input("Digite a base para sua senha:")

senha = ""
for letra in chave:
    if letra in "Aa":
        senha=senha + "@"
    elif letra in "Bb":
        senha = senha + "11"

    elif letra in "Cc":
        senha = senha + "12"

    elif letra in "Dd":
        senha = senha + "13"

    elif letra in "Ee":
        senha = senha + "14"

    elif letra in "Ff":
        senha = senha + "15"

    elif letra in "Gg":
        senha = senha + "5"

    elif letra in "Hh":
        senha = senha + "8"

    elif letra in "Ii":
        senha = senha + "1"

    elif letra in "Jj":
        senha = senha + "9"

    elif letra in "Kk":
        senha = senha + "5"

    elif letra in "Ll":
        senha = senha + "!"

    elif letra in "Mm":
        senha = senha + ">"

    elif letra in "Nn":
        senha = senha + "<"

    elif letra in "Oo":
        senha = senha + "0"

    elif letra in "Pp":
        senha = senha + "?"

    elif letra in "Qq":
        senha = senha + "#"


    elif letra in "Rr":
        senha = senha + "#"

    elif letra in "Ss":
        senha = senha + "$"

    elif letra in "Tt":
        senha = senha + "%"

    elif letra in "Uu":
        senha = senha + "8"

    elif letra in "Vv":
        senha = senha + "6"

    elif letra in "Ww":
        senha = senha + "2"

    elif letra in "Xx":
        senha = senha + "="

    elif letra in "Yy":
        senha = senha + "?"

    elif letra in "Zz":
        senha = senha + "^"

    else: senha = senha + letra
    print(senha)
