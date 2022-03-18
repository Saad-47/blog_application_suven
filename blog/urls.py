from django.urls import	path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name	=	'blog'
urlpatterns	=	[
	path("", views.PostListView.as_view(), name='post_list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/',
									views.post_detail,
									name='post_detail'),
    path('<int:post_id>/share/',views.post_share,
                                name='post_share'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
