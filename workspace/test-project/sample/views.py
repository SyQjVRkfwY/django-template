from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from .constants.constants import Constants
from urllib.parse import urljoin, urlparse



def get_sample(request):
    context = convert_request_to_context(request)
    context["current"] = "/sample?manual_id=" + context["manual_id"]
    context["next"] = request.path.rstrip('/') + "/description?manual_id=" + context["manual_id"]
    print(context)

    if not context:
        return HttpResponseBadRequest("parameter has error.")

    template = loader.get_template("sample/sample.html")
    return HttpResponse(template.render(context, request))


def get_sample_description (request):
    context = convert_request_to_context(request)
    context["current"] = "/sample/description?manual_id=" + context["manual_id"]
    context["next"] = get_parent_url(request.path).rstrip('/') + "/image?manual_id=" + context["manual_id"]

    if not context:
        return HttpResponseBadRequest("parameter has error.")

    template = loader.get_template("sample/sample_description.html")
    return HttpResponse(template.render(context, request))


def get_sample_image (request):
    context = convert_request_to_context(request)
    context["current"] = "/sample/image?manual_id=" + context["manual_id"]
    context["next"] = get_parent_url(request.path).rstrip('/') + "/audio?manual_id=" + context["manual_id"]

    if not context:
        return HttpResponseBadRequest("parameter has error.")

    template = loader.get_template("sample/sample_image.html")
    return HttpResponse(template.render(context, request))


def get_sample_audio (request): 
    context = convert_request_to_context(request)
    context["current"] = "/sample/audio?manual_id=" + context["manual_id"]
    context["next"] = get_parent_url(request.path).rstrip('/') + "?manual_id=" + context["manual_id"]

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


def get_parent_url(url):
    parsed_url = urlparse(url)  # URLを解析
    parent_path = "/".join(parsed_url.path.rstrip('/').split('/')[:-1])  # 最後の階層を削除
    parent_url = urljoin(url, parent_path)  # 新しいURLを生成
    
    return parent_url
