from django.shortcuts import render,redirect

from django.views import View
from .models import Topic

class BbsView(View):

    def get(self, request, *args, **kwargs):

        #読み込み処理
        data    = Topic.objects.all()
        context = { "data":data }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        #書き込み処理
        posted  = Topic( comment = request.POST["comment"] )
        #書き込み確定
        posted.save()

        #読み込み処理
        """
        data    = Topic.objects.all()
        context = { "data":data }
        """

        #return render(request,"bbs/index.html",context)
        return redirect("bbs:index")

index   = BbsView.as_view()

