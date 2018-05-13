import pymysql.cursors
from ticket import Ticket


def get_tickets():
    connection = pymysql.connect(
        host='localhost',
        user='trac',
        password='trac',
        db='trac',
        cursorclass=pymysql.cursors.DictCursor
    )

    tickets = []

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT t.id, t.summary, t.time as created, dl.value as deadline, t.changetime as closed
            FROM ticket t, ticket_custom dl 
            WHERE t.type='Weekly Plan Task' AND t.id>3
              AND t.id=dl.ticket
              AND dl.name='deadline_dt'
        """)
        for ticket in cursor.fetchall():
            tickets.append(Ticket(**ticket))

    return tickets
