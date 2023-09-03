from django.urls import path

from .views import SignUpView, AccountDetail, AccountList

urlpatterns = [
    path("", AccountList.as_view(), name="account_list"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("<int:pk>/", AccountDetail.as_view(), name="acoount_datail"),

]
