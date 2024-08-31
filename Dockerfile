# Python bazlı bir image kullanıyoruz
FROM python:3.8-slim

# Çalışma dizinini oluşturuyoruz
WORKDIR /app

# Gereksinimleri yükleme
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Uygulama kodunu kopyalama
COPY . .

# Portu belirtme
EXPOSE 8080

# Uygulamayı çalıştırma
CMD ["python", "app.py"]
