from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo,
        fields = ['id','titulo','estado']


# Importamos del rest_framework el modulo serializers para agrupar la información

# Usamos el modelo Todo que tiene la estuctura de la tarea del ToDo

# Dentro del class heredamos para utilizar las funcionalidades de ModelSerializer

# La estrucutra es: Definir de donde viene el modelo, y con que campos se va a ejecutar la agrupación de la información