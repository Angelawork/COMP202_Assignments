#name: Angela(Qingchen) Hu, McGill student ID: 261075832
import requests

def dict_to_query(my_dict):
    '''(dict) -> str
    Returns the inputted my_dict as a string
    containing my_dict's items in 'key=value' format
    with '&' in-between.
    
    >>> dict_to_query({'email': 'qingchen.hu@mail.mcgill.ca', 'token': 'A1B2C3'})
    'email=qingchen.hu@mail.mcgill.ca&token=A1B2C3'
    >>> dict_to_query({123: 'str1', 456: 'str2'})
    '123=str1&456=str2'
    >>> dict_to_query({5.5: [1,2,3], 4.0: [4,5,6], 5.0: [7,8]})
    '5.5=[1, 2, 3]&4.0=[4, 5, 6]&5.0=[7, 8]'
    '''
    my_link=''
    for key, value in my_dict.items():
        my_link+=str(key)+'='+str(value)
        my_link+='&'
    return my_link[:-1]
        
class Account:
    '''A class to represent a COMP202COIN account.

    Instance attributes:
    * email: str
    * token: str
    * balance: int
    * request_log: list
    
    Class attributes:
    * API_URL: str
    '''
    API_URL='https://coinsbot202.herokuapp.com/api/'

    def __init__(self, email, token):
        ''' (str, str) -> NoneType
        Creates an object of the type Account with the given
        email and token. An AssertionError is raised if the inputted
        values are in wrong types or format.
        
        >>> my_acct1 = Account("qingchen.hu@mail.mcgill.ca", "123")
        >>> my_acct1.balance
        -1
        >>> my_acct2 = Account(123, "5566")
        Traceback (most recent call last):
        AssertionError: The inputted values are not of the correct type.
        >>> my_acct3 = Account("angela", 'A1B2C3')
        Traceback (most recent call last):
        AssertionError: The format of the inputted email is not correct.
        '''
        if type(email)!=str or type(token)!=str:
            raise AssertionError('The inputted values are not of the correct type.')
        elif email[-9:]!='mcgill.ca':
            raise AssertionError('The format of the inputted email is not correct.')
        self.email = email
        self.token = token
        self.balance = -1
        self.request_log = []
    
    def __str__(self):
        ''' () -> str
        Returns a string containing instance attributes email
        and balance in a format with ' has balance ' in-between.
        
        >>> my_acct1 = Account("angela.hu@mcgill.ca", "123")
        >>> print(my_acct1)
        angela.hu@mcgill.ca has balance -1
        >>> my_acct2 = Account("hu@mcgill.ca", "1038294030")
        >>> print(my_acct2)
        hu@mcgill.ca has balance -1
        >>> my_acct3 = Account("123", "456")
        Traceback (most recent call last):
        AssertionError: The format of the inputted email is not correct.
        '''
        return self.email+" has balance "+str(self.balance)
    
    def call_api(self, end_point, request):
        '''(str, dict) -> dict
        Adds into the inputted request an item with the key 'token'
        and value given by the Account object's token attribute.
        Constructs an API request URL using the inputted end_point,
        request and sends the request. An AssertionError is raised
        if the inputted values are invalid, of wrong types or wrong format.
        Returns the resulted dictionary if the key 'status' has value 'OK'.
        Otherwise, raises an AssertionError with the value of the key
        'message' as error message.
        
        >>> my_acct1 = Account("qingchen.hu@mail.mcgill.ca", "123")
        >>> my_acct1.call_api("balance", {'email': my_acct1.email})
        Traceback (most recent call last):
        AssertionError: The token in the API request did not match the token that was sent over Slack.
        >>> my_acct1.call_api(345, {'email': my_acct1.email})
        Traceback (most recent call last):
        AssertionError: The inputted values are not of the correct type.
        >>> my_acct1.call_api('345', {'email': my_acct1.email})
        Traceback (most recent call last):
        AssertionError: The inputted end_point is not a valid one.
        >>> my_acct2 = Account("qingchen.hu@mail.mcgill.ca", "nDF5rcsMwpKpnpnk")
        >>> my_acct2.call_api("balance", {34: 123})
        Traceback (most recent call last):
        AssertionError: Field email not present in API query.
        >>> my_acct2.call_api("balance", {'email': my_acct1.email})
        {'message': 10927, 'status': 'OK'}
        '''
        valid_endpoint=['balance','transfer']
        if type(end_point)!=str or type(request)!=dict:
            raise AssertionError('The inputted values are not of the correct type.')
        elif end_point not in valid_endpoint:
            raise AssertionError('The inputted end_point is not a valid one.')
        
        request['token']=self.token
        request_url=Account.API_URL+end_point+'?'+dict_to_query(request)
        result = requests.get(url=request_url).json()
        if result['status']!='OK':
            raise AssertionError(result['message'])
        return result
    
    def retrieve_balance(self):
        '''() -> int
        Calls the API on the Account object and retrieve
        the balance according to the Account's user email.
        Updates the Account object's balance attribute to
        the retrieved value and returns as an integer.

        >>> my_acct1 = Account("qingchen.hu@mail.mcgill.ca", "nDF5rcsMwpKpnpnk")
        >>> cur_balance = my_acct1.retrieve_balance()
        >>> 10202 <= cur_balance and cur_balance <= 1e9
        True
        >>> my_acct2 = Account("qingchen.hu@mail.mcgill.ca", "123")
        >>> cur_balance = my_acct2.retrieve_balance()
        Traceback (most recent call last):
        AssertionError: The token in the API request did not match the token that was sent over Slack.
        >>> my_acct3 = Account("abc@mail.mcgill.ca", "123")
        >>> cur_balance = my_acct3.retrieve_balance()
        Traceback (most recent call last):
        AssertionError: No Slack account found for email abc@mail.mcgill.ca (API query field 'email'). Are you sure that is the email you used to signup to our Slack workspace?
        '''
        result = self.call_api('balance',{'email': self.email})
        self.balance=result['message']
        return self.balance
        
    def transfer(self, amount, email):
        '''(int, str) -> str
        Calls the API on the Account object and transfers
        the inputted amount of coins from the current
        user Account to the inputted email's user. Returns
        the value of the key 'message' in the resulting
        dictionary.
        An AssertionError is raised if the inputted values
        are of wrong types or wrong format, if the current
        Account's email equals the inputted email, if the
        current balance is -1, or if the inputted amount
        is invalid and doesn't match with current balance.

        >>> my_acct1 = Account("qingchen.hu@mail.mcgill.ca", "123")
        >>> my_acct1.transfer(3.5, "alexa.infelise@mail.mcgill.ca")
        Traceback (most recent call last):
        AssertionError: The inputted values are invalid or not of the correct type.
        >>> my_acct2 = Account("qingchen.hu@mail.mcgill.ca", "123")
        >>> my_acct2.transfer(10, "alexa.infelise@mail.mcgill.ca")
        Traceback (most recent call last):
        AssertionError: Transfer can't be made because your balance is not enough.
        >>> my_acct2 = Account("qingchen.hu@mail.mcgill.ca", "nDF5rcsMwpKpnpnk")
        >>> my_acct2.retrieve_balance()
        10927
        >>> my_acct2.transfer(1, "alexa.infelise@mail")
        Traceback (most recent call last):
        AssertionError: Transfer can't be made because inputted email is not valid or is in wrong format
        >>> my_acct2 = Account("qingchen.hu@mail.mcgill.ca", "nDF5rcsMwpKpnpnk")
        >>> my_acct2.retrieve_balance()
        11852
        >>> my_acct2.transfer(25, "alexa.infelise@mail.mcgill.ca")
        'You have transferred 25 coins of your balance of 11852 coins to alexa.infelise. Your balance is now 11827.'
        '''
        if type(amount)!=int or type(email)!=str or amount<=0:
            raise AssertionError("The inputted values are invalid or "
            " not of the correct type.")
        elif self.balance==-1 or amount>self.balance:
            raise AssertionError("Transfer can't be made because "
            "your balance is not enough.")
        elif email==self.email or email[-9:]!='mcgill.ca':
            raise AssertionError("Transfer can't be made because "
            "inputted email is not valid or is in wrong format")      
        my_dict={'withdrawal_email': self.email,'token': self.token,'deposit_email':email,'amount':amount}
        result = self.call_api('transfer',my_dict)
        return result['message']