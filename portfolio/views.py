from django.shortcuts import render

def index(request):
    context = {
        'about_text': """Ram is an esteemed photographer whose expertise spans across the realms of Fashion, Portrait, Nature, and Architecture photography. His journey in the world of photography has been one of dedication and relentless pursuit of perfection, culminating in a portfolio that exemplifies his mastery of the craft.

         In Fashion Photography, Ram captures the essence of style and sophistication, seamlessly blending elegance with contemporary trends. Each image tells a story of glamour and allure, showcasing his ability to create visually captivating compositions.

         In Portrait Photography, Ram's keen eye for detail and empathy for his subjects shine through, as he skillfully reveals their innermost emotions and personalities. Every portrait exudes authenticity and intimacy, reflecting his profound connection with the people he photographs.

         In Nature Photography, Ram's reverence for the natural world is palpable, as he immortalizes its beauty in breathtaking detail. From majestic landscapes to delicate flora and fauna, his images evoke a sense of wonder and reverence for the wonders of the earth.

         In Architecture Photography, Ram explores the interplay of light, shadow, and form, capturing the essence of architectural marvels with precision and finesse. Each photograph is a testament to his ability to transform the ordinary into the extraordinary, revealing the soul of the built environment.

         Through his portfolio, Ram invites viewers on a journey through the realms of beauty, emotion, and creativity, leaving a lasting impression of his talent and passion for the art of photography....""",
        'education': [
            "Bachelor of Fine Arts degree from Lovely Professional University",
            "Diploma in Photography from the National Institute of Photography",
            "Certified Professional Photographer (CPP)",
            "Canon Certified Professional Photographer",
            "Certified Digital Photographer (CDP)"
        ],
        'work_experience': {
            'start_date': "January 2010",
            'end_date': "January 2013",
            'company': "CoStar Group",
            'location': "San Francisco, CA",
            'job_title': "Freelance Photographer",
            'responsibilities': [
                "Established a recognized freelance photography business and a portfolio of 60 faithful customers.",
                "Set up personal photography equipment and created the best environment for aesthetically pleasing shots.",
                "Received recognition from multiple local newspapers and magazines for outstanding work.",
                "Mastered photography basics over five years of consistent work."
            ]
        },
        'images': [
            {'url': "https://images.unsplash.com/photo-1708848504369-55f60bc664e2?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 'alt': "Image 1"},
            {'url': "https://images.unsplash.com/photo-1708848504369-55f60bc664e2?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 'alt': "Image 2"},
            {'url': "https://images.unsplash.com/photo-1708848504369-55f60bc664e2?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 'alt': "Image 3"}
        ],
        'contact_info': "You can reach out to Ram at: Email: ram@example.com &nbsp;&nbsp; Phone: 123-456-7890 &nbsp;&nbsp; Address: 123 Main Street, San Francisco, CA 12345"
    }
    return render(request, 'portfolio/index.html', context)