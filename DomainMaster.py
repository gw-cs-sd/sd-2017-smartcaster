import json

### note : Will never be called directly. 

class DomainMaster(object):

    def __init__(self, domainDIR):
        self.domainDIR = domainDIR # directory
        self.domain_name = "" # domain label (str)
        self.domain = {} # domain dictionary
        self.values = {} # domain values dictionary
        self.pronoun = "" # content pronoun / primary subject (str)

##### ##### ##### ##### #####
##### ##### ##### ##### ##### TESTING METHODS
##### ##### ##### ##### #####

    ### Prints report of current domain dictionary.
    def display_domain_dictionary(self):
        print ("Current dictionary for domain : " + self.get_domain_name())
        print (self.get_domain())
        print ()

    ### Prints report of current domain data values.
    def display_domain_data_values(self):
        print ("Current data values for domain : " + self.get_domain_name())
        print (self.get_value_dict())
        print ()

##### ##### ##### ##### #####
##### ##### ##### ##### ##### (ABSTRACTED) DATA RETRIEVAL
##### ##### ##### ##### #####

##### !!!!! MUST IMPLEMENT IN ALL DOMAIN MASTER CHILD CLASSES.

    ### Updates most recently available data in given domain.
    def refresh_data(self):
        raise NotImplementedError("Please Implement this method")
    
    ### Returns data from domain-specific file given a term.
    def get_data_value(self, term):
        raise NotImplementedError("Please Implement this method")

##### ##### ##### ##### #####
##### ##### ##### ##### ##### DOMAIN
##### ##### ##### ##### #####

    ### Returns the name of the current domain of operation.
    def get_domain_name(self):
        return (self.domain_name)

    ### Returns domain JSON data already set in object.
    def get_domain(self):
        return (self.domain)
    
    ### Returns a given subdomain from a given domain.
    def extract_subdomain(self, d, sd):
        return (self.get_domain()[sd])

    ### Sets the domain of operation given a domain.
    def set_domain(self, d):
        self.domain_name = d
        self.domain = self.retrieve_domain_data_from_JSON(d)

    ### Returns domain JSON data from a given domain.
    def retrieve_domain_data_from_JSON(self, d):
        fp = self.domainDIR + d + ".json"

        ## Load and set JSON domain data as dictionary.
        with open(fp, 'r') as raw:
            data = json.load(raw)
        
        return (data)

##### ##### ##### ##### #####
##### ##### ##### ##### ##### VALUES
##### ##### ##### ##### #####
    
    ### Returns the entire domain value dictionary.
    def get_value_dict(self):
        return (self.values)
    
    ### Sets all available JSON dictionary terms with available data values.
    def set_value_dict(self, d):
        self.values = self.retrieve_data_values_from_SUBJS(d)

    ### Returns a dictionary of data values corresponding to the SUBJS of the domain.
    def retrieve_data_values_from_SUBJS(self, d):
        val_dict = {}

        sd = self.extract_subdomain(d, "SUBJS")

        ## Iterate across the SUBJS list in domain.
        for item in sd:
            ## Insert SUBJ as key, and retrieved data as value.
            val_dict[item["SUBJ"]] = self.get_data_value(item["SUBJ"])

        return (val_dict)
    
    ### Adds new keys to the value dictionary and updates existing ones.
    ### USED IN CHILD CLASSES.
    def update_value_dict(self, d):
        val_dict = self.retrieve_data_values_from_SUBJS(d)

        ## Iterate across terms in temporary value dictionary.
        for item in val_dict:
            ## Insert / update keys and values.
            self.set_key_and_value(item, val_dict[item])

    ### Returns a value in the domain value dictionary given a key.
    def get_value_by_key(self, key):
        return (self.values[key])

    ### Sets the key and value in the domain value dictionary.
    def set_key_and_value(self, key, val):
        self.values[key] = val

##### ##### ##### ##### #####
##### ##### ##### ##### ##### PRONOUN
##### ##### ##### ##### #####
    
    ### Returns the current pronoun of the domain.
    def get_pronoun(self):
        return (self.pronoun)

    ### Sets the pronoun of the domain given a pronoun.
    def set_pronoun(self, PN):
        self.pronoun = PN
        
        ## Set pronoun tag.
        self.set_key_and_value("PN", PN)

    ### Sets the domain and pronoun given both.
    ### USED IN CHILD CLASSES.
    def set_pronoun_and_domain(self, PN, d):
        self.set_pronoun(PN)
        self.set_domain(d)