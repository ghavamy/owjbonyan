from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'اینجا بنویس ...',
            'dir': 'rtl',  # Set text direction to right-to-left
            'style': 'text-align: right;',  # Optional: align text to the right
        }
    ), label='Comment', max_length=500)