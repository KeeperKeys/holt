from helpers import str2date, date2str, tstamp2date


class Ticket:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.created = tstamp2date(kwargs.get('created'))
        self.closed = tstamp2date(kwargs.get('closed'))
        self.time_of_life = (self.closed - self.created).days

    def start_date_and_duration(self):
        return {'date': self.created, 'duration': self.time_of_life}

    def date_and_duration(self):
        return {'date': date2str(self.created), 'duration': self.time_of_life}

    def __str__(self):
        return "<Ticket: {id}. Time of life: {time_of_life}".format(
            id=self.id, time_of_life=self.time_of_life
        )

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def merge_dates(tickets):
        res_tickets = {}
        for ticket in tickets:
            if ticket.created not in res_tickets:
                res_tickets[ticket.created] = []
            res_tickets[ticket.created].append(ticket.time_of_life)
        for date, durations in res_tickets.items():
            res_tickets[date] = sum(durations) / len(durations)
        return res_tickets


class SimpleTicket:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.summary = kwargs.get('summary')
        self.created = tstamp2date(kwargs.get('created'))
        self.deadline = tstamp2date(kwargs.get('deadline'))
        self.closed = tstamp2date(kwargs.get('closed'))

    def __str__(self):
        return "<Ticket: {0}. Summary: {1}. Created: {2}. Deadline: {3}. Closed: {4}".format(
            self.id, self.summary, self.created, self.deadline, self.closed
        )

    def __repr__(self):
        return self.__str__()
