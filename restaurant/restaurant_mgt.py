import json
from django.http import HttpResponse

from django.shortcuts import render
from django.contrib import messages

from restaurant.models import *
from accounts.models import background_color

import datetime

def restaurantindex(request):
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
    return render(request,'restaurant/restaurantindex.html',context)



#########################################################
###******CREATER MASTER START HERE
###################################################################################

##******************KITCHEN CREATER START HERE




def view_all_kitchen_rest11(request):
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


            'kitchen' : kitchen.objects.all().filter(flag=1).order_by('-id'),

        }
        return render(request,'restaurant/creater_master/kitchen/view_all_kitchen.html',context)
    return render(request, 'index.html')

def create_new_kitchen_rest11(request):
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


            'kitchen' : kitchen.objects.all().filter(flag=1).order_by('-id'),

        }
        return render(request,'restaurant/creater_master/kitchen/create_new_kitchen.html',context)
    return render(request, 'index.html')

def regi_new_kitchen_rest11(request):
    if 'username' in request.session:
        kitchen_names = request.POST.get('kitchen')
        ir = kitchen.objects.all().filter(kitchen_name=kitchen_names,flag=1).exists()

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

                #'item': kitchen.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'danger',
                'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'CATERGORY ALREADY EXISTS')
            return render(request, 'restaurant/creater_master/items/view_all_items.html', context)
        else:

            ic = kitchen()
            ic.kitchen_name = kitchen_names
            ic.enter_by = 'CB ' + request.session['username']
            import datetime
            ic.cb_date = datetime.datetime.now()
            ic.ub_flag = 0
            ic.flag = 1

            ic.qty = 0
            ic.total_kitchen_wise_amt = 0
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

                'kitchen' : kitchen.objects.all().filter(flag=1).order_by('-id'),

            }
            messages.info(request, 'KITCHEN CREATED SUCCESSFULLY')
            return render(request,'restaurant/creater_master/kitchen/view_all_kitchen.html',context)
        return render(request, 'index.html')


def update_kitchen_rest11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            kitchen_names = request.POST.get('kitchen')
            ir = kitchen.objects.all().filter(kitchen_name=kitchen_names,flag=1).exclude(id=id).exists()

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
                    'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
                }
                messages.info(request,'KITCHEN ALREADY EXISTS')
                return render(request, 'restaurant/creater_master/kitchen/view_all_kitchen.html', context)
            else:
                ic = kitchen.objects.get(id=id)
                ic.kitchen_name = kitchen_names
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
                    'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
                }
                messages.info(request, 'KITCHEN UPDATED SUCCESSFULLY')
                return render(request, 'restaurant/creater_master/kitchen/view_all_kitchen.html', context)


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


            #'item' : table1.objects.all().filter(flag=1).order_by('-id'),
            'msg' : 'success',
            'sd' : kitchen.objects.get(id=id),
            'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
        }

        return render(request,'restaurant/creater_master/kitchen/update_kitchen.html',context)
    return render(request, 'index.html')


def delete_kitchen_rest11(request,id):
    if 'username' in request.session:
        r=kitchen.objects.all().filter(id=id,flag=1).exists()
        if r == True:
            d=kitchen.objects.get(id=id)
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

                #'item': table1.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'success',
                'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'KITCHEN Deleted Successfully')
            return render(request, 'restaurant/creater_master/kitchen/view_all_kitchen.html', context)
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

                #'item': table1.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'warning',
                'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'KITCHEN already  Deleted')
            return render(request,'restaurant/creater_master/kitchen/view_all_kitchen.html',context)
        return render(request, 'index.html')



def view_all_kitchen_delete_rest11(request):
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


            'kitchen' : kitchen.objects.all().filter(flag=2).order_by('-id'),

        }
        return render(request,'restaurant/creater_master/kitchen/view_all_kitchen_delete.html',context)
    return render(request, 'index.html')


##******************KITCHEN CREATER END HERE



##******************CATERGORY CREATER START HERE

def view_all_category_rest11(request):
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
        return render(request,'restaurant/creater_master/category/view_all_category.html',context)
    return render(request, 'index.html')

