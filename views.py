from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from project.models import Supplier,User,Medicine,Order
from project.serialize import SupplierSerializer,UserSerializer,MedicineSerializer,OrderSerializer

import datetime

@api_view(['GET', 'POST', 'DELETE'])
def supplier_list(request):
    if request.method == 'GET':
        docs = Supplier.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            docs = docs.filter(name__icontains=name)
        
        supplier_serializer = SupplierSerializer(docs, many=True)
        return JsonResponse(supplier_serializer.data, safe=False)

    elif request.method == 'POST':
        sup_data = JSONParser().parse(request)
        supplier_serializer = SupplierSerializer(data=sup_data)
        if supplier_serializer.is_valid():
            supplier_serializer.save()
            return JsonResponse(supplier_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(supplier_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Supplier.objects.all().delete()
        return JsonResponse({'message': '{} Documents were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def supplier_detail(request, pk):
    try: 
        doc = Supplier.objects.get(pk=pk)
        if request.method == 'GET': 
            supplier_serializer = SupplierSerializer(doc) 
            return JsonResponse(supplier_serializer.data) 

        elif request.method == 'PUT': 
            doc_data = JSONParser().parse(request) 
            supplier_serializer = SupplierSerializer(doc, data=doc_data) 
            if supplier_serializer.is_valid(): 
                supplier_serializer.save() 
                return JsonResponse(supplier_serializer.data) 
            return JsonResponse(supplier_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        elif request.method == 'DELETE': 
            doc.delete() 
            return JsonResponse({'message': 'Document was deleted successfully!'})
  
    except Supplier.DoesNotExist: 
        return JsonResponse({'message': 'The document does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        docs = User.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            docs = docs.filter(name__icontains=name)
        
        user_serializer = UserSerializer(docs, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Documents were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try: 
        doc = User.objects.get(pk=pk)
        if request.method == 'GET': 
            user_serializer = UserSerializer(doc) 
            return JsonResponse(user_serializer.data) 

        elif request.method == 'PUT': 
            doc_data = JSONParser().parse(request) 
            user_serializer = UserSerializer(doc, data=doc_data) 
            if user_serializer.is_valid(): 
                user_serializer.save() 
                return JsonResponse(user_serializer.data) 
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        elif request.method == 'DELETE': 
            doc.delete() 
            return JsonResponse({'message': 'Document was deleted successfully!'})
  
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The document does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'DELETE'])
def medicine_list(request):
    if request.method == 'GET':
        docs = Medicine.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            docs = docs.filter(name__icontains=name)
        
        medicine_serializer = MedicineSerializer(docs, many=True)
        return JsonResponse(medicine_serializer.data, safe=False)

    elif request.method == 'POST':
        medicine_data = JSONParser().parse(request)
        medicine_serializer = MedicineSerializer(data=medicine_data)
        if medicine_serializer.is_valid():
            medicine_serializer.save()
            return JsonResponse(medicine_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(medicine_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Medicine.objects.all().delete()
        return JsonResponse({'message': '{} Documents were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def medicine_detail(request, pk):
    try: 
        doc = Medicine.objects.get(pk=pk)
        if request.method == 'GET': 
            medicine_serializer = MedicineSerializer(doc) 
            return JsonResponse(medicine_serializer.data) 

        elif request.method == 'PUT': 
            doc_data = JSONParser().parse(request) 
            medicine_serializer = MedicineSerializer(doc, data=doc_data) 
            if medicine_serializer.is_valid(): 
                medicine_serializer.save() 
                return JsonResponse(medicine_serializer.data) 
            return JsonResponse(medicine_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        elif request.method == 'DELETE': 
            doc.delete() 
            return JsonResponse({'message': 'Document was deleted successfully!'})
  
    except Medicine.DoesNotExist:
        return JsonResponse({'message': 'The document does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'DELETE'])
def order_list(request):
    if request.method == 'GET':
        docs = Order.objects.all()
        order_serializer = OrderSerializer(docs, many=True)
        return JsonResponse(order_serializer.data, safe=False)

    elif request.method == 'POST':
        ord_data = JSONParser().parse(request)
        medid=ord_data['medId']
        quantity=ord_data['quantity']
        doc = Medicine.objects.get(pk=medid)
        price=quantity*doc.price
        ord_data['price']=price
        order_serializer = OrderSerializer(data=ord_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse(order_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Order.objects.all().delete()
        return JsonResponse({'message': '{} Documents were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try: 
        doc = Order.objects.get(pk=pk)
        if request.method == 'GET': 
            order_serializer = OrderSerializer(doc) 
            return JsonResponse(order_serializer.data) 

        elif request.method == 'PUT': 
            doc_data = JSONParser().parse(request) 
            order_serializer = OrderSerializer(doc, data=doc_data) 
            if order_serializer.is_valid(): 
                order_serializer.save() 
                return JsonResponse(order_serializer.data) 
            return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        elif request.method == 'DELETE': 
            doc.delete() 
            return JsonResponse({'message': 'Document was deleted successfully!'})
  
    except Order.DoesNotExist: 
        return JsonResponse({'message': 'The document does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def medicine_search(request):
    docs=Medicine.objects.all()
    med_data = JSONParser().parse(request)
    key = med_data['key']
    value = med_data['value']
    if key=='name':
        docs=docs.filter(name__icontains=value)
        if len(docs):
            medicine_serializer = MedicineSerializer(docs, many=True)
            return JsonResponse(medicine_serializer.data, safe=False)
        else:
            return JsonResponse({"message":"List is empty"})

    elif key=='category':
        docs=docs.filter(category__icontains=value)
        if len(docs):
            medicine_serializer = MedicineSerializer(docs, many=True)
            return JsonResponse(medicine_serializer.data, safe=False)
        else:
            return JsonResponse({"message":"List is empty"})

    elif key=='content':
        docs=docs.filter(content__icontains=value)
        if len(docs) >0:
            medicine_serializer = MedicineSerializer(docs, many=True)
            return JsonResponse(medicine_serializer.data, safe=False)
        else:
            return JsonResponse({"message":"List is empty"})

    elif key=='expDate':
        docs = Medicine.objects.all()
        l=[]
        try:
            value=datetime.datetime.strptime(value,"%Y-%m-%d").date()
        except:
            return JsonResponse({"message":"Invalid date"})
        for doc in docs:
            if doc.expDate < value:
                l.append(doc)
        if len(l)>0:
            medicine_serializer = MedicineSerializer(l, many=True)
            return JsonResponse(medicine_serializer.data, safe=False)
        else:
            return JsonResponse({"message":"List is empty"})

    elif key=='stock':
        docs = Medicine.objects.all()
        l=[]
        for doc in docs:
            if doc.stock < value:
                l.append(doc)
        if len(l)>0:
            medicine_serializer = MedicineSerializer(l, many=True)
            return JsonResponse(medicine_serializer.data, safe=False)
        else:
            return JsonResponse({"message":"List is empty"})

    elif key=='supplier_id':
        docs=docs.filter(supplier=int(value))
        if len(docs) >0:
            medicine_serializer = MedicineSerializer(docs, many=True)
            return JsonResponse(medicine_serializer.data, safe=False)
        else:
            return JsonResponse({"message":"No medicines were supplied by this supplier"})

    elif key=='supplier_name':
        docs1=Supplier.objects.filter(name__icontains=value)
        sid=docs1[0].id
        docs=docs.filter(supplier=sid)
        if len(docs)>0:
            medicine_serializer = MedicineSerializer(docs, many=True)
            return JsonResponse(medicine_serializer.data, safe=False)
        else:
            return JsonResponse({"message":"There are no medicines supplied by {}".format(value)})

    else:
        return JsonResponse({"message":"key not crt"})

@api_view(['POST'])
def medicine_search_all(request):
    med_data = JSONParser().parse(request)
    value = med_data['value']
    docs = Medicine.objects.all()
    docs1 = docs.filter(name__icontains=value)
    docs2 = docs.filter(content__icontains=value)
    docs3 = docs.filter(category__icontains=value)
    docs = docs1 | docs2 | docs3 
    docs = docs.distinct()
    if len(docs)==0:
        return JsonResponse({"message":"No data found"})
    medicine_serializer = MedicineSerializer(docs, many=True)
    return JsonResponse(medicine_serializer.data, safe=False)

@api_view(['POST'])
def order_search(request):
    docs = Order.objects.all()
    ord_data = JSONParser().parse(request)
    key = ord_data['key']
    value = ord_data['value']
    if key=="ordDate":
        docs = Order.objects.all()
        l=[]
        value=datetime.datetime.strptime(value,"%Y-%m-%d").date()
        for doc in docs:
            if doc.ordDate == value:
                l.append(doc)
        if len(l)>0:
            order_serializer = OrderSerializer(l, many=True)
            return JsonResponse(order_serializer.data, safe=False)
        else:
            return JsonResponse({"message":"No orders were placed on this date"})

    elif key=='medId':
        meds = Medicine.objects.all()
        value = int (value)
        f=0
        for med in meds:
            if value == med.id:
                f=1
                break
        if f==0:
            return JsonResponse({"message":"Invalid medicine id, there is no medicine with th given id"})
        
        docs = Order.objects.all()
        l=[]
        for doc in docs:
            if doc.medId_id==value:
                l.append(doc)
        if len(l)>0:
            order_serializer = OrderSerializer(l, many=True)
            return JsonResponse(order_serializer.data, safe=False)
        else:
            return JsonResponse({"message":"No orders were placed on this medicine"})

    elif key=='userId':
        usrs = User.objects.all()
        value=int(value)
        f=0
        for usr in usrs:
            if value == usr.id:
                f=1
                break
        if f==0:
            return JsonResponse({"message":"User does not exist"})
        
        docs = Order.objects.all()
        l=[]
        for doc in docs:
            if doc.userId_id==value:
                l.append(doc)
        if len(l)>0:
            order_serializer = OrderSerializer(l, many=True)
            return JsonResponse(order_serializer.data, safe=False)
        else:
            return JsonResponse({"message":"No orders were placed by this user"})

    elif key=='userName':
        docs1=User.objects.filter(name__icontains=value)
        if len(docs1)==0:
            return JsonResponse({"message":"User not found"})
        uid=docs1[0].id
        docs=docs.filter(userId=uid)
        if len(docs)>0:
            order_serializer = OrderSerializer(docs, many=True)
            return JsonResponse(order_serializer.data, safe=False)
        else:
            return JsonResponse({"message":"No orders were placed by this user"})

    elif key=='medName':
        docs1=Medicine.objects.filter(name__icontains=value)
        if len(docs1)==0:
            return JsonResponse({"message":"medicine not found"})

        mid=docs1[0].id
        docs=docs.filter(medId=mid)
        if len(docs)>0:
            order_serializer = OrderSerializer(docs, many=True)
            return JsonResponse(order_serializer.data, safe=False)
        else:
            return JsonResponse({"message":"No orders were placed on this medicine"})

    elif key=='price':
        op=ord_data['op']
        docs = Order.objects.all()
        l=[]
        if op=='above':
            for doc in docs:
                if doc.price > value:
                    l.append(doc)
            if len(l)>0:
                order_serializer = OrderSerializer(l, many=True)
                return JsonResponse(order_serializer.data, safe=False)
            else:
                return JsonResponse({"message":"There are no orders above {}".format(value)})
        
        elif op=='below':
            for doc in docs:
                if doc.price < value:
                    l.append(doc)
            if len(l)>0:
                order_serializer = OrderSerializer(l, many=True)
                return JsonResponse(order_serializer.data, safe=False)
            else:
                return JsonResponse({"message":"There are no orders below {}".format(value)})
        
        else:
            return JsonResponse({"message":"Invalid operation"})
    else:
        return JsonResponse({"message":"Key not correct"})
