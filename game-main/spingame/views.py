import random
import datetime

from django.shortcuts import render, redirect
from .models import Value_set, Value_choosed, spin_time


def value_blinker(request):
    value = None
    now = datetime.datetime.now()
    try:
        va = Value_choosed.objects.get(user_name=request.user)

        form = 0
    except Value_choosed.DoesNotExist:

        form = 1
    print("now:::", now)
    dict = {}
    spin = spin_time.objects.all()
    for s in spin:
        dict[s.hours] = s.minutes

    hou = list(dict.keys())

    hou.sort()
    print("spin:::", hou)
    try:
        spi = spin_time.objects.get(hint=True)
    except spin_time.DoesNotExist:
        pass
    for count in range(len(hou)):
        print(hou[count])
        print(spi.hours)
        print("count::::::::", count)
        modi_time = now.replace(hour=hou[count], minute=dict[hou[count]], second=00)
        c = modi_time - now
        if now.hour == hou[count]:
            if spi.hours == hou[count]:
                if now < modi_time:
                    print(spi.hours, "spi.hours")
                    break
        if now.hour < hou[count]:

            if hou[count] < spi.hours or hou[count] > spi.hours:
                try:
                    va = Value_choosed.objects.get(user_name=request.user)
                    print("1st")
                    v = Value_set.objects.all()
                    print(v[0].value)
                    value = None
                    va.save()
                    modified_date = now.replace(hour=hou[count], minute=dict[hou[count]], second=00)
                    modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
                    return render(request, 'game_value.html', {'value': value, 'f': form, 'date': modified_date})
                except Value_choosed.DoesNotExist:
                    print("1st expect bidding start in")
                    value = None
                    modified_date = now.replace(hour=hou[count], minute=dict[hou[count]], second=00)
                    start_date = modified_date - datetime.timedelta(hours=0, minutes=6)

                    modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
                    start_date = f"{start_date:%d %b, %Y %H:%M:%S}"
                    form = 2
                    # if request.method == 'POST':
                    #     val = request.POST.get('work_days')
                    #     bet_amount = request.POST.get('bet_amount')
                    #     print('val::', val)
                    #
                    #     print(modified_date)
                    #     V = Value_choosed(value=val, bet_amount=bet_amount, datetime=modified_date, count=count)
                    #     print('vdatetime==', V.datetime)
                    #     V.save()
                    #     print(V.count)
                    #
                    #     print(form)
                    #     return redirect('/game')
                    return render(request, 'game_value.html', {'value': value, 'f': form, 'date': start_date})
            else:
                break

        if 6 < c.total_seconds() / 60:
            if hou[count] < spi.hours or hou[count] > spi.hours:
                try:
                    va = Value_choosed.objects.get(user_name=request.user)
                    print("1st")
                    v = Value_set.objects.all()
                    print(v[0].value)
                    value = None
                    va.save()
                    modified_date = now.replace(hour=hou[count], minute=dict[hou[count]], second=00)
                    modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
                    return render(request, 'game_value.html', {'value': value, 'f': form, 'date': modified_date})
                except Value_choosed.DoesNotExist:
                    print("1st expect bidding start in")
                    value = None
                    modified_date = now.replace(hour=hou[count], minute=dict[hou[count]], second=00)
                    start_date = modified_date - datetime.timedelta(hours=0, minutes=6)

                    modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
                    start_date = f"{start_date:%d %b, %Y %H:%M:%S}"
                    form = 2
                    # if request.method == 'POST':
                    #     val = request.POST.get('work_days')
                    #     bet_amount = request.POST.get('bet_amount')
                    #     print('val::', val)
                    #
                    #     print(modified_date)
                    #     V = Value_choosed(value=val, bet_amount=bet_amount, datetime=modified_date, count=count)
                    #     print('vdatetime==', V.datetime)
                    #     V.save()
                    #     print(V.count)
                    #
                    #     print(form)
                    #     return redirect('/game')
                    return render(request, 'game_value.html', {'value': value, 'f': form, 'date': start_date})
            else:

                break

        elif 6 >= c.total_seconds() / 60 >= 1:
            if hou[count] < spi.hours or hou[count] > spi.hours:
                try:
                    va = Value_choosed.objects.get(user_name=request.user)
                    print("1st hanji")
                    v = Value_set.objects.all()
                    print(v[0].value)
                    value = None
                    va.save()
                    modified_date = now.replace(hour=hou[count], minute=dict[hou[count]], second=00)
                    modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
                    return render(request, 'game_value.html', {'value': value, 'f': form, 'date': modified_date})
                except Value_choosed.DoesNotExist:
                    print("1st expect")
                    value = None
                    modified_date = now.replace(hour=hou[count], minute=dict[hou[count]], second=00)
                    end_date = modified_date - datetime.timedelta(hours=0, minutes=1)

                    end_date = f"{end_date:%d %b, %Y %H:%M:%S}"
                    if request.method == 'POST':
                        val = request.POST.get('work_days')
                        bet_amount = request.POST.get('bet_amount')
                        print('val::', val)

                        print(modified_date)
                        V = Value_choosed(user_name=request.user,value=val, bet_amount=bet_amount, datetime=modified_date, count=count)
                        print('vdatetime==', V.datetime)
                        V.save()
                        print(V.count)
                        form = 0
                        print(form)
                        return redirect('/game')
                    return render(request, 'game_value.html', {'value': value, 'f': form, 'date': end_date})
            else:
                break
        # if (now.hour == hou[count] and now.minute == dict[hou[count]]):
        #     if hou[count] <= spi.hours and dict[hou[count]] < spi.minutes:
        #         try:
        #             va = Value_choosed.objects.get(user_name=request.user)
        #             print("1st")
        #             v = Value_set.objects.all()
        #             print(v[0].value)
        #             value = None
        #             va.save()
        #             modified_date = now.replace(hour=hou[count], minute=dict[hou[count]])
        #             modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
        #             return render(request, 'game_value.html', {'value': value, 'f': form, 'date': modified_date})
        #         except Value_choosed.DoesNotExist:
        #             print("1st expect")
        #             value = None
        #             modified_date = now.replace(hour=hou[count], minute=dict[hou[count]])
        #
        #             modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
        #
        #             form = 3
        #             # if request.method == 'POST':
        #             #     val = request.POST.get('work_days')
        #             #     bet_amount = request.POST.get('bet_amount')
        #             #     print('val::', val)
        #             #
        #             #     print(modified_date)
        #             #     V = Value_choosed(value=val, bet_amount=bet_amount, datetime=modified_date, count=count)
        #             #     print('vdatetime==', V.datetime)
        #             #     V.save()
        #             #     print(V.count)
        #             #
        #             #     print(form)
        #             #     return redirect('/game')
        #             return render(request, 'game_value.html', {'value': value, 'f': form, 'date': modified_date})
        #     else:
        #         print('break')
        #         break
        elif c.total_seconds() / 60 == 0:
            print('yt')
            try:

                va = Value_choosed.objects.get(user_name=request.user)
                print("yt try", count, va.count)

                print("helllo count   ")
                if va.spin:
                    return redirect('/game')
                else:
                    print("helllo count   spin")
                    va.spin = True
                    va.save()

                    return redirect('/spin')

            except Value_choosed.DoesNotExist:
                value = None
                modified_date = now.replace(hour=hou[count], minute=dict[hou[count]], second=00)
                modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
                form = 3

                return render(request, 'game_value.html', {'value': value, 'f': form, 'date': modified_date})

    print(now.hour, spi.hours)

    modi_time = now.replace(hour=spi.hours, minute=spi.minutes, second=00)
    c = modi_time - now
    if (now.hour < spi.hours):

        # modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
        try:
            print("2nd")
            va = Value_choosed.objects.get(user_name=request.user)

            v = Value_set.objects.all()
            print(v[0].value)
            value = v[0].value
            va.save()
            # date = va.datetime
            # form = 0

        except Value_choosed.DoesNotExist:
            print("2nd expect")

            start_date = modi_time - datetime.timedelta(hours=0, minutes=6)
            start_date = f"{start_date:%d %b, %Y %H:%M:%S}"
            print("start::::", start_date)
            v = Value_set.objects.all()
            print(v[0].value)
            value = v[0].value
            form = 2
            #
            # # date = now
            # # form = 1
            #
            # print(modified_date)
            #
            # if request.method == 'POST':
            #     val = request.POST.get('work_days')
            #     bet_amount = request.POST.get('bet_amount')
            #     print('val::', val)
            #     count = len(hou)
            #
            #     print(modified_date)
            #     V = Value_choosed(value=val, bet_amount=bet_amount, datetime=modified_date, count=count)
            #     V.save()
            #     print(V.count)
            #     form = 0
            #     return redirect('/game')
            return render(request, 'game_value.html', {'value': value, 'f': form, 'date': start_date})

        return render(request, 'game_value.html', {'value': value, 'f': form, 'date': modi_time})
    if c.total_seconds() / 60 > 6:
        modified_date = now.replace(hour=spi.hours, minute=spi.minutes, second=00)
        # modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
        try:
            print("2nd")
            va = Value_choosed.objects.get(user_name=request.user)

            v = Value_set.objects.all()
            print(v[0].value)
            value = v[0].value
            va.save()
            # date = va.datetime
            # form = 0
            return render(request, 'game_value.html', {'value': value, 'f': form, 'date': modified_date})
        except Value_choosed.DoesNotExist:
            print("2nd expect")
            start_date = modified_date - datetime.timedelta(hours=0, minutes=6)
            start_date = f"{start_date:%d %b, %Y %H:%M:%S}"
            print(start_date, "start_date")
            v = Value_set.objects.all()
            print(v[0].value)
            value = v[0].value
            form = 2
            #
            # # date = now
            # # form = 1
            #
            # print(modified_date)
            #
            # if request.method == 'POST':
            #     val = request.POST.get('work_days')
            #     bet_amount = request.POST.get('bet_amount')
            #     print('val::', val)
            #     count = len(hou)
            #
            #     print(modified_date)
            #     V = Value_choosed(value=val, bet_amount=bet_amount, datetime=modified_date, count=count)
            #     V.save()
            #     print(V.count)
            #     form = 0
            #     return redirect('/game')
            return render(request, 'game_value.html', {'value': value, 'f': form, 'date': start_date})

    if 6 >= c.total_seconds() / 60 > 1:
        print("hmmm how////")
        try:
            va = Value_choosed.objects.get(user_name=request.user)
            print("2nd hanji")
            v = Value_set.objects.all()
            print(v[0].value)
            value = None
            va.save()
            modified_date = now.replace(hour=spi.hours, minute=spi.minutes, second=00)
            modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
            return render(request, 'game_value.html', {'value': value, 'f': form, 'date': modified_date})
        except Value_choosed.DoesNotExist:
            print("2nd expect")
            v = Value_set.objects.all()
            print(v[0].value)
            value = v[0].value
            modified_date = now.replace(hour=spi.hours, minute=spi.minutes, second=00)
            end_date = modified_date - datetime.timedelta(hours=0, minutes=1)
            end_date = f"{end_date:%d %b, %Y %H:%M:%S}"
            form = 1
            print("end:", end_date)
            if request.method == 'POST':
                val = request.POST.get('work_days')
                bet_amount = request.POST.get('bet_amount')
                print('val::', val)
                count = len(hou)
                print(modified_date)
                V = Value_choosed(value=val, bet_amount=bet_amount, datetime=modified_date, count=count)
                print('vdatetime==', V.datetime)
                V.save()
                print(V.count)
                form = 0
                print(form)
                return redirect('/game')
            return render(request, 'game_value.html', {'value': value, 'f': form, 'date': end_date})

    # if (now.hour == spi.hours and now.minute < spi.minutes):
    #     modified_date = now.replace(hour=spi.hours, minute=spi.minutes)
    #     modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
    #     try:
    #         print("2nd")
    #         va = Value_choosed.objects.get(user_name=request.user)
    #
    #         v = Value_set.objects.all()
    #         print(v[0].value)
    #         value = v[0].value
    #         va.save()
    #         # date = va.datetime
    #         # form = 0
    #     except Value_choosed.DoesNotExist:
    #         print("2nd expect")
    #         v = Value_set.objects.all()
    #         print(v[0].value)
    #         value = v[0].value
    #
    #         # date = now
    #         # form = 1
    #         count = len(hou)
    #         print(modified_date)
    #
    #         if request.method == 'POST':
    #             val = request.POST.get('work_days')
    #             bet_amount = request.POST.get('bet_amount')
    #             print('val::', val)
    #
    #             print(modified_date)
    #             V = Value_choosed(value=val, bet_amount=bet_amount, datetime=modified_date, count=count)
    #             V.save()
    #             print(V.count)
    #             form = 0
    #             return redirect('/game')
    #
    #     return render(request, 'game_value.html', {'value': value, 'f': form, 'date': modified_date})

    if c.total_seconds() / 60 == 0:
        try:
            va = Value_choosed.objects.get(user_name=request.user)
            if va.spin:
                return redirect('/game')
            else:

                va.spin = True
                va.save()
                return redirect('/spin')

        except Value_choosed.DoesNotExist:
            value = None
            modified_date = now.replace(hour=spi.hours, minute=dict[spi.hours], second=00)

            modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
            form = 3
            # if request.method == 'POST':
            #     val = request.POST.get('work_days')
            #     bet_amount = request.POST.get('bet_amount')
            #     print('val::', val)
            #     count = len(hou)
            #     print(modified_date)
            #     V = Value_choosed(value=val, bet_amount=bet_amount, datetime=modified_date, count=count)
            #     V.save()
            #     print(V.count)
            #     form = 0
            #     return redirect('/game')
            return render(request, 'game_value.html', {'value': value, 'f': form, 'date': modified_date})
    else:
        print("hiihmmmmm")
        h = hou[0]
        print(h)
        print(now.date())
        now += datetime.timedelta(days=1)

        print(now.date())

        modified_date = now.replace(hour=h, minute=dict[h], second=00)
        modified_date = modified_date - datetime.timedelta(minutes=6)
        modified_date = f"{modified_date:%d %b, %Y %H:%M:%S}"
        form = 2

        return render(request, 'game_value.html', {'value': value, 'f': form, 'date': modified_date})


def home(request):
    flag = 0
    try:
        va = Value_choosed.objects.get(user_name=request.user)
        va_ch = va.value
        v = Value_set.objects.all()
        print(len(v))
        print(v[0].value)
        val = v[0].value
        if va_ch == val:
            flag = 1
        else:
            flag = 0
        print("delete")
        va.delete()
    except Value_choosed.DoesNotExist:
        v = Value_set.objects.all()
        va_ch = None
        print(v[0].value)
        print("expect")
        val = v[0].value

    return render(request, 'home.html', {'value': val, 'va': va_ch, 'press': 1, 'flag': flag})


def wallet(request, win):

    if int(win) == 0:
        win_str = "you loose"
    else:
        win_str = "you win"
    return render(request, 'result.html', {'value': win_str})
