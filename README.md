# Webfest2024-Quantum-AR-for-Education

### Running

#### Standalone

```
# in .venv path
Scripts/activate
cd src/app
flask run
```

#### Docker

```
cd src
docker build --tag proman3419/webfest2024-quantum-ar .
docker run -it -p 127.0.0.1:32000:32000/tcp webfest2024-quantum-ar
```

#### Kubernetes

```
cd src
docker build --tag proman3419/webfest2024-quantum-ar:0.0.1 .
docker login
docker push proman3419/webfest2024-quantum-ar:0.0.1

cd deploy
helm upgrade --install webfest2024-quantum-ar . -f values.yaml
```
