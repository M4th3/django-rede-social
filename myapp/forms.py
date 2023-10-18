from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' #Define que todos os campos da classe serão selecionados
                             # Caso queira campos específicos, defina o valor como uma lista com o nome dos campos em str

         