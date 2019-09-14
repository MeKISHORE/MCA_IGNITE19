from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import auth

from .models import studentregistration, collegeverification, contact_us, events, event_details


def index(request):
    if request.session.get('session_name') is not None:
        sobj = studentregistration.objects.filter(college_code=request.session.get('session_name')).first()
        obj = collegeverification.objects.filter(collegecode=request.session.get('session_name')).first()
        ob = request.session.get('session_name')
        return render(request, 'workshop/Home.html', {'sobj': sobj, 'obj': obj, 'ob': ob})
    return render(request, 'workshop/Home.html')


def profile(request):
    return redirect('login')


def login(request):
    array_obj=collegeverification.objects.values_list('collegename')
    if request.session.get('session_name') is not None:
        print("session")
        sobj = studentregistration.objects.filter(college_code=request.session.get('session_name')).first()
        obj = collegeverification.objects.filter(collegecode=request.session.get('session_name')).first()
        ob = request.session.get('session_name')
        return render(request, 'workshop/registered.html', {'sobj': sobj, 'obj': obj, 'ob': ob})
    else:
        obj = collegeverification.objects.all()
        print("ref")
        return render(request, 'workshop/login.html', {'obj': obj,'array_obj':array_obj })


def sign_in(request):
    try:
        if request.method == 'POST':
            cname = request.POST['cname']
            leader_email = request.POST['leader_email']
            college_code = request.POST['college_code']
            obj = collegeverification.objects.filter(Q(collegecode=college_code) & Q(collegename=cname)).first()
            print(obj)
            if obj is not None:
                sobj = studentregistration.objects.filter(college_code=obj).first()
                if sobj is not None:
                    if sobj.leader_email == leader_email:
                        request.session['session_name'] = obj.collegecode
                        ob = request.session.get('session_name')
                        print("err")
                        return render(request, 'workshop/registered.html', {'sobj': sobj, 'obj': obj, 'ob': ob})
                    else:
                        print('1')
                        # error = {'error': 'Invalid E-mail id and #Code'}
                        obj = collegeverification.objects.all()
                        return render(request, 'workshop/login.html',
                                      {'obj': obj, 'error': 'Invalid E-mail id and #Code'})
                else:
                    print('2')
                    # create 10 min sission
                    request.session.set_expiry(60)
                    request.session['session_email'] = leader_email
                    return render(request, 'workshop/regstudent.html',
                                  {'sobj': sobj, 'obj': obj, 'email': leader_email})
                    # return render(request, 'workshop/login.html', {'obj': obj})
            else:
                print('3')
                obj = collegeverification.objects.all()
                return render(request, 'workshop/login.html', {'obj': obj, 'error': 'Invalid e-mail id or #code'})
        else:
            print('4')
            return redirect('login')
    except:
        print('5')
        return redirect('login')


def team_ignite(request):
    try:
        if request.method == 'POST':
            invitation_code = request.POST['invitation_code']
            invitation_file = request.FILES['invitation_file']

            print(invitation_file.size)
            splt = invitation_file.name

            if splt.endswith('.pdf'):
                print('successfully validate the file')

            leader_name = request.POST['leader_name']
            college_id_of_leader = request.FILES['college_id_of_leader']
            leader_mobile = request.POST['leader_mobile']
            leader_mail_id = request.POST['leader_mail_id']

            member1_name = request.POST['member1_name']
            member1_e_mail = request.POST['member1_e_mail']
            member1_mobile = request.POST['member1_mobile']
            member1_file = request.FILES['member1_file']

            member2_name = request.POST['member2_name']
            member2_e_mail = request.POST['member2_e_mail']
            member2_mobile = request.POST['member2_mobile']
            member2_file = request.FILES['member2_file']

            member3_name = request.POST['member3_name']
            member3_e_mail = request.POST['member3_e_mail']
            member3_mobile = request.POST['member3_mobile']
            member3_file = request.FILES['member3_file']

            member4_name = request.POST['member4_name']
            member4_e_mail = request.POST['member4_e_mail']
            member4_mobile = request.POST['member4_mobile']
            member4_file = request.FILES['member4_file']

            obj = collegeverification.objects.filter(collegecode=invitation_code).first()
            sobj = studentregistration.objects.filter(college_code=obj).first()
            if obj is not None and sobj is None:
                print(obj.collegename)
                stu_obj = studentregistration(
                    college_code=obj,
                    invitation_letter=invitation_file,

                    leader_name=leader_name,
                    leader_id=college_id_of_leader,
                    leader_mobile=leader_mobile,
                    leader_email=leader_mail_id,

                    member1_name=member1_name,
                    member1_id=member1_e_mail,
                    member1_mobile=member1_mobile,
                    member1_file=member1_file,

                    member2_name=member2_name,
                    member2_id=member2_e_mail,
                    member2_mobile=member2_mobile,
                    member2_file=member2_file,

                    member3_name=member3_name,
                    member3_id=member3_e_mail,
                    member3_mobile=member3_mobile,
                    member3_file=member3_file,

                    member4_name=member4_name,
                    member4_id=member4_e_mail,
                    member4_mobile=member4_mobile,
                    member4_file=member4_file
                )

                stu_obj.save()
                cname = request.POST['college_name']
                college_code = request.POST['invitation_code']
                obj = collegeverification.objects.filter(Q(collegecode=college_code) & Q(collegename=cname)).first()
                sobj = studentregistration.objects.filter(college_code=obj).first()
                request.session['session_name'] = obj.collegecode
                ob = request.session.get('session_name')
                print("err")
                return render(request, 'workshop/registered.html', {'sobj': sobj, 'obj': obj, 'ob': ob})
            else:
                print('else')
                return HttpResponse('you are already registered')
        else:
            print('outer else')
            return redirect('regstudent')
    except:
        print('exe')
        return redirect('regstudent')


