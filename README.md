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
docker build --tag webfest2024-quantum-ar .
docker run -it -p 127.0.0.1:5000:5000/tcp webfest2024-quantum-ar
```
