from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Title"}))
    description = forms.CharField(label='',
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Description",
                                          "class": 'class-name',
                                          "rows": 5,
                                          "cols": 40,
                                      }
                                  )
                                  )
    price = forms.DecimalField(label='', widget=forms.NumberInput(attrs={"placeholder": "Price"}))
    summary = forms.CharField(label='',
                              widget=forms.Textarea(
                                  attrs={
                                      "placeholder": "Summary",
                                      "class": 'class-name',
                                      "rows": 5,
                                      "cols": 40,
                                  }
                              )
                              )
    featured = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'featured'
        ]

    #     For validation on title
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if len(title) < 10:
            raise forms.ValidationError("Title must be greater than 10 characters")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Title"}))
    description = forms.CharField(label='',
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Description",
                                          "class": 'class-name',
                                          "rows": 5,
                                          "cols": 40,
                                      }
                                  )
                                  )
    price = forms.DecimalField(label='', widget=forms.NumberInput(attrs={"placeholder": "Price"}))
    summary = forms.CharField(label='',
                              widget=forms.Textarea(
                                  attrs={
                                      "placeholder": "Summary",
                                      "class": 'class-name',
                                      "rows": 5,
                                      "cols": 40,
                                  }
                              )
                              )
    featured = forms.BooleanField(required=False, initial=False)
