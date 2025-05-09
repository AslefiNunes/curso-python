def notas(*lst, sit = False):
    dic = {}
    dic['total'] = len(lst)
    dic['maior'] = max(lst)
    dic['menor'] = min(lst)
    dic['medeia'] = sum(lst) / len(lst)
    if sit:
        if dic['medeia'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['medeia'] >= 5:
            dic['situação'] = 'RAZOAVEL'
        else:
             dic['situação'] = 'RUIM'
    return dic


resp = notas(5.5, 9.5, 10, 6.5, sit = True)
print(resp)