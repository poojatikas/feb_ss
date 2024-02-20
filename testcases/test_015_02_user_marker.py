import pytest

class Test_015_02_user_marker():

    @pytest.mark.customer
    def test_add_cust(self):
        print('\n---------Customer Added Sucessfully------------')

    @pytest.mark.customer
    def test_del_cust(self):
        print('\n---------Customer Deleted Sucessfully-----------')

    @pytest.mark.product
    def test_add_prod(self):
        print('\n---------Product Added Sucessfully-------------')

    @pytest.mark.product
    def test_del_prod(self):
        print('\n---------Product Deleted Sucessfully-----------')

    @pytest.mark.bill
    def test_add_bill(self):
        print('\n---------Bill Added Sucessfully----------------')

    @pytest.mark.bill
    @pytest.mark.regression
    def test_del_bill(self):
        print('\n-----------Bill DEleted Sucessfully-------------')

    @pytest.mark.patient
    def test_add_patient(self):
        print('\n-----------Patient Added Sucessfully-------------')

    @pytest.mark.pateint
    @pytest.mark.sanity
    def test_del_patient(self):
        print('\n------------Patient Deleted Sucessfully-----------')



