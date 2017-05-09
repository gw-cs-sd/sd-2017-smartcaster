import DomainSelect
import SyntaxMaster

### Class handles syntax construction by domain.
class SmartCaster(object):

    def __init__(self, d, PN):
        ## Assign domain.
        self.DS = DomainSelect.DomainSelect("domains/")
        self.DM = self.DS.select_domain_and_pronoun(d, PN)

        ## Assign syntax.
        self.SM = SyntaxMaster.SyntaxMaster("syntax/")

    def RUN(self):
        print ("!!! SC CONSTRUCTION_")
        report = self.generate_syntax_body_given_start("START-PHRASE")
        print (report)
        print ()
        print ("!!! SC DICTIONARY TAGS_")
        report = self.assign_data_points_to_syntax(report)
        print (report)
        print ()
        self.SM.display_current_counters()
        print ()

##### ##### ##### ##### #####
##### ##### ##### ##### ##### CONTENT CONSTRUCTION / GENERATION
##### ##### ##### ##### #####

    ### Defines syntax construction parameters to fit domain content.
    ### Returns a sequence of syntax tags / template for the domain to fill.
    def generate_syntax_body_given_start(self, S):
        syntax = S

        ## Only mention pronoun once.
        self.SM.set_term_threshold_by_category("PN-PHRASE", 1, "phrase type")

        ## Number of SUBJS items in domain --> START-PHRASE threshold in syntax.
        SUBJS = self.DM.extract_subdomain(self.DM.get_domain_name(), "SUBJS")
        self.SM.set_term_threshold_by_category("START-PHRASE", len(SUBJS), "phrase type")

        ## Construct syntax body with the given parameters.
        # syntax = self.SM.generate_guided_syntax_given_start("START-PHRASE") # GUIDED : WIP
        syntax = self.SM.generate_random_syntax_given_start("START-PHRASE") # RANDOM : PLACEHOLDER

        return (syntax)
    
    ### Takes a sequence of syntax tags and assigns them to corresponding data points.
    ### Returns a string filled with the necessary information.
    def assign_data_points_to_syntax(self, SYNTAX):
        content = SYNTAX

        ## Replace tags from domain data.
        content = self.SM.replace_tags_given_DICT(content, self.DM.get_domain())

        ## Replace tags from value dictionary.
        content = self.SM.replace_tags_given_DICT(content, self.DM.get_value_dict())

        return (content)
    
    ### CREATE DICTIONARY OF SUBJECTS WITH OTHER VALUES BENEATH 
    ### EACH "SUB-DICT" CAN BE PASSED THROUGH THE REPLACE_TAGS_GIVEN_DICT TO CLUSTER INFO
    #def 

    ### THEN WORK ON COUNTERS TO GUIDE CONSTRUCTION