import json

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from accounts.models import table1,in_exp_items_daily,opening_balance,category,ledger,accounts_book,background_color,share_holders
from django.http import JsonResponse



#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

def view_all_category11(request):
    if 'username' in request.session:

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


            'category' : category.objects.all().filter(flag=1).order_by('-id'),

        }
        return render(request,'branches/branch11/accounts/creater_master/category/view_all_category.html',context)
    return render(request, 'index.html')

def create_new_category11(request):
    if 'username' in request.session:

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


            'category' : category.objects.all().filter(flag=1).order_by('-id'),

        }
        return render(request,'branches/branch11/accounts/creater_master/category/create_new_category.html',context)
    return render(request, 'index.html')

def regi_new_category11(request):
    if 'username' in request.session:
        category_names = request.POST.get('category')
        ir = category.objects.all().filter(category_name=category_names,flag=1).exists()

        if ir == True:

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

                'item': category.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'danger',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'CATERGORY ALREADY EXISTS')
            return render(request, 'branches/branch11/accounts/creater_master/items/view_all_items.html', context)
        else:

            ic = category()
            ic.category_name = category_names
            ic.enter_by = 'CB ' + request.session['username']
            import datetime
            ic.cb_date = datetime.datetime.now()
            ic.ub_flag = 0
            ic.flag = 1
            ic.save()

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

                'category' : category.objects.all().filter(flag=1).order_by('-id'),

            }
            messages.info(request, 'CATEGORY CREATED SUCCESSFULLY')
            return render(request,'branches/branch11/accounts/creater_master/category/view_all_category.html',context)
        return render(request, 'index.html')


def update_category11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            category_names = request.POST.get('category')
            ir = category.objects.all().filter(category_name=category_names,flag=1).exclude(id=id).exists()

            if ir == True:

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

                    'msg' : 'danger',
                    'category': category.objects.all().filter(flag=1).order_by('-id'),
                }
                messages.info(request,'CATEGORY ALREADY EXISTS')
                return render(request, 'branches/branch11/accounts/creater_master/category/view_all_category.html', context)
            else:
                ic = category.objects.get(id=id)
                ic.category_name = category_names
                ic.updated_by = 'UB ' + request.session['username']
                import datetime
                ic.ub_date = datetime.datetime.now()
                ic.ub_flag = 1
                ic.flag = 1
                ic.save()

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

                    'msg': 'info',
                    'category': category.objects.all().filter(flag=1).order_by('-id'),
                }
                messages.info(request, 'CATEGORY UPDATED SUCCESSFULLY')
                return render(request, 'branches/branch11/accounts/creater_master/category/view_all_category.html', context)


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


            'item' : table1.objects.all().filter(flag=1).order_by('-id'),
            'msg' : 'success',
            'sd' : category.objects.get(id=id),
            'category': category.objects.all().filter(flag=1).order_by('-id'),
        }

        return render(request,'branches/branch11/accounts/creater_master/category/update_category.html',context)
    return render(request, 'index.html')


def delete_category11(request,id):
    if 'username' in request.session:
        r=category.objects.all().filter(id=id,flag=1).exists()
        if r == True:
            d=category.objects.get(id=id)
            d.deleted_by = 'DB ' + request.session['username']
            import datetime
            d.db_date = datetime.datetime.now()
            d.flag = 2
            d.save()

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

                'item': table1.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'success',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'CATEGORY Deleted Successfully')
            return render(request, 'branches/branch11/accounts/creater_master/category/view_all_category.html', context)
        else:

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

                'item': table1.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'warning',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'CATEGORY already  Deleted')
            return render(request,'branches/branch11/accounts/creater_master/category/view_all_category.html',context)
        return render(request, 'index.html')



def view_all_category_delete11(request):
    if 'username' in request.session:

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


            'category' : category.objects.all().filter(flag=2).order_by('-id'),

        }
        return render(request,'branches/branch11/accounts/creater_master/category/view_all_category_delete.html',context)
    return render(request, 'index.html')

##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

def view_all_items11(request):
    if 'username' in request.session:

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


            'item' : table1.objects.all().filter(flag=1).order_by('-id'),

        }
        return render(request,'branches/branch11/accounts/creater_master/items/view_all_items.html',context)
    return render(request, 'index.html')

def create_new_item11(request):
    if 'username' in request.session:

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


            'item' : table1.objects.all().filter(flag=1).order_by('-id'),
            'category': category.objects.all().filter(flag=1).order_by('-id'),

        }
        return render(request,'branches/branch11/accounts/creater_master/items/create_new_item.html',context)
    return render(request, 'index.html')

def regi_new_item11(request):
    if 'username' in request.session:
        item_name = request.POST.get('name')
        item_category = request.POST.get('category')
        ir = table1.objects.all().filter(name=item_name,flag=1).exists()

        if ir == True:

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

                'item': table1.objects.all().filter(flag=1).order_by('-id'),
                'msg' : 'danger',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request,'ITEM ALREADY EXISTS')
            return render(request, 'branches/branch11/accounts/creater_master/items/view_all_items.html', context)
        else:
            ic = table1()
            ic.name = item_name
            ic.item_category = item_category
            ic.created_by = 'CB '+ request.session['username']
            import datetime
            ic.cb_date = datetime.datetime.now()
            ic.ub_flag = 0
            ic.flag = 1
            ic.save()

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

                'item' : table1.objects.all().filter(flag=1).order_by('-id'),
                'msg' : 'success',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'ITEM CREATED SUCCESSFULLY !!!')
            return render(request,'branches/branch11/accounts/creater_master/items/view_all_items.html',context)
        return render(request, 'index.html')

def delete_item11(request,id):
    if 'username' in request.session:
        r=table1.objects.all().filter(id=id).exists()
        if r == True:
            d=table1.objects.get(id=id)
            d.deleted_by = 'DB ' + request.session['username']
            import datetime
            d.db_date = datetime.datetime.now()
            d.flag = 2
            d.save()

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

                'item': table1.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'success',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'ITEM Deleted Successfully')
            return render(request, 'branches/branch11/accounts/creater_master/items/view_all_items.html', context)
        else:

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

                'item': table1.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'warning',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'ITEM already  Deleted')
            return render(request,'branches/branch11/accounts/creater_master/items/view_all_items.html',context)
        return render(request, 'index.html')


def update_item11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            item_name = request.POST.get('name')
            item_category = request.POST.get('category')
            ir = table1.objects.all().filter(name=item_name,flag=1).exclude(id=id).exists()

            if ir == True:

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

                    'item': table1.objects.all().filter(flag=1).order_by('-id'),
                    'msg' : 'danger',
                    'category': category.objects.all().filter(flag=1).order_by('-id'),
                }
                messages.info(request,'ITEM ALREADY EXISTS')
                return render(request, 'branches/branch11/accounts/creater_master/items/view_all_items.html', context)
            else:
                ic = table1.objects.get(id=id)
                ic.name = item_name
                ic.item_category = item_category
                ic.updated_bys = 'UB '+ request.session['username']
                import datetime
                ic.ub_date = datetime.datetime.now()
                ic.ub_flag = 1
                ic.flag = 1
                ic.save()

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

                    'item': table1.objects.all().filter(flag=1).order_by('-id'),
                    'msg': 'info',
                    'category': category.objects.all().filter(flag=1).order_by('-id'),
                }
                messages.info(request, 'ITEM UPDATED SUCCESSFULLY')
                return render(request, 'branches/branch11/accounts/creater_master/items/view_all_items.html', context)


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


            'item' : table1.objects.all().filter(flag=1).order_by('-id'),
            'msg' : 'success',
            'sd' : table1.objects.get(id=id),
            'category': category.objects.all().filter(flag=1).order_by('-id'),
        }

        return render(request,'branches/branch11/accounts/creater_master/items/update_item.html',context)
    return render(request, 'index.html')

def view_all_items_delete11(request):
    if 'username' in request.session:

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


            'item' : table1.objects.all().filter(flag=2).order_by('-id'),

        }
        return render(request,'branches/branch11/accounts/creater_master/items/view_all_items_delete.html',context)
    return render(request, 'index.html')

##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

def view_all_ledger11(request):
    if 'username' in request.session:

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


            'ledger' : ledger.objects.all().filter(flag=1).order_by('-id'),

        }
        return render(request,'branches/branch11/accounts/creater_master/ledger/view_all_ledger.html',context)
    return render(request, 'index.html')

def create_new_ledger11(request):
    if 'username' in request.session:

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


            'ledger' : ledger.objects.all().filter(flag=1).order_by('-id'),

        }
        return render(request,'branches/branch11/accounts/creater_master/ledger/create_new_ledger.html',context)
    return render(request, 'index.html')

def regi_new_ledger11(request):
    if 'username' in request.session:
        ledger_name = request.POST.get('ledger_name')
        contact_person_name = request.POST.get('contact_person_name')
        contact_person_number = request.POST.get('contact_person_number')
        addres = request.POST.get('address')

        lr=ledger.objects.all().filter(ledger_name=ledger_name,flag=1).exists()
        if lr == False:
            ic = ledger()
            ic.ledger_name = ledger_name
            ic.contact_person_name = contact_person_name
            ic.contact_person_mob = contact_person_number
            ic.address = addres
            ic.created_by = 'CB ' + request.session['username']
            import datetime
            ic.cb_date = datetime.datetime.now()
            ic.ub_flag = 0
            ic.flag = 1
            ic.save()

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

                'ledger' : ledger.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'success'
            }
            messages.info(request, 'LEDGER CREATED SUCCESSFULLY')
            return render(request,'branches/branch11/accounts/creater_master/ledger/view_all_ledger.html',context)
        else:

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

                'ledger': ledger.objects.all().filter(flag=1).order_by('-id'),
                'msg' : 'danger'
            }
            messages.info(request,'LEDGER ALREADY EXISTS')
            return render(request, 'branches/branch11/accounts/creater_master/ledger/view_all_ledger.html', context)
        return render(request, 'index.html')


def delete_ledger11(request,id):
    if 'username' in request.session:
        r=ledger.objects.all().filter(id=id).exists()
        if r == True:
            d=ledger.objects.get(id=id)
            d.deleted_by = 'DB ' + request.session['username']
            import datetime
            d.db_date = datetime.datetime.now()
            d.flag = 2
            d.save()

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

                'ledger': ledger.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'success'
            }
            messages.info(request, 'LEDGER Deleted Successfully')
            return render(request, 'branches/branch11/accounts/creater_master/ledger/view_all_ledger.html', context)
        else:

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

                'ledger': ledger.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'warning'
            }
            messages.info(request, 'LEDGER already  Deleted')
            return render(request,'branches/branch11/accounts/creater_master/ledger/view_all_ledger.html',context)
        return render(request, 'index.html')


def update_ledger11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            ledger_name = request.POST.get('ledger_name')
            contact_person_name = request.POST.get('contact_person_name')
            contact_person_number = request.POST.get('contact_person_number')
            addres = request.POST.get('address')

            ir = ledger.objects.all().filter(ledger_name=ledger_name,flag=1).exclude(id=id).exists()

            if ir == True:

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

                    'msg' : 'danger',
                    'ledger': ledger.objects.all().filter(flag=1).order_by('-id'),
                }
                messages.info(request,'CATEGORY ALREADY EXISTS')
                return render(request, 'branches/branch11/accounts/creater_master/ledger/view_all_ledger.html', context)
            else:
                ic = ledger.objects.get(id=id)
                ic.ledger_name = ledger_name
                ic.contact_person_name = contact_person_name
                ic.contact_person_mob = contact_person_number
                ic.address = addres
                ic.updated_by = 'UB ' + request.session['username']
                import datetime
                ic.ub_date = datetime.datetime.now()
                ic.ub_flag = 1
                ic.flag = 1
                ic.save()

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

                    'msg': 'info',
                    'ledger': ledger.objects.all().filter(flag=1).order_by('-id'),
                }
                messages.info(request, 'CATEGORY UPDATED SUCCESSFULLY')
                return render(request, 'branches/branch11/accounts/creater_master/ledger/view_all_ledger.html', context)


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


            'item' : table1.objects.all().filter(flag=1).order_by('-id'),
            'msg' : 'success',
            'sd' : ledger.objects.get(id=id),
            'ledger': ledger.objects.all().filter(flag=1).order_by('-id'),
        }

        return render(request,'branches/branch11/accounts/creater_master/ledger/update_ledger.html',context)
    return render(request, 'index.html')

