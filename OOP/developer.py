class Developer():

    def __init__(self, name, surname, salary, languages):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.languages = languages

    def show_info(self):
        print(
            """
            Developer:

            Name: {}
            Surname: {}
            Salary: {}
            Languages: {}

            """.format(self.name, self.surname, self.salary, self.languages)
        )
    
    def raise_salary(self, money):
        self.salary += money

    def add_lang(self, lang):
        self.languages.append(lang)

developer = Developer("Merve", "Alpay", 300 , ["Python","Java"])
developer.show_info()
developer.add_lang("GoLang")
developer.raise_salary(500)
developer.show_info()