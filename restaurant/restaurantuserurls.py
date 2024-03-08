from django.contrib import admin
from django.urls import path, include

from . import restaurant_mgt
from . import rest_report

urlpatterns = [

    path('restaurantindex/',restaurant_mgt.restaurantindex,name='restaurantindex'),

    #########################################################
    ###******CREATER MASTER START HERE
    ###################################################################################

    ##******************KITCHEN CREATER START HERE





    ##******************KITCHEN CREATER END HERE

    path('view_all_kitchen_rest11/', restaurant_mgt.view_all_kitchen_rest11, name='view_all_kitchen_rest11'),
    path('create_new_kitchen_rest11/', restaurant_mgt.create_new_kitchen_rest11, name='create_new_kitchen_rest11'),
    path('regi_new_kitchen_rest11/', restaurant_mgt.regi_new_kitchen_rest11, name='regi_new_kitchen_rest11'),
    path('update_kitchen11/<id>', restaurant_mgt.update_kitchen_rest11, name='update_kitchen_rest11'),

    path('delete_kitchen_rest11/<id>', restaurant_mgt.delete_kitchen_rest11, name='delete_kitchen_rest11'),
    path('view_all_kitchen_delete_rest11/', restaurant_mgt.view_all_kitchen_delete_rest11, name='view_all_kitchen_delete_rest11'),

    ##******************CATERGORY CREATER START HERE

    path('view_all_category_rest11/', restaurant_mgt.view_all_category_rest11, name='view_all_category_rest11'),
    path('create_new_category_rest11/', restaurant_mgt.create_new_category_rest11, name='create_new_category_rest11'),
    path('regi_new_category_rest11/', restaurant_mgt.regi_new_category_rest11, name='regi_new_category_rest11'),
    path('update_category11/<id>', restaurant_mgt.update_category_rest11, name='update_category_rest11'),

    path('delete_category_rest11/<id>', restaurant_mgt.delete_category_rest11, name='delete_category_rest11'),
    path('view_all_category_delete_rest11/', restaurant_mgt.view_all_category_delete_rest11, name='view_all_category_delete_rest11'),

    ##*****************CATERY CREATER END HERE

    ##******************ITEM CREATER START HERE

    path('view_all_items_rest11/', restaurant_mgt.view_all_items_rest11, name='view_all_items_rest11'),
    path('create_new_item_rest11/', restaurant_mgt.create_new_item_rest11, name='create_new_item_rest11'),
    path('regi_new_item_rest11/', restaurant_mgt.regi_new_item_rest11, name='regi_new_item_rest11'),
    path('delete_item_rest11/<id>', restaurant_mgt.delete_item_rest11, name='delete_item_rest11'),
    path('update_itemV/<id>', restaurant_mgt.update_item_rest11, name='update_item_rest11'),
    path('view_all_items_delete_rest11/', restaurant_mgt.view_all_items_delete_rest11, name='view_all_items_delete_rest11'),

    ##*****************ITEM CREATER END HERE

#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******BILLING ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries_rest11/', restaurant_mgt.get_countries_rest11, name='get_countries_rest11'),

    path('billing_rest11/<tab>', restaurant_mgt.billing_rest11, name='billing_rest11'),
    path('regi_temp_billing_rest11/',restaurant_mgt.regi_temp_billing_rest11,name='regi_temp_billing_rest11'),

    path('final_billing/',restaurant_mgt.final_billing,name='final_billing'),
    path('print_bill/',restaurant_mgt.print_bill,name='print_bill'),

    #path('reg_in_exp_items_entry11/', restaurant_mgt.reg_in_exp_items_entry11, name='reg_in_exp_items_entry11'),
    path('cancel_order/<id>', restaurant_mgt.cancel_order, name='cancel_order'),
    path('update_orders/<id>', restaurant_mgt.update_orders,name='update_orders'),
    #path('detailed_journal_report11/', restaurant_mgt.detailed_journal_report11, name='detailed_journal_report11'),
    path('view_all_canceled_orders/<tab>', restaurant_mgt.view_all_canceled_orders, name='view_all_canceled_orders'),

    #########################################################
    ###******BILLING ENTRY FORM MASTER END HERE
    ###################################################################################

    path('bill_wise_report/',rest_report.bill_wise_report,name='bill_wise_report'),
    path('bill_wise_item_report/',rest_report.bill_wise_item_report,name='bill_wise_item_report'),

    path('item_wise_report/',rest_report.item_wise_report,name='item_wise_report'),
    path('item_date_wise_report/',rest_report.item_date_wise_report,name='item_date_wise_report'),
    path('kitchen_wise_report/',rest_report.kitchen_wise_report,name='kitchen_wise_report'),

    path('print_kot/',restaurant_mgt.print_kot,name='print_kot'),
    path('test_bil/',restaurant_mgt.test_bil,name='test_bil'),

]