def view_all_ledger_delete11(request):
    if 'username' in request.session:

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


            'ledger' : ledger.objects.all().filter(flag=2).order_by('-id'),

        }
        return render(request,'branches/branch11/accounts/creater_master/ledger/view_all_ledger_delete.html',context)
    return render(request, 'index.html')


##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOfOK CREATER START HERE

def view_all_accounts_book11(request):
    if 'username' in request.session:

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


            'accounts_book' : accounts_book.objects.all().filter(flag=1).order_by('-id'),

        }
        return render(request,'branches/branch11/accounts/creater_master/accounts_book/view_all_accounts_book.html',context)
    return render(request, 'index.html')

def create_new_accounts_book11(request):
    if 'username' in request.session:

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


            'accounts_book' : accounts_book.objects.all().filter(flag=1).order_by('-id'),

        }
        return render(request,'branches/branch11/accounts/creater_master/accounts_book/create_new_accounts_book.html',context)
    return render(request, 'index.html')

def regi_new_accounts_book11(request):
    if 'username' in request.session:
        accounts_book_name = request.POST.get('accounts_book_name')

        ar=accounts_book.objects.all().filter(accounts_book_name=accounts_book_name,flag=1).exists()

        if ar == True:

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

                'accounts_book': accounts_book.objects.all().filter(flag=1).order_by('-id'),
                'msg' : 'danger'
            }
            messages.info(request,'ACCOUNTS BOOK Already Exists')
            return render(request, 'branches/branch11/accounts/creater_master/accounts_book/view_all_accounts_book.html',context)
        else:
            ic = accounts_book()
            ic.accounts_book_name = accounts_book_name
            ic.created_by = 'CB ' + request.session['username']
            import datetime
            ic.cb_date = datetime.datetime.now()
            ic.ub_flag = 0
            ic.flag = 1
            ic.save()

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

                'accounts_book' : accounts_book.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'success'
            }
            messages.info(request, 'ACCOUNTS BOOK Created Successfully')
            return render(request,'branches/branch11/accounts/creater_master/accounts_book/view_all_accounts_book.html',context)
        return render(request, 'index.html')



def delete_accounts_book11(request,id):
    if 'username' in request.session:
        r=accounts_book.objects.all().filter(id=id).exists()
        if r == True:
            d=accounts_book.objects.get(id=id)
            d.deleted_by = 'DB ' + request.session['username']
            import datetime
            d.db_date = datetime.datetime.now()
            d.flag = 2
            d.save()

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

                'accounts_book': accounts_book.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'success'
            }
            messages.info(request, 'ACCOUNTS BOOK Deleted Successfully')
            return render(request, 'branches/branch11/accounts/creater_master/accounts_book/view_all_accounts_book.html', context)
        else:

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

                'accounts_book': accounts_book.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'warning'
            }
            messages.info(request, 'ACCOUNTS BOOK already  Deleted')
            return render(request,'branches/branch11/accounts/creater_master/accounts_book/view_all_accounts_book.html',context)
        return render(request, 'index.html')


def update_accounts_book11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            accounts_book_name = request.POST.get('accounts_book_name')
            ir = accounts_book.objects.all().filter(accounts_book_name=accounts_book_name,flag=1).exclude(id=id).exists()

            if ir == True:

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

                    'msg' : 'danger',
                    'accounts_book': accounts_book.objects.all().filter(flag=1).order_by('-id'),
                }
                messages.info(request,'ACCOUNTS BOOK ALREADY EXISTS')
                return render(request, 'branches/branch11/accounts/creater_master/accounts_book/view_all_accounts_book.html', context)
            else:
                ic = accounts_book.objects.get(id=id)
                ic.accounts_book_name = accounts_book_name
                ic.updated_by = 'UB ' + request.session['username']
                import datetime
                ic.ub_date = datetime.datetime.now()
                ic.ub_flag = 1
                ic.flag = 1
                ic.save()

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

                    'msg': 'info',
                    'accounts_book': accounts_book.objects.all().filter(flag=1).order_by('-id'),
                }
                messages.info(request, 'ACCOUNTS BOOK UPDATED SUCCESSFULLY')
                return render(request, 'branches/branch11/accounts/creater_master/accounts_book/view_all_accounts_book.html', context)


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


            'item' : table1.objects.all().order_by('-id'),
            'msg' : 'success',
            'sd' : accounts_book.objects.get(id=id),
            'accounts_book': accounts_book.objects.all().filter(flag=1).order_by('-id'),
        }

        return render(request,'branches/branch11/accounts/creater_master/accounts_book/update_accounts_book.html',context)
    return render(request, 'index.html')

def view_all_accounts_book_delete11(request):
    if 'username' in request.session:

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


            'accounts_book' : accounts_book.objects.all().filter(flag=2).order_by('-id'),

        }
        return render(request,'branches/branch11/accounts/creater_master/accounts_book/view_all_accounts_book_delete.html',context)
    return render(request, 'index.html')

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

def get_countries11(request):
    if 'username' in request.session:

        countries = []
        t1 = table1.objects.all().filter(flag=1)
        for i in t1:
            countries.append(i.name)

        mimetype = 'application/json'
        return HttpResponse(json.dumps(countries), mimetype)
    return render(request, 'index.html')


def in_exp_items_entry11(request):
    if 'username' in request.session:

        a='Afghanistan'
        b='Albania'
        l=[]
        l.append(a)
        l.append(b)

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


            "countries" : ["Afghanistan", "Albania", "a", 'aaaa', 'aa', "Algeria", "Andorra", "Angola", "Anguilla"],
            'items': in_exp_items_daily.objects.all().filter(flag=1).order_by('-id')[:10],
            'ledger' : ledger.objects.all().filter(flag=1),
            'accounts_book': accounts_book.objects.all().filter(flag=1),
        }
        print(context)
        return render(request,'branches/branch11/accounts/journal/in_exp_items_entry.html',context)
    return render(request, 'index.html')



def reg_in_exp_items_entry11(request):
    if 'username' in request.session:

        particulars = request.POST.get('particular')
        amounts = request.POST.get('amount')
        ledgers = request.POST.get('ledger')
        accounts_book_name = request.POST.get('accounts_book_name')
        types = request.POST.get('type')
        dates = request.POST.get('date')
        descriptions = request.POST.get('description')

        dl = []
        for i in dates:
            dl.append(i)

        dll = []
        dll.append(dl[5])
        dll.append(dl[6])

        print(dll)

        month = ''.join(dll)
        print(month)

        dal = []
        dal.append(dl[8])
        dal.append(dl[9])
        print(dal)
        day = ''.join(dal)
        print('date', day)

        yl = []
        yl.append(dl[0])
        yl.append(dl[1])
        yl.append(dl[2])
        yl.append(dl[3])
        print(yl)
        year = ''.join(yl)
        print('year', year)

        res = in_exp_items_daily.objects.all().filter(particulars=particulars,amount=amounts,accounts_book_name=accounts_book_name,type=types,date=dates,description=descriptions,flag=1).exists()
        print('res',res)

        if res == True:

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

                'items': in_exp_items_daily.objects.all().filter(flag=1).order_by('-id')[:10],
                'message_bg' : 'alert-danger',

                'ledger': ledger.objects.all().filter(flag=1),
                'accounts_book': accounts_book.objects.all().filter(flag=1),
            }
            messages.info(request, 'ITEM already exists')
            return render(request, 'branches/branch11/accounts/journal/in_exp_items_entry.html', context)

        else:
            dup = table1.objects.all().filter(name=particulars,flag=1).exists()
            if dup == False:

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

                    'items': in_exp_items_daily.objects.all().filter(flag=1).order_by('-id')[:10],
                    'message_bg': 'alert-danger',

                    'ledger': ledger.objects.all().filter(flag=1),
                    'accounts_book': accounts_book.objects.all().filter(flag=1),
                }
                messages.info(request, 'ITEM NOT FOUND')
                return render(request, 'branches/branch11/accounts/journal/in_exp_items_entry.html', context)

            else:
                cat = table1.objects.all().filter(flag=1)
                lnam = []
                lcat = []
                for i in cat:
                    if i.name == particulars:
                        lnam.append(i.name)
                        lcat.append(i.item_category)
                print('lll nam',lnam)
                print('ljljl ca',lcat)

                ic = in_exp_items_daily()
                ic.particulars = particulars
                ic.amount = float(amounts)
                ic.ledger = ledgers
                ic.accounts_book_name = accounts_book_name
                ic.type = types
                ic.date = dates
                ic.item_catergory = lcat[0]
                ic.description = descriptions
                ic.day = day
                ic.month = month
                ic.year = year
                ic.enter_by = 'CB ' + request.session['username']
                import datetime
                ic.cb_date = datetime.datetime.now()
                ic.ub_flag = 0
                ic.flag = 1
                ic.save()

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

                    'items' : in_exp_items_daily.objects.all().filter(flag=1).order_by('-id')[:10],
                    'message_bg': 'alert-success',

                    'ledger': ledger.objects.all().filter(flag=1),
                    'accounts_book': accounts_book.objects.all().filter(flag=1),
                }
                messages.info(request, 'ITEM Entered Successfully')
                return render(request,'branches/branch11/accounts/journal/in_exp_items_entry.html',context)
        return render(request, 'branches/branch11/accounts/journal/in_exp_items_entry.html', context)
    return render(request, 'index.html')

def delete_journal11(request,id):
    if 'username' in request.session:

        r=in_exp_items_daily.objects.all().filter(id=id,flag=1).exists()
        if r == True:
            d=in_exp_items_daily.objects.get(id=id)
            d.deleted_by = 'DB ' + request.session['username']
            import datetime
            d.db_date = datetime.datetime.now()
            d.flag = 2
            d.save()

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

                'items': in_exp_items_daily.objects.all().filter(flag=1).order_by('-id')[:10],
                'message_bg': 'alert-success',

                'ledger': ledger.objects.all().filter(flag=1),
                'accounts_book': accounts_book.objects.all().filter(flag=1),
            }
            messages.info(request, 'ITEM Deleted Successfully')
            return render(request, 'branches/branch11/accounts/journal/in_exp_items_entry.html', context)
        else:

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

                'items': in_exp_items_daily.objects.all().filter(flag=1).order_by('-id')[:10],
                'message_bg': 'alert-warning',

                'ledger': ledger.objects.all().filter(flag=1),
                'accounts_book': accounts_book.objects.all().filter(flag=1),
            }
            messages.info(request, 'ITEM already  Deleted')
            return render(request,'branches/branch11/accounts/journal/in_exp_items_entry.html',context)
        return render(request, 'index.html')



def update_in_exp_items_entry11(request,id):
    if 'username' in request.session:

        if request.method == 'POST':
            particulars = request.POST.get('particular')
            amounts = request.POST.get('amount')
            ledgers = request.POST.get('ledger')
            accounts_book_name = request.POST.get('accounts_book_name')
            types = request.POST.get('type')
            dates = request.POST.get('date')
            descriptions = request.POST.get('description')

            dup = table1.objects.all().filter(name=particulars,flag=1).exists()
            if dup == False:

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

                    'items': in_exp_items_daily.objects.all().filter(flag=1).order_by('-id')[:10],
                    'message_bg': 'alert-danger',
                    'ledger': ledger.objects.all().filter(flag=1),
                    'accounts_book': accounts_book.objects.all().filter(flag=1),
                }
                messages.info(request, 'ITEM NOT FOUND')
                return render(request, 'branches/branch11/accounts/journal/in_exp_items_entry.html', context)
            else:

                dl = []
                for i in dates:
                    dl.append(i)

                dll = []
                dll.append(dl[5])
                dll.append(dl[6])

                print(dll)

                month = ''.join(dll)
                print(month)

                dal = []
                dal.append(dl[8])
                dal.append(dl[9])
                print(dal)
                day = ''.join(dal)
                print('date', day)

                yl = []
                yl.append(dl[0])
                yl.append(dl[1])
                yl.append(dl[2])
                yl.append(dl[3])
                print(yl)
                year = ''.join(yl)
                print('year', year)

                cat = table1.objects.all().filter(flag=1)
                lnam = []
                lcat = []
                for i in cat:
                    if i.name == particulars:
                        lnam.append(i.name)
                        lcat.append(i.item_category)
                print('lll nam', lnam)
                print('ljljl ca', lcat)

                ic = in_exp_items_daily.objects.get(id=id)
                ic.particulars = particulars
                ic.amount = float(amounts)
                ic.ledger = ledgers
                ic.accounts_book_name = accounts_book_name
                ic.type = types
                ic.date = dates
                ic.item_catergory = lcat[0]
                ic.description = descriptions
                ic.day = day
                ic.month = month
                ic.year = year
                ic.updated_by = 'UB ' + request.session['username']
                import datetime
                ic.ub_date = datetime.datetime.now()
                ic.ub_flag = 1
                ic.flag = 1
                ic.save()

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

                    'items': in_exp_items_daily.objects.all().filter(flag=1).order_by('-id')[:10],
                    'message_bg': 'alert-info',
                    'ledger': ledger.objects.all().filter(flag=1),
                    'accounts_book': accounts_book.objects.all().filter(flag=1),
                }
                messages.info(request, 'ITEM Updated Successfully')
                return render(request, 'branches/branch11/accounts/journal/in_exp_items_entry.html', context)


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


            'items': in_exp_items_daily.objects.all().filter(flag=1).order_by('-id')[:10],
            'message_bg': 'alert-success',

            'ledger': ledger.objects.all().filter(flag=1),
            'accounts_book': accounts_book.objects.all().filter(flag=1),
            'sd': in_exp_items_daily.objects.get(id=id)
        }
        return render(request, 'branches/branch11/accounts/journal/update_in_exp_items_entry.html', context)
    return render(request, 'index.html')

