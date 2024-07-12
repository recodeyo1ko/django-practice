from django import forms

class SearchForm(forms.Form):
    search_name = forms.CharField(max_length=100)

    def clean_search_name(self):
        search_name = self.cleaned_data['search_name']
        if search_name.strip() == '':
            raise forms.ValidationError('検索する名前を入力してください')
        return search_name