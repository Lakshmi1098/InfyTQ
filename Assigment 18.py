#PF-Tryout

def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    if(current_currency_name=="Euro"):
        currency_needed=amount_needed_inr*0.01417
    elif(current_currency_name=="British Pound"):
       currency_needed=amount_needed_inr*0.0100
    elif(current_currency_name=="Australian Dollar"):
        currency_needed=amount_needed_inr*0.02140
    elif(current_currency_name=="Canadian Dollar"):
        currency_needed=amount_needed_inr*0.02027
    else:
        currency_needed=-1
    return currency_needed

print(convert_currency(3500,"British Pound"))


        
  


