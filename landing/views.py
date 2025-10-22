from django.shortcuts import render

# Create your views here.
from django.utils.timezone import now

def home(request):
    ctx = {"year": now().year}
    if request.method == "POST":
        email = request.POST.get("email")
        ctx["submitted_email"] = email  # demo: muestra el email enviado
    return render(request, "landing/home.html", ctx)
