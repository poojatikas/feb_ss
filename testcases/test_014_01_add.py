class Test_014_01():

    def test_014_01_addition(self):

        a=10
        b=5
        add=a+b
        if(add==15):
            print('\n----------ADDITION IS DONE-----------')
            print('\nRESULTS =',add)
            assert True

        else:
            print('\n----------sorry,invalid operation----------')
            assert False