def detailed_journal_report11(request):
    if 'username' in request.session:


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


            'items': in_exp_items_daily.objects.all().filter(flag=1).order_by('-id'),
            'message_bg': 'alert-danger',

            'ledger': ledger.objects.all().filter(flag=1),
            'accounts_book': accounts_book.objects.all().filter(flag=1),
        }
        return render(request, 'branches/branch11/accounts/journal/detailed_journal_report.html', context)
    return render(request, 'index.html')

def journal_report_deleted11(request):
    if 'username' in request.session:


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


            'items': in_exp_items_daily.objects.all().filter(flag=2).order_by('-id'),
            'message_bg': 'alert-danger',

        }
        return render(request, 'branches/branch11/accounts/journal/journal_report_deleted.html', context)
    return render(request, 'index.html')



#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################

###************ CATEGORY WISE REPORT START HERE ***********


def daily_category_wise11(request):
    if 'username' in request.session:

        item_catergory = request.POST.get('item_catergory')
        dates = request.POST.get('day')
        import datetime
        if dates == None:
            d = datetime.datetime.now()
            month = d.strftime("%m")
            day = d.strftime(("%d"))
            r_dates = d
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

        a=in_exp_items_daily.objects.all().filter(day=day,month=month,item_catergory=item_catergory,flag=1)
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


            'hb' : in_exp_items_daily.objects.all().filter(day=day,month=month,item_catergory=item_catergory,flag=1),
            'hname' : item_catergory,
            'r_dates' : r_dates,
            #'total' : r,
            'category' : category.objects.all().filter(flag=1),
            'sil': sil,
            'sel': sel,
            'd_bal': d_bal,
            'particular' : item_catergory,

        }
        return render(request,'branches/branch11/accounts/accounts_reports/category/daily_category_wise.html',context)
    return render(request, 'index.html')


def monthly_category_based_reports11(request):
    if 'username' in request.session:

        item_catergory = request.POST.get('item_catergory')
        month = request.POST.get('month')

        a =  in_exp_items_daily.objects.all().filter(item_catergory=item_catergory,month=month,flag=1)
        l=[]
        for i in a:
            if i.amount > 0:
                l.append(float(i.amount))
        r=sum(l)

        a = in_exp_items_daily.objects.all().filter(item_catergory=item_catergory,month=month,flag=1)
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

        import datetime
        r_dates = datetime.datetime.now()


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


            'hb' : in_exp_items_daily.objects.all().filter(item_catergory=item_catergory,month=month,flag=1),
            'hname' : item_catergory,
            'total' : r,

            'sil': sil,
            'sel': sel,
            'd_bal': d_bal,
            'dates': r_dates,
            'category': category.objects.all().filter(flag=1),

        }
        return render(request,'branches/branch11/accounts/accounts_reports/category/monthly_category_based_reports.html',context)
    return render(request, 'index.html')


def yearly_category_based_reports11(request):
    if 'username' in request.session:

        item_catergory = request.POST.get('item_catergory')

        a=in_exp_items_daily.objects.all().filter(item_catergory=item_catergory,flag=1)
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


            'hb' : in_exp_items_daily.objects.all().filter(item_catergory=item_catergory,flag=1).order_by('month'),
            'hname' : item_catergory,
            'category' : category.objects.all().filter(flag=1),
            'sil': sil,
            'sel': sel,
            'd_bal': d_bal,

        }
        return render(request,'branches/branch11/accounts/accounts_reports/category/yearly_category_based_reports.html',context)
    return render(request, 'index.html')


####********* CATEGORY WISE REPORT END HERE ***************

###*************DAILY DETAILED REPORTS  START HERE


def daily_detailed11(request):
    if 'username' in request.session:

        dates = request.POST.get('day')
        import datetime
        if dates == None:
            d = datetime.datetime.now()
            month = d.strftime("%m")
            day=d.strftime(("%d"))
            r_dates = d
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

        a = in_exp_items_daily.objects.all().filter(day=day,month=month,flag=1)
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


            'dd' : in_exp_items_daily.objects.all().filter(day=day,month=month,flag=1),
            'sil' : sil,
            'sel' : sel,
            'd_bal' : d_bal,
            'dates' : r_dates,
        }
        return render(request,'branches/branch11/accounts/accounts_reports/detailed/daily_detailed.html',context)
    return render(request, 'index.html')


def monthly_detailed11(request):
    if 'username' in request.session:

        month = request.POST.get('month')
        a = in_exp_items_daily.objects.all().filter(month=month,flag=1)
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


            'dd' : in_exp_items_daily.objects.all().filter(month=month,flag=1),
            'sil' : sil,
            'sel' : sel,
            'd_bal' : d_bal,

        }
        return render(request,'branches/branch11/accounts/accounts_reports/detailed/monthly_detailed.html',context)
    return render(request, 'index.html')


def yearly_detailed11(request):
    if 'username' in request.session:

        a = in_exp_items_daily.objects.all().filter(flag=1).order_by('month')
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


            'dd' : in_exp_items_daily.objects.all().filter(flag=1).order_by('month'),
            'sil' : sil,
            'sel' : sel,
            'd_bal' : d_bal,

        }
        return render(request,'branches/branch11/accounts/accounts_reports/detailed/yearly_detailed.html',context)
    return render(request, 'index.html')


###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

def item_based_reports11(request):
    if 'username' in request.session:

        particular = request.POST.get('item')

        a=in_exp_items_daily.objects.all().filter(particulars=particular,flag=1)
        l=[]
        for i in a:
            if i.amount > 0:
                l.append(float(i.amount))
        r=sum(l)


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


            'hb' : in_exp_items_daily.objects.all().filter(particulars=particular,flag=1),
            'hname' : particular,
            'total' : r,
            'item' : in_exp_items_daily.objects.all().filter(flag=1),

        }
        return render(request,'branches/branch11/accounts/accounts_reports/item/item_based_reports.html',context)
    return render(request, 'index.html')



def daily_item_based_reports11(request):
    if 'username' in request.session:

        particular = request.POST.get('item')
        dates = request.POST.get('day')
        import datetime
        if dates == None:
            d = datetime.datetime.now()
            month = d.strftime("%m")
            day = d.strftime(("%d"))
            r_dates = d
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

        a=in_exp_items_daily.objects.all().filter(day=day,month=month,particulars=particular,flag=1)
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


            'hb' : in_exp_items_daily.objects.all().filter(day=day,month=month,particulars=particular,flag=1),
            'hname' : particular,
            'r_dates' : r_dates,
            #'total' : r,
            'item' : table1.objects.all().filter(flag=1),
            'sil': sil,
            'sel': sel,
            'd_bal': d_bal,
            'particular' : particular,

        }
        return render(request,'branches/branch11/accounts/accounts_reports/item/daily_item_based_reports.html',context)
    return render(request, 'index.html')



def monthly_item_based_reports11(request):
    if 'username' in request.session:

        particular = request.POST.get('item')
        month = request.POST.get('month')


        a=in_exp_items_daily.objects.all().filter(month=month,particulars=particular,flag=1)
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


            'hb' : in_exp_items_daily.objects.all().filter(month=month,particulars=particular,flag=1),
            'hname' : particular,
            #'r_dates' : r_dates,
            #'total' : r,
            'item' : table1.objects.all().filter(flag=1),
            'sil': sil,
            'sel': sel,
            'd_bal': d_bal,
            'particular' : particular,

        }
        return render(request,'branches/branch11/accounts/accounts_reports/item/monthly_item_based_reports.html',context)
    return render(request, 'index.html')


###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE


def daily_ledger_based_reports11(request):
    if 'username' in request.session:

        dates = request.POST.get('day')
        ledgers = request.POST.get('ledger')
        import datetime
        if dates == None:
            d = datetime.datetime.now()
            month = d.strftime("%m")
            day=d.strftime(("%d"))
            r_dates = d
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

        a = in_exp_items_daily.objects.all().filter(day=day,month=month,ledger=ledgers,flag=1)
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


            'hb' : in_exp_items_daily.objects.all().filter(day=day,month=month,ledger=ledgers,flag=1),
            'sil' : sil,
            'sel' : sel,
            'd_bal' : d_bal,
            'dates' : r_dates,
            'ledger': ledger.objects.all().filter(flag=1),
            'lname': ledgers,
        }
        return render(request,'branches/branch11/accounts/accounts_reports/ledger/daily_ledger_based_reports.html',context)
    return render(request, 'index.html')


def ledger_based_reports11(request):
    if 'username' in request.session:

        ledgers = request.POST.get('ledger')

        a =  in_exp_items_daily.objects.all().filter(ledger=ledgers,flag=1)
        l=[]
        for i in a:
            if i.amount > 0:
                l.append(float(i.amount))
        r=sum(l)

        a = in_exp_items_daily.objects.all().filter(ledger=ledgers,flag=1)
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

        import datetime
        r_dates = datetime.datetime.now()


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


            'hb' : in_exp_items_daily.objects.all().filter(ledger=ledgers,flag=1),
            'hname' : ledgers,
            'total' : r,

            'sil': sil,
            'sel': sel,
            'd_bal': d_bal,
            'dates': r_dates,
            'ledger': ledger.objects.all(),

        }
        return render(request,'branches/branch11/accounts/accounts_reports/ledger/ledger_based_reports.html',context)
    return render(request, 'index.html')



def monthly_ledger_based_reports11(request):
    if 'username' in request.session:

        ledgers = request.POST.get('ledger')
        month = request.POST.get('month')

        a =  in_exp_items_daily.objects.all().filter(ledger=ledgers,month=month,flag=1)
        l=[]
        for i in a:
            if i.amount > 0:
                l.append(float(i.amount))
        r=sum(l)

        a = in_exp_items_daily.objects.all().filter(ledger=ledgers,month=month,flag=1)
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

        import datetime
        r_dates = datetime.datetime.now()


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


            'hb' : in_exp_items_daily.objects.all().filter(ledger=ledgers,month=month,flag=1),
            'hname' : ledgers,
            'total' : r,

            'sil': sil,
            'sel': sel,
            'd_bal': d_bal,
            'dates': r_dates,
            'ledger': ledger.objects.all().filter(flag=1),

        }
        return render(request,'branches/branch11/accounts/accounts_reports/ledger/monthly_ledger_based_reports.html',context)
    return render(request, 'index.html')


###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE


def accounts_book_based_reports11(request):
    if 'username' in request.session:

        accounts_book_name = request.POST.get('accounts_book_name')
        a=in_exp_items_daily.objects.all().filter(accounts_book_name=accounts_book_name,flag=1)

        l=[]
        for i in a:
            if i.amount > 0:
                l.append(float(i.amount))
        r=sum(l)


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


            'hb' : in_exp_items_daily.objects.all().filter(accounts_book_name=accounts_book_name,flag=1),
            'hname' : accounts_book_name,
            'total' : r,
            'accounts_book' : accounts_book.objects.all().filter(flag=1),

        }
        return render(request,'branches/branch11/accounts/accounts_reports/accounts_book/accounts_book_name_based_reports.html',context)
    return render(request, 'index.html')



