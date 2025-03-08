# home.py - Django views for the home page
from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
import json
import os


def index(request):
    """
    View function for the home page of the site.
    """
    # Load projects from JSON file
    with open('projects.json', 'r') as file:
        projects = json.load(file)

    # Get featured projects (first 3)
    featured_projects = projects[:3]

    # Context to pass to template
    context = {
        'title': 'Django Portfolio',
        'description': 'A modern portfolio website with Django',
        'featured_projects': featured_projects,
    }

    # Render the template with the data
    return render(request, 'index.html', context)



def projects(request):
    """
    View function for the projects page.
    """
    # Load projects from JSON file
    with open('projects.json', 'r') as file:
        projects = json.load(file)

    # Context to pass to template
    context = {
        'title': 'My Projects',
        'description': 'A showcase of my recent work and personal projects.',
        'projects': projects,
    }

    # Render the template with the data
    return render(request, 'projects.html', context)


def contact(request):
    """
    View function for the contact page.
    """
    # Handle form submission
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # In a real application, you would save this to a database
        # or send an email

        # For demonstration, just return a success message
        return render(request, 'contact.html', {
            'title': 'Contact Me',
            'description': 'Get in touch with me for inquiries, collaborations, or just to say hello.',
            'success': True,
            'message': f'Thank you {name}, your message has been sent!'
        })

    # Context to pass to template for GET request
    context = {
        'title': 'Contact Me',
        'description': 'Get in touch with me for inquiries, collaborations, or just to say hello.',
    }

    # Render the template with the data
    return render(request, 'contact.html', context)