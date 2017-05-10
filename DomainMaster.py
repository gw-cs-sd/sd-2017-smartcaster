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
        return (d[sd])

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

        ##### ##### ##### SUBJS ##### ##### #####
        
        sd = self.extract_subdomain(d, "SUBJS")
        subj_data = {}
        
        ## Iterate over SUBJS list and retrieve values of all SUBJ subdomains.
        for subj in sd:
            ## Insert SUBJ as top-level dictionary key and set term values beneath.
            subj_data = self.retrieve_data_values_from_SUBJ(subj)
            self.values[subj_data[0]] = subj_data[1]

    ### Returns a tuple consisting of:
    ###     [0] the SUBJ of this subdomain
    ###     [1] dictionary of productions and data values corresponding to the SUBJ.
    def retrieve_data_values_from_SUBJ(self, SUBJ):
        val_dict = {}

        ## Iterate across the values in this SUBJ.
        for term in SUBJ:
            if SUBJ[term]:
                ## Insert term tags and corresponding productions in dictionary.
                val_dict[term] = SUBJ[term]

        ## Retrieve corresponding data value.
        val_dict["VALUE"] = self.get_data_value(SUBJ["SUBJ"])
        return (SUBJ["SUBJ"], val_dict)

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