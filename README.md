# Galaxy Book 4 Intel Arc GPU 가속 가이드

이 저장소는 갤럭시북4의 Intel Arc GPU를 활용하여 PyTorch 및 Ultralytics 환경을 구축하는 방법을 설명합니다.

## 🚀 설치 순서

### 1. 드라이버 설치 및 권한 설정
```bash
chmod +x scripts/install_driver.sh
./scripts/install_driver.sh
# 완료 후 반드시 시스템 재부팅!

2. 가상환경 및 AI 라이브러리 설치
Bash

chmod +x scripts/setup_env.sh
./scripts/setup_env.sh

3. 정상 작동 확인
Bash

source venv_arc/bin/activate
python3 examples/check_xpu.py

💡 주의사항

    NumPy 버전: ultralytics 설치 시 NumPy 2.x가 깔릴 수 있으니 반드시 numpy<2를 유지해야 합니다.

    환경 변수: 실행 전 source /opt/intel/oneapi/setvars.sh가 필요할 수 있습니다.


---

## 5. 저장 후 최종 업로드
파일 내용을 다 채우셨다면, 터미널에서 아래 명령어로 GitHub에 올리세요.

```bash
cd ~/galaxybook4_intel_xpu
git add .
git commit -m "Complete scripts and README for Intel Arc setup"
git push -u origin main