def create_new_category_rest11(request):
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
        return render(request,'restaurant/creater_master/category/create_new_category.html',context)
    return render(request, 'index.html')

def regi_new_category_rest11(request):
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

                #'item': category.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'danger',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'CATERGORY ALREADY EXISTS')
            return render(request, 'restaurant/creater_master/items/view_all_items.html', context)
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
            return render(request,'restaurant/creater_master/category/view_all_category.html',context)
        return render(request, 'index.html')


def update_category_rest11(request,id):
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
                return render(request, 'restaurant/creater_master/category/view_all_category.html', context)
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
                return render(request, 'restaurant/creater_master/category/view_all_category.html', context)


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


            #'item' : table1.objects.all().filter(flag=1).order_by('-id'),
            'msg' : 'success',
            'sd' : category.objects.get(id=id),
            'category': category.objects.all().filter(flag=1).order_by('-id'),
        }

        return render(request,'restaurant/creater_master/category/update_category.html',context)
    return render(request, 'index.html')


def delete_category_rest11(request,id):
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

                #'item': table1.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'success',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'CATEGORY Deleted Successfully')
            return render(request, 'restaurant/creater_master/category/view_all_category.html', context)
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

                #'item': table1.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'warning',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'CATEGORY already  Deleted')
            return render(request,'restaurant/creater_master/category/view_all_category.html',context)
        return render(request, 'index.html')



def view_all_category_delete_rest11(request):
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
        return render(request,'restaurant/creater_master/category/view_all_category_delete.html',context)
    return render(request, 'index.html')

##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

def view_all_items_rest11(request):
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


            'item' : resturant_items.objects.all().filter(flag=1).order_by('-id'),

        }
        return render(request,'restaurant/creater_master/items/view_all_items.html',context)
    return render(request, 'index.html')

def create_new_item_rest11(request):
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


            'item' : resturant_items.objects.all().filter(flag=1).order_by('-id'),
            'category': category.objects.all().filter(flag=1).order_by('-id'),
            'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),

        }
        return render(request,'restaurant/creater_master/items/create_new_item.html',context)
    return render(request, 'index.html')

def regi_new_item_rest11(request):
    if 'username' in request.session:
        item_name = request.POST.get('name')
        price = request.POST.get('price')
        kitchen_nam = request.POST.get('kitchens')
        item_category = request.POST.get('category')
        ir = resturant_items.objects.all().filter(name=item_name,flag=1).exists()

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

                'item': resturant_items.objects.all().filter(flag=1).order_by('-id'),
                'msg' : 'danger',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
                'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request,'ITEM ALREADY EXISTS')
            return render(request, 'restaurant/creater_master/items/view_all_items.html', context)
        else:
            ic = resturant_items()
            ic.name = item_name
            ic.price = price
            ic.kitchen_nam = kitchen_nam
            ic.item_category = item_category
            ic.qty = 0
            ic.total_item_wise_amt=0
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

                'item' : resturant_items.objects.all().filter(flag=1).order_by('-id'),
                'msg' : 'success',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
                'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'ITEM CREATED SUCCESSFULLY !!!')
            return render(request,'restaurant/creater_master/items/view_all_items.html',context)
        return render(request, 'index.html')

def delete_item_rest11(request,id):
    if 'username' in request.session:
        r=resturant_items.objects.all().filter(id=id).exists()
        if r == True:
            d=resturant_items.objects.get(id=id)
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

                'item': resturant_items.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'success',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
                'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'ITEM Deleted Successfully')
            return render(request, 'restaurant/creater_master/items/view_all_items.html', context)
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

                'item': resturant_items.objects.all().filter(flag=1).order_by('-id'),
                'msg': 'warning',
                'category': category.objects.all().filter(flag=1).order_by('-id'),
                'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
            }
            messages.info(request, 'ITEM already  Deleted')
            return render(request,'restaurant/creater_master/items/view_all_items.html',context)
        return render(request, 'index.html')


