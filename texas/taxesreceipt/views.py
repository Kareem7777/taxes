from django.shortcuts import render
from .models import *
# Create your views here.

def receipt(request) :
    a1=customer.objects.all()
    a2=invoice_result.objects.all()
    a3=invoice_line.objects.all()
    a4=invoice.objects.all()    
    for cust in a1:
        inv = invoice.objects.filter(customer_id = cust.id)
        for kkk in inv:
            sel = invoice_result.objects.filter(invoice_id = kkk.internal_id)
        
    my_list = zip(a1,inv,sel)
    return render(request,'receipts.html',{'a1':a1,'a2':a2,'a3':a3,'a4':a4,'list':my_list})

def errorreport(request) :
    a1=customer.objects.all()
    a2=invoice_result.objects.filter(state = 80)
    a3=invoice_line.objects.all()
    a4=invoice.objects.all()    


    return render(request,'sendingreport.html',{'a1':a1,'a2':a2,'a3':a3,'a4':a4})
