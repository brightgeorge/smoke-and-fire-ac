import json
from django.http import HttpResponse

from django.shortcuts import render
from django.contrib import messages

from restaurant.models import *
from accounts.models import background_color

def bill_wise_report(request):
    if 'username' in request.session:

        dates = request.POST.get('day')
        # ledgers = request.POST.get('ledger')
        print('dates', dates)
        import datetime
        if dates == None:
            d = datetime.datetime.now()
            month = d.strftime("%m")
            day = d.strftime(("%d"))
            r_dates = d
            print('r_dates none', r_dates)
        else:
            dl = []
            for i in dates:
                dl.append(i)

            dll = []
            dll.append(dl[5])
            dll.append(dl[6])
            month = ''.join(dll)

            dal = []
            dal.append(dl[8])
            dal.append(dl[9])
            day = ''.join(dal)

            r_dates = dates
            print('r_dates second', r_dates)

        a = temp_billing.objects.all().filter(day=day, month=month, flag=2)
        il = []
        el = []
        for i in a:
            if i.type == 'income':
                il.append(float(i.amount))
            if i.type == 'expense':
                el.append(float(i.amount))
        print('ill', il)
        sil = sum(il)
        sel = sum(el)

        d_bal = sil - sel

        print('dayyyyy', day)
        print('monthhhhh', month)
        # month='1'

        #####################

        bil = []
        item = temp_billing.objects.all().filter(flag=2, day=day, month=month)
        for i in item:
            bil.append(i.bill_no)
        print('illl', bil)
        sr = []
        gr = []
        grt = []
        a = temp_billing.objects.all().filter(flag=2, day=day, month=month)
        for i in range(len(bil)):
            for j in a:
                if j.bill_no == bil[i]:
                    sr.append(j.amount)
            gr.append(sum(sr))
            grt.append(sum(sr))
            sr.clear()
        print('grrr', gr)
        print('grrrtt', grt)

        itemp = resturant_items.objects.all().filter(flag=1)
        for i in range(len(il)):
            for j in itemp:
                if j.name == il[i]:
                    j.total_item_wise_amt = float(gr[0])
                    j.qty = j.total_item_wise_amt / j.price
            del gr[0]


        stud=dict(zip(bil,grt))
        print('stud',stud)


        #########################
        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,

            # 'hb' : temp_billing.objects.all().filter(day=day,month=month,flag=2),
            'hb': itemp,
            'sil': sil,
            'sel': sel,
            'd_bal': d_bal,
            'dates': r_dates,

            'res' : stud,

        }
    return render(request,'restaurant/reports/bill_wise_report.html',context)


def bill_wise_item_report(request):

    bln = request.POST.get('bn')
    print('bil_no',bln)

    #fbln = int(bln)

    res=[]
    dt=[]
    table=[]
    re=temp_billing.objects.all().filter(flag=2,bill_no=bln)
    for i in re:
        res.append(i.amount)
        dt.append(i.date)
        table.append(i.table_name)

    us = request.session['username']
    bgs = background_color.objects.all().filter(username=us)
    bg = background_color.objects.all().filter(username=us).exists()
    a = []
    if bg == True:
        a.append(us)
    else:
        a.append('f')

    context = {
        'bg': bgs,
        'us': us,
        'th_us': a[0],
        'name': us,

        'item' : temp_billing.objects.all().filter(flag=2,bill_no=bln),
        'gt' : sum(res),
        'bilno' : bln,
        'date' : dt,
        'table' : table,

    }
    return render(request,'restaurant/reports/bill_wise_item_report.html',context)



def item_wise_report(request):
    il = []
    item = resturant_items.objects.all().filter(flag=1)
    for i in item:
        il.append(i.name)
    print(il)
    sr = []
    gr = []
    grt=[]
    a = temp_billing.objects.all().filter(flag=2)
    for i in range(len(il)):
        for j in a:
            if j.particulars == il[i]:
                sr.append(j.amount)
        gr.append(sum(sr))
        grt.append(sum(sr))
        sr.clear()
    print('grrr',gr)

    itemp = resturant_items.objects.all().filter(flag=1)
    for i in range(len(il)):
        for j in itemp:
            if j.name == il[i]:
                j.total_item_wise_amt = float(gr[0])
                j.qty = j.total_item_wise_amt/j.price
        del gr[0]

    us = request.session['username']
    bgs = background_color.objects.all().filter(username=us)
    bg = background_color.objects.all().filter(username=us).exists()
    a = []
    if bg == True:
        a.append(us)
    else:
        a.append('f')

    context = {
        'bg': bgs,
        'us': us,
        'th_us': a[0],
        'name': us,

        'reports' : itemp,
        'grt' : sum(grt),
    }
    return render(request,'restaurant/reports/item_wise_report.html',context)

