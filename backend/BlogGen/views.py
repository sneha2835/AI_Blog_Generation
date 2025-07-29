from django.http import JsonResponse

def handler404(request, exception):
    return JsonResponse({"error": "Endpoint not found"}, status=404)

def handler500(request):
    return JsonResponse({"error": "Internal server error"}, status=500)

handler404 = "BlogGen.urls.handler404"
handler500 = "BlogGen.urls.handler500"
