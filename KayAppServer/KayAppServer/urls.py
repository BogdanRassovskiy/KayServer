from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include#,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_json/', views.test_json,name="test_json"),
    path('enter/', views.enter,name="enter"),
    path('privacy/', views.privacy,name="privacy"),
    path('check_mark_inn/', views.check_mark_inn,name="check_mark_inn"),
    path('send_var_pswd/', views.send_var_pswd,name="send_var_pswd"),
    path('send_self_create_market/', views.send_self_create_market,name="send_self_create_market"),
    path('send_self_create_prodavac/', views.send_self_create_prodavac,name="send_self_create_prodavac"),
    path('check_version/', views.check_version,name="check_version"),
    path('get_messages/', views.get_messages,name="get_messages"),
    path('send_readed/', views.send_readed,name="send_readed"),
    path('send_message_to_server/', views.send_message_to_server,name="send_message_to_server"),
    path('get_chat_admins/', views.get_chat_admins,name="get_chat_admins"),
    #driver
    path('get_app/', views.get_app,name="get_app"),
    path('get_money/', views.get_money,name="get_money"),
    path('get_districts/', views.get_districts,name="get_districts"),
    path('get_nak/', views.get_nak,name="get_nak"),
    path('get_orders/', views.get_orders,name="get_orders"),
    path('get_dolgs/', views.get_dolgs,name="get_dolgs"),
    path('get_prices/', views.get_prices,name="get_prices"),
    path('get_location/', views.get_location,name="get_location"),
    path('get_market_list/', views.get_market_list,name="get_market_list"),
    path('get_default_market/', views.get_default_market,name="get_default_market"),
    path('get_updates_driver/', views.get_updates_driver,name="get_updates_driver"),
    path('get_product_list/', views.get_product_list,name="get_product_list"),
    path('uber_driver_request/', views.uber_driver_request,name="uber_driver_request"),
    path('send_order/', views.send_order,name="send_order"),
    path('send_dolg/', views.send_dolg,name="send_dolg"),
    path('send_new_inn/', views.send_new_inn,name="send_new_inn"),
    path('send_new_phone/', views.send_new_phone,name="send_new_phone"),
    path('send_new_location/', views.send_new_location,name="send_new_location"),
    path('get_adres_from_coords/', views.get_adres_from_coords,name="get_adres_from_coords"),
    path('create_new_market/', views.create_new_market,name="create_new_market"),
    path('get_all_orders_sells/', views.get_all_orders_sells,name="get_all_orders_sells"),
    #admin
    path('get_history/', views.get_history,name="get_history"),
    path('get_market_history/', views.get_market_history,name="get_market_history"),
    path('get_drivers/', views.get_drivers,name="get_drivers"),
    path('get_admin_orders/', views.get_admin_orders,name="get_admin_orders"),
    path('uber_admin_request/', views.uber_admin_request,name="uber_admin_request"),
    path('get_updates_admin/', views.get_updates_admin,name="get_updates_admin"),
    path('send_hist_var/', views.send_hist_var,name="send_hist_var"),
    path('send_defaults/', views.send_defaults,name="send_defaults"),
    path('send_prod_settings/', views.send_prod_settings,name="send_prod_settings"),
    path('get_all_users/', views.get_all_users,name="get_all_users"),
    path('send_new_driver/', views.send_new_driver,name="send_new_driver"),
    path('send_remove_driver/', views.send_remove_driver,name="send_remove_driver"),
    path('send_remove_order/', views.send_remove_order,name="send_remove_order"),
    path('send_give_him_order/', views.send_give_him_order,name="send_give_him_order"),
    path('send_remove_wrong_order/', views.send_remove_wrong_order,name="send_remove_wrong_order"),
    path('send_market_settings/', views.send_market_settings,name="send_market_settings"),
    path('send_new_price_type_name/', views.send_new_price_type_name,name="send_new_price_type_name"),
    path('send_rem_price_type_name/', views.send_rem_price_type_name,name="send_rem_price_type_name"),
    path('send_create_price_type/', views.send_create_price_type,name="send_create_price_type"),
    path('send_req_for_excel/', views.send_req_for_excel,name="send_req_for_excel"),
    path('get_excel/', views.get_excel,name="get_excel"),
    path('save_excel/', views.save_excel,name="save_excel"),
    path('send_url_in_tg/', views.send_url_in_tg,name="send_url_in_tg"),
    path('get_admins/', views.get_admins,name="get_admins"),
    path('send_new_admin/', views.send_new_admin,name="send_new_admin"),
    path('send_remove_admin/', views.send_remove_admin,name="send_remove_admin"),
    path('send_new_acces_admin/', views.send_new_acces_admin,name="send_new_acces_admin"),
    path('send_about_not/', views.send_about_not,name="send_about_not"),
    path('send_create_new_product/', views.send_create_new_product,name="send_create_new_product"),
    path('send_rem_product/', views.send_rem_product,name="send_rem_product"),
    path('get_cat_list/', views.get_cat_list,name="get_cat_list"),
    path('send_edit_cat/', views.send_edit_cat,name="send_edit_cat"),
    path('send_rem_cat/', views.send_rem_cat,name="send_rem_cat"),
    path('send_edit_market/', views.send_edit_market,name="send_edit_market"),
    path('send_null_driver/', views.send_null_driver,name="send_null_driver"),
    path('send_now_self_order/', views.send_now_self_order,name="send_now_self_order"),
    path('api_create_order/', views.api_create_order,name="api_create_order"),
    path('send_photo/', views.send_photo,name="send_photo"),
    path('send_photo_new/', views.send_photo_new,name="send_photo_new"),
    path('send_new_merch_rev/', views.send_new_merch_rev,name="send_new_merch_rev"),
    path('send_hand_nak/', views.send_hand_nak,name="send_hand_nak"),
    path('send_new_nulls/', views.send_new_nulls,name="send_new_nulls"),
    path('send_act_req/', views.send_act_req,name="send_act_req"),
    path('get_mikro_market/', views.get_mikro_market,name="get_mikro_market"),
    path('get_search_text/', views.get_search_text,name="get_search_text"),
    path('get_search_loc/', views.get_search_loc,name="get_search_loc"),
    path('send_box_settings/', views.send_box_settings,name="send_box_settings"),
    path('send_admin_pswd/', views.send_admin_pswd,name="send_admin_pswd"),
    path('send_site/', views.send_site,name="send_site"),
    path('send_edit_prices/', views.send_edit_prices,name="send_edit_prices"),
    path('send_districts_driver/', views.send_districts_driver,name="send_districts_driver"),
    path('get_kladmens/', views.get_kladmens,name="get_kladmens"),
    path('send_new_kladmen/', views.send_new_kladmen,name="send_new_kladmen"),
    path('send_remove_kladmen/', views.send_remove_kladmen,name="send_remove_kladmen"),
    path('klad_add/', views.klad_add,name="klad_add"),
    path('change_klad_pswd/', views.change_klad_pswd,name="change_klad_pswd"),
    #market
    path('get_merchants/', views.get_merchants,name="get_merchants"),
    path('get_market_categories/', views.get_market_categories,name="get_market_categories"),
    path('get_market_products/', views.get_market_products,name="get_market_products"),
    path('get_photo/', views.get_photo,name="get_photo"),
    path('get_i_market/', views.get_i_market,name="get_i_market"),
    path('send_market_order/', views.send_market_order,name="send_market_order"),
    path('get_market_news/', views.get_market_news,name="get_market_news"),
    path('send_market_rem_order/', views.send_market_rem_order,name="send_market_rem_order"),
    path('uber_market_request/', views.uber_market_request,name="uber_market_request"),
    path('send_self_market_data/', views.send_self_market_data,name="send_self_market_data"),
    path('check_send_tg_settings/', views.check_send_tg_settings,name="check_send_tg_settings"),
    path('get_updates_market/', views.get_updates_market,name="get_updates_market"),
    #api
    path('add_mass_market/', views.add_mass_market,name="add_mass_market"),
    path('get_api_categories/', views.get_api_categories,name="get_api_categories"),
    path('get_api_products/', views.get_api_products,name="get_api_products"),
    path('check_order_status/', views.check_order_status,name="check_order_status"),
    #root
    path('send_market_var/', views.send_market_var,name="send_market_var"),
    path('send_new_merch_pswd/', views.send_new_merch_pswd,name="send_new_merch_pswd"),
    path('send_new_acces/', views.send_new_acces,name="send_new_acces"),
    path('get_roots/', views.get_roots,name="get_roots"),
    path('send_new_root_pswd/', views.send_new_root_pswd,name="send_new_root_pswd"),
    path('send_new_root_level/', views.send_new_root_level,name="send_new_root_level"),
    path('send_create_new_root/', views.send_create_new_root,name="send_create_new_root"),
    path('send_remove_new_root/', views.send_remove_new_root,name="send_remove_new_root"),
    path('send_remove_district/', views.send_remove_district,name="send_remove_district"),
    path('send_create_new_district/', views.send_create_new_district,name="send_create_new_district"),
    path('send_remove_location/', views.send_remove_location,name="send_remove_location"),
    path('send_remove_market/', views.send_remove_market,name="send_remove_market"),
    path('send_save_market/', views.send_save_market,name="send_save_market"),
    path('uber_root_request/', views.uber_root_request,name="uber_root_request"),
    path('get_updates_root/', views.get_updates_root,name="get_updates_root"),
    path('send_get_this_history/', views.send_get_this_history,name="send_get_this_history"),
    path('send_create_new_merchant/', views.send_create_new_merchant,name="send_create_new_merchant"),
    path('send_remove_photo/', views.send_remove_photo,name="send_remove_photo"),
    path('send_accept_photo/', views.send_accept_photo,name="send_accept_photo"),
    path('get_var_levels/', views.get_var_levels,name="get_var_levels"),
    path('send_var_level_settings/', views.send_var_level_settings,name="send_var_level_settings"),
    path('get_cislo/', views.get_cislo,name="get_cislo"),

    #web
    path('web_enter/', views.web_enter,name="web_enter"),
    path('check_web_enter/', views.check_web_enter,name="check_web_enter"),
    path('get_docs/', views.get_docs,name="get_docs"),
    path('get_photo_html/', views.get_photo_html,name="get_photo_html"),

    path('mass_page/', views.mass_page,name="mass_page"),
    path('test_mass/', views.test_mass,name="test_mass"),
    path('get_strings/', views.get_strings,name="get_strings"),
    path('get_languages/', views.get_languages,name="get_languages"),
    path('get_unvarified_markets/', views.get_unvarified_markets,name="get_unvarified_markets"),
    path('get_notifications/', views.get_notifications,name="get_notifications"),
    path('not_was_seen/', views.not_was_seen,name="not_was_seen"),
    path('refresh_gen_link/', views.refresh_gen_link,name="refresh_gen_link"),
    path('excel_space/', views.excel_space,name="excel_space"),
    path('save_excel_space/', views.save_excel_space,name="save_excel_space"),
    path('get_excel_naks/', views.get_excel_naks,name="get_excel_naks"),
    path('send_cho_chosen_nak/', views.send_cho_chosen_nak,name="send_cho_chosen_nak"),
    path('get_updates/', views.get_updates,name="get_updates"),
    path('get_mikro_history/', views.get_mikro_history,name="get_mikro_history"),

]
