from django.urls import path

from cms.contract.upload import UploadedContractList, UploadedContractAction, DeployContract

urlpatterns = [
    path('', UploadedContractList.as_view()),
    path('<int:contract_id>/', UploadedContractAction.as_view()),
    path('<int:contract_id>/deploy/', DeployContract.as_view()),
]
