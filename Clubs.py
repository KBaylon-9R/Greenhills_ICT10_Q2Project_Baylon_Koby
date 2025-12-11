from pyscript import display, document

Science_Club = {
    'name': 'Science Club',
    'description': 'For students who love experiments',
    'meeting_time': 'Every Tuesday, 3:00 - 4:00 PM',
    'location': 'Room 510',
    'moderator': 'Calpo',
    'members': 12
}

Varsity = {
    'name': 'Varsity',
    'description': 'Student athletes of OBMC',
    'meeting_time': 'Monday 3:00 - 4:00 PM',
    'location': 'Quadrangle',
    'moderator': 'Coach Amargo',
    'members': 67
}

Art_Club = {
    'name': 'Art Club',
    'description': 'For creative minds who love to draw or paint',
    'meeting_time': 'Every Thursday, 2:00 PM - 3:30 PM',
    'location': 'Room 307',
    'moderator': 'Mr Ramos',
    'members': 18
}

COCC = {
    'name': 'COCC',
    'description': 'Cadet officers training',
    'meeting_time': 'Friday 3:00 - 4:30 PM',
    'location': 'Quadrangle',
    'moderator': 'Ms Mobillia',
    'members': 22
}

clubs = {
    'Science_Club': Science_Club,
    'Varsity': Varsity,
    'Art_Club': Art_Club,
    'COCC': COCC
}

def show_club(event):
    club_name = document.getElementById('club_select').value
    info = clubs[club_name]

    document.getElementById('output').innerHTML = ""

    display(f"Name: {info['name']}", target='output')
    display(f"Description: {info['description']}", target='output')
    display(f"Meeting Time: {info['meeting_time']}", target='output')
    display(f"Location: {info['location']}", target='output')
    display(f"Moderator: {info['moderator']}", target='output')
    display(f"Members: {info['members']}", target='output')
