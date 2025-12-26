#!/bin/bash
echo "1. Python 3.10 기반 가상환경(venv_arc)을 생성합니다..."
python3.10 -m venv venv_arc
source venv_arc/bin/activate

echo "2. Intel 전용 PyTorch 및 IPEX를 설치합니다 (버전 주의)..."
pip install torch==2.1.0.post2 torchvision==0.16.0.post2 torchaudio==2.1.0.post2 \
intel-extension-for-pytorch==2.1.30+xpu oneccl_bind_pt==2.1.300+xpu \
--extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/

echo "3. Ultralytics를 설치합니다..."
pip install ultralytics

echo "4. NumPy 2.x 충돌 방지를 위해 1.26.4 버전으로 고정합니다..."
pip install "numpy<2"

echo "환경 구축이 완료되었습니다. 'source venv_arc/bin/activate'로 활성화하세요."