def update_item_rest11(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            item_name = request.POST.get('name')
            item_category = request.POST.get('category')
            ir = resturant_items.objects.all().filter(name=item_name,flag=1).exclude(id=id).exists()

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

                    'item': resturant_items.objects.all().filter(flag=1).order_by('-id'),
                    'msg' : 'danger',
                    'category': category.objects.all().filter(flag=1).order_by('-id'),
                    'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
                }
                messages.info(request,'ITEM ALREADY EXISTS')
                return render(request, 'restaurant/creater_master/items/view_all_items.html', context)
            else:
                ic = resturant_items.objects.get(id=id)
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

                    'item': resturant_items.objects.all().filter(flag=1).order_by('-id'),
                    'msg': 'info',
                    'category': category.objects.all().filter(flag=1).order_by('-id'),
                    'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
                }
                messages.info(request, 'ITEM UPDATED SUCCESSFULLY')
                return render(request, 'restaurant/creater_master/items/view_all_items.html', context)


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


            'item' : resturant_items.objects.all().filter(flag=1).order_by('-id'),
            'msg' : 'success',
            'sd' : resturant_items.objects.get(id=id),
            'category': category.objects.all().filter(flag=1).order_by('-id'),
            'kitchen': kitchen.objects.all().filter(flag=1).order_by('-id'),
        }

        return render(request,'restaurant/creater_master/items/update_item.html',context)
    return render(request, 'index.html')

def view_all_items_delete_rest11(request):
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


            'item' : resturant_items.objects.all().filter(flag=2).order_by('-id'),

        }
        return render(request,'restaurant/creater_master/items/view_all_items_delete.html',context)
    return render(request, 'index.html')

##*****************ITEM CREATER END HERE




#########################################################
###******CREATER MASTER END HERE
###################################################################################


#########################################################
###******BILLING MASTER START HERE
###################################################################################

def get_countries_rest11(request):
    if 'username' in request.session:

        countries = []
        t1 = resturant_items.objects.all().filter(flag=1)
        for i in t1:
            countries.append(i.name)

        mimetype = 'application/json'
        return HttpResponse(json.dumps(countries), mimetype)
    return render(request, 'index.html')



def billing_rest11(request,tab):
    if 'username' in request.session:
        print('my tabbbb',tab)
        res=list(tab)
        print(res)
        sres=''.join(res)
        print(sres)
        rtab_lis=[]
        rtab_lis.append('hbct')
        rtab_lis.append(sres)

        print('rtab_lis',rtab_lis)

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
            'items': temp_billing.objects.all().filter(flag=1,table_name=tab).order_by('-id'),
            #'ledger' : ledger.objects.all().filter(flag=1),
            #'accounts_book': accounts_book.objects.all().filter(flag=1),
            'tabl' : tab,
            'ltab' : rtab_lis,
            'blno': bills_no.objects.all().filter(id=1),
            'it': resturant_items.objects.all().order_by('name'),
        }
        return render(request,'restaurant/billing/billing.html',context)
    return render(request, 'index.html')



