def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    req=0
    c1=c2=c3=c4=1
    if re.search(r'\d',password):
        c1=0
    if re.search(r'[A-Z]',password):
        c2=0
    if re.search(r'[a-z]',password):
        c3=0
    if re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]',password):
        c4=0
    req=c1+c2+c3+c4
    if n<6:
        req=max(req,6-n)
    return req