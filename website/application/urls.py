from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about, name='about'),
    path('category/<slug:value>', views.CategoryView.as_view(), name='category'),
    path("category-title/<value>", views.CategoryTitle.as_view(), name='category-title'),
    path('parent-category/<slug:value>', views.ParentCategoryView.as_view(), name='parent-category'),
    path("parent-category-title/<value>", views.ParentCategoryTitle.as_view(), name='parent-category-title'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),
    path('delete_address/<int:pk>', views.delete_address, name='deleteAddress'),


    path('checkout/', views.checkout.as_view(), name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('orders/', views.orders, name='orders'),
    path('search/',views.search, name='search'),
    path('wishlist/', views.show_wishlist, name='showwishlist'),


    path('pluswishlist/', views.plus_wishlist),
    path('minuswishlist/', views.minus_wishlist),
    path('deletewishlist/', views.delete_wishlist),

    #login authentification
    path('registration/', views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login', auth_view.LoginView.as_view(template_name='application/login.html',
        authentication_form=LoginForm), name='login'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='application/changepassword.html',
        form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeView.as_view
        (template_name='application/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    #password reset
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='application/changepassword.html',
        form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='application/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='application/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='application/password_reset_complete.html'), name='password_reset_complete'),
    path('blog/', include('blog.urls')),
    path('', include('cart.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Tea & Cofee Shop"
admin.site.site_title = "Tea & Cofee Shop"
admin.site.site_index_title = "Welcome to Tea & Cofee Shop"