def daily_accounts_book_based_reports11(request):
    if 'username' in request.session:

        accounts_book_name = request.POST.get('accounts_book_name')
        dates = request.POST.get('day')
        import datetime
        if dates == None:
            d = datetime.datetime.now()
            month = d.strftime("%m")
            day = d.strftime(("%d"))
            r_dates = d
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

        a=in_exp_items_daily.objects.all().filter(day=day,month=month,accounts_book_name=accounts_book_name,flag=1)
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


            'hb' : in_exp_items_daily.objects.all().filter(day=day,month=month,accounts_book_name=accounts_book_name,flag=1),
            'hname' : accounts_book_name,
            'r_dates' : r_dates,
            'item' : table1.objects.all().filter(flag=1),
            'sil': sil,
            'sel': sel,
            'd_bal': d_bal,
            'accounts_book' : accounts_book.objects.all().filter(flag=1),

        }
        return render(request,'branches/branch11/accounts/accounts_reports/accounts_book/daily_accounts_book_based_reports.html',context)
    return render(request, 'index.html')



def monthly_accounts_book_based_reports11(request):
    if 'username' in request.session:

        accounts_book_name = request.POST.get('accounts_book_name')
        month = request.POST.get('month')


        a=in_exp_items_daily.objects.all().filter(month=month,accounts_book_name=accounts_book_name,flag=1)
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


            'hb' : in_exp_items_daily.objects.all().filter(month=month,accounts_book_name=accounts_book_name,flag=1),
            'hname' : accounts_book_name,
            'item' : table1.objects.all().filter(flag=1),
            'sil': sil,
            'sel': sel,
            'd_bal': d_bal,
            'accounts_book' : accounts_book.objects.all().filter(flag=1),

        }
        return render(request,'branches/branch11/accounts/accounts_reports/accounts_book/monthly_accounts_book_based_reports.html',context)
    return render(request, 'index.html')



###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

def monthly_reports_choose_months11(request):
    if 'username' in request.session:

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



        }
        return render(request,'branches/branch11/accounts/monthly_reports/monthly_reports_choose_months.html',context)
    return render(request, 'index.html')


def monthly_detailed_daily_in_exp_items_report11(request,mo):
    if 'username' in request.session:

        mth=mo
        print('moooooo0',mo)

        queryset = in_exp_items_daily.objects.filter(month=mth,type='income',flag=1)
        totals = queryset.aggregate(sum=Sum('amount'))

        mth_list= ['*','JAN','FEB','MARCH','APRIL','MAY','JUN','JUL','AUG','SEPT','OCT','NOV','DEC']
        n_mth= int(mth)
        month_name_dis = mth_list[n_mth]

        ye_list= ['*','2024','2024','2024','2023','2023','2023','2023','2023','2023','2023','2023','2023']
        n_ye= int(mth)
        ye_name_dis = ye_list[n_ye]

        #ob = opening_balance.objects.all().filter(month_no=mth,month_name='aug',flag=1)
        #l_opening_balance=[]
        #for i in ob:
            #l_opening_balance.append(float(i.month_amount))
        #aug_opening_balance= sum(l_opening_balance)

        #if aug_opening_balance >0:
            #color='green'
        #elif aug_opening_balance < 0:
            #color = 'red'
        #else:
            #color = 'orange'
        opening_balance = 0


        income_1 = in_exp_items_daily.objects.filter(month=mth, type='income', day='01',flag=1)
        l_income_1 = []
        for i in income_1:
            l_income_1.append(float(i.amount))
        r_income_1 = sum(l_income_1)
        expense_1 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='01',flag=1)
        l_expense_1 = []
        for i in expense_1:
            l_expense_1.append(float(i.amount))
        r_expense_1 = sum(l_expense_1)
        r_balance_1 = opening_balance + r_income_1 - r_expense_1

        income_2 = in_exp_items_daily.objects.filter(month=mth, type='income', day='02',flag=1)
        l_income_2 = []
        for i in income_2:
            l_income_2.append(float(i.amount))
        r_income_2 = sum(l_income_2)
        expense_2 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='02',flag=1)
        l_expense_2 = []
        for i in expense_2:
            l_expense_2.append(float(i.amount))
        r_expense_2 = sum(l_expense_2)
        r_balance_2 = r_balance_1+r_income_2 - r_expense_2

        income_3 = in_exp_items_daily.objects.filter(month=mth, type='income', day='03',flag=1)
        l_income_3 = []
        for i in income_3:
            l_income_3.append(float(i.amount))
        r_income_3 = sum(l_income_3)
        expense_3 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='03',flag=1)
        l_expense_3 = []
        for i in expense_3:
            l_expense_3.append(float(i.amount))
        r_expense_3 = sum(l_expense_3)
        r_balance_3 = r_balance_2+r_income_3 - r_expense_3

        income_4 = in_exp_items_daily.objects.filter(month=mth, type='income', day='04',flag=1)
        l_income_4 = []
        for i in income_4:
            l_income_4.append(float(i.amount))
        r_income_4 = sum(l_income_4)
        expense_4 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='04',flag=1)
        l_expense_4 = []
        for i in expense_4:
            l_expense_4.append(float(i.amount))
        r_expense_4 = sum(l_expense_4)
        r_balance_4 = r_balance_3+r_income_4 - r_expense_4

        income_5 = in_exp_items_daily.objects.filter(month=mth, type='income', day='05',flag=1)
        l_income_5 = []
        for i in income_5:
            l_income_5.append(float(i.amount))
        r_income_5 = sum(l_income_5)
        expense_5 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='05',flag=1)
        l_expense_5 = []
        for i in expense_5:
            l_expense_5.append(float(i.amount))
        r_expense_5 = sum(l_expense_5)
        r_balance_5 = r_balance_4+r_income_5 - r_expense_5

        income_6 = in_exp_items_daily.objects.filter(month=mth, type='income', day='06',flag=1)
        l_income_6 = []
        for i in income_6:
            l_income_6.append(float(i.amount))
        r_income_6 = sum(l_income_6)
        expense_6 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='06',flag=1)
        l_expense_6 = []
        for i in expense_6:
            l_expense_6.append(float(i.amount))
        r_expense_6 = sum(l_expense_6)
        r_balance_6 = r_balance_5+r_income_6 - r_expense_6

        income_7 = in_exp_items_daily.objects.filter(month=mth, type='income', day='07',flag=1)
        l_income_7 = []
        for i in income_7:
            l_income_7.append(float(i.amount))
        r_income_7 = sum(l_income_7)
        expense_7 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='07',flag=1)
        l_expense_7 = []
        for i in expense_7:
            l_expense_7.append(float(i.amount))
        r_expense_7 = sum(l_expense_7)
        r_balance_7 = r_balance_6+r_income_7 - r_expense_7
    ###***************************************
        income_8 = in_exp_items_daily.objects.filter(month=mth, type='income', day='08',flag=1)
        l_income_8 = []
        for i in income_8:
            l_income_8.append(float(i.amount))
        r_income_8 = sum(l_income_8)
        expense_8 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='08',flag=1)
        l_expense_8 = []
        for i in expense_8:
            l_expense_8.append(float(i.amount))
        r_expense_8 = sum(l_expense_8)
        r_balance_8 = r_balance_7 + r_income_8 - r_expense_8

        income_9 = in_exp_items_daily.objects.filter(month=mth, type='income', day='09',flag=1)
        l_income_9 = []
        for i in income_9:
            l_income_9.append(float(i.amount))
        r_income_9 = sum(l_income_9)
        expense_9 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='09',flag=1)
        l_expense_9 = []
        for i in expense_9:
            l_expense_9.append(float(i.amount))
        r_expense_9 = sum(l_expense_9)
        r_balance_9 = r_balance_8 + r_income_9 - r_expense_9

        income_10 = in_exp_items_daily.objects.filter(month=mth, type='income', day='10',flag=1)
        l_income_10 = []
        for i in income_10:
            l_income_10.append(float(i.amount))
        r_income_10 = sum(l_income_10)
        expense_10 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='10',flag=1)
        l_expense_10 = []
        for i in expense_10:
            l_expense_10.append(float(i.amount))
        r_expense_10 = sum(l_expense_10)
        r_balance_10 = r_balance_9 + r_income_10 - r_expense_10

        income_11 = in_exp_items_daily.objects.filter(month=mth, type='income', day='11',flag=1)
        l_income_11 = []
        for i in income_11:
            l_income_11.append(float(i.amount))
        r_income_11 = sum(l_income_11)
        expense_11 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='11',flag=1)
        l_expense_11 = []
        for i in expense_11:
            l_expense_11.append(float(i.amount))
        r_expense_11 = sum(l_expense_11)
        r_balance_11 = r_balance_10 + r_income_11 - r_expense_11

        income_12 = in_exp_items_daily.objects.filter(month=mth, type='income', day='12',flag=1)
        l_income_12 = []
        for i in income_12:
            l_income_12.append(float(i.amount))
        r_income_12 = sum(l_income_12)
        expense_12 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='12',flag=1)
        l_expense_12 = []
        for i in expense_12:
            l_expense_12.append(float(i.amount))
        r_expense_12 = sum(l_expense_12)
        r_balance_12 = r_balance_11 + r_income_12 - r_expense_12

        income_13 = in_exp_items_daily.objects.filter(month=mth, type='income', day='13',flag=1)
        l_income_13 = []
        for i in income_13:
            l_income_13.append(float(i.amount))
        r_income_13 = sum(l_income_13)
        expense_13 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='13',flag=1)
        l_expense_13 = []
        for i in expense_13:
            l_expense_13.append(float(i.amount))
        r_expense_13 = sum(l_expense_13)
        r_balance_13 = r_balance_12 + r_income_13 - r_expense_13

        income_14 = in_exp_items_daily.objects.filter(month=mth, type='income', day='14',flag=1)
        l_income_14 = []
        for i in income_14:
            l_income_14.append(float(i.amount))
        r_income_14 = sum(l_income_14)
        expense_14 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='14',flag=1)
        l_expense_14 = []
        for i in expense_14:
            l_expense_14.append(float(i.amount))
        r_expense_14 = sum(l_expense_14)
        r_balance_14 = r_balance_13 + r_income_14 - r_expense_14
    ###*****************************
        income_15 = in_exp_items_daily.objects.filter(month=mth, type='income', day='15',flag=1)
        l_income_15 = []
        for i in income_15:
            l_income_15.append(float(i.amount))
        r_income_15 = sum(l_income_15)
        expense_15 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='15',flag=1)
        l_expense_15 = []
        for i in expense_15:
            l_expense_15.append(float(i.amount))
        r_expense_15 = sum(l_expense_15)
        r_balance_15 = r_balance_14 + r_income_15 - r_expense_15

        income_16 = in_exp_items_daily.objects.filter(month=mth, type='income', day='16',flag=1)
        l_income_16 = []
        for i in income_16:
            l_income_16.append(float(i.amount))
        r_income_16 = sum(l_income_16)
        expense_16 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='16',flag=1)
        l_expense_16 = []
        for i in expense_16:
            l_expense_16.append(float(i.amount))
        r_expense_16 = sum(l_expense_16)
        r_balance_16 = r_balance_15 + r_income_16 - r_expense_16

        income_17 = in_exp_items_daily.objects.filter(month=mth, type='income', day='17',flag=1)
        l_income_17 = []
        for i in income_17:
            l_income_17.append(float(i.amount))
        r_income_17 = sum(l_income_17)
        expense_17 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='17',flag=1)
        l_expense_17 = []
        for i in expense_17:
            l_expense_17.append(float(i.amount))
        r_expense_17 = sum(l_expense_17)
        r_balance_17 = r_balance_16 + r_income_17 - r_expense_17

        income_18 = in_exp_items_daily.objects.filter(month=mth, type='income', day='18',flag=1)
        l_income_18 = []
        for i in income_18:
            l_income_18.append(float(i.amount))
        r_income_18 = sum(l_income_18)
        expense_18 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='18',flag=1)
        l_expense_18 = []
        for i in expense_18:
            l_expense_18.append(float(i.amount))
        r_expense_18 = sum(l_expense_18)
        r_balance_18 = r_balance_17 + r_income_18 - r_expense_18

        income_19 = in_exp_items_daily.objects.filter(month=mth, type='income', day='19',flag=1)
        l_income_19 = []
        for i in income_19:
            l_income_19.append(float(i.amount))
        r_income_19 = sum(l_income_19)
        expense_19 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='19',flag=1)
        l_expense_19 = []
        for i in expense_19:
            l_expense_19.append(float(i.amount))
        r_expense_19 = sum(l_expense_19)
        r_balance_19 = r_balance_18 + r_income_19 - r_expense_19

        income_20 = in_exp_items_daily.objects.filter(month=mth, type='income', day='20',flag=1)
        l_income_20 = []
        for i in income_20:
            l_income_20.append(float(i.amount))
        r_income_20 = sum(l_income_20)
        expense_20 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='20',flag=1)
        l_expense_20 = []
        for i in expense_20:
            l_expense_20.append(float(i.amount))
        r_expense_20 = sum(l_expense_20)
        r_balance_20 = r_balance_19 + r_income_20 - r_expense_20

        income_21 = in_exp_items_daily.objects.filter(month=mth, type='income', day='21',flag=1)
        l_income_21 = []
        for i in income_21:
            l_income_21.append(float(i.amount))
        r_income_21 = sum(l_income_21)
        expense_21 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='21',flag=1)
        l_expense_21 = []
        for i in expense_21:
            l_expense_21.append(float(i.amount))
        r_expense_21 = sum(l_expense_21)
        r_balance_21 = r_balance_20 + r_income_21 - r_expense_21

        income_22 = in_exp_items_daily.objects.filter(month=mth, type='income', day='22',flag=1)
        l_income_22 = []
        for i in income_22:
            l_income_22.append(float(i.amount))
        r_income_22 = sum(l_income_22)
        expense_22 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='22',flag=1)
        l_expense_22 = []
        for i in expense_22:
            l_expense_22.append(float(i.amount))
        r_expense_22 = sum(l_expense_22)
        r_balance_22 = r_balance_21 + r_income_22 - r_expense_22
    ####************************
        income_23 = in_exp_items_daily.objects.filter(month=mth, type='income', day='23',flag=1)
        l_income_23 = []
        for i in income_23:
            l_income_23.append(float(i.amount))
        r_income_23 = sum(l_income_23)
        expense_23 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='23',flag=1)
        l_expense_23 = []
        for i in expense_23:
            l_expense_23.append(float(i.amount))
        r_expense_23 = sum(l_expense_23)
        r_balance_23 = r_balance_22 + r_income_23 - r_expense_23

        income_24 = in_exp_items_daily.objects.filter(month=mth, type='income', day='24',flag=1)
        l_income_24 = []
        for i in income_24:
            l_income_24.append(float(i.amount))
        r_income_24 = sum(l_income_24)
        expense_24 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='24',flag=1)
        l_expense_24 = []
        for i in expense_24:
            l_expense_24.append(float(i.amount))
        r_expense_24 = sum(l_expense_24)
        r_balance_24 = r_balance_23 + r_income_24 - r_expense_24

        income_25 = in_exp_items_daily.objects.filter(month=mth, type='income', day='25',flag=1)
        l_income_25 = []
        for i in income_25:
            l_income_25.append(float(i.amount))
        r_income_25 = sum(l_income_25)
        expense_25 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='25',flag=1)
        l_expense_25 = []
        for i in expense_25:
            l_expense_25.append(float(i.amount))
        r_expense_25 = sum(l_expense_25)
        r_balance_25 = r_balance_24 + r_income_25 - r_expense_25

        income_26 = in_exp_items_daily.objects.filter(month=mth, type='income', day='26',flag=1)
        l_income_26 = []
        for i in income_26:
            l_income_26.append(float(i.amount))
        r_income_26 = sum(l_income_26)
        expense_26 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='26',flag=1)
        l_expense_26 = []
        for i in expense_26:
            l_expense_26.append(float(i.amount))
        r_expense_26 = sum(l_expense_26)
        r_balance_26 = r_balance_25 + r_income_26 - r_expense_26

        income_27 = in_exp_items_daily.objects.filter(month=mth, type='income', day='27',flag=1)
        l_income_27 = []
        for i in income_27:
            l_income_27.append(float(i.amount))
        r_income_27 = sum(l_income_27)
        expense_27 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='27',flag=1)
        l_expense_27 = []
        for i in expense_27:
            l_expense_27.append(float(i.amount))
        r_expense_27 = sum(l_expense_27)
        r_balance_27 = r_balance_26 + r_income_27 - r_expense_27

        income_28 = in_exp_items_daily.objects.filter(month=mth, type='income', day='28',flag=1)
        l_income_28 = []
        for i in income_28:
            l_income_28.append(float(i.amount))
        r_income_28 = sum(l_income_28)
        expense_28 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='28',flag=1)
        l_expense_28 = []
        for i in expense_28:
            l_expense_28.append(float(i.amount))
        r_expense_28 = sum(l_expense_28)
        r_balance_28 = r_balance_27 + r_income_28 - r_expense_28
    ####**************************
        income_29 = in_exp_items_daily.objects.filter(month=mth, type='income', day='29',flag=1)
        l_income_29 = []
        for i in income_29:
            l_income_29.append(float(i.amount))
        r_income_29 = sum(l_income_29)
        expense_29 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='29',flag=1)
        l_expense_29 = []
        for i in expense_29:
            l_expense_29.append(float(i.amount))
        r_expense_29 = sum(l_expense_29)
        r_balance_29 = r_balance_28 + r_income_29 - r_expense_29

        income_30 = in_exp_items_daily.objects.filter(month=mth, type='income', day='30',flag=1)
        l_income_30 = []
        for i in income_30:
            l_income_30.append(float(i.amount))
        r_income_30 = sum(l_income_30)
        expense_30 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='30',flag=1)
        l_expense_30 = []
        for i in expense_30:
            l_expense_30.append(float(i.amount))
        r_expense_30 = sum(l_expense_30)
        r_balance_30 = r_balance_29 + r_income_30 - r_expense_30

        income_31 = in_exp_items_daily.objects.filter(month=mth, type='income', day='31',flag=1)
        l_income_31 = []
        for i in income_31:
            l_income_31.append(float(i.amount))
        r_income_31 = sum(l_income_31)
        expense_31 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='31',flag=1)
        l_expense_31 = []
        for i in expense_31:
            l_expense_31.append(float(i.amount))
        r_expense_31 = sum(l_expense_31)
        r_balance_31 = r_balance_30 + r_income_31 - r_expense_31

    ##****************************************
        a = in_exp_items_daily.objects.all().filter(month=mth,flag=1)
        il=[]
        el=[]
        for i in a:
            if i.type == 'income':
                il.append(float(i.amount))
            if i.type == 'expense':
                el.append(float(i.amount))

        sil=sum(il)
        silop = sum(il)+opening_balance
        sel=sum(el)
        d_bal = sil - sel



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


            'object_list': queryset,
            'totals': totals,
            'res' : in_exp_items_daily.objects.all().filter(month=mth,flag=1),

            'opening_balance' : opening_balance,
            #'color' : color,
            'year' : ye_name_dis,
            'month' : mth,
            'monthname' : month_name_dis,

            'sil' : sil,
            'silop' : silop,
            'sel' : sel,
            'd_bal' : d_bal,

            'income_1': r_income_1,
            'expense_1': r_expense_1,
            'balance_1': r_balance_1,

            'income_2': r_income_2,
            'expense_2': r_expense_2,
            'balance_2': r_balance_2,

            'income_3': r_income_3,
            'expense_3': r_expense_3,
            'balance_3': r_balance_3,

            'income_4': r_income_4,
            'expense_4': r_expense_4,
            'balance_4': r_balance_4,

            'income_5': r_income_5,
            'expense_5': r_expense_5,
            'balance_5': r_balance_5,

            'income_6': r_income_6,
            'expense_6': r_expense_6,
            'balance_6': r_balance_6,

            'income_7': r_income_7,
            'expense_7': r_expense_7,
            'balance_7': r_balance_7,

            'income_8': r_income_8,
            'expense_8': r_expense_8,
            'balance_8': r_balance_8,

            'income_9': r_income_9,
            'expense_9': r_expense_9,
            'balance_9': r_balance_9,

            'income_10': r_income_10,
            'expense_10': r_expense_10,
            'balance_10': r_balance_10,

            'income_11': r_income_11,
            'expense_11': r_expense_11,
            'balance_11': r_balance_11,

            'income_12': r_income_12,
            'expense_12': r_expense_12,
            'balance_12': r_balance_12,

            'income_13': r_income_13,
            'expense_13': r_expense_13,
            'balance_13': r_balance_13,

            'income_14': r_income_14,
            'expense_14': r_expense_14,
            'balance_14': r_balance_14,

            'income_15': r_income_15,
            'expense_15': r_expense_15,
            'balance_15': r_balance_15,

            'income_16': r_income_16,
            'expense_16': r_expense_16,
            'balance_16': r_balance_16,

            'income_17': r_income_17,
            'expense_17': r_expense_17,
            'balance_17': r_balance_17,

            'income_18': r_income_18,
            'expense_18': r_expense_18,
            'balance_18': r_balance_18,

            'income_19': r_income_19,
            'expense_19': r_expense_19,
            'balance_19': r_balance_19,

            'income_20': r_income_20,
            'expense_20': r_expense_20,
            'balance_20': r_balance_20,

            'income_21': r_income_21,
            'expense_21': r_expense_21,
            'balance_21': r_balance_21,

            'income_22': r_income_22,
            'expense_22': r_expense_22,
            'balance_22': r_balance_22,

            'income_23': r_income_23,
            'expense_23': r_expense_23,
            'balance_23': r_balance_23,

            'income_24': r_income_24,
            'expense_24': r_expense_24,
            'balance_24': r_balance_24,

            'income_25': r_income_25,
            'expense_25': r_expense_25,
            'balance_25': r_balance_25,

            'income_26': r_income_26,
            'expense_26': r_expense_26,
            'balance_26': r_balance_26,

            'income_27': r_income_27,
            'expense_27': r_expense_27,
            'balance_27': r_balance_27,

            'income_28': r_income_28,
            'expense_28': r_expense_28,
            'balance_28': r_balance_28,

            'income_29': r_income_29,
            'expense_29': r_expense_29,
            'balance_29': r_balance_29,

            'income_30': r_income_30,
            'expense_30': r_expense_30,
            'balance_30': r_balance_30,

            'income_31': r_income_31,
            'expense_31': r_expense_31,
            'balance_31': r_balance_31,

        }
        return render(request,'branches/branch11/accounts/monthly_reports/monthly_detailed_daily_in_exp_items_report.html',context)
    return render(request, 'index.html')





