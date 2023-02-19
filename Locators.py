#Login

login_username="//*[@id='loginform']/div[1]/input[4]"
login_btn_submit_next="//*[@id='loginform']/div[2]/button"
login_password="//*[@id='codeform']/div[1]/input"
login_btn_submit="//*[@id='codeform']/div[2]/button"

#Orders

click_orders= "/html/body/div[1]/aside/section/ul/li[7]/a"
orders_start_date= "//*[@id='start-date']"
orders_start_date_back= "//*[@id='plotId']/div[1]/div[3]"
orders_start_date_month= "//*[@id='plotId']/div[1]/div[2]"
orders_start_date_month_option= "//*[@id='plotId']/div[2]/div/div[1]"
orders_start_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[1]/td[3]"
orders_end_date= "//*[@id='end-date']"
# orders_end_date_month= "//*[@id='plotId']/div[1]/div[2]"
orders_end_date_month= "/html/body/div[8]/div/div[1]/div[2]"
# orders_end_date_month_option= "//*[@id='plotId']/div[2]/div/div[1]"
orders_end_date_month_option= "/html/body/div[8]/div/div[2]/div/div[1]"
orders_end_date_back= "//*[@id='plotId']/div[1]/div[3]"
# orders_end_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[5]/td[5]"
orders_end_date_option= "/html/body/div[8]/div/div[2]/div/div/table/tbody/tr[5]/td[5]"
orders_click_span= "//*[@id='dateFilter']/div[2]/input"
# orders_dateFilter= "//*[@id='dateFilter']"
orders_dateFilter= "/html/body/div[1]/div[1]/section[2]/span[1]/div[2]/div/div/div/div/div/form/div[1]/button"
# orders_result= "//*[@id='table-753']/thead/tr[1]/th"
orders_result= "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div/table/thead/tr[1]"
orders_normalize_space= "//*[normalize-space(text())='نتایج 1 تا 30 از 1353 نتیجه']"

###orders_create

click_orders_create= "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/a[1]"
orders_create_name_select= "//*[@id='chooseservices']/form/div[1]/div/div/div[2]/div/div/span/span[1]"
orders_create_name_select_option= "//*[@id='select2-formuser_id_owner-n1-results']/li"
orders_create_name_select_text= "/html/body/span/span/span[1]/input"
orders_create_check_transport= "//*[@id='transport']"
orders_create_check_clearance="//*[@id='clearance']"
orders_create_chooseservices="//*[@id='chooseservices']/form/div[2]/div/div/button"
orders_create_products_holder="//*[@id='orderproductsholder']/div[3]/a"
orders_create_category_select="//*[@id='formop_category']"
orders_create_category_select_option="//*[@id='formop_category']/option[2]"
orders_create_form_name="//*[@id='formname']"
orders_create_form_name_en="//*[@id='formname_en']"
orders_create_form_type="//*[@id='formop_type']"
orders_create_form_type_option="//*[@id='formop_type']/option[1]"
orders_create_form_quantity="//*[@id='formop_quantity']"
orders_create_form_quantity_option="//*[@id='formop_quantity']/option[2]"
orders_create_form_quantity_number="//*[@id='formquantity']"
orders_create_form_one_weight="//*[@id='formoneweight']"
orders_create_form_length="//*[@id='formlength']"
orders_create_form_width="//*[@id='formwidth']"
orders_create_form_height="//*[@id='formheight']"
orders_create_form_quantity_in_box="//*[@id='formquantity_in_box']"
orders_create_form_price_unit="//*[@id='formpriceunit']"
orders_create_form_price_unit_option="//*[@id='formpriceunit']/option[2]"
orders_create_form_one_price="//*[@id='formoneprice']"
orders_create_form_price="//*[@id='formprice']"
orders_create_HSCODE="/html/body/div[8]/div/div/div/section[2]/div/div/div/div/form/div[20]/div/div/span/span[1]/span/span[2]"
orders_create_HSCODE_option="//*[@id='select2-formhscode-results']/li[2]"
orders_create_form_part_number="//*[@id='formpartnumber']"
orders_create_form_buy_url="//*[@id='formbuy_url']"
orders_create_form_text="//*[@id='formtext']"
orders_create_form_country="//*[@id='formcreate_country']"
orders_create_submit_information="/html/body/div[8]/div/div/div/section[2]/div/div/div/div/form/div[30]/div/button"

###Completion_of_information

orders_create_information_type="//*[@id='formorder_type-n1']"
orders_create_information_type_option="//*[@id='formorder_type-n1']/option[1]"
orders_create_information_transport="//*[@id='formtransport_type-n1']"
orders_create_information_transport_option="//*[@id='formtransport_type-n1']/option[1]"
orders_create_information_senders="//*[@id='formsenders_count-n1']"
orders_create_information_must_pay_before_transport="//*[@id='formmustpaybeforetransport-n1']"
orders_create_information_must_pay_before_transport_option="//*[@id='formmustpaybeforetransport-n1']/option[1]"
orders_create_information_description="//*[@id='formsenders_description-n1']"
orders_create_information_pay_in_china="//*[@id='formpay_in_china-n1']"
orders_create_information_pay_in_china_option="//*[@id='formpay_in_china-n1']/option[1]"
orders_create_information_area_one="//*[@id='formis_areaone-n1']"

###information_sender

