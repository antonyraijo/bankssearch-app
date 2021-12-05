from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.serializers import ValidationError

from bankapp.models import Banks, Branches
from bankapp.serializers import BranchesSerializer


class CustomPagination(LimitOffsetPagination):
    default_limit = 100
    max_limit = 10000
    min_limit = 1
    min_offset = 1
    max_offset = 10000

    def paginate_queryset(self, queryset, request, view=None):
        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')

        if limit:
            limit = int(limit)
            if limit > self.max_limit:
                raise ValidationError({"limit" : ["Limit should be less than or equal to {0}".format(self.max_limit)]})
            elif limit < self.min_limit:
                raise ValidationError({"limit" : ["Limit should be greater than or equal to {0}".format(self.min_limit)]})
        if offset:
            offset = int(offset)
            if offset > self.max_offset:
                raise ValidationError({"offset" : ["Offset should be less than or equal to {0}".format(self.max_offset)]})
            elif offset < self.min_offset:
                raise ValidationError({"offset" : ["Offset should be greater than or equal to {0}".format(self.min_offset)]})

        return super(self.__class__, self).paginate_queryset(queryset, request, view)


class BankDataView(ModelViewSet):
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    serializer_class = BranchesSerializer
    queryset = Branches.objects.all()
    http_method_names = ['get']

    def list(self, request):
        bank_name = request.GET.get('bank_name', None)
        city = request.GET.get('city', None)
        if bank_name and city:
            self.queryset = self.queryset.filter(bank_id__name=bank_name, city=city)
        else:
            raise ValidationError({"error": "bank name and city parameters required"})

        return super(BankDataView, self).list(request)


class BankDataDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            branch = Branches.objects.get(ifsc=pk)
        except Branches.DoesNotExist:
            raise ValidationError({"error": "Branch doesn't exist in this ifsc"})
        return Response(BranchesSerializer(branch, read_only=True).data)