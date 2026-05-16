from django.contrib.auth import get_user_model

User = get_user_model()
users = User.objects.all()
print(f"Toplam kullanici: {users.count()}")

for user in users:
    print(f"Kullanici: {user.username} | Hash baslangici: {user.password[:30]}")
    if not user.password.startswith('pbkdf2_sha256'):
        user.set_password('Demo12345!')
        user.save()
        print(f"  -> Sifre duzeltildi: {user.username}")
    else:
        print(f"  -> Sifre zaten dogru formatta: {user.username}")

print("Tamamlandi!")
