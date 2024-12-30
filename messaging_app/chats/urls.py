from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import ConversationViewSet, MessageViewSet

# Create the main router and register the ConversationViewSet
router = DefaultRouter()
router.register(r'conversations', ConversationViewSet)

# Create a nested router for messages under conversations
nested_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# Include the router URLs
urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