def regi_temp_billing_rest11(request):
    if 'username' in request.session:

        particulars = request.POST.get('particular')
        qty = request.POST.get('qty')
        descriptions = request.POST.get('description')
        tables = request.POST.get('table')
        billno = request.POST.get('bilno')

        import datetime


        res = temp_billing.objects.all().filter(particulars=particulars,description=descriptions,flag=1,table_name=tables).exists()
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

                'items': temp_billing.objects.all().filter(flag=1,table_name=tables).order_by('-id'),
                'message_bg' : 'alert-danger',
                'it': resturant_items.objects.all().order_by('name'),

                #'ledger': ledger.objects.all().filter(flag=1),
                #'accounts_book': accounts_book.objects.all().filter(flag=1),
                'tabl': tables,
            }
            messages.info(request, 'ITEM already exists')
            return render(request, 'restaurant/billing/billing.html', context)

        else:
            dup = resturant_items.objects.all().filter(name=particulars,flag=1).exists()
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

                    'items': temp_billing.objects.all().filter(flag=1,table_name=tables).order_by('-id'),
                    'message_bg': 'alert-danger',

                    #'ledger': ledger.objects.all().filter(flag=1),
                    #'accounts_book': accounts_book.objects.all().filter(flag=1),
                    'tabl': tables,
                    'it': resturant_items.objects.all().order_by('name'),
                }
                messages.info(request, 'ITEM NOT FOUND')
                return render(request, 'restaurant/billing/billing.html', context)

            else:
                cat = resturant_items.objects.all().filter(flag=1)
                lnam = []
                lcat = []
                al = []
                kitchen = []
                ir=[]
                for i in cat:
                    if i.name == particulars:
                        lnam.append(i.name)
                        lcat.append(i.item_category)
                        al.append(float(i.price))
                        kitchen.append(i.kitchen_nam)
                        ir.append(float(i.price))
                amounts = int(qty) * al[0]


                ic = temp_billing()
                #ic.bill_no  = billno
                ic.bill_no = 0
                ic.particulars = particulars
                ic.qty=qty
                ic.price = ir[0]
                ic.amount = float(amounts)
                ic.kitchen = kitchen[0]

                ic.table_name = tables

                ic.type = "income"
                ic.date = datetime.date.today()
                ic.item_catergory = lcat[0]
                ic.description = descriptions

                from datetime import date
                d = datetime.date.today()
                ic.day = '%02d' % d.day
                ic.month = '%02d' % d.month
                ic.year = '%02d' % d.year
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

                    'items' : temp_billing.objects.all().filter(flag=1,table_name=tables).order_by('-id'),
                    'message_bg': 'alert-success',

                    #'ledger': ledger.objects.all().filter(flag=1),
                    #'accounts_book': accounts_book.objects.all().filter(flag=1),
                    'tabl': tables,
                    'blno' : bills_no.objects.all().filter(id=1),
                    'it': resturant_items.objects.all().order_by('name'),
                }
                messages.info(request, 'ITEM Entered Successfully')
                return render(request,'restaurant/billing/billing.html',context)
        return render(request, 'restaurant/billing/billing.html', context)
    return render(request, 'index.html')

