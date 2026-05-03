# Azure DevOps Pipeline ve Deploy Rehberi (Adim Adim)

Bu rehber, backend tarafini Azure DevOps ile test/build/deploy akisinda canli gostermek icin hazirlandi.

## 1) Zorluk Seviyesi

- Temel pipeline kurulum: orta
- Docker image build + push: orta
- Canli ortama deploy: orta/ileri
- Ilk kurulum bir kere yapilir; sonrasi kolayca tekrar edilir.

## 2) On Kosullar

- Azure DevOps projesi acik
- Repo Azure DevOps'a bagli (veya GitHub baglantisi kurulu)
- Docker image push icin bir registry:
  - Azure Container Registry (onerilen) veya Docker Hub
- Deploy hedefi:
  - Azure VM (docker compose ile) veya Azure App Service for Containers
- Secret degerleri hazir:
  - `DJANGO_SECRET_KEY`
  - `POSTGRES_HOST`
  - `POSTGRES_PORT`
  - `POSTGRES_DB`
  - `POSTGRES_USER`
  - `POSTGRES_PASSWORD`
  - `CORS_ALLOWED_ORIGINS`
  - `DJANGO_ALLOWED_HOSTS`

## 3) Azure DevOps'ta Service Connection Olustur

1. Project Settings -> Service connections
2. Yeni baglanti:
   - Azure Resource Manager (deploy icin)
   - Docker Registry / ACR (image push icin)
3. Pipeline icinde kullanilacak connection ismini not et.

## 4) Pipeline Secret ve Variable Tanimla

Pipelines -> Library veya Pipeline Variables icinde:

- `DJANGO_SECRET_KEY` (secret)
- `POSTGRES_HOST` (secret olabilir)
- `POSTGRES_PORT`
- `POSTGRES_DB`
- `POSTGRES_USER` (secret olabilir)
- `POSTGRES_PASSWORD` (secret)
- `CORS_ALLOWED_ORIGINS`
- `DJANGO_ALLOWED_HOSTS`
- `IMAGE_REPOSITORY` (ornek: `sigortaweb-backend`)
- `CONTAINER_REGISTRY` (ornek: `myregistry.azurecr.io`)

Not: Secret'lari asla yaml dosyasina duz metin yazma.

## 5) Pipeline Asamalari (Onerilen)

1. **Test**
   - Python setup
   - Dependency install
   - `python manage.py test`
2. **Build**
   - Docker image build
3. **Push**
   - Image'i registry'e push
4. **Deploy**
   - Hedef ortama yeni image deploy
5. **Smoke Test**
   - `GET /api/pages/home/` 200
   - `POST /api/auth/token/` 200

## 6) Ornek `azure-pipelines.yml`

Bu dosyayi repo kokunde kullanabilirsin (connection isimlerini kendine gore degistir):

```yaml
trigger:
  - main

pool:
  vmImage: "ubuntu-latest"

variables:
  pythonVersion: "3.12"
  imageRepository: "$(IMAGE_REPOSITORY)"
  containerRegistry: "$(CONTAINER_REGISTRY)"
  dockerfilePath: "backend/Dockerfile"
  tag: "$(Build.BuildId)"

stages:
  - stage: Test
    jobs:
      - job: BackendTests
        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: "$(pythonVersion)"
          - script: |
              cd backend
              python -m pip install --upgrade pip
              pip install -r requirements.txt
              python manage.py test -v 1
            displayName: "Run Django tests"

  - stage: BuildAndPush
    dependsOn: Test
    jobs:
      - job: DockerBuildPush
        steps:
          - task: Docker@2
            displayName: Build and Push
            inputs:
              command: buildAndPush
              repository: "$(imageRepository)"
              dockerfile: "$(dockerfilePath)"
              containerRegistry: "YOUR_DOCKER_SERVICE_CONNECTION"
              tags: |
                $(tag)
                latest

  - stage: Deploy
    dependsOn: BuildAndPush
    jobs:
      - job: DeployToVMOrAppService
        steps:
          - script: |
              echo "Deploy step: VM veya App Service scriptini burada calistir."
              echo "Sonra health check yap."
            displayName: "Deploy placeholder"
```

## 7) Deploy Secenegi A: Azure VM (Docker Compose)

1. VM'e SSH/RDP ile baglan
2. Sunucuda docker + compose kur
3. Backend icin `docker-compose.prod.yml` hazirla
4. Image'i registry'den cek:
   - `docker pull <registry>/<image>:latest`
5. Servisi ayaga kaldir:
   - `docker compose -f docker-compose.prod.yml up -d`
6. Health kontrol:
   - `curl http://<sunucu-adresi>/api/pages/home/`

## 8) Deploy Secenegi B: Azure App Service (Container)

1. App Service (Linux, Container) olustur
2. Container image kaynagini ACR/Registry olarak sec
3. App Settings icine environment degerlerini gir
4. Startup tamamlaninca endpoint health kontrol yap

## 9) Canli Gosterimde Gosterilecek Minimum Kanit

- Pipeline run ekrani:
  - Test stage yesil
  - Build/Push stage yesil
  - Deploy stage yesil
- Canli endpoint:
  - `GET /api/pages/home/` -> 200
  - `POST /api/auth/token/` -> 200
  - Token ile `GET /api/me/policies/` -> 200

## 10) En Sik Hatalar ve Cozum

- `401 unauthorized`:
  - Token yok/yanlis/expired -> login + refresh
- `DisallowedHost`:
  - `DJANGO_ALLOWED_HOSTS` eksik
- DB connection error:
  - Host/user/password/port yanlis veya firewall kapali
- SSL hatasi:
  - Azure DB icin `POSTGRES_SSLMODE=require`
  - Local docker postgres icin `POSTGRES_SSLMODE=disable`

## 11) Sunum Gunu Icin 5 Dakika Plan

1. Basarili pipeline run ekranini ac
2. Deploy hedefinde container/app statusunu goster
3. Public endpoint 200 goster
4. Login alip private endpoint 200 goster
5. Kisa ozet: test + build + deploy + smoke test tamam
