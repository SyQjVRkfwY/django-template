from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from .constants.constants import Constants


def get_sample(request):
    context = convert_request_to_context(request)

    if not context:
        return HttpResponseBadRequest("parameter has error.")

    template = loader.get_template("sample/sample.html")
    return HttpResponse(template.render(context, request))


def get_sample_description (request):
    context = convert_request_to_context(request)

    if not context:
        return HttpResponseBadRequest("parameter has error.")

    template = loader.get_template("sample/sample_description.html")
    return HttpResponse(template.render(context, request))


def get_sample_image (request):
    context = convert_request_to_context(request)

    if not context:
        return HttpResponseBadRequest("parameter has error.")

    template = loader.get_template("sample/sample_image.html")
    return HttpResponse(template.render(context, request))


def get_sample_audio (request): 
    context = convert_request_to_context(request)
    print(context)

    if not context:
        return HttpResponseBadRequest("parameter has error.")

    template = loader.get_template("sample/sample_audio.html")
    return HttpResponse(template.render(context, request))


def convert_request_to_context(request):
    """_summary_

    Args:
        request (HttpRequest): 

    Returns:
        dict: パラメータの辞書。 パラメータに異常がある場合はNone
    """
    # マニュアルIDの取得
    if "manual_id" in request.GET:
        manual_id = request.GET.get("manual_id")
    else:
        manual_id = Constants.DEFAULT_MANUAL_ID
    
    # ユーザ名の取得
    if "user_name" in request.GET:
        user_name = request.GET.get("user_name")
    else:
        user_name = Constants.DEFAULT_USER_NAME

    return  {
        "manual_id": manual_id,
        "user_name": user_name,
    }