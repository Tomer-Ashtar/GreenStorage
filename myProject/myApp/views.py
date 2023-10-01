import datetime
from django.shortcuts import render, redirect
from .models import Customer, workers, SalesHistory,Equipment ,type_of_customer
from django.http import HttpResponse

def home(request):
    equipment_entries = Equipment.objects.all()
    return render(request, 'home.html',{'equipment_entries': equipment_entries})

def add_customer(request):
    equipment_entries = Equipment.objects.all()
    if request.method == 'POST':
        # Get the form data from the POST request
        date=request.POST.get('date')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        customer_id = request.POST.get('customer_id')
        mail= request.POST.get('mail')
        phone = request.POST.get('phone')
        customer_type = request.POST.get('customer_type')
        
        # Get other form data

        # Create a new Customer instance
        customer = Customer(
            date=date,
            mail=mail, 
            phone =phone,
            customer_type = customer_type,
            product_table ={"empty":"0"},
            totalbuys=0,
            fname=fname,
            lname=lname,
            customer_id=customer_id,
            # Set other fields
        )

        # Save the customer instance to the database
        customer.save()
        return render(request, 'add_customer_success.html',{'equipment_entries': equipment_entries})
    return render(request, 'add_customer.html',{'equipment_entries': equipment_entries})

def print_customers(request):
    customers = Customer.objects.all()
    equipment_entries = Equipment.objects.all()
    
    return render(request, 'customers.html', {'customers': customers, 'equipment_entries': equipment_entries,'type_of_customer':type_of_customer})


def print_workers(request):
    # Retrieve all workers from the database
    equipment_entries = Equipment.objects.all()
    workers_list = workers.objects.all()

    return render(request, 'workers.html', {'workers': workers_list,'equipment_entries': equipment_entries})


def print_history(request):
    workers_entries= workers.objects.all()
    equipment_entries = Equipment.objects.all() 
    sales_history_entries = list(SalesHistory.objects.all())
    customers_entries= Customer.objects.all()
    return render(request, 'History.html', {'sales_history': sales_history_entries,
    'equipment_entries': equipment_entries,
    'workers_entries':workers_entries,
    'customers_entries':customers_entries,
    })


def add_buy(request):
    equipment_entries = Equipment.objects.all()  # Retrieve all equipment entries
    customers_entries=Customer.objects.all()
    worker_entries= workers.objects.all()
    price=0
    final_prize=0
    original_cost=0
    sum_costs=0
    prof=0
    if request.method == 'POST':
        fname = request.POST.get('name_fill')
        lname = request.POST.get('lname')
        customer_id = request.POST.get('customer_id')
        customer_type= request.POST.get('customer_type')
        sales_man= request.POST.get('sales_man')
        date = request.POST.get('date')
        discount = request.POST.get('discount')
        products = request.POST.getlist('products')  # Get the list of selected products
        quantities = request.POST.getlist('quantities')  # Get the list of corresponding quantities
        
        product_table = {}  # Dictionary to store products and quantities
        price_table={}      # Dictionary to store products and quantities

        for product, quantity in zip(products, quantities):
            equipment = Equipment.objects.get(product_type=product)
            if equipment.origin_product=='0':#if this is independent product
                equipment.current_stock -= int(quantity)  # Decrease the stock by the specified quantity
                original_cost=equipment.cost
                equipment.save()
            else:
                equipment_origin=Equipment.objects.get(product_type=equipment.origin_product)
                equipment_origin.current_stock-= int(quantity) * int(equipment.package)
                original_cost=equipment_origin.cost* int(equipment.package)
                equipment_origin.save()
            product_table[product] = int(quantity)  # Add product and its quantity to the dictionary
            if customer_type=='private':price=equipment.price_for_private
            else:price=equipment.price_for_drivers

            price_table[product]= price
            final_prize=final_prize+(int(quantity)*price)
            sum_costs=sum_costs+(int(quantity)*original_cost)
        final_prize=final_prize-float(discount)
        final_prize=round(final_prize, 2)
        customer_type=update_return_total_buys(customer_id,customer_type,final_prize,customer_type)#updating the sum of money the client spent overall, and updating his type
        prof= final_prize-sum_costs
        prof=round(prof,2)
        # Create a new sales history entry with the product_table dictionary
        sales_history_entry = SalesHistory(
            price=price_table,
            final_prize=final_prize,
            fname=fname,
            lname=lname,
            customer_id=customer_id,
            customer_type=customer_type,
            sales_man=sales_man,
            date=date,
            product_table=product_table,
            profit=prof
            
        )
        sales_history_entry.save()
        update_seller(sales_man, final_prize, customer_type)

        return render(request, 'success.html', {
            'fname': fname,
            'lname': lname,
            'product_table': product_table,
            'date': date
        })

    return render(request, 'add_buy.html', {'equipment_entries': equipment_entries,'worker_entries':worker_entries,
    'final_prize':final_prize,'customers_entries':customers_entries})

def update_seller(sales_man, final_prize, customer_type):
    current_month = datetime.datetime.now().month
    month=get_month_string(current_month)     
    worker = workers.objects.get(fname=sales_man)
    if customer_type == 'new':
      worker.new_customer[month]=worker.new_customer[month]+1
    worker.sum_of_sales[month]=worker.sum_of_sales[month]+final_prize
    worker.save()


def update_return_total_buys(_id, type, final_prize,Ctype):
    try:
        customer = Customer.objects.get(customer_id=_id,)
        if customer.customer_type == 'new' and customer.totalbuys > 0:
            customer.customer_type = 'return'
            type = 'return'
        customer.totalbuys = customer.totalbuys + final_prize
        customer.save()
        return type
    except Customer.DoesNotExist:
        return Ctype

def add_product(request):
    equipment_entries = Equipment.objects.all() 
    if request.method == 'POST':
        product_type = request.POST.get('product_type').strip()  # Remove leading/trailing whitespaces
        price_for_private = request.POST.get('price_for_private')
        price_for_drivers = request.POST.get('price_for_drivers')
        over_all_stock = request.POST.get('over_all_stock')
        cost=request.POST.get('cost')
        notice=request.POST.get('notice')
        origin_product=request.POST.get('origin_product')
        package=request.POST.get('package')
        # Check if the product type already exists in the product table
        try:
            product = Equipment.objects.get(product_type__iexact=product_type)  # Case-insensitive comparison
            # Product exists, update the price and stock
            product.price_for_private = price_for_private
            product.price_for_drivers = price_for_drivers
            product.current_stock = over_all_stock
            product.cost=cost
            product.notice=notice
            product.origin_product=origin_product
            product.package=package
            product.save()
        except Equipment.DoesNotExist:
            # Product does not exist, create a new entry
            product = Equipment(
                product_type=product_type,
                price_for_private=price_for_private,
                price_for_drivers=price_for_drivers,
                over_all_stock=over_all_stock,
                current_stock=over_all_stock,
                cost=cost,
                notice=notice,
                origin_product=origin_product,
                package=package
            )
            product.save()
        return render(request, 'add_product_success.html',{'equipment_entries': equipment_entries})

    return render(request, 'add_product.html',{'equipment_entries': equipment_entries})

def get_month_string(month):
    month_mapping = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sept",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    return month_mapping.get(month, "Invalid Month")

def print_product(request):
    equipment_entries = Equipment.objects.all()
    return render(request, 'print_product.html', {'equipment_entries': equipment_entries})


