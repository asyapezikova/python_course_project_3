class Operation:
    '''
    Класс с информацией о произведенной банковской операции
    '''
    def __init__(self, id, state, date, description, where_from, to, amount, currency):
        self.id = id
        self.state = state
        self.date = date
        self.description = description
        self.where_from = where_from
        self.to = to
        self.amount = amount
        self.currency = currency

    def get_date(self):
        '''
        :return: дату проведения операции
        '''
        return self.date

    def get_state(self):
        '''
        :return: статус перевода
        '''
        return self.state

    def __repr__(self):
        '''
        Выводит информаци о банковском переводе в понятном виде
        '''
        return (f"{self.date} {self.description}\n"
                f"{self.where_from} -> {self.to}\n"
                f"{self.amount} {self.currency}\n")
