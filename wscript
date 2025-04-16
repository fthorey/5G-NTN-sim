#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import sys

class ContainerManager:
    def __init__(self):
        # Context for container management
        self.ctx = None
        # Register signal handler for graceful container cleanup on Ctrl+C
        signal.signal(signal.SIGINT, self.cleanup_containers)

    def set_context(self, ctx):
        # Set the context for container management
        self.ctx = ctx

    def cleanup_containers(self, sig=None, frame=None):
        """Clean up containers when Ctrl+C is received"""
        if self.ctx:
            print("\nCleaning up containers...")
            self.ctx.exec_command('docker rm -f oai-gnb oai-ue 2>/dev/null || true', stdout=None, stderr=None)
        sys.exit(0)

# Create a single instance of the manager
manager = ContainerManager()

def options(opt):
    pass

def configure(conf):
    pass

def build(bld):
    pass

def create_network(ctx):
    manager.set_context(ctx)
    # Check if network exists, create if it doesn't
    ctx.exec_command('docker network inspect oai-net >/dev/null 2>&1 || docker network create oai-net', stdout=None, stderr=None)

def build_gnb(ctx):
    manager.set_context(ctx)
    # Build the container
    ctx.exec_command('docker build -t oai-gnb -f docker/Dockerfile.gnb .', stdout=None, stderr=None)

def run_gnb(ctx):
    manager.set_context(ctx)
    # Ensure network exists before running
    create_network(ctx)
    # Remove existing container if it exists
    ctx.exec_command('docker rm -f oai-gnb 2>/dev/null || true', stdout=None, stderr=None)
    # Run the container
    ctx.exec_command('docker run --rm --network oai-net --name oai-gnb oai-gnb', stdout=None, stderr=None)

def build_ue(ctx):
    manager.set_context(ctx)
    # Build the container
    ctx.exec_command('docker build -t oai-ue -f docker/Dockerfile.ue .', stdout=None, stderr=None)

def run_ue(ctx):
    manager.set_context(ctx)
    # Ensure network exists before running
    create_network(ctx)
    # Remove existing container if it exists
    ctx.exec_command('docker rm -f oai-ue 2>/dev/null || true', stdout=None, stderr=None)
    # Run the container
    ctx.exec_command('docker run --rm --network oai-net --name oai-ue oai-ue', stdout=None, stderr=None)

def build_all(ctx):
    manager.set_context(ctx)
    # Build the containers
    build_gnb(ctx)
    build_ue(ctx)
