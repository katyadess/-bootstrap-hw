from django.shortcuts import render

# Create your views here.

def archives(request):
    return render(request, 'main/archives.html')


def blog_july(request):
    return render(request, 'main/blog.html')


def demo(request):
    return render(request, 'main/demo.html')


def index(request):
    return render(request, 'main/index.html')


def page(request):
    return render(request, 'main/page.html')


def single(request):
    return render(request, 'main/single.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def faq(request):
    faqs = [
        {
            'question': 'What is a website template?',
            'answer': 'A site template is a ready-made webpage or set of webpages that helps you set-up a high-quality \
            website in a short period of time. It speeds up your design process since the pre-designed and pre-built webpages will serve as your starting point. \
            It provides you with a fully designed and coded site layout that you can modify allowing you to build a website without the need to hire a professional web designer. \
            Site templates help you save time and money.'
        },
        {
            'question': 'How should I credit you?',
            'answer': 'Just visibly credit us somewhere on your site. We prefer the footer credit that comes with the site template but if you don\'t want it there, you\'re still free to move it somewhere else on your site.'
        },
        {
            'question': 'Can I modify the templates?',
            'answer': 'Yes, you can fully customize the template to match your specific needs. \
                You can change the design, colors, layout, and any other aspect of the template. \
                Our templates are designed to be flexible and easy to modify, allowing you to \
                create a unique website that fits your brand.'
        },
        {
            'question': 'What if I encounter issues with the template?',
            'answer': ' If you encounter any issues with the template, feel free to reach out to us for support. \
            We are here to help you resolve any problems you may face. Additionally, our templates come with documentation \
            that can guide you through the setup and customization process.'
        },
        {
            'question': 'Do your templates support mobile devices?',
            'answer': 'Yes, all our templates are designed to be fully responsive, meaning they will automatically adjust \
                to fit different screen sizes and devices, including mobile phones and tablets. \
                This ensures that your website looks great and functions well on any device.'
        }
    ]

    context = {'faqs': faqs}
    return render(request, 'main/faq.html', context)


def blog_august(request):
    return render(request, 'main/blog_august.html')


def single_one(request):
    return render(request, 'main/single_one.html')

def single_two(request):
    return render(request, 'main/single_two.html')

def single_three(request):
    return render(request, 'main/single_three.html')

def single_four(request):
    return render(request, 'main/single_four.html')

def single_five(request):
    return render(request, 'main/single_five.html')


def wordpress(request):
    return render(request, 'main/wordpress.html')