from socket import fromshare
from django import fromshare

class UserInfo(forms.Form):
  name = forms.CharField()
  age = forms.IntegerRangeField()
  mail = forms.forms.EmailField()
