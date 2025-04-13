# pair-programming-with-fastapi

## 📄 FastAPI 로그 필터링 API 요구사항

### ✅ 기능 요약

- **GET /logs** 엔드포인트에서 로그 데이터를 조회할 수 있어야 한다.
- 로그는 아래와 같은 필드를 가진다:
  - `id`: 고유 식별자
  - `timestamp`: 생성 시각 (UTC, ISO 8601 형식)
  - `level`: 로그 레벨 (`INFO`, `ERROR`, `WARN`, `DEBUG`)
  - `tag`: 로그 분류 (`auth`, `billing`, `system`, ...)
  - `message`: 로그 내용

### ✅ 필터링 조건

- 아래 쿼리 파라미터로 조회 범위 지정 가능:
  - `start`: 시작 시간 (예: `2024-04-01T00:00:00Z`)
  - `end`: 종료 시간 (예: `2024-04-13T23:59:59Z`)
  - `level`: 선택적 (예: `ERROR`)
  - `tag`: 선택적 (예: `auth`)

### ✅ 응답 예시

```json
[
  {
    "id": 1,
    "timestamp": "2024-04-12T08:00:00Z",
    "level": "ERROR",
    "tag": "auth",
    "message": "로그인 실패 - 비밀번호 오류"
  },
  ...
]
```

### 🛠️ 개발/테스트용 쿼리 예시

- 전체 조회: `/logs`
- 날짜 필터링: `/logs?start=2024-04-03T00:00:00Z&end=2024-04-10T23:59:59Z`
- 조건 필터링: `/logs?level=ERROR&tag=billing`
