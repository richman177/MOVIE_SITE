from  rest_framework import permissions


class CheckStatus(permissions.BasePermission):
    def hes_object_permission(self, request, view, obj):
        if request.user.status == 'simple' and obj.movie_status == 'simple':
            return True
        elif request.user.status == 'pro':
            return True
        return False


class CheckAuthorHistory(permissions.BasePermission):
    def hes_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False



class CheckStatusActor(permissions.BasePermission):
    def hes_permission(self, request, view):
        if request.user.status == 'pro':
            return True
        return False
