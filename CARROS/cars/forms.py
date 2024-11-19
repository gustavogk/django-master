from django import forms
from cars.models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(label='Modelo', max_length=200)
    brand = forms.ModelChoiceField(label='Marca', queryset=Brand.objects.all())
    factory_year = forms.IntegerField(label='Ano de Fabricação')
    model_year = forms.IntegerField(label='Ano do Modelo')
    plate = forms.CharField(label='Placa', max_length=10)
    value = forms.FloatField(label='Valor')
    photo = forms.ImageField(label='Foto')

    def save(self):
        car = Car(
            model=self.cleaned_data['model'],
            brand=self.cleaned_data['brand'],
            factory_year=self.cleaned_data['factory_year'],
            model_year=self.cleaned_data['model_year'],
            plate=self.cleaned_data['plate'],
            value=self.cleaned_data['value'],
            photo=self.cleaned_data['photo']
        )
        car.save()
        return car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'color': forms.CheckboxSelectMultiple(),
        }

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 0:
            self.add_error('value', 'O valor não pode ser negativo')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Ano de fabricação não pode ser inferior a 1975')
        return factory_year