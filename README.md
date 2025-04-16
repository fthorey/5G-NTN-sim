# 5G-NTN-sim

This repository contains a 5G Non-Terrestrial Network (NTN) simulator using OpenAirInterface (OAI).

## Prerequisites

- Docker
- Python 3.x
- Waf build system

## Building and Running

### Using Docker Compose (Recommended)

1. Build and start the gNB:
```bash
docker-compose up gnb
```

2. In another terminal, start the UE:
```bash
docker-compose up ue
```

To stop the services:
```bash
docker-compose down
```

### Using Waf (Alternative)

Alternatively, you can use the Waf build system:

1. Build the containers:
```bash
# Build gNB container
./waf build_gnb

# Build UE container
./waf build_ue

# Or build both containers
./waf build_all
```

2. Run the simulation:
```bash
# Run gNB container
./waf run_gnb

# Run UE container
./waf run_ue
```

## Configuration

The simulation uses the following configuration:

- Band 78 (3.5GHz)
- Numerology 1 (30kHz subcarrier spacing)
- 106 resource blocks
- RF simulator for baseband processing

## Network Configuration

The containers communicate over a Docker network named `oai-net`. This network is automatically created when using docker-compose or the waf script.

## Troubleshooting

If you encounter issues:

1. Check Docker logs:
```bash
docker-compose logs
```

2. Verify network connectivity:
```bash
docker network inspect oai-net
```

3. Ensure ports are not in use by other processes

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