def final_billing(request):
    tables = request.POST.get('table')
    billno = request.POST.get('bilno')

    width = 33
    currency = "INR"
    bri_f = "****************************"
    shop_name = "*******_SMOKE & FIRE_*******"
    shop_address = "Opposite Kerala Bank"
    shop_address1 = "Vellayil Gandhi Road"
    shop_address2 = "Kozhikode"

    import datetime
    dat = datetime.datetime.now()
    d = dat.replace(microsecond=0)
    t = datetime.datetime.today().date()
    dine_in = 'DINE IN: ' + tables
    emp_name = request.session['username']
    print_bill_no = 'BILL NO: ' + billno

    def receipt(purchases):
        total = 0
        items = [
            bri_f.center(width),
            shop_name.center(width),
            shop_address.center(width),
            shop_address1.center(width),
            shop_address2.center(width),
            bri_f.center(width),

            f'{d}'.ljust(width - len(dine_in)) + dine_in,
            f'NAME: {emp_name}'.ljust(width - len(print_bill_no)) + print_bill_no,
            '---------------------------------',
            "\nITEMS:".ljust(width - len(currency) + 1) + currency,
            '---------------------------------',
            # currency.rjust(width)
        ]
        for name, price, count in purchases:
            total += price * count

            all_price = str(round(price * count, 2))
            # all_price = str(round(price,2))

            msg = f'{name}'.ljust(width - len(all_price), ' ')
            msg += all_price

            if type(count) is int and count >= 2:
                msg += f'\n QTY:{price} x RS:{count}'
            elif type(count) is float:
                msg += f'\n {count} kg x {price}'

            items.append(msg)
        total = str(round(total, 2))
        items.append("\nTOTAL:".ljust(width - len(total) + 1) + total)
        items.append('............................'.center(width))
        items.append(' Consume Food '.center(width))
        items.append(' Within Two Hours of Purchase '.center(width))
        items.append(''.center(width))
        items.append(' THANKS VISIT AGAIN US '.center(width))
        items.append(' Designed & Developed by HBCT.IN '.center(width))

        return '\n'.join(items)


    fitem = temp_billing.objects.all().filter(flag=1,table_name=tables)
    fil=[]
    resil=[]
    #resil.append('ITEM NAME','RATE')
    for i in fitem:
        if i.flag == 1:
            fil.append(i.particulars)
            fil.append(i.qty)
            fil.append(i.price)
        resil.append(tuple(fil))
        fil.clear()

    p = (receipt(resil))

    path="demofile2.txt"

    f = open(path, "r+")

    # absolute file positioning
    f.seek(0)

    # to erase all data
    f.truncate()

    f = open(path, "a")
    f.write(p)
    f.close()

    # open and read the file after the appending:
    f = open(path, "r")

    import os
    os.startfile(path, 'print')
    # os.O_TEXT(file_path)





    it=temp_billing.objects.all().filter(flag=1,table_name=tables),
    #print(len(it))
    print('..................')
    cat = temp_billing.objects.all().filter(flag=1,table_name=tables)
    als = []
    for i in cat:
        if i.flag == 1:
            ic=temp_billing.objects.get(id=i.id)
            ic.bill_no = billno
            ic.billed_by = request.session['username']
            ic.date = datetime.date.today()
            from datetime import date
            d = datetime.date.today()
            ic.day = '%02d' % d.day
            ic.month = '%02d' % d.month
            ic.year = '%02d' % d.year

            ic.flag=2
            ic.save()
            als.append(i.flag)





        #ic=temp_billing.objects.get(id=i.id)
        #ic.flag = 2
        #ic.save()
    ic=bills_no.objects.get(id=1)
    ic.billing_no = int(billno) + 1
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

        'items': temp_billing.objects.all().filter(flag=1, table_name=tables).order_by('-id'),
        'message_bg': 'alert-success',
        'tabl': tables,
        'blno': bills_no.objects.all().filter(id=1),
        'it': resturant_items.objects.all().order_by('name'),
    }
    messages.info(request, 'Billing Successfully Completed')
    return render(request, 'restaurant/billing/billing.html', context)



def print_kot(request):
    tables = request.POST.get('ptable')
    print_table = "DINE IN: " + tables

    width = 33
    currency = "QTY"
    shop_name = "smoke and fire"

    def receipt(purchases):
        total = 0
        items = [
            print_table.center(width),
            '---------------------------------',
            "\nITEMS:".ljust(width - len(currency) + 1) + currency,
            '---------------------------------',
        ]
        for name, price, count in purchases:
            all_price = str(round(price, 2))

            msg = f'{name}'.ljust(width - len(all_price), ' ')
            msg += all_price

            items.append(msg)

        return '\n'.join(items)


    fitem = temp_billing.objects.all().filter(flag=1,table_name=tables)
    fil=[]
    resil=[]
    #resil.append('ITEM NAME','RATE')
    for i in fitem:
        if i.flag == 1:
            fil.append(i.particulars)
            fil.append(i.qty)
            fil.append(i.price)
        resil.append(tuple(fil))
        fil.clear()

    p = (receipt(resil))

    path="demofile2.txt"

    f = open(path, "r+")

    # absolute file positioning
    f.seek(0)

    # to erase all data
    f.truncate()

    f = open(path, "a")
    f.write(p)
    f.close()

    # open and read the file after the appending:
    f = open(path, "r")

    import os
    os.startfile(path, 'print')
    # os.O_TEXT(file_path)


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

        'items': temp_billing.objects.all().filter(flag=1, table_name=tables).order_by('-id'),
        'message_bg': 'alert-success',
        'tabl': tables,
        'blno': bills_no.objects.all().filter(id=1),
        'it': resturant_items.objects.all().order_by('name')
    }
    messages.info(request, 'Printing Successfully Completed')
    return render(request, 'restaurant/billing/billing.html', context)









