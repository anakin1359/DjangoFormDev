from django.shortcuts import render
from . import forms

def index(request):
  return render(request, "formapp/index.html")

def form_page(request):
  form = forms.UserInfo()
  if request.method == "POST":
    # Formで送信されたデータを取得する
    form = forms.UserInfo(request.POST)
    
    if form.is_valid():   # フィールの適正値検査（バリデーションの実装）
      print("フォールドの内容に誤りはありません。")
      print(
        f"name: {form.cleaned_data['name']}, mail: {form.cleaned_data['mail']}, age: {form.cleaned_data['age']}"
      )
      
  return render(
    request, "formapp/form_page.html", context={
      "form": form
    }
  )
