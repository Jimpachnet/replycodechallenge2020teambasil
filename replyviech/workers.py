class Developer:
    def __init__(self, company, bonus, skillset):
        self.company = company
        self.bonus = bonus
        self.skillset = skillset

    @classmethod
    def parse(cls, string):
        tokens = string.split(' ')
        return cls(
            company=tokens[0],
            bonus=int(tokens[1]),
            skillset=set(token.strip() for token in tokens[3:])
        )


class Manager:
    def __init__(self, company, bonus):
        self.company = company
        self.bonus = bonus


    @classmethod
    def parse(cls, string):
        tokens = string.split(' ')
        return cls(
            company=tokens[0],
            bonus=int(tokens[1]),
        )
