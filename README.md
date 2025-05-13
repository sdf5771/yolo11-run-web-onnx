# YOLO11 웹 ONNX 실행

## 소개

이 프로젝트는 객체 감지 모델인 'YOLO11'을 웹 환경에서 실행할 수 있도록 구현한 애플리케이션입니다. ONNX 런타임을 활용하여 브라우저에서 직접 객체 감지가 가능합니다.

- ONNX Runtime - https://onnxruntime.ai/docs/tutorials/web/
- YOLO11 Docs - https://docs.ultralytics.com/ko/models/#what-types-of-tasks-can-yolo11-perform-and-how-does-it-compare-to-other-yolo-versions

## 주요 기능

- 웹 브라우저에서 YOLO11 객체 감지 모델 실행
- 카메라, 이미지, 비디오 파일에서 실시간 객체 감지
- ONNX 런타임을 활용한 빠른 추론 속도
- 다양한 객체 클래스 감지 및 분류

## 시작하기

### 사전 요구사항

- Node.js 14.0 이상
- Python
- 현대적인 웹 브라우저 (Chrome, Firefox, Safari 최신 버전 권장)

### 설치

```bash
# 저장소 클론
git clone https://github.com/sdf5771/yolo11-run-web-onnx.git
cd yolo11-run-web-onnx

# Install YOLO11
pip install ultralytics

# "yolo11n" 모델 다운로드 후 ONNX 모델로 변환 + example image 다운로드
python main.py

# 의존성 설치
npm install -g http-server

# 개발 서버 실행
http-server -c-1
```

## 사용 방법
1. main.py 파일을 실행해서 "yolo11n" 모델을 다운로드 후 ONNXX 모델로 변환합니다.
2. 개발 서버를 실행한 후 브라우저에서 로컬 서버에 접속합니다. (http-server 사용 권장)
3. 이미지 업로드, 카메라 사용, 또는 비디오 파일을 통해 객체 감지를 시작할 수 있습니다.
4. 감지된 객체는 경계 상자와 클래스 레이블로 표시됩니다.

## 기술 스택

- ONNX 런타임 웹
- WebGL 가속

## 라이센스

이 프로젝트는 GNU General Public License v3.0에 따라 라이센스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 기여하기

프로젝트에 기여하고 싶으시다면 이슈를 등록하거나 풀 리퀘스트를 보내주세요. 모든 기여는 환영합니다!
