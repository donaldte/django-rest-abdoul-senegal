from rest_framework.permissions import BasePermission


class AuthorPermission(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if obj.author:
                if obj.author == request.user:
                    return True 
            elif request.user.is_superuser:
                return True    
        return False    
                
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.has_perms(['add_category']):
                return True
        return False