import torch
import intel_extension_for_pytorch as ipex
import numpy as np

print(f"--- 환경 검증 결과 ---")
print(f"NumPy Version: {np.__version__}")
print(f"PyTorch Version: {torch.__version__}")
print(f"XPU Available: {torch.xpu.is_available()}")

if torch.xpu.is_available():
    print(f"XPU Device Name: {torch.xpu.get_device_name(0)}")
else:
    print("XPU를 사용할 수 없습니다. 드라이버 설치와 환경 변수를 확인하세요.")
