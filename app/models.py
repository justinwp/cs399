from app import fake

"""
Fake models generated by faker...
"""

print fake.__dict__
def generate_events(num):
    events = []

    for i in range(num):
        events.append({
            'date': fake.dateTimeBetween('now','+1y'),
            'city': fake.city(),
            'state': fake.stateAbbr(),
            'description': fake.text()
        })

    events.sort(key=lambda x: x['date'])

    return events


def generate_members(num=5):
    members = []

    for i in range(num):
        members.append({
            'name': fake.name(),
            'state': fake.stateAbbr(),
            'bio': fake.text()
        })
    return members

events = generate_events(10)
members = generate_members()

