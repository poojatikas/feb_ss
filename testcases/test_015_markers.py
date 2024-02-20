import pytest

class Test_015_markers():

    @pytest.mark.skip
    def test_001_add(self):
        a=20
        b=10
        add=a+b
        if(add==30):
          print('\n----------ADDITION SUCESSFUL--------')
          print('\nRESULTS = ', add)
          assert True
        else:
            print('\n---------invalid operation')
            assert False

    @pytest.mark.xfail
    def test_002_sub(self):
        a=20
        b=10
        sub=a+b
        if(sub==10):
            print('\n---------substraction sucessfully--------')
            print('\nRESULTS =', sub)
            assert True
        else:
            print('\n---------invalid operation------------')
            assert False


    def test_003_mul(self):
        a=20
        b=10
        mul=a*b
        if(mul==200):
            print('\n----------multiplication sucessfully-----------')
            print('\nRESULTS =',mul)
            assert True
        else:
            print('\n---------invalid operation-------')
            assert False

    @pytest.mark.skipif
    def test_004_div(self):
        a=20
        b=10
        div=a/b
        if(div==2):
            print('\n--------------division sucessfully----------')
            print('\nRESULTS = ',div)
            assert True
        else:
            print('\n-------------invalid operation---------------')
            assert False
