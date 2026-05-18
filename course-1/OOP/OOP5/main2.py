#Write a program to create two classes for two different countries 
#that consist of three methods to display the following information 
#of respective country - capital, language and type of country. 
#Then, use Polymorphism to create a common interface for both classes.
class New_Zealand:
    def capital(self):
        print("The capital of New Zealand is Wellington.")
    def Language(self):
        print("The languages of New Zealand are English, Maori and NZ Sign Language.")
    def type(self):
        print("New Zealand is a Oceanic country.\n--------------------------------")
class Australia:
    def capital(self):
        print("The capital of Australia is Canberra.")
    def Language(self):
        print("The language of Australia is English.")
    def type(self):
        print("Australia is a country and continent.\n--------------------------------")
class India:
    def capital(self):
        print("The capital of India is New Delhi.")
    def Language(self):
        print("The primary language of India is Hindi.")
    def type(self):
        print("India is a South Asian country.\n--------------------------------")
nz=New_Zealand()
au=Australia()
ind=India()
for country in (nz,au,ind):
    country.capital()
    country.Language()
    country.type()
