from django.shortcuts import render

def home(request):
    context = {
        'name': 'Shaik Mohammed Zubair',
        'role': 'Python Django Developer',
        'about': 'I am a Python developer interested in web development, Django and AI.',
        'skills': [
            'Python',
            'Django',
            'HTML',
            'CSS',
            'JavaScript',
            'SQL'
        ],
        'projects': [
            {
                'name': 'Student Result Prediction',
                'description': 'A machine learning project for predicting student results.'
            },
            {
                'name': 'Railway Reservation System',
                'description': 'A Python-based railway ticket reservation system.'
            },
            {
                'name': 'Portfolio Website',
                'description': 'A personal portfolio website developed using Django.'
            }
        ]
    }

    return render(request, 'home.html', context)