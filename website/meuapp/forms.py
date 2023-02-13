from django import forms


class IpAddressForm(forms.Form):
    ip_address = forms.CharField()
    port = forms.IntegerField(min_value=0, max_value=65535)
