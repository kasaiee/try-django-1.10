from rest_framework.permissions import BasePermission, SAFE_METHODS
# SAFE_METHODS contains 
# (u'GET', u'HEAD', u'OPTIONS')

class OwnerCanManageOrReadOnly(BasePermission):
    message = ''

    # This function called sooner than has_object_permission
    # It is check general permission on view level
    def has_permission(self, request, view):
        self.message = 'Your request does not have permission or you are is not the post owner!'
        if request.method in SAFE_METHODS:
            return True
        return False


    # It is check general permission on object level
    def has_object_permission(self, request, view, obj):
        self.message = 'You must be the owner of this object!'
        return request.user == obj.owner