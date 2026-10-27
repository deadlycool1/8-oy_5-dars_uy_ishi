from rest_framework.routers import DefaultRouter
from .views import JanrViewSet, BookViewSet

router = DefaultRouter()

router.register("genres", JanrViewSet, basename="genre")
router.register("books", BookViewSet, basename="book")

urlpatterns = router.urls
