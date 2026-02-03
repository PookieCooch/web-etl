
import json
from django.shortcuts import render
from etl.spark_etl import run_etl

def etl_form(request):
    result = None

    if request.method == "POST":
        url = request.POST["url"]
        headers = json.loads(request.POST.get("headers", "{}"))
        token = request.POST.get("token")

        if token:
            headers["Authorization"] = f"Bearer {token}"

        result = run_etl(url, headers)

    return render(request, "etl_form.html", {"result": result})
