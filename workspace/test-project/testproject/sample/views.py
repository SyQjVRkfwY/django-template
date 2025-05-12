from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
 
def get_sample(request):
    if "manual_id" not in request.GET or "user_name" not in request.GET:
        # query_paramが指定されていない場合の処理
        return HttpResponseBadRequest("parameter not in request")
    
    context = {
        "manual_id": request.GET.get("manual_id"),
        "user_name": request.GET.get("user_name"),
    }

    print(context)

    template = loader.get_template("sample/sample.html")
    return HttpResponse(template.render(context, request))