def single_monthly_reports_choose_months11(request):
    if 'username' in request.session:

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
        }
        return render(request,'branches/branch11/accounts/monthly_reports/single_monthly_reports_choose_months.html',context)
    return render(request, 'index.html')

def single_monthly_daily_in_exp_items_report11(request,mo):
    if 'username' in request.session:

        mth = mo
        print('moooooo0', mo)

        queryset = in_exp_items_daily.objects.filter(month=mth, type='income', flag=1)
        totals = queryset.aggregate(sum=Sum('amount'))

        mth_list = ['*', 'JAN', 'FEB', 'MARCH', 'APRIL', 'MAY', 'JUN', 'JUL', 'AUG', 'SEPT', 'OCT', 'NOV', 'DEC']
        n_mth = int(mth)
        month_name_dis = mth_list[n_mth]

        ye_list = ['*', '2024', '2024', '2024', '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023']
        n_ye = int(mth)
        ye_name_dis = ye_list[n_ye]

        # ob = opening_balance.objects.all().filter(month_no=mth,month_name='aug',flag=1)
        # l_opening_balance=[]
        # for i in ob:
        # l_opening_balance.append(float(i.month_amount))
        # aug_opening_balance= sum(l_opening_balance)

        # if aug_opening_balance >0:
        # color='green'
        # elif aug_opening_balance < 0:
        # color = 'red'
        # else:
        # color = 'orange'
        opening_balance = 0

        income_1 = in_exp_items_daily.objects.filter(month=mth, type='income', day='01', flag=1)
        l_income_1 = []
        for i in income_1:
            l_income_1.append(float(i.amount))
        r_income_1 = sum(l_income_1)
        expense_1 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='01', flag=1)
        l_expense_1 = []
        for i in expense_1:
            l_expense_1.append(float(i.amount))
        r_expense_1 = sum(l_expense_1)
        r_balance_1 = opening_balance + r_income_1 - r_expense_1

        income_2 = in_exp_items_daily.objects.filter(month=mth, type='income', day='02', flag=1)
        l_income_2 = []
        for i in income_2:
            l_income_2.append(float(i.amount))
        r_income_2 = sum(l_income_2)
        expense_2 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='02', flag=1)
        l_expense_2 = []
        for i in expense_2:
            l_expense_2.append(float(i.amount))
        r_expense_2 = sum(l_expense_2)
        r_balance_2 = r_balance_1 + r_income_2 - r_expense_2

        income_3 = in_exp_items_daily.objects.filter(month=mth, type='income', day='03', flag=1)
        l_income_3 = []
        for i in income_3:
            l_income_3.append(float(i.amount))
        r_income_3 = sum(l_income_3)
        expense_3 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='03', flag=1)
        l_expense_3 = []
        for i in expense_3:
            l_expense_3.append(float(i.amount))
        r_expense_3 = sum(l_expense_3)
        r_balance_3 = r_balance_2 + r_income_3 - r_expense_3

        income_4 = in_exp_items_daily.objects.filter(month=mth, type='income', day='04', flag=1)
        l_income_4 = []
        for i in income_4:
            l_income_4.append(float(i.amount))
        r_income_4 = sum(l_income_4)
        expense_4 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='04', flag=1)
        l_expense_4 = []
        for i in expense_4:
            l_expense_4.append(float(i.amount))
        r_expense_4 = sum(l_expense_4)
        r_balance_4 = r_balance_3 + r_income_4 - r_expense_4

        income_5 = in_exp_items_daily.objects.filter(month=mth, type='income', day='05', flag=1)
        l_income_5 = []
        for i in income_5:
            l_income_5.append(float(i.amount))
        r_income_5 = sum(l_income_5)
        expense_5 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='05', flag=1)
        l_expense_5 = []
        for i in expense_5:
            l_expense_5.append(float(i.amount))
        r_expense_5 = sum(l_expense_5)
        r_balance_5 = r_balance_4 + r_income_5 - r_expense_5

        income_6 = in_exp_items_daily.objects.filter(month=mth, type='income', day='06', flag=1)
        l_income_6 = []
        for i in income_6:
            l_income_6.append(float(i.amount))
        r_income_6 = sum(l_income_6)
        expense_6 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='06', flag=1)
        l_expense_6 = []
        for i in expense_6:
            l_expense_6.append(float(i.amount))
        r_expense_6 = sum(l_expense_6)
        r_balance_6 = r_balance_5 + r_income_6 - r_expense_6

        income_7 = in_exp_items_daily.objects.filter(month=mth, type='income', day='07', flag=1)
        l_income_7 = []
        for i in income_7:
            l_income_7.append(float(i.amount))
        r_income_7 = sum(l_income_7)
        expense_7 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='07', flag=1)
        l_expense_7 = []
        for i in expense_7:
            l_expense_7.append(float(i.amount))
        r_expense_7 = sum(l_expense_7)
        r_balance_7 = r_balance_6 + r_income_7 - r_expense_7
        ###***************************************
        income_8 = in_exp_items_daily.objects.filter(month=mth, type='income', day='08', flag=1)
        l_income_8 = []
        for i in income_8:
            l_income_8.append(float(i.amount))
        r_income_8 = sum(l_income_8)
        expense_8 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='08', flag=1)
        l_expense_8 = []
        for i in expense_8:
            l_expense_8.append(float(i.amount))
        r_expense_8 = sum(l_expense_8)
        r_balance_8 = r_balance_7 + r_income_8 - r_expense_8

        income_9 = in_exp_items_daily.objects.filter(month=mth, type='income', day='09', flag=1)
        l_income_9 = []
        for i in income_9:
            l_income_9.append(float(i.amount))
        r_income_9 = sum(l_income_9)
        expense_9 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='09', flag=1)
        l_expense_9 = []
        for i in expense_9:
            l_expense_9.append(float(i.amount))
        r_expense_9 = sum(l_expense_9)
        r_balance_9 = r_balance_8 + r_income_9 - r_expense_9

        income_10 = in_exp_items_daily.objects.filter(month=mth, type='income', day='10', flag=1)
        l_income_10 = []
        for i in income_10:
            l_income_10.append(float(i.amount))
        r_income_10 = sum(l_income_10)
        expense_10 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='10', flag=1)
        l_expense_10 = []
        for i in expense_10:
            l_expense_10.append(float(i.amount))
        r_expense_10 = sum(l_expense_10)
        r_balance_10 = r_balance_9 + r_income_10 - r_expense_10

        income_11 = in_exp_items_daily.objects.filter(month=mth, type='income', day='11', flag=1)
        l_income_11 = []
        for i in income_11:
            l_income_11.append(float(i.amount))
        r_income_11 = sum(l_income_11)
        expense_11 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='11', flag=1)
        l_expense_11 = []
        for i in expense_11:
            l_expense_11.append(float(i.amount))
        r_expense_11 = sum(l_expense_11)
        r_balance_11 = r_balance_10 + r_income_11 - r_expense_11

        income_12 = in_exp_items_daily.objects.filter(month=mth, type='income', day='12', flag=1)
        l_income_12 = []
        for i in income_12:
            l_income_12.append(float(i.amount))
        r_income_12 = sum(l_income_12)
        expense_12 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='12', flag=1)
        l_expense_12 = []
        for i in expense_12:
            l_expense_12.append(float(i.amount))
        r_expense_12 = sum(l_expense_12)
        r_balance_12 = r_balance_11 + r_income_12 - r_expense_12

        income_13 = in_exp_items_daily.objects.filter(month=mth, type='income', day='13', flag=1)
        l_income_13 = []
        for i in income_13:
            l_income_13.append(float(i.amount))
        r_income_13 = sum(l_income_13)
        expense_13 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='13', flag=1)
        l_expense_13 = []
        for i in expense_13:
            l_expense_13.append(float(i.amount))
        r_expense_13 = sum(l_expense_13)
        r_balance_13 = r_balance_12 + r_income_13 - r_expense_13

        income_14 = in_exp_items_daily.objects.filter(month=mth, type='income', day='14', flag=1)
        l_income_14 = []
        for i in income_14:
            l_income_14.append(float(i.amount))
        r_income_14 = sum(l_income_14)
        expense_14 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='14', flag=1)
        l_expense_14 = []
        for i in expense_14:
            l_expense_14.append(float(i.amount))
        r_expense_14 = sum(l_expense_14)
        r_balance_14 = r_balance_13 + r_income_14 - r_expense_14
        ###*****************************
        income_15 = in_exp_items_daily.objects.filter(month=mth, type='income', day='15', flag=1)
        l_income_15 = []
        for i in income_15:
            l_income_15.append(float(i.amount))
        r_income_15 = sum(l_income_15)
        expense_15 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='15', flag=1)
        l_expense_15 = []
        for i in expense_15:
            l_expense_15.append(float(i.amount))
        r_expense_15 = sum(l_expense_15)
        r_balance_15 = r_balance_14 + r_income_15 - r_expense_15

        income_16 = in_exp_items_daily.objects.filter(month=mth, type='income', day='16', flag=1)
        l_income_16 = []
        for i in income_16:
            l_income_16.append(float(i.amount))
        r_income_16 = sum(l_income_16)
        expense_16 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='16', flag=1)
        l_expense_16 = []
        for i in expense_16:
            l_expense_16.append(float(i.amount))
        r_expense_16 = sum(l_expense_16)
        r_balance_16 = r_balance_15 + r_income_16 - r_expense_16

        income_17 = in_exp_items_daily.objects.filter(month=mth, type='income', day='17', flag=1)
        l_income_17 = []
        for i in income_17:
            l_income_17.append(float(i.amount))
        r_income_17 = sum(l_income_17)
        expense_17 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='17', flag=1)
        l_expense_17 = []
        for i in expense_17:
            l_expense_17.append(float(i.amount))
        r_expense_17 = sum(l_expense_17)
        r_balance_17 = r_balance_16 + r_income_17 - r_expense_17

        income_18 = in_exp_items_daily.objects.filter(month=mth, type='income', day='18', flag=1)
        l_income_18 = []
        for i in income_18:
            l_income_18.append(float(i.amount))
        r_income_18 = sum(l_income_18)
        expense_18 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='18', flag=1)
        l_expense_18 = []
        for i in expense_18:
            l_expense_18.append(float(i.amount))
        r_expense_18 = sum(l_expense_18)
        r_balance_18 = r_balance_17 + r_income_18 - r_expense_18

        income_19 = in_exp_items_daily.objects.filter(month=mth, type='income', day='19', flag=1)
        l_income_19 = []
        for i in income_19:
            l_income_19.append(float(i.amount))
        r_income_19 = sum(l_income_19)
        expense_19 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='19', flag=1)
        l_expense_19 = []
        for i in expense_19:
            l_expense_19.append(float(i.amount))
        r_expense_19 = sum(l_expense_19)
        r_balance_19 = r_balance_18 + r_income_19 - r_expense_19

        income_20 = in_exp_items_daily.objects.filter(month=mth, type='income', day='20', flag=1)
        l_income_20 = []
        for i in income_20:
            l_income_20.append(float(i.amount))
        r_income_20 = sum(l_income_20)
        expense_20 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='20', flag=1)
        l_expense_20 = []
        for i in expense_20:
            l_expense_20.append(float(i.amount))
        r_expense_20 = sum(l_expense_20)
        r_balance_20 = r_balance_19 + r_income_20 - r_expense_20

        income_21 = in_exp_items_daily.objects.filter(month=mth, type='income', day='21', flag=1)
        l_income_21 = []
        for i in income_21:
            l_income_21.append(float(i.amount))
        r_income_21 = sum(l_income_21)
        expense_21 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='21', flag=1)
        l_expense_21 = []
        for i in expense_21:
            l_expense_21.append(float(i.amount))
        r_expense_21 = sum(l_expense_21)
        r_balance_21 = r_balance_20 + r_income_21 - r_expense_21

        income_22 = in_exp_items_daily.objects.filter(month=mth, type='income', day='22', flag=1)
        l_income_22 = []
        for i in income_22:
            l_income_22.append(float(i.amount))
        r_income_22 = sum(l_income_22)
        expense_22 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='22', flag=1)
        l_expense_22 = []
        for i in expense_22:
            l_expense_22.append(float(i.amount))
        r_expense_22 = sum(l_expense_22)
        r_balance_22 = r_balance_21 + r_income_22 - r_expense_22
        ####************************
        income_23 = in_exp_items_daily.objects.filter(month=mth, type='income', day='23', flag=1)
        l_income_23 = []
        for i in income_23:
            l_income_23.append(float(i.amount))
        r_income_23 = sum(l_income_23)
        expense_23 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='23', flag=1)
        l_expense_23 = []
        for i in expense_23:
            l_expense_23.append(float(i.amount))
        r_expense_23 = sum(l_expense_23)
        r_balance_23 = r_balance_22 + r_income_23 - r_expense_23

        income_24 = in_exp_items_daily.objects.filter(month=mth, type='income', day='24', flag=1)
        l_income_24 = []
        for i in income_24:
            l_income_24.append(float(i.amount))
        r_income_24 = sum(l_income_24)
        expense_24 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='24', flag=1)
        l_expense_24 = []
        for i in expense_24:
            l_expense_24.append(float(i.amount))
        r_expense_24 = sum(l_expense_24)
        r_balance_24 = r_balance_23 + r_income_24 - r_expense_24

        income_25 = in_exp_items_daily.objects.filter(month=mth, type='income', day='25', flag=1)
        l_income_25 = []
        for i in income_25:
            l_income_25.append(float(i.amount))
        r_income_25 = sum(l_income_25)
        expense_25 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='25', flag=1)
        l_expense_25 = []
        for i in expense_25:
            l_expense_25.append(float(i.amount))
        r_expense_25 = sum(l_expense_25)
        r_balance_25 = r_balance_24 + r_income_25 - r_expense_25

        income_26 = in_exp_items_daily.objects.filter(month=mth, type='income', day='26', flag=1)
        l_income_26 = []
        for i in income_26:
            l_income_26.append(float(i.amount))
        r_income_26 = sum(l_income_26)
        expense_26 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='26', flag=1)
        l_expense_26 = []
        for i in expense_26:
            l_expense_26.append(float(i.amount))
        r_expense_26 = sum(l_expense_26)
        r_balance_26 = r_balance_25 + r_income_26 - r_expense_26

        income_27 = in_exp_items_daily.objects.filter(month=mth, type='income', day='27', flag=1)
        l_income_27 = []
        for i in income_27:
            l_income_27.append(float(i.amount))
        r_income_27 = sum(l_income_27)
        expense_27 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='27', flag=1)
        l_expense_27 = []
        for i in expense_27:
            l_expense_27.append(float(i.amount))
        r_expense_27 = sum(l_expense_27)
        r_balance_27 = r_balance_26 + r_income_27 - r_expense_27

        income_28 = in_exp_items_daily.objects.filter(month=mth, type='income', day='28', flag=1)
        l_income_28 = []
        for i in income_28:
            l_income_28.append(float(i.amount))
        r_income_28 = sum(l_income_28)
        expense_28 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='28', flag=1)
        l_expense_28 = []
        for i in expense_28:
            l_expense_28.append(float(i.amount))
        r_expense_28 = sum(l_expense_28)
        r_balance_28 = r_balance_27 + r_income_28 - r_expense_28
        ####**************************
        income_29 = in_exp_items_daily.objects.filter(month=mth, type='income', day='29', flag=1)
        l_income_29 = []
        for i in income_29:
            l_income_29.append(float(i.amount))
        r_income_29 = sum(l_income_29)
        expense_29 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='29', flag=1)
        l_expense_29 = []
        for i in expense_29:
            l_expense_29.append(float(i.amount))
        r_expense_29 = sum(l_expense_29)
        r_balance_29 = r_balance_28 + r_income_29 - r_expense_29

        income_30 = in_exp_items_daily.objects.filter(month=mth, type='income', day='30', flag=1)
        l_income_30 = []
        for i in income_30:
            l_income_30.append(float(i.amount))
        r_income_30 = sum(l_income_30)
        expense_30 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='30', flag=1)
        l_expense_30 = []
        for i in expense_30:
            l_expense_30.append(float(i.amount))
        r_expense_30 = sum(l_expense_30)
        r_balance_30 = r_balance_29 + r_income_30 - r_expense_30

        income_31 = in_exp_items_daily.objects.filter(month=mth, type='income', day='31', flag=1)
        l_income_31 = []
        for i in income_31:
            l_income_31.append(float(i.amount))
        r_income_31 = sum(l_income_31)
        expense_31 = in_exp_items_daily.objects.filter(month=mth, type='expense', day='31', flag=1)
        l_expense_31 = []
        for i in expense_31:
            l_expense_31.append(float(i.amount))
        r_expense_31 = sum(l_expense_31)
        r_balance_31 = r_balance_30 + r_income_31 - r_expense_31

        ##****************************************
        a = in_exp_items_daily.objects.all().filter(month=mth, flag=1)
        il = []
        el = []
        for i in a:
            if i.type == 'income':
                il.append(float(i.amount))
            if i.type == 'expense':
                el.append(float(i.amount))

        sil = sum(il)
        silop = sum(il) + opening_balance
        sel = sum(el)
        d_bal = sil - sel


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


            'object_list': queryset,
            'totals': totals,
            'res': in_exp_items_daily.objects.all().filter(month=mth, flag=1),

            'opening_balance': opening_balance,
            # 'color' : color,
            'year': ye_name_dis,
            'month': mth,
            'monthname': month_name_dis,

            'sil': sil,
            'silop': silop,
            'sel': sel,
            'd_bal': d_bal,

            'income_1': r_income_1,
            'expense_1': r_expense_1,
            'balance_1': r_balance_1,

            'income_2': r_income_2,
            'expense_2': r_expense_2,
            'balance_2': r_balance_2,

            'income_3': r_income_3,
            'expense_3': r_expense_3,
            'balance_3': r_balance_3,

            'income_4': r_income_4,
            'expense_4': r_expense_4,
            'balance_4': r_balance_4,

            'income_5': r_income_5,
            'expense_5': r_expense_5,
            'balance_5': r_balance_5,

            'income_6': r_income_6,
            'expense_6': r_expense_6,
            'balance_6': r_balance_6,

            'income_7': r_income_7,
            'expense_7': r_expense_7,
            'balance_7': r_balance_7,

            'income_8': r_income_8,
            'expense_8': r_expense_8,
            'balance_8': r_balance_8,

            'income_9': r_income_9,
            'expense_9': r_expense_9,
            'balance_9': r_balance_9,

            'income_10': r_income_10,
            'expense_10': r_expense_10,
            'balance_10': r_balance_10,

            'income_11': r_income_11,
            'expense_11': r_expense_11,
            'balance_11': r_balance_11,

            'income_12': r_income_12,
            'expense_12': r_expense_12,
            'balance_12': r_balance_12,

            'income_13': r_income_13,
            'expense_13': r_expense_13,
            'balance_13': r_balance_13,

            'income_14': r_income_14,
            'expense_14': r_expense_14,
            'balance_14': r_balance_14,

            'income_15': r_income_15,
            'expense_15': r_expense_15,
            'balance_15': r_balance_15,

            'income_16': r_income_16,
            'expense_16': r_expense_16,
            'balance_16': r_balance_16,

            'income_17': r_income_17,
            'expense_17': r_expense_17,
            'balance_17': r_balance_17,

            'income_18': r_income_18,
            'expense_18': r_expense_18,
            'balance_18': r_balance_18,

            'income_19': r_income_19,
            'expense_19': r_expense_19,
            'balance_19': r_balance_19,

            'income_20': r_income_20,
            'expense_20': r_expense_20,
            'balance_20': r_balance_20,

            'income_21': r_income_21,
            'expense_21': r_expense_21,
            'balance_21': r_balance_21,

            'income_22': r_income_22,
            'expense_22': r_expense_22,
            'balance_22': r_balance_22,

            'income_23': r_income_23,
            'expense_23': r_expense_23,
            'balance_23': r_balance_23,

            'income_24': r_income_24,
            'expense_24': r_expense_24,
            'balance_24': r_balance_24,

            'income_25': r_income_25,
            'expense_25': r_expense_25,
            'balance_25': r_balance_25,

            'income_26': r_income_26,
            'expense_26': r_expense_26,
            'balance_26': r_balance_26,

            'income_27': r_income_27,
            'expense_27': r_expense_27,
            'balance_27': r_balance_27,

            'income_28': r_income_28,
            'expense_28': r_expense_28,
            'balance_28': r_balance_28,

            'income_29': r_income_29,
            'expense_29': r_expense_29,
            'balance_29': r_balance_29,

            'income_30': r_income_30,
            'expense_30': r_expense_30,
            'balance_30': r_balance_30,

            'income_31': r_income_31,
            'expense_31': r_expense_31,
            'balance_31': r_balance_31,

        }
        return render(request,'branches/branch11/accounts/monthly_reports/single_monthly_daily_in_exp_items_report.html',context)
    return render(request, 'index.html')





