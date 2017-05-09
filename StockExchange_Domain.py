from DomainMaster import DomainMaster
from googlefinance import getQuotes
import json

### References_
### https://pypi.python.org/pypi/googlefinance

class StockExchange_Domain(DomainMaster):

    def __init__(self, domainDIR, d, PN):
        DomainMaster.__init__(self, domainDIR)
        self.set_pronoun_and_domain(PN, d)

        ## Retrieve stock data of given symbol.
        self.refresh_data()

##### ##### ##### ##### #####
##### ##### ##### ##### ##### STOCK VALUE RETRIEVAL
##### ##### ##### ##### #####

    ### Updates most recently available data.
    def refresh_data(self):
        self.raw = json.dumps(getQuotes(self.get_pronoun()), indent=2)
        self.data = json.loads(self.raw)

        ## Update value dictionary.
        self.update_value_dict(self.domain_name)

    ### Retrieves specified stock data given a type term.
    def get_data_value(self, term):
        ## Check against available terms.
        if term == "value":
            val = self.data[0]['LastTradePrice']
        else:
            return ("")
    
        return (val)