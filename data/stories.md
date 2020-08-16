## thank
* thank
  - utter_noworries

## goodbye
* bye
  - utter_bye

## Some question from FAQ
* faq
    - respond_faq

## just sales, continue
* contact_sales
    - patient_appointment
    - form{"name": "patient_appointment"}
* faq
    - respond_faq
    - patient_appointment
    - form{"name": null}

## patient appointment
* schedule_meeting
    - patient_appointment                   <!--Run the sales_form action-->
    - form{"name": "patient_appointment"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->

* out_of_scope
  utter_out_of_scope