#############################################################################
#*****************************************
#******SEPT END HERE
###############################################################

#############################################################################
#*****************************************
#****** HOME PAGE YEARLY INCOME AND EXP
###############################################################


def accounts_dash_board_ob_ch11(request):
    if 'username' in request.session:

        opening_balance = 0

        income_1 = in_exp_items_daily.objects.filter(month='01', type='income', flag=1)
        l_income_1 = []
        for i in income_1:
            l_income_1.append(float(i.amount))
        r_income_1 = sum(l_income_1)
        expense_1 = in_exp_items_daily.objects.filter(month='01', type='expense',flag=1)
        l_expense_1 = []
        for i in expense_1:
            l_expense_1.append(float(i.amount))
        r_expense_1 = sum(l_expense_1)
        r_balance_1 = opening_balance + r_income_1 - r_expense_1

        income_2 = in_exp_items_daily.objects.filter(month='02', type='income',flag=1)
        l_income_2 = []
        for i in income_2:
            l_income_2.append(float(i.amount))
        r_income_2 = sum(l_income_2)
        expense_2 = in_exp_items_daily.objects.filter(month='02', type='expense',flag=1)
        l_expense_2 = []
        for i in expense_2:
            l_expense_2.append(float(i.amount))
        r_expense_2 = sum(l_expense_2)
        r_balance_2 = r_income_2 - r_expense_2

        income_3 = in_exp_items_daily.objects.filter(month='03', type='income',flag=1)
        l_income_3 = []
        for i in income_3:
            l_income_3.append(float(i.amount))
        r_income_3 = sum(l_income_3)
        expense_3 = in_exp_items_daily.objects.filter(month='03', type='expense',flag=1)
        l_expense_3 = []
        for i in expense_3:
            l_expense_3.append(float(i.amount))
        r_expense_3 = sum(l_expense_3)
        r_balance_3 = r_income_3 - r_expense_3

        income_4 = in_exp_items_daily.objects.filter(month='04', type='income', flag=1)
        l_income_4 = []
        for i in income_4:
            l_income_4.append(float(i.amount))
        r_income_4 = sum(l_income_4)
        expense_4 = in_exp_items_daily.objects.filter(month='04', type='expense',flag=1)
        l_expense_4 = []
        for i in expense_4:
            l_expense_4.append(float(i.amount))
        r_expense_4 = sum(l_expense_4)
        r_balance_4 = r_income_4 - r_expense_4

        income_5 = in_exp_items_daily.objects.filter(month='05', type='income', flag=1)
        l_income_5 = []
        for i in income_5:
            l_income_5.append(float(i.amount))
        r_income_5 = sum(l_income_5)
        expense_5 = in_exp_items_daily.objects.filter(month='05', type='expense', flag=1)
        l_expense_5 = []
        for i in expense_5:
            l_expense_5.append(float(i.amount))
        r_expense_5 = sum(l_expense_5)
        r_balance_5 = r_income_5 - r_expense_5

        income_6 = in_exp_items_daily.objects.filter(month='06', type='income', flag=1)
        l_income_6 = []
        for i in income_6:
            l_income_6.append(float(i.amount))
        r_income_6 = sum(l_income_6)
        expense_6 = in_exp_items_daily.objects.filter(month='06', type='expense', flag=1)
        l_expense_6 = []
        for i in expense_6:
            l_expense_6.append(float(i.amount))
        r_expense_6 = sum(l_expense_6)
        r_balance_6 = +r_income_6 - r_expense_6

        income_7 = in_exp_items_daily.objects.filter(month='07', type='income',flag=1)
        l_income_7 = []
        for i in income_7:
            l_income_7.append(float(i.amount))
        r_income_7 = sum(l_income_7)
        expense_7 = in_exp_items_daily.objects.filter(month='07', type='expense',flag=1)
        l_expense_7 = []
        for i in expense_7:
            l_expense_7.append(float(i.amount))
        r_expense_7 = sum(l_expense_7)
        r_balance_7 = r_income_7 - r_expense_7
        ###***************************************
        income_8 = in_exp_items_daily.objects.filter(month='08', type='income',flag=1)
        l_income_8 = []
        for i in income_8:
            l_income_8.append(float(i.amount))
        r_income_8 = sum(l_income_8)
        expense_8 = in_exp_items_daily.objects.filter(month='08', type='expense',flag=1)
        l_expense_8 = []
        for i in expense_8:
            l_expense_8.append(float(i.amount))
        r_expense_8 = sum(l_expense_8)
        r_balance_8 = r_income_8 - r_expense_8

        income_9 = in_exp_items_daily.objects.filter(month='09', type='income',flag=1)
        l_income_9 = []
        for i in income_9:
            l_income_9.append(float(i.amount))
        r_income_9 = sum(l_income_9)
        expense_9 = in_exp_items_daily.objects.filter(month='09', type='expense',flag=1)
        l_expense_9 = []
        for i in expense_9:
            l_expense_9.append(float(i.amount))
        r_expense_9 = sum(l_expense_9)
        r_balance_9 = r_income_9 - r_expense_9

        income_10 = in_exp_items_daily.objects.filter(month='10', type='income', flag=1)
        l_income_10 = []
        for i in income_10:
            l_income_10.append(float(i.amount))
        r_income_10 = sum(l_income_10)
        expense_10 = in_exp_items_daily.objects.filter(month='10', type='expense', flag=1)
        l_expense_10 = []
        for i in expense_10:
            l_expense_10.append(float(i.amount))
        r_expense_10 = sum(l_expense_10)
        r_balance_10 = r_income_10 - r_expense_10

        income_11 = in_exp_items_daily.objects.filter(month='11', type='income', flag=1)
        l_income_11 = []
        for i in income_11:
            l_income_11.append(float(i.amount))
        r_income_11 = sum(l_income_11)
        expense_11 = in_exp_items_daily.objects.filter(month='11', type='expense', flag=1)
        l_expense_11 = []
        for i in expense_11:
            l_expense_11.append(float(i.amount))
        r_expense_11 = sum(l_expense_11)
        r_balance_11 = r_income_11 - r_expense_11

        income_12 = in_exp_items_daily.objects.filter(month='12', type='income', flag=1)
        l_income_12 = []
        for i in income_12:
            l_income_12.append(float(i.amount))
        r_income_12 = sum(l_income_12)
        expense_12 = in_exp_items_daily.objects.filter(month='12', type='expense', flag=1)
        l_expense_12 = []
        for i in expense_12:
            l_expense_12.append(float(i.amount))
        r_expense_12 = sum(l_expense_12)
        r_balance_12 = r_income_12 - r_expense_12

        ##***************************************

        a = in_exp_items_daily.objects.all().filter(flag=1)
        il=[]
        el=[]
        for i in a:
            if i.type == 'income':
                il.append(float(i.amount))
            if i.type == 'expense':
                el.append(float(i.amount))

        sil=sum(il)
        silop = sum(il)+opening_balance
        sel=sum(el)
        d_bal = sil - sel



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



            'sil': sil,
            'sel': sel,
            'd_bal': d_bal,

            'income_1': r_income_1,
            'expense_1': r_expense_1,
            'balance_1': r_balance_1,

            'income_2': r_income_2,
            'expense_2': r_expense_2,
            'balance_2': r_balance_2,

            'income_3': r_income_3,
            'expense_3': r_expense_3,
            'balance_3': r_balance_3,

            'income_4': r_income_4,
            'expense_4': r_expense_4,
            'balance_4': r_balance_4,

            'income_5': r_income_5,
            'expense_5': r_expense_5,
            'balance_5': r_balance_5,

            'income_6': r_income_6,
            'expense_6': r_expense_6,
            'balance_6': r_balance_6,

            'income_7': r_income_7,
            'expense_7': r_expense_7,
            'balance_7': r_balance_7,

            'income_8': r_income_8,
            'expense_8': r_expense_8,
            'balance_8': r_balance_8,

            'income_9': r_income_9,
            'expense_9': r_expense_9,
            'balance_9': r_balance_9,

            'income_10': r_income_10,
            'expense_10': r_expense_10,
            'balance_10': r_balance_10,

            'income_11': r_income_11,
            'expense_11': r_expense_11,
            'balance_11': r_balance_11,

            'income_12': r_income_12,
            'expense_12': r_expense_12,
            'balance_12': r_balance_12,

        }
        return render(request,'branches/branch11/accounts/accounts_dash_board.html',context)
    return render(request, 'index.html')




