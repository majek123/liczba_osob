from functions import *
def test1():
    assert ile_osob(1,1,1) == 0
    assert ile_osob(20, 50, 2) == 266
    assert ile_osob(20, 50, -3) == 0
    assert ile_osob(20, 50, "dwa") == 0
    assert ile_osob(20, 50, 2.5) == 0
    assert ile_osob(20, -50, -3) == 0
    assert ile_osob(10.5, 30.7, 3) == 128

def test2():
    assert ile_ze_srodkami(100, "T") == 110

    assert ile_ze_srodkami(87, "N") == 43