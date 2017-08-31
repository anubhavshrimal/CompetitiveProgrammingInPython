

def hideEmail(userData):
    email = userData.strip().split('E:')[1].strip()
    emailName, domain = email.split('@')
    hiddenEmail = emailName[0]+'*****'+emailName[-1]+'@'+domain

    return 'E:'+hiddenEmail


def phone_format(n):
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


def hidePhone(userData):
    phone = list(userData.strip().split('P:')[1].strip())
    plus = False

    if phone[0] == '+':
        plus = True

    temp = []

    for ch in phone:
        if 48 <= ord(ch) <= 57:
            temp.append(ch)

    temp = list(phone_format(''.join(temp)))

    for i in range(0, len(temp)-4):
        if 48 <= ord(temp[i]) <= 57:
            temp[i] = '*'

    if plus:
        return 'P:+' + ''.join(temp)
    else:
        return 'P:' + ''.join(temp)


userData = input()

while userData:
    if userData[0] == 'E':
        print(hideEmail(userData))
    else:
        print(hidePhone(userData))

    try:
        userData = input()
    except EOFError:
        userData = ''