#############################################################################
#*****************************************
#****** HOME PAGE YEARLY INCOME AND EXP
###############################################################


#*****************************************
#****** PROFIT SHARING STARTING HERE
###############################################################

def profit_sharing_choose_months11(request):
    if 'username' in request.session:
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
        }
        return render(request,'branches/branch11/accounts/profit_sharing/profit_sharing_choose_months.html',context)

def profit_sharing11(request,mo):
    if 'username' in request.session:

        opening_balance = 0

        income_1 = in_exp_items_daily.objects.filter(month='01', type='income', flag=1)
        l_income_1 = []
        for i in income_1:
            l_income_1.append(float(i.amount))
        r_income_1 = sum(l_income_1)
        expense_1 = in_exp_items_daily.objects.filter(month='01', type='expense', flag=1)
        l_expense_1 = []
        for i in expense_1:
            l_expense_1.append(float(i.amount))
        r_expense_1 = sum(l_expense_1)
        r_balance_1 = opening_balance + r_income_1 - r_expense_1

        income_2 = in_exp_items_daily.objects.filter(month='02', type='income', flag=1)
        l_income_2 = []
        for i in income_2:
            l_income_2.append(float(i.amount))
        r_income_2 = sum(l_income_2)
        expense_2 = in_exp_items_daily.objects.filter(month='02', type='expense', flag=1)
        l_expense_2 = []
        for i in expense_2:
            l_expense_2.append(float(i.amount))
        r_expense_2 = sum(l_expense_2)
        r_balance_2 = r_income_2 - r_expense_2

        income_3 = in_exp_items_daily.objects.filter(month='03', type='income', flag=1)
        l_income_3 = []
        for i in income_3:
            l_income_3.append(float(i.amount))
        r_income_3 = sum(l_income_3)
        expense_3 = in_exp_items_daily.objects.filter(month='03', type='expense', flag=1)
        l_expense_3 = []
        for i in expense_3:
            l_expense_3.append(float(i.amount))
        r_expense_3 = sum(l_expense_3)
        r_balance_3 = r_income_3 - r_expense_3

        income_4 = in_exp_items_daily.objects.filter(month='04', type='income', flag=1)
        l_income_4 = []
        for i in income_4:
            l_income_4.append(float(i.amount))
        r_income_4 = sum(l_income_4)
        expense_4 = in_exp_items_daily.objects.filter(month='04', type='expense', flag=1)
        l_expense_4 = []
        for i in expense_4:
            l_expense_4.append(float(i.amount))
        r_expense_4 = sum(l_expense_4)
        r_balance_4 = r_income_4 - r_expense_4

        income_5 = in_exp_items_daily.objects.filter(month='05', type='income', flag=1)
        l_income_5 = []
        for i in income_5:
            l_income_5.append(float(i.amount))
        r_income_5 = sum(l_income_5)
        expense_5 = in_exp_items_daily.objects.filter(month='05', type='expense', flag=1)
        l_expense_5 = []
        for i in expense_5:
            l_expense_5.append(float(i.amount))
        r_expense_5 = sum(l_expense_5)
        r_balance_5 = r_income_5 - r_expense_5

        income_6 = in_exp_items_daily.objects.filter(month='06', type='income', flag=1)
        l_income_6 = []
        for i in income_6:
            l_income_6.append(float(i.amount))
        r_income_6 = sum(l_income_6)
        expense_6 = in_exp_items_daily.objects.filter(month='06', type='expense', flag=1)
        l_expense_6 = []
        for i in expense_6:
            l_expense_6.append(float(i.amount))
        r_expense_6 = sum(l_expense_6)
        r_balance_6 = +r_income_6 - r_expense_6

        income_7 = in_exp_items_daily.objects.filter(month='07', type='income', flag=1)
        l_income_7 = []
        for i in income_7:
            l_income_7.append(float(i.amount))
        r_income_7 = sum(l_income_7)
        expense_7 = in_exp_items_daily.objects.filter(month='07', type='expense', flag=1)
        l_expense_7 = []
        for i in expense_7:
            l_expense_7.append(float(i.amount))
        r_expense_7 = sum(l_expense_7)
        r_balance_7 = r_income_7 - r_expense_7
        ###***************************************
        income_8 = in_exp_items_daily.objects.filter(month='08', type='income', flag=1)
        l_income_8 = []
        for i in income_8:
            l_income_8.append(float(i.amount))
        r_income_8 = sum(l_income_8)
        expense_8 = in_exp_items_daily.objects.filter(month='08', type='expense', flag=1)
        l_expense_8 = []
        for i in expense_8:
            l_expense_8.append(float(i.amount))
        r_expense_8 = sum(l_expense_8)
        r_balance_8 = r_income_8 - r_expense_8

        income_9 = in_exp_items_daily.objects.filter(month='09', type='income', flag=1)
        l_income_9 = []
        for i in income_9:
            l_income_9.append(float(i.amount))
        r_income_9 = sum(l_income_9)
        expense_9 = in_exp_items_daily.objects.filter(month='09', type='expense', flag=1)
        l_expense_9 = []
        for i in expense_9:
            l_expense_9.append(float(i.amount))
        r_expense_9 = sum(l_expense_9)
        r_balance_9 = r_income_9 - r_expense_9

        income_10 = in_exp_items_daily.objects.filter(month='10', type='income', flag=1)
        l_income_10 = []
        for i in income_10:
            l_income_10.append(float(i.amount))
        r_income_10 = sum(l_income_10)
        expense_10 = in_exp_items_daily.objects.filter(month='10', type='expense', flag=1)
        l_expense_10 = []
        for i in expense_10:
            l_expense_10.append(float(i.amount))
        r_expense_10 = sum(l_expense_10)
        r_balance_10 = r_income_10 - r_expense_10

        income_11 = in_exp_items_daily.objects.filter(month='11', type='income', flag=1)
        l_income_11 = []
        for i in income_11:
            l_income_11.append(float(i.amount))
        r_income_11 = sum(l_income_11)
        expense_11 = in_exp_items_daily.objects.filter(month='11', type='expense', flag=1)
        l_expense_11 = []
        for i in expense_11:
            l_expense_11.append(float(i.amount))
        r_expense_11 = sum(l_expense_11)
        r_balance_11 = r_income_11 - r_expense_11

        income_12 = in_exp_items_daily.objects.filter(month='12', type='income', flag=1)
        l_income_12 = []
        for i in income_12:
            l_income_12.append(float(i.amount))
        r_income_12 = sum(l_income_12)
        expense_12 = in_exp_items_daily.objects.filter(month='12', type='expense', flag=1)
        l_expense_12 = []
        for i in expense_12:
            l_expense_12.append(float(i.amount))
        r_expense_12 = sum(l_expense_12)
        r_balance_12 = r_income_12 - r_expense_12

        ##***************************************

        a = in_exp_items_daily.objects.all().filter(flag=1)
        il = []
        el = []
        for i in a:
            if i.type == 'income':
                il.append(float(i.amount))
            if i.type == 'expense':
                el.append(float(i.amount))

        sil = sum(il)
        silop = sum(il) + opening_balance
        sel = sum(el)
        d_bal = sil - sel

        sha = []
        sha.append(r_balance_1)
        sha.append(r_balance_2)
        sha.append(r_balance_3)
        sha.append(r_balance_4)
        sha.append(r_balance_5)
        sha.append(r_balance_6)
        sha.append(r_balance_7)
        sha.append(r_balance_8)
        sha.append(r_balance_9)
        sha.append(r_balance_10)
        sha.append(r_balance_11)
        sha.append(r_balance_12)

        sh = share_holders.objects.all().filter(flag=1)
        mon = int(mo)
        print('my mo', mo)
        print('float(sha[mon])', float(sha[mon]))
        for i in sh:
            ta = float(sha[mon]) / 100 * float(i.share_holders_percentage)
            i.share_holders_amt = ta

        #        r_balance_9

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

            'mysh': sh,

        }
        return render(request,'branches/branch11/accounts/profit_sharing/profit_sharing.html',context)
    return render(request, 'index.html')

