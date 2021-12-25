#this file should contain all funcitons necessary to place orders

import sign_up
import json
from tda.orders.common import OrderType
from tda.orders.generic import OrderBuilder
from tda.orders import EquityOrderBuilder
from tda.orders.equities import equity_buy_limit
from tda.orders.common import Duration, Session


def order(company_symbol, quantity): # we need an equity builder order object to place trades
    
    
    #this is the simples possible order build
        
        # All orders execute during the current normal trading session. If placed outside of trading hours, the execute during the next normal trading session.

        # Time-in-force is set to DAY.

        # All other fields (such as requested destination, etc.) are left unset, meaning they receive default treatment from TD Ameritrade. Note this treatment depends on TDA’s implementation, and may change without warning.


    
    
    client_local=sign_up.client_local # we need a reference to the local client
    #client_local.place_order()
