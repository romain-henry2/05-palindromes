#### Fonction secondaire


def ispalindrome(p):
    n = len(p)
    for i in range(n // 2):
        if p[i] != p[n - 1 - i]:
            break
    else:
        return True
    return False

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()