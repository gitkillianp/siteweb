from django import forms

JOBS = (
    ("python", "Développeur Python"),
    ("javascript", "Développeur Javascript"),
    ("csharp", "Développeur C#")
)

class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6)
    job = forms.ChoiceField(choices=JOBS)
    cdu_accept = forms.BooleanField(initial=True)
