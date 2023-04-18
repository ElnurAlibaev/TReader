from rest_framework.routers import DefaultRouter

from books import views


router = DefaultRouter()
router.register(r'books', views.BookViewSet1, basename='books')

urlpatterns = router.urls