def print_bill(request):
    tables = request.POST.get('ptable')

    width = 33
    currency = "INR"
    bri_f = "****************************"
    shop_name = "*******_SMOKE & FIRE_*******"
    shop_address="Opposite Kerala Bank"
    shop_address1="Vellayil Gandhi Road"
    shop_address2 = "Kozhikode"

    import datetime
    dat = datetime.datetime.now()
    d = dat.replace(microsecond=0)
    t = datetime.datetime.today().date()
    dine_in = 'DINE IN: ' + tables
    emp_name=request.session['username']
    print_bill_no='BILL NO: ' + '125'

    def receipt(purchases):
        total = 0
        items = [
            bri_f.center(width),
            shop_name.center(width),
            shop_address.center(width),
            shop_address1.center(width),
            shop_address2.center(width),
            bri_f.center(width),

            f'{d}'.ljust(width - len(dine_in)) + dine_in,
            f'NAME: {emp_name}'.ljust(width - len(print_bill_no)) + print_bill_no,
            '---------------------------------',
            "\nITEMS:".ljust(width - len(currency) + 1) + currency,
            '---------------------------------',
            # currency.rjust(width)
        ]
        for name, price, count in purchases:
            total += price * count

            all_price = str(round(price * count, 2))
            # all_price = str(round(price,2))

            msg = f'{name}'.ljust(width - len(all_price), ' ')
            msg += all_price

            if type(count) is int and count >= 2:
                msg += f'\n QTY:{price} x RS:{count}'
            elif type(count) is float:
                msg += f'\n {count} kg x {price}'

            items.append(msg)
        total = str(round(total, 2))
        items.append("\nTOTAL:".ljust(width - len(total) + 1) + total)
        items.append('............................'.center(width))
        items.append(' Consume Food '.center(width))
        items.append(' Within Two Hours of Purchase '.center(width))
        items.append(''.center(width))
        items.append(' THANKS VISIT AGAIN US '.center(width))
        items.append(' Designed & Developed by HBCT.IN '.center(width))

        return '\n'.join(items)


    fitem = temp_billing.objects.all().filter(flag=1,table_name=tables)
    fil=[]
    resil=[]
    #resil.append('ITEM NAME','RATE')
    for i in fitem:
        if i.flag == 1:
            fil.append(i.particulars)
            fil.append(i.qty)
            fil.append(i.price)
        resil.append(tuple(fil))
        fil.clear()

    p = (receipt(resil))

    path="demofile2.txt"

    f = open(path, "r+")

    # absolute file positioning
    f.seek(0)

    # to erase all data
    f.truncate()

    f = open(path, "a")
    f.write(p)
    f.close()

    # open and read the file after the appending:
    f = open(path, "r")

    import os
    os.startfile(path, 'print')
    # os.O_TEXT(file_path)


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

        'items': temp_billing.objects.all().filter(flag=1, table_name=tables).order_by('-id'),
        'message_bg': 'alert-success',
        'tabl': tables,
        'blno': bills_no.objects.all().filter(id=1),
        'it': resturant_items.objects.all().order_by('name')
    }
    messages.info(request, 'Printing Successfully Completed')
    return render(request, 'restaurant/billing/billing.html', context)



#########################################################
###******BILLING MASTER END HERE
###################################################################################


def view_all_canceled_orders(request,tab):
    print('my tabbbb', tab)
    res = list(tab)
    print(res)
    sres = ''.join(res)
    print(sres)
    rtab_lis = []
    rtab_lis.append('hbct')
    rtab_lis.append(sres)

    print('rtab_lis', rtab_lis)

    tables = rtab_lis[1]

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

        #'tabl' : tab,
        'tabl' : rtab_lis,
        'items': temp_billing.objects.all().filter(flag=101, table_name=tables).order_by('-id'),
        'it': resturant_items.objects.all().order_by('name')

    }
    return render(request, 'restaurant/billing/view_all_canceled_orders.html', context)


