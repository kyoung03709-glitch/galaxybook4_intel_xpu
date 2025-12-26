#!/bin/bash
echo "1. Intel Arc GPU 드라이버 및 OpenCL 관련 패키지 설치를 시작합니다..."
sudo apt update
sudo apt install -y intel-opencl-icd intel-level-zero-gpu level-zero clinfo

echo "2. 사용자 권한을 설정합니다 (render, video 그룹 추가)..."
sudo usermod -aG render,video $USER

echo "-----------------------------------------------------------"
echo "설치가 완료되었습니다! 권한 적용을 위해 반드시 '재부팅' 하세요."
echo "-----------------------------------------------------------"
