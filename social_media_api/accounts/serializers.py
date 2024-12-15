from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomUser  # Directly import your custom user model if available


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Dynamically fetch the user model
        User = CustomUser
        # Create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        # Generate a token for the new user
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Dynamically fetch the user model
        User = CustomUser

        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise serializers.ValidationError("Invalid password.")
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid username.")

        # Retrieve or create a token for the user
        token, _ = Token.objects.get_or_create(user=user)
        return {'token': token.key}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