def cancel_order(request,id):
    if 'username' in request.session:
        hb=temp_billing.objects.filter(id=id)
        rtab_lis = []
        rtab_lis.append('hbct')
        for i in hb:
            rtab_lis.append(i.table_name)
        print('rtab_lis', rtab_lis)
        tables = rtab_lis[1]

        r=temp_billing.objects.all().filter(id=id,flag=1).exists()
        if r == True:
            d=temp_billing.objects.get(id=id)
            d.deleted_by = 'DB ' + request.session['username']
            import datetime
            d.db_date = datetime.datetime.now()
            d.flag = 101
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

                'items': temp_billing.objects.all().filter(flag=1, table_name=tables).order_by('-id'),
                'message_bg': 'alert-success',

                'tabl': rtab_lis,
                'it': resturant_items.objects.all().order_by('name')


            }
            messages.info(request, 'ITEM Deleted Successfully')
            return render(request, 'restaurant/billing/billing.html', context)
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

                'items': temp_billing.objects.all().filter(flag=1, table_name=tables).order_by('-id'),
                'message_bg': 'alert-warning',

                'tabl': rtab_lis,
                'it': resturant_items.objects.all().order_by('name')

            }
            messages.info(request, 'ITEM already  Deleted')
            return render(request,'restaurant/billing/billing.html',context)
        return render(request, 'index.html')



def update_orders(request,id):
    if 'username' in request.session:
        hb = temp_billing.objects.filter(id=id)
        rtab_lis = []
        rtab_lis.append('hbct')
        for i in hb:
            rtab_lis.append(i.table_name)
        print('rtab_lis', rtab_lis)
        tables = rtab_lis[1]

        if request.method == 'POST':
            particulars = request.POST.get('particular')
            qty = request.POST.get('qty')
            descriptions = request.POST.get('description')
            tables = request.POST.get('table')
            billno = request.POST.get('bilno')
            pri = request.POST.get('pr')

            dup = temp_billing.objects.all().filter(particulars=particulars,flag=1).exists()
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

                    'items': temp_billing.objects.all().filter(flag=1, table_name=tables).order_by('-id'),
                    'message_bg': 'alert-danger',

                    'tabl': tables,
                    'it': resturant_items.objects.all().order_by('name')

                }
                messages.info(request, 'ITEM NOT FOUND')
                return render(request, 'restaurant/billing/billing.html', context)
            else:

                cat = resturant_items.objects.all().filter(flag=1)
                lnam = []
                lcat = []
                al = []
                kitchen = []
                ir = []
                for i in cat:
                    if i.name == particulars:
                        lnam.append(i.name)
                        lcat.append(i.item_category)
                        al.append(float(i.price))
                        kitchen.append(i.kitchen_nam)
                        ir.append(float(i.price))
                #amounts = int(qty) * al[0]
                amounts = int(qty) * pri

                ic = temp_billing.objects.get(id=id)
                # ic.bill_no  = billno
                ic.bill_no = 0
                ic.particulars = particulars
                ic.qty = qty
                #ic.price = ir[0]
                ic.price = pri
                ic.amount = float(amounts)
                ic.kitchen = kitchen[0]

                ic.table_name = tables

                ic.type = "income"
                from datetime import date
                ic.date = date.today()
                ic.item_catergory = lcat[0]
                ic.description = descriptions

                from datetime import date
                d = date.today()
                ic.day = '%02d' % d.day
                ic.month = '%02d' % d.month
                ic.year = '%02d' % d.year
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

                    'items': temp_billing.objects.all().filter(flag=1, table_name=tables).order_by('-id'),
                    'message_bg': 'alert-info',

                    'tabl': tables,
                    'it': resturant_items.objects.all().order_by('name')
                }
                messages.info(request, 'ITEM Updated Successfully')
                return render(request, 'restaurant/billing/billing.html', context)


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


            'items': temp_billing.objects.all().filter(flag=1, table_name=tables).order_by('-id'),
            'message_bg': 'alert-success',
            'tabl': tables,

            'sd': temp_billing.objects.get(id=id),
            'it': resturant_items.objects.all().order_by('name')
        }
        return render(request, 'restaurant/billing/update_orders.html', context)
    return render(request, 'index.html')

def test_bil(request):
    context={
        'it' : resturant_items.objects.all().order_by('name')
    }
    return render(request, 'restaurant/billing/test_bil.html', context)



