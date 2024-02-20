class Test_014_03():

    def test_014_03_multiplication(self):

        a=10
        b=5
        mul=a*b
        if(mul==50):
            print('\n-------------multiplication is sucessful----------')
            print('\nRESULTS = ',mul)
            assert True
        else:
            print('\n-------------SORRY INALID OPERATION----------')
            assert False