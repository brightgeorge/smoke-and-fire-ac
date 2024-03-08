from django.contrib import admin
from django.urls import path, include

from . import accounts11

urlpatterns = [

    #####********************************************************************************************************
    # ACCOUNTS START HERE
    ####***************************************************

    #########################################################
    ###******CREATER MASTER START HERE
    ###################################################################################

    ##******************CATERGORY CREATER START HERE

    path('view_all_category11/', accounts11.view_all_category11, name='view_all_category11'),
    path('create_new_category11/', accounts11.create_new_category11, name='create_new_category11'),
    path('regi_new_category11/', accounts11.regi_new_category11, name='regi_new_category11'),
    path('update_category11/<id>', accounts11.update_category11, name='update_category11'),

    path('delete_category11/<id>', accounts11.delete_category11, name='delete_category11'),
    path('view_all_category_delete11/', accounts11.view_all_category_delete11, name='view_all_category_delete11'),

    ##*****************CATERY CREATER END HERE

    ##******************ITEM CREATER START HERE

    path('view_all_items11/', accounts11.view_all_items11, name='view_all_items11'),
    path('create_new_item11/', accounts11.create_new_item11, name='create_new_item11'),
    path('regi_new_item11/', accounts11.regi_new_item11, name='regi_new_item11'),
    path('delete_item11/<id>', accounts11.delete_item11, name='delete_item11'),
    path('update_item11/<id>', accounts11.update_item11, name='update_item11'),
    path('view_all_items_delete11/', accounts11.view_all_items_delete11, name='view_all_items_delete11'),

    ##*****************ITEM CREATER END HERE

    ##******************LEDGER CREATER START HERE

    path('view_all_ledger11/', accounts11.view_all_ledger11, name='view_all_ledger11'),
    path('create_new_ledger11/', accounts11.create_new_ledger11, name='create_new_ledger11'),
    path('regi_new_ledger11/', accounts11.regi_new_ledger11, name='regi_new_ledger11'),
    path('delete_ledger11/<id>', accounts11.delete_ledger11, name='delete_ledger11'),
    path('update_ledger11/<id>', accounts11.update_ledger11, name='update_ledger11'),
    path('view_all_ledger_delete11/', accounts11.view_all_ledger_delete11, name='view_all_ledger_delete11'),

    ##*****************LEDGER CREATER END HERE

    ##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book11/', accounts11.view_all_accounts_book11, name='view_all_accounts_book11'),
    path('create_new_accounts_book11/', accounts11.create_new_accounts_book11, name='create_new_accounts_book11'),
    path('regi_new_accounts_book11/', accounts11.regi_new_accounts_book11, name='regi_new_accounts_book11'),
    path('update_accounts_book11/<id>', accounts11.update_accounts_book11, name='update_accounts_book11'),
    path('delete_accounts_book11/<id>', accounts11.delete_accounts_book11, name='delete_accounts_book11'),
    path('view_all_accounts_book_delete11/', accounts11.view_all_accounts_book_delete11,
         name='view_all_accounts_book_delete11'),

    ##*****************ACCOUNTS_BOOK CREATER END HERE

    #########################################################
    ###******CREATER MASTER END HERE
    ###################################################################################

    #########################################################
    ###******INCOME EXPENSE ENTRY FORM MASTER START HERE
    ###################################################################################

    path('get_countries11/', accounts11.get_countries11, name='get_countries11'),

    path('in_exp_items_entry11/', accounts11.in_exp_items_entry11, name='in_exp_items_entry11'),
    path('reg_in_exp_items_entry11/', accounts11.reg_in_exp_items_entry11, name='reg_in_exp_items_entry11'),
    path('delete_journal11/<id>', accounts11.delete_journal11, name='delete_journal11'),
    path('update_in_exp_items_entry11/<id>', accounts11.update_in_exp_items_entry11,name='update_in_exp_items_entry11'),
    path('detailed_journal_report11/', accounts11.detailed_journal_report11, name='detailed_journal_report11'),
    path('journal_report_deleted11/', accounts11.journal_report_deleted11, name='journal_report_deleted11'),

    #########################################################
    ###******INCOME EXPENSE ENTRY FORM MASTER END HERE
    ###################################################################################
    #########*******************************************************************************************************************
    #########################################################
    ###******ALL REPORTS  START HERE
    ###################################################################################

    ###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise11/', accounts11.daily_category_wise11, name='daily_category_wise11'),
    path('monthly_category_based_reports11/', accounts11.monthly_category_based_reports11,
         name='monthly_category_based_reports11'),
    path('yearly_category_based_reports11/', accounts11.yearly_category_based_reports11,
         name='yearly_category_based_reports11'),

    ###*************CATEGORY WISE REPORTS  END HERE

    ###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed11/', accounts11.daily_detailed11, name='daily_detailed11'),
    path('monthly_detailed11/', accounts11.monthly_detailed11, name='monthly_detailed11'),
    path('yearly_detailed11/', accounts11.yearly_detailed11, name='yearly_detailed11'),

    ###*************DAILY DETAILED REPORTS  START HERE

    ###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports11/', accounts11.item_based_reports11, name='item_based_reports11'),
    path('daily_item_based_reports11/', accounts11.daily_item_based_reports11, name='daily_item_based_reports11'),
    path('monthly_item_based_reports11/', accounts11.monthly_item_based_reports11, name='monthly_item_based_reports11'),

    ###*************ITEM BASED REPORTS  START HERE

    ###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports11/', accounts11.ledger_based_reports11, name='ledger_based_reports11'),
    path('monthly_ledger_based_reports11/', accounts11.monthly_ledger_based_reports11,
         name='monthly_ledger_based_reports11'),
    path('daily_ledger_based_reports11/', accounts11.daily_ledger_based_reports11, name='daily_ledger_based_reports11'),

    ###*************LEDGER BASED REPORTS  START HERE

    ###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports11/', accounts11.accounts_book_based_reports11,
         name='accounts_book_based_reports11'),
    path('daily_accounts_book_based_reports11/', accounts11.daily_accounts_book_based_reports11,
         name='daily_accounts_book_based_reports11'),
    path('monthly_accounts_book_based_reports11/', accounts11.monthly_accounts_book_based_reports11,
         name='monthly_accounts_book_based_reports11'),

    ###*************ACCOUNTS-BOOK BASED REPORTS  END HERE

    #########################################################
    ###******ALL REPORTS  END HERE
    ###################################################################################

    path('monthly_reports_choose_months11/', accounts11.monthly_reports_choose_months11,
         name='monthly_reports_choose_months11'),
    path('monthly_detailed_daily_in_exp_items_report11/<mo>', accounts11.monthly_detailed_daily_in_exp_items_report11,
         name='monthly_detailed_daily_in_exp_items_report11'),

    path('single_monthly_reports_choose_months11/', accounts11.single_monthly_reports_choose_months11,
         name='single_monthly_reports_choose_months11'),
    path('single_monthly_daily_in_exp_items_report11/<mo>', accounts11.single_monthly_daily_in_exp_items_report11,
         name='single_monthly_daily_in_exp_items_report11'),

    path('accounts_dash_board_ob_ch11/', accounts11.accounts_dash_board_ob_ch11, name='accounts_dash_board_ob_ch11'),

    path('profit_sharing_choose_months11', accounts11.profit_sharing_choose_months11,
         name='profit_sharing_choose_months11'),
    path('profit_sharing11/<mo>', accounts11.profit_sharing11, name='profit_sharing11'),
    path('view_share_holders11', accounts11.view_share_holders11, name='view_share_holders11'),
    path('create_share_holders11', accounts11.create_share_holders11, name='create_share_holders11'),
    path('regi_share_holders11', accounts11.regi_share_holders11, name='regi_share_holders11'),
    path('update_share_holders11/<id>', accounts11.update_share_holders11, name='update_share_holders11'),
    path('delete_share_holders11/<id>', accounts11.delete_share_holders11, name='delete_share_holders11'),
    path('view_deleted_share_holders11', accounts11.view_deleted_share_holders11, name='view_deleted_share_holders11'),

]
