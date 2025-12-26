import sys
import time
import torch
import intel_extension_for_pytorch as ipex

# =================================================================
# [1단계] 라이브러리 패치 (반드시 YOLO import보다 먼저 해야 함!)
# =================================================================
from ultralytics.utils import torch_utils
from ultralytics.utils import checks

# 1. 장치 선택 함수 강제 개조 (XPU 인식)
_original_select_device = torch_utils.select_device

def force_xpu_select_device(device='', batch=None, newline=True, verbose=True):
    if device == 'xpu':
        if verbose:
            print(f"⚡ [System] Intel Arc GPU ({torch.xpu.get_device_name(0)}) 강제 할당 성공!")
        return torch.device('xpu')
    return _original_select_device(device, batch, newline, verbose)

torch_utils.select_device = force_xpu_select_device

# 2. AMP 검사 우회
def bypass_check_amp(model):
    return False
checks.check_amp = bypass_check_amp

# =================================================================
# [2단계] 메모리 체크 무력화 (학습 도중 멈춤 방지)
# =================================================================
# Trainer 모듈을 불러와서 메모리 체크 함수를 바꿔치기 합니다.
from ultralytics.engine import trainer

def bypass_get_memory(self, fraction=True):
    # 메모리 검사 요청이 오면 무조건 "0 사용 중"이라고 속임
    return 0.0

trainer.BaseTrainer._get_memory = bypass_get_memory

# =================================================================
# [3단계] 이제야 비로소 YOLO를 불러옵니다 (안전함)
# =================================================================
from ultralytics import YOLO

def train_final_xpu():
    print("\n--- 🚀 Intel Arc GPU 완벽 학습 시작 ---")
   
    # 모델 로드
    model = YOLO('yolov8n.pt')

    print("학습을 시작합니다... (intel_gpu_top을 확인하세요)")
    start_time = time.time()

    # 학습 시작
    model.train(
        data='coco8.yaml',  
        epochs=100,          
        imgsz=640,          
       
        # 필수 설정들
        device='xpu',      
        batch=2,            
        workers=0,           # 데이터 로딩 멈춤 방지
        deterministic=False, # 무한 대기 방지
        amp=False,           # 호환성 확보
        half=False,
       
        project='drone_project',
        name='arc_gpu_complete',
        exist_ok=True
    )
   
    end_time = time.time()
    print(f"\n✅ 학습 대성공! 소요 시간: {end_time - start_time:.2f}초")

if __name__ == "__main__":
    if torch.xpu.is_available():
        train_final_xpu()
    else:
        print("❌ 심각: XPU(Intel GPU)가 잡히지 않습니다.")
