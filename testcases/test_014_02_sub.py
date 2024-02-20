class Test_014_02():

    def test_014_02_substraction(self):

        a=10
        b=5
        sub=a-b
        if(sub==5):
            print('\n-----------substraction is sucessfully')
            print('\nRESULTS = ',sub)
            assert True
        else:
            print('\n-----------invalid operation------------')
            assert False