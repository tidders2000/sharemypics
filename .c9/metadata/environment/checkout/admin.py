{"filter":false,"title":"admin.py","tooltip":"/checkout/admin.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":1,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["","# Register your models here.",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":12,"column":38},"action":"insert","lines":["","from django.contrib import admin","from .models import Order, OrderLineItem","","# Register your models here.","","class OrderLineAdminInline(admin.TabularInline):","    model = OrderLineItem","    ","class OrderAdmin (admin.ModelAdmin):","    inlines = (OrderLineAdminInline, )","admin.site.register(Order, OrderAdmin)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":38},"end":{"row":12,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564732790711,"hash":"59ed3deb81736012810fcf84adbd0c10c3ad128d"}