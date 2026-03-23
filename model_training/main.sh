#!/usr/bin/env bash

# Remove potentially conflicting packages
! echo "Removing potentially conflicting packages: torch torchvision torchaudio triton transformers accelerate datasets evaluate numpy jax jaxlib"
! pip -q uninstall -y torch torchvision torchaudio triton transformers accelerate datasets evaluate numpy jax jaxlib

# Upgrade pip
! echo "Upgrading pip"
! pip -q install --upgrade pip

# Install PyTorch CUDA build
! echo "Installing pyTorch CUDA build"
! pip -q install --index-url https://download.pytorch.org/whl/cu121 \
  torch==2.2.2+cu121 torchvision==0.17.2+cu121 torchaudio==2.2.2+cu121

# Install compatible stack
! echo "Installing compatible stack"
! pip -q install numpy==1.26.4
! pip -q install triton==2.2.0
! pip -q install transformers==4.40.2 accelerate==0.29.3 datasets==2.19.1 evaluate==0.4.2 scikit-learn

# Restart runtime
! echo "Restarting runtime"
python3 ./scripts.py restart_runtime