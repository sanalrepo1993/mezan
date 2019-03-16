from rest_framework import serializers
from .models import Mahal

class MahalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Mahal
        #exclude = ['patient_image','patient_address']
        field = '__all__'
        '''
        (
            'id', 'patient_name','patient_dob'
        )
        '''
        datatables_always_serialize = ('id', )