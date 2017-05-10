import SmartCaster

## More dynamic content assembly.

##### ##### ##### ##### #####
##### ##### ##### ##### ##### SMART CASTER TESTING
##### ##### ##### ##### #####

domain = "weather"
pronoun = "Washington, d.c."

print ()

print ("##### ##### SMART CASTER TESTING (WEATHER)___")
print ()
SC1 = SmartCaster.SmartCaster(domain, pronoun)
SC1.RUN()

domain = "stock-exchange"
pronoun = "BAC"

print ()

print ("##### ##### SMART CASTER TESTING (STOCK-EXCHANGE)___")
print ()
SC2 = SmartCaster.SmartCaster(domain, pronoun)
SC2.RUN()