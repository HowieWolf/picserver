from django.urls import path

from client.appeal.judgement import JudgeAppeal
from client.appeal.list_detail import MyAppealList, MyJudgeAppealList, AppealDetail

urlpatterns = [
    # 我提出申诉列表
    path('my/', MyAppealList.as_view()),
    # 我评审的申诉列表
    path('judge/', MyJudgeAppealList.as_view()),
    # 申诉详情
    path('<int:appeal_id>/', AppealDetail.as_view()),
    # 评审
    path('<int:appeal_id>/judge/', JudgeAppeal.as_view()),
]
