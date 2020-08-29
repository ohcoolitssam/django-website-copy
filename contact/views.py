#from django.core.mail import send_mail, BadHeaderError, EmailMessage
#from django.http import HttpResponse, HttpResponseRedirect
#from django.shortcuts import render, redirect
#from django.template.loader import get_template
#from .forms import ContactForm

from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.template.loader import get_template

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            cname = form.cleaned_data['contact_name']
            cemail = form.cleaned_data['contact_email']
            ccontent = form.cleaned_data['content']
            content = { 'cname':cname, 'cemail':cemail, 'ccontent':ccontent }
            template = get_template("contact_form.txt")
            content = template.render(content)

            if len(cname) > 50 or len(cemail) > 50 or len(ccontent) > 500:
                messages.error(request, 'Error: Your input has exceeded the character limit. Please keep your name and email below 50 characters and your message below 500.')
                return redirect('/contact')

            try:
                send_mail('new sphill.info/contact email', content, 'sphill67.work@gmail.com' ,['sphill67.work@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/contact/success')
      
    form = ContactForm()
    return render(request, "contact.html", {'form': form})

def success_view(request):
	return render(request, "success.html", {})

#contact view
#def contact_view(request):
#	Contact_Form = ContactForm
#	if request.method == 'POST':
#		form = Contact_Form(data=request.POST)

#		if form.is_valid():

#			contact_name = request.POST.get('contact_name')
#			contact_email = request.POST.get('contact_email')
#			contact_content = request.POST.get('content')

#			template = get_template("contact_form.txt")

#			content = {
#				'contact_name' : contact_name,
#				'contact_email' : contact_email,
#				'contact_content' : contact_content,
#			}

#			content = template.render(content)

#			email = EmailMessage( 
#				"New Personal Portfolio Contact Message",
#				content,
#				"portfolio website contact form" + '',
#				['sphill67.work@gmail.com'],
#			)
#
#			email.send()
#
#			return redirect('/contact/success')
#	return render(request, "contact.html", {'form': Contact_Form})

