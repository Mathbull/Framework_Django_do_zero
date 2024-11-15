from django import forms
from django.contrib.auth import get_user_model

User = get_user_model() # Dedecta automaticamente qual o model para user

class AccountSingupForms(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        max_length=50,
        widget=forms.PasswordInput()
    )

    # Após criar os novos campos iremos chamalos aqui para mostrar o usuario
    class Meta:
        model = User
        #podemos defir a order de exibição
        fields = ('username', 'email', 'data_nascimento', 'cpf', 'password',) 
        widgets ={
            'data_nascimento':forms.DateInput(
                attrs={"type":'date', 'required': 'required',}),
        }    