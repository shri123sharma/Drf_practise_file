from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart.views import *
from rest_framework.routers import DefaultRouter,SimpleRouter
from .import views

app_name='quickstart'

router=DefaultRouter()

# router.register('entryset',views.EntryViewSet,basename='entryview')
# router.register('entryset1',views.EntryViewSet_1,basename='entryset1')
# router.register('entryset',EntryViewSet,basename='entryset')
# router.register('authorviewset',AuthorViewSet,basename='authorviewset')
# router.register('blogviewset',BlogViewSet,basename='blogviewset')
router.register('itemviewset',ItemsViewset,basename='itemviewset')
router.register('itemviewset1/',ItemsViewset1,basename='itemviewset1')



urlpatterns = [
    path('as',include(router.urls)),
    # path('sniserializer/',views.snippetserializer_1,name='sniserializer'),
    # path('sniserializer1/',views.snippet_list,name='sniserializer1'),
    # path('snippet_list/',views.snippet_list,name='snippetlist'),
    # path('snippet_detail/<int:pk>/',views.snippet_detail,name='snippetdetail'),
    # path('snippet_list_1/',views.snippet_list_1,name='snippetlist1'),
    # path('snippet_class_list/',views.Snippetclasslist.as_view(),name='snippetclasslist'),
    # path('snippet_class_detail/<int:pk>/',views.Snippetclassdetail.as_view(),name='snippetclassdetail'),
    # path('snippet_class_list_1/',views.Snippetsclasslist_1.as_view(),name='snippetclasslist1'),
    # path('snippet_class_detail_1/',views.Snippetclassdetail_1.as_view(),name='snippetclassdetail1'),
    # path('blogserialzerfun/<int:pk>/',views.blog_serialzer_fun,name='blogserialzerfun'),
    # path('userlist/',views.SnippetListSerializerView.as_view(),name='userlist'),
    # path('userdetail/<int:pk>/',views.SnippetDetailSerializerView.as_view(),name='userdetail')
    # path('snippethighlight/<int:pk>/',views.SnippetHightlight.as_view(),name='snippethighlight')
    # path('entryserializer/',views.entryseralizer,name='entryserializer'),
    # path('entrylistview/',views.EntryListView.as_view(),name='entrylistview'),
    # path('fun1/',views.fun_1,name='fun1'),
    # path('helloworld/',views.hello_world,name='helloworld'),
    # path('onceperdayuser/',views.OncePerDayUserThrottle,name='onceperdayuser'),
    # path('customautosechema/',views.CustomAutoScehma,name='customautosechema'),
    # path('entrylist/',views.EntryList.as_view(),name='entrylist'),
    # path('entrydetail/<int:pk>/',views.EntryDetail.as_view(),name='entrydetail'),
    # path('bloglist/',views.BlogList.as_view(),name='bloglist'),
    # path('blogview/',views.BlogView.as_view(),name='blogview'),
    # path('blogview_1/<int:pk>/',views.BlogView_1.as_view(),name='blogview_1'),
    # path('authorview/<int:pk>/',views.AuthorView.as_view(),name='authorview'),
    # path('authorview1/<int:pk>/',views.AuthorView_1.as_view(),name='authorview1'),
    # path('itemlist/',views.ItemsList.as_view(),name='itemlist'),
    # path('itemsdetail/<int:pk>/',views.ItemsDetail.as_view(),name='itemsdetail'),
    # path('exampleview/',views.ExampleView.as_view(),name='exampleview'),
    # path('demoview/',views.DemoView.as_view(),name='demoview'),
    # path('demoview1/<int:pk>/',views.DemoView_1.as_view(),name='demoview1'),
    # path('publisherview/',views.PublisherView.as_view(),name='publisherview'),
    # path('contactfrom/',views.ContactFormView.as_view(),name='contactfrom'),
    # path('collage/',views.CollageView.as_view(),name='collage'),
    # path('departmentview/',views.DepartmentSeralizerView.as_view(),name='departmentview')
    # path('collageserializer/',views.CollageSerializerView.as_view(),name='collageserializer'),
    path('publisher/',views.publisher_view,name='publisher'),
    path('albumview/',views.AlbumSerializerView.as_view(),name='albumview')
    
]


