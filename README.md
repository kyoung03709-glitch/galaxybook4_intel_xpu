⚡ Intel Arc GPU (XPU) Acceleration Guide for Galaxy Book 4

This repository provides a step-by-step guide and automation scripts to set up a high-performance PyTorch and Ultralytics (YOLO) environment utilizing the Intel Arc GPU (Meteor Lake architecture) on the Galaxy Book 4.
💡 Background

Modern Intel Integrated GPUs (Arc Graphics) are accelerated through the Intel Extension for PyTorch (IPEX) rather than the traditional NVIDIA CUDA stack. This guide ensures a stable installation by using a "Golden Combination" of library versions to prevent dependency conflicts common in the Intel XPU ecosystem.
📋 Prerequisites

    OS: Ubuntu 22.04 / 24.04 LTS

    Hardware: Intel Core Ultra (Meteor Lake) with Arc Graphics

    Python: 3.10 (Recommended)

🚀 Installation Steps
1. Driver Installation & Permission Setup

Configure the Intel Compute Runtime and set the necessary hardware permissions for the system to recognize the Arc GPU.
Bash

chmod +x scripts/install_driver.sh
./scripts/install_driver.sh

# ⚠️ Mandatory: System REBOOT is required after installation!
sudo reboot

2. Virtual Environment & AI Library Setup

Install PyTorch and IPEX compatible with Intel XPU. This script specifically forces numpy<2 to avoid version conflicts with Ultralytics.
Bash

chmod +x scripts/setup_env.sh
./scripts/setup_env.sh

3. Verification

Test if the GPU (XPU) is correctly recognized within your virtual environment.
Bash

# Activate the virtual environment
source venv_arc/bin/activate

# Check XPU recognition status
python3 examples/check_xpu.py

    Expected Output: XPU Available: True / Device Name: Intel(R) Arc(TM) Graphics

💡 Critical Notes
1. NumPy Version Compatibility (NumPy < 2.0)

    The Problem: Installing ultralytics may automatically upgrade NumPy to version 2.x.

    The Solution: IPEX and PyTorch 2.1 are currently incompatible with NumPy 2.x. You must maintain NumPy 1.26.4 or lower. (pip install "numpy<2")

2. Intel oneAPI Environment Variables

    If you encounter "Library not found" errors during execution, you may need to manually source the Intel runtime paths:

Bash

source /opt/intel/oneapi/compiler/latest/env/vars.sh
source /opt/intel/oneapi/mkl/latest/env/vars.sh

3. Performance Optimization

To maximize inference speed, you can utilize the following environment variables:
Bash

export ZE_AFFINITY_MASK=0.0         # Specify GPU device ID
export IPEX_XPU_ONEDNN_LAYOUT=1     # Enable oneDNN layout acceleration

📂 Project Structure

    scripts/install_driver.sh: Configures Intel Compute Runtime and oneAPI repositories.

    scripts/setup_env.sh: Creates the venv, installs IPEX, PyTorch, and YOLO.

    examples/check_xpu.py: A verification script to test GPU availability and performance.

