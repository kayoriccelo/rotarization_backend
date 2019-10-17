from django.db.models import Q
from rest_framework import serializers

from .models import UserRotarization


class UserRotarizationSerializer(serializers.Serializer):
    fields_required = [
        ('first_name', 'Primeiro Nome'),
        ('last_name', 'Ultimo Nome'),
        ('cpf', 'Cpf'),
        ('username', 'Usuário'),
        ('email', 'Email'),
        ('password', 'Senha')
    ]

    def validate(self, attrs):
        data = self.context['request'].data

        criticas = []
        for field in self.fields_required:
            if not field[0] in data:
                criticas.append(f'{field[1]} não informado.')
                continue

            attrs[field[0]] = data[field[0]]

        if len(criticas) > 0:
            raise serializers.ValidationError(criticas)

        try:
            UserRotarization.objects.get(
                Q(cpf=attrs['cpf']),
                Q(username=attrs['username']),
                Q(email=attrs['email'])
            )

            raise serializers.ValidationError(u'Conta já cadastrado.')
        except UserRotarization.DoesNotExist:
            pass

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')

        try:
            user_rotarization = UserRotarization(
                **validated_data,
                is_active=True,
                is_staff=False
            )

            user_rotarization.set_password(password)
            user_rotarization.save()
        except Exception as e:
            raise serializers.ValidationError({'non_field_errors': [
                u'Não foi possível registrar uma nova conta.'
            ]})

        return user_rotarization
 