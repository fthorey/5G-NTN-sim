# 5G-NTN Simulation with OAI

This project uses OpenAirInterface (OAI) with RF simulator for 5G NTN simulation, using separate containers for gNB and UE.

## Prerequisites

- Docker installed on your system
- Git
- Waf build system (included in the repository)

## Building the Docker Images

The project uses Waf as its build system. Available commands:

### Build Commands
```bash
# Build gNB image
./waf build_gnb

# Build UE image
./waf build_ue

# Build both images
./waf build_all
```

### Run Commands
```bash
# Run gNB container
./waf run_gnb

# Run UE container
./waf run_ue

# Run both containers
./waf run_all
```

### Network Management
```bash
# Create the Docker network (automatically done by run commands)
./waf create_network
```

## Notes

- Both containers are configured to automatically remove themselves when stopped (`--rm` flag)
- The containers communicate over the `oai-net` Docker network
- Container names are used for DNS resolution within the network
- Press Ctrl+C to gracefully stop and clean up containers

## Project Structure

```
.
├── docker/
│   ├── Dockerfile.gnb
│   ├── Dockerfile.ue
│   ├── .dockerignore
├── waf                 # Waf build system
├── wscript            # Build configuration
└── README.md
```