#item_date_wise_report


def item_date_wise_report(request):
    if 'username' in request.session:

        dates = request.POST.get('day')
        #ledgers = request.POST.get('ledger')
        print('dates',dates)
        import datetime
        if dates == None:
            d = datetime.datetime.now()
            month = d.strftime("%m")
            day=d.strftime(("%d"))
            r_dates = d
            print('r_dates none',r_dates)
        else:
            dl = []
            for i in dates:
                dl.append(i)

            dll = []
            dll.append(dl[5])
            dll.append(dl[6])
            month = ''.join(dll)

            dal = []
            dal.append(dl[8])
            dal.append(dl[9])
            day = ''.join(dal)

            r_dates = dates
            print('r_dates second',r_dates)

        a = temp_billing.objects.all().filter(day=day,month=month,flag=2)
        il=[]
        el=[]
        for i in a:
            if i.type == 'income':
                il.append(float(i.amount))
            if i.type == 'expense':
                el.append(float(i.amount))
        print('ill',il)
        sil=sum(il)
        sel=sum(el)

        d_bal = sil - sel

        print('dayyyyy',day)
        print('monthhhhh',month)
        #month='1'

        #####################

        il = []
        item = resturant_items.objects.all().filter(flag=1)
        for i in item:
            il.append(i.name)
        print('illl',il)
        sr = []
        gr = []
        grt = []
        a = temp_billing.objects.all().filter(flag=2,day=day,month=month)
        for i in range(len(il)):
            for j in a:
                if j.particulars == il[i]:
                    sr.append(j.amount)
            gr.append(sum(sr))
            grt.append(sum(sr))
            sr.clear()
        print('grrr', gr)

        itemp = resturant_items.objects.all().filter(flag=1)
        for i in range(len(il)):
            for j in itemp:
                if j.name == il[i]:
                    j.total_item_wise_amt = float(gr[0])
                    j.qty = j.total_item_wise_amt / j.price
            del gr[0]


    #########################
        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,


            #'hb' : temp_billing.objects.all().filter(day=day,month=month,flag=2),
            'hb' : itemp,
            'sil' : sil,
            'sel' : sel,
            'd_bal' : d_bal,
            'dates' : r_dates,

        }
        return render(request,'restaurant/reports/item_date_wise_report.html',context)
    return render(request, 'index.html')





def kitchen_wise_report(request):
    if 'username' in request.session:

        dates = request.POST.get('day')
        kitchen_names = request.POST.get('kitchen_name')
        print('dates',dates)
        import datetime
        if dates == None:
            d = datetime.datetime.now()
            month = d.strftime("%m")
            day=d.strftime(("%d"))
            r_dates = d
            print('r_dates none',r_dates)
        else:
            dl = []
            for i in dates:
                dl.append(i)

            dll = []
            dll.append(dl[5])
            dll.append(dl[6])
            month = ''.join(dll)

            dal = []
            dal.append(dl[8])
            dal.append(dl[9])
            day = ''.join(dal)

            r_dates = dates
            print('r_dates second',r_dates)

        a = temp_billing.objects.all().filter(day=day,month=month,flag=2)
        il=[]
        el=[]
        for i in a:
            if i.type == 'income':
                il.append(float(i.amount))
            if i.type == 'expense':
                el.append(float(i.amount))
        print('ill',il)
        sil=sum(il)
        sel=sum(el)

        d_bal = sil - sel

        print('dayyyyy',day)
        print('monthhhhh',month)
        #month='1'

        #####################

        ilk = []
        item = kitchen.objects.all().filter(flag=1)
        for i in item:
            ilk.append(i.kitchen_name)
        print('illl kitchen_name ilk',ilk)
        sr = []
        gr = []
        grt = []
        a = temp_billing.objects.all().filter(flag=2,day=day,month=month)
        for i in range(len(ilk)):
            for j in a:
                if j.kitchen == ilk[i]:
                    sr.append(j.amount)
            gr.append(sum(sr))
            grt.append(sum(sr))
            sr.clear()
        print('grrr', gr)

        itemp = kitchen.objects.all().filter(flag=1)
        for i in range(len(ilk)):
            for j in itemp:
                if j.kitchen_name == ilk[i]:
                    j.total_kitchen_wise_amt = float(gr[0])
                    #j.qty = j.total_kitchen_wise_amt / j.price
            del gr[0]


    #########################
        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,


            #'hb' : temp_billing.objects.all().filter(day=day,month=month,flag=2),
            'hb' : itemp,
            'sil' : sil,
            'sel' : sel,
            'd_bal' : d_bal,
            'dates' : r_dates,

            'kitchen_name' : kitchen.objects.all().filter(flag=1),

        }
        return render(request,'restaurant/reports/kitchen_wise_report.html',context)
    return render(request, 'index.html')
