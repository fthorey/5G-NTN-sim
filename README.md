# 5G-NTN Simulation with OAI

This project uses OpenAirInterface (OAI) with RF simulator for 5G NTN simulation, using separate containers for gNB and UE.

## Prerequisites

- Docker installed on your system
- Git

## Building the Docker Images

### gNB Image
```bash
docker build -t oai-gnb -f docker/Dockerfile.gnb .
```

### UE Image
```bash
docker build -t oai-ue -f docker/Dockerfile.ue .
```

## Setting Up the Network

Create a Docker network for gNB and UE communication:
```bash
docker network create oai-net
```

## Running the Containers

### gNB Container
```bash
docker run -it --rm --network oai-net --name oai-gnb oai-gnb
```

### UE Container
```bash
docker run -it --rm --network oai-net --name oai-ue oai-ue
```

## Project Structure

```
.
├── docker/
│   ├── Dockerfile.gnb
│   ├── Dockerfile.ue
│   ├── .dockerignore
│   └── env
└── README.md
```

## Environment Variables

### gNB Container
- `RF_SIMULATOR_SERVER`: Address of the UE container (default: "oai-ue")

### UE Container
- `RF_SIMULATOR_SERVER`: Address of the gNB container (default: "oai-gnb")

## Notes

- Both containers are configured to automatically remove themselves when stopped (`--rm` flag)
- The containers communicate over the `oai-net` Docker network
- Container names are used for DNS resolution within the network 