def view_share_holders11(request):
    if 'username' in request.session:
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

            'vsh' : share_holders.objects.all().filter(flag=1)
        }
        return render(request, 'branches/branch11/accounts/profit_sharing/view_share_holders.html',context)

def create_share_holders11(request):
    if 'username' in request.session:
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
        }

        return render(request, 'branches/branch11/accounts/profit_sharing/create_share_holders.html',context)


def regi_share_holders11(request):
    if 'username' in request.session:
        a=share_holders.objects.all().filter(flag=1)
        tsp=[]
        for i in a:
            tsp.append(float(i.share_holders_percentage))
        sa=sum(tsp)
        print('sa',sa)
        share = request.POST.get('share')
        tsa=sa+float(share)
        print('tsa', tsa)

        if tsa <101:

            if request.method == 'POST':
                name = request.POST.get('name')
                share = request.POST.get('share')

                ic = share_holders()
                ic.share_holders_name = name
                ic.share_holders_percentage = share
                ic.created_by = 'CB ' + request.session['username']
                import datetime
                ic.cb_date = datetime.datetime.now()
                ic.ub_flag = 0
                ic.flag = 1
                ic.save()

            return view_share_holders11(request)
        me= 'SHARE HOLDER DOES NOT CREATED, BECAUSE SHARE % OUT OF 100!. NOW TOTAL % IS ' + str(tsa)
        messages.info(request,me)
        return view_share_holders11(request)

def update_share_holders11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            name = request.POST.get('name')
            share = request.POST.get('share')

            ic = share_holders.objects.get(id=id)
            ic.share_holders_name = name
            ic.share_holders_percentage = share
            ic.updated_by = 'UB ' + request.session['username']
            import datetime
            ic.ub_date = datetime.datetime.now()
            ic.ub_flag = 1
            ic.flag = 1
            ic.save()
            return view_share_holders11(request)

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

            'sd' : share_holders.objects.get(id=id)
        }

        return render(request, 'branches/branch11/accounts/profit_sharing/update_share_holders.html',context)

def delete_share_holders11(request,id):
    if 'username' in request.session:
        #de=share_holders.objects.get(id=id)
        #de.delete()
        d = share_holders.objects.get(id=id)
        d.deleted_by = 'DB ' + request.session['username']
        import datetime
        d.db_date = datetime.datetime.now()
        d.flag = 2
        d.save()
        return view_share_holders11(request)


def view_deleted_share_holders11(request):
    if 'username' in request.session:
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

            'vsh' : share_holders.objects.all().filter(flag=2)
        }
        return render(request, 'branches/branch11/accounts/profit_sharing/view_deleted_share_holders.html',context)

#*****************************************
#****** PROFIT END STARTING HERE
###############################################################

