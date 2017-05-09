import DomainMaster

### AVAILABLE DOMAINS_
import StockExchange_Domain
import Weather_Domain

### Class selects a DomainMaster object based on its inputs.
class DomainSelect(object):

    def __init__(self, domainDIR):
        self.domainDIR = domainDIR

    ### Returns a DomainMaster object given the domain and pronoun / primary subject.
    def select_domain_and_pronoun(self, d, PN):
        ## Look through available domains.
        if d == "stock-exchange":
            DM = StockExchange_Domain.StockExchange_Domain(self.domainDIR, d, PN)
        elif d == "weather":
            DM = Weather_Domain.Weather_Domain(self.domainDIR, d, PN)
        else:
            return ("!!!!! DOMAIN NOT AVAILABLE !!!!!")
        
        return (DM)