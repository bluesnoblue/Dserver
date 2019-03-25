# from rest_framework.views import APIView
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Question,Choice
from .serializers import QuestionSerializer,ChoiceSerializer

class QuestionList(generics.ListCreateAPIView):
    # def get(self,request):
    #     polls = Question.objects.all()[:20]  # 从Poll模型对应的表中取出所有记录，并切片前20条记录。这是一个QuerySet类的实例，其中包含了如何取数的信息。
    #     serialized = QuestionSerializer(polls, many=True)  # 利用QuerySet实例化一个序列化器。many=True表示，这是对多条记录的请求。
    #     return Response(serialized.data)  # serialized.data是一个有序字典对象
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    # def get(self, request, pk):
    #     poll = get_object_or_404(Question, pk=pk)  # get_object_or_404要么取回记录实例要么返回404 Not Found状态
    #     serialized = QuestionSerializer(poll)  # 序列化这个记录实例
    #     return Response(data=serialized.data)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceList(generics.ListCreateAPIView):
    name = 'choice_list'

    def get_queryset(self):
        queryset = Choice.objects.filter(question_id=self.kwargs['pk'])
        return queryset

    serializer_class = ChoiceSerializer

