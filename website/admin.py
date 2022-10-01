from django.contrib import admin

from website.models import Account,Orders,OrderDetails,Stores,StoreMenu,OffersCarousel

# Register your models here.

admin.site.site_header = "DoiNk Shippers Database"
admin.site.register(Account)
admin.site.register(Orders)
admin.site.register(OrderDetails)
admin.site.register(Stores)
admin.site.register(StoreMenu)
admin.site.register(OffersCarousel)