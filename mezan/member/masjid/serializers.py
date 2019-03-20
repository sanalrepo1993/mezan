from rest_framework import serializers
from .models import Masjid

class MasjidSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Masjid
        #exclude = ['patient_image','patient_address']
        fields = '__all__'
        '''
        (
            'id', 'patient_name','patient_dob'
        )
        '''
        datatables_always_serialize = ('id', )