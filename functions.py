def ile_osob(dl, szer, pietra):
    if isinstance(dl, str) or isinstance(szer, str) or isinstance(pietra, str):
        return 0
    elif isinstance(pietra, float):
        return 0
    elif dl < 1 or szer < 1 or pietra < 1:
        return 0

    ilosc = dl * szer * pietra / 7.5
    if ilosc < 0:
        return 0

    else:
        return int(ilosc)



def ile_ze_srodkami(ilosc_osob, srodki):
    if srodki =="T":
        return int(ilosc_osob * 1.1)
    elif srodki == "N":
        return int(ilosc_osob * 0.5)
    else:
        return 0
