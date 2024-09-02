from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """
    Пользовательское разрешение для предоставления доступа на чтение всем,
    но разрешения на редактирование только автору объекта.
    """

    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        """Проверяет разрешение на выполнение действия с объектом."""

        return request.method in SAFE_METHODS or obj.author == request.user