def teams(request):
    if request.session.get('session_name') is not None:
        sobj = studentregistration.objects.filter(college_code=request.session.get('session_name')).first()
        obj = collegeverification.objects.filter(collegecode=request.session.get('session_name')).first()
        ob = request.session.get('session_name')
        return render(request, 'workshop/teams.html', {'sobj': sobj, 'obj': obj, 'ob': ob})
    return render(request, 'workshop/teams.html')


def aboutus(request):
    if request.session.get('session_name') is not None:
        sobj = studentregistration.objects.filter(college_code=request.session.get('session_name')).first()
        obj = collegeverification.objects.filter(collegecode=request.session.get('session_name')).first()
        ob = request.session.get('session_name')
        return render(request, 'workshop/aboutus.html', {'sobj': sobj, 'obj': obj, 'ob': ob})
    return render(request, 'workshop/aboutus.html')


def gallery(request):
    if request.session.get('session_name') is not None:
        sobj = studentregistration.objects.filter(college_code=request.session.get('session_name')).first()
        obj = collegeverification.objects.filter(collegecode=request.session.get('session_name')).first()
        ob = request.session.get('session_name')
        return render(request, 'workshop/gallery.html', {'sobj': sobj, 'obj': obj, 'ob': ob})
    return render(request, 'workshop/gallery.html')


def event(request):
    tech = events.objects.filter(belongs_to="tech_event", active=1)
    non_tech = events.objects.filter(belongs_to="non_tech_event", active=1)
    online = events.objects.filter(belongs_to="online_event", active=1)
    if request.session.get('session_name') is not None:
        # sobj = studentregistration.objects.filter(college_code=request.session.get('session_name')).first()
        # obj = collegeverification.objects.filter(collegecode=request.session.get('session_name')).first()
        ob = request.session.get('session_name')
        return render(request, 'workshop/event.html', {'ob': ob, 'tech': tech, 'non_tech': non_tech, 'online': online})
    else:
        return render(request, 'workshop/event.html', {'tech': tech, 'non_tech': non_tech, 'online': online})


def contact(request):
    if request.session.get('session_name') is not None:
        sobj = studentregistration.objects.filter(college_code=request.session.get('session_name')).first()
        obj = collegeverification.objects.filter(collegecode=request.session.get('session_name')).first()
        ob = request.session.get('session_name')
        return render(request, 'workshop/contactus.html', {'sobj': sobj, 'obj': obj, 'ob': ob})
    return render(request, 'workshop/contactus.html')


def contact_reg(request):
    try:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            subject = request.POST['subject']
            college_name = request.POST['college_name']
            message = request.POST['message']

            obj = contact_us(
                first_name=first_name,
                last_name=last_name,
                email=email,
                subject=subject,
                college_name=college_name,
                message=message
            )
            obj.save()
            # return HttpResponse("successfully sent message")
            redirect('contact')
        else:
            pass
        # return HttpResponse("not message")
        return render(request, 'workshop/contactus.html', { 'success': 'Messege sent'})
    except:
        # return HttpResponse("not message")
        redirect('contact')


def logout(request):
    auth.logout(request)
    return redirect('index')

def event_detail(request, slug):
    event = events.objects.get(short_url=slug)
    event_detail=event_details.objects.get(event_name_id=event.id)
    return render(request, 'workshop/event_detail.html',{'event': event, 'event_detail': event_detail })





