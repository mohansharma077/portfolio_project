from django.shortcuts import render
import json
import os
from django.conf import settings


def index(request):
    # Load projects from JSON file for the home page
    json_path = os.path.join(settings.BASE_DIR, 'projects.json')

    try:
        with open(json_path, 'r') as file:
            projects_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback data if file is not found or invalid
        projects_data = []

    # Separate featured projects from regular projects
    featured_projects = [p for p in projects_data if p.get("featured", False) or p.get("is_featured", False)]
    regular_projects = [p for p in projects_data if not p.get("featured", False) and not p.get("is_featured", False)]

    # Limit the number of regular projects for the home page
    limited_projects = regular_projects[:3]  # Show only 3 projects on home page

    context = {
        'featured_projects': featured_projects,
        'projects': limited_projects,
        # Get unique categories for filtering
        'categories': sorted(set(cat for p in projects_data
                                 for cat in p.get("categories", []) if "categories" in p))
    }

    return render(request, 'index.html', context)





def projects(request):
    # Load projects from JSON file
    json_path = os.path.join(settings.BASE_DIR, 'projects.json')

    try:
        with open(json_path, 'r') as file:
            projects_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback data if file is not found or invalid
        projects_data = []

    # Separate featured projects from regular projects
    featured_projects = [p for p in projects_data if p.get("featured", False) or p.get("is_featured", False)]
    regular_projects = [p for p in projects_data if not p.get("featured", False) and not p.get("is_featured", False)]

    context = {
        'featured_projects': featured_projects,
        'projects': regular_projects,
        # Get unique categories for filtering
        'categories': sorted(set(cat for p in projects_data
                                 for cat in p.get("categories", []) if "categories" in p))
    }

    return render(request, 'projects.html', context)


def contact(request):
    success = False
    message = ""

    if request.method == 'POST':
        # In a real application, you would process the form data here
        # For example, sending an email or saving to database
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message_text = request.POST.get('message', '')

        # Simple validation
        if name and email and message_text:
            # Process the message (this is a placeholder)
            # In a real app, you would send an email or save to database
            success = True
            message = "Your message has been sent successfully! I'll get back to you soon."
        else:
            message = "Please fill in all required fields."

    return render(request, 'contact.html', {'success': success, 'message': message})

