from rest_framework import generics
from rest_framework.response import Response


class ContentList(generics.ListAPIView):
    queryset = None
    serializer_class = None

    def get(self, request, *args, **kwargs):
        user = request.user.user_id
        # user = "fake"
        print(user)
        return super().get(request, *args, **kwargs)

    def list(self, request, *args, **kwargs) -> Response:
        user = request.user.user_id
        # user = "fake"
        print(user)
        return Response({"user": user})