# orders_create_information_sender_city="//*[@id='information']/div/div/form/div[2]/div[2]/div[2]/div/a[1]"
orders_create_information_sender_city="//*[@id='information']/div/div/form/div[2]/div[2]/div[1]/div/div/span"
orders_create_information_sender_city_name="/html/body/span/span/span[1]/input"
orders_create_information_sender_city_option="//*[@id='select2-formsender_city-n1-results']/li"
orders_create_information_sender_name_select="//*[@id='select2-formsender_p-n1-container']"
orders_create_information_sender_name="/html/body/span/span/span[1]/input"
orders_create_information_sender_name_option="//*[@id='select2-formsender_p-n1-results']/li"

###information_receiver

orders_create_information_receiver_city="//*[@id='information']/div/div/form/div[3]/div[3]/div[1]/div/div/span"
# orders_create_information_receiver_city="//*[@id='information']/div/div/form/div[3]/div[3]/div[2]/div/a[1]"
orders_create_information_receiver_city_name="/html/body/span/span/span[1]/input"
orders_create_information_receiver_city_option="//*[@id='select2-formreceiver_city-n1-results']/li"
orders_create_information_receiver_name_select="//*[@id='select2-formreceiver_p-n1-container']"
# orders_create_information_receiver_name_select="/html/body/div[1]/div/section[2]/div/div/div/div/div/div/div/form/div[3]/div[4]/div[1]/div[1]/div/div/span/span[1]/span/span[1]"
orders_create_information_receiver_name="/html/body/span/span/span[1]/input"
orders_create_information_receiver_option="//*[@id='select2-formreceiver_p-n1-results']/li"

###factor

orders_create_information_sub_bill="//*[@id='formsubbill-n1']"
orders_create_information_sub_bill_option="//*[@id='formsubbill-n1']/option[1]"
orders_create_information_factor_rasmi_transport="//*[@id='formfactorrasmi_transport-n1']"
orders_create_information_factor_rasmi_transport_option="//*[@id='formfactorrasmi_transport-n1']/option[2]"
orders_create_information_factor_rasmi_clearance="//*[@id='formfactorrasmi_clearance-n1']"
orders_create_information_factor_rasmi_clearance_option="//*[@id='formfactorrasmi_clearance-n1']/option[1]"
orders_create_information_need_clearance_inquery="//*[@id='formneed_clearance_inquery-n1']"
orders_create_information_need_clearance_inquery_option="//*[@id='formneed_clearance_inquery-n1']/option[1]"
orders_create_information_clearance_youan_invoice_request="//*[@id='formclearance_youan_invoice_request-n1']"
orders_create_information_clearance_youan_invoice_request_option="//*[@id='formclearance_youan_invoice_request-n1']/option[1]"
orders_create_information_factor_rasmi="//*[@id='formfactorrasmi-n1']"
orders_create_information_factor_rasmi_option="//*[@id='formfactorrasmi-n1']/option[1]"
orders_create_information_invoice_to_container="//*[@id='select2-forminvoiceto_p-n1-container']"
orders_create_information_invoice_to_container_name="/html/body/span/span/span[1]/input"
orders_create_information_invoice_to_container_option="//*[@id='select2-forminvoiceto_p-n1-results']/li"
orders_create_information_goback="//*[@id='information']/div/div/form/div[6]/div[2]/button"
orders_create_information_approve="//*[@id='information']/div/div/form/div[6]/div[1]/button"

###review

orders_create_next_review="//*[@id='review']/div/div/form/div[34]/div[1]/button"

###check_the_order

click_checking_the_order="//*[@id='main-content-wrapper']/section[2]/div[4]/a"
check_the_order_approved="//*[@id='boxConfirmOrder']/div/div[2]/form/button"

###clearance_inquiry

click_clearance_inquiry="//*[@id='main-content-wrapper']/section[1]/div[2]/div[6]/a"
clearance_inquiry_cargo_clearance="//*[@id='boxclearanceinqueryForm']/div/div[4]/div/div/span"
clearance_inquiry_cargo_clearance_option="//*[@id='select2-formagent-results']/li[1]"
clearance_inquiry_type="//*[@id='formclearance_type']"
clearance_inquiry_type_option="//*[@id='formclearance_type']/option[1]"
clearance_inquiry_Price="//*[@id='formprice']"
clearance_inquiry_Price_unit="//*[@id='formpriceunit']"
clearance_inquiry_comment="//*[@id='formcomment']"
clearance_inquiry_form_save="//*[@id='boxclearanceinqueryForm']/button"

###other_inquiries

click_other_inquiries="//*[@id='main-content-wrapper']/section[1]/div[2]/div[7]/a"
other_inquiries_services_invoice_type="//*[@id='formfactorrasmi']"
other_inquiries_services_invoice_type_option="//*[@id='formfactorrasmi']/option[2]"
other_inquiries_services_invoice_type_update="//*[@id='formotherinquery_type']"
other_inquiries_pre_factor_type="//*[@id='formotherinquery_type']/option[2]"
other_inquiries_price="//*[@id='formprice']"
other_inquiries_price_unit="//*[@id='formpriceunit']"
other_inquiries_price_unit_option="//*[@id='formpriceunit']/option[1]"
other_inquiries_description="//*[@id='formtext']"
other_inquiries_save_submit="//*[@id='fastinvoice']/div/div[2]/form/button"













