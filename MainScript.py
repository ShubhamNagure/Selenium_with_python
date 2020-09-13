from MyUtility import Util
import time

def main():
    #call search and product method
    _keys = 'Samsung'
    _model = 'Samsung Galaxy M11 ( 32GB , 3 GB ) Black'
    Util._search_and_add(_keys,_model)

    #Call login method
    time.sleep(3)
    Util._doLogin(0)

    #call logout method
    Util._doLogOut(0)


if __name__ == '__main__':
    main()