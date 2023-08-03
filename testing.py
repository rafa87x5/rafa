lista = ['20', '50', '19', '60', '43', '4', '13', '26', '32', '28', '7',
         '11', '6', '9', '67', '24', '8', '29', '2', '4', '10', '7', '15', '17']


def re_stock():
    lowest = int(lista[0])
    for item in lista:
        if lowest > int(item):
            lowest = int(item)
    return lowest



