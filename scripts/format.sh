#!/bin/bash

# 안 쓰는 임포트/변수 제거
poetry run autoflake . --remove-all-unused-imports --remove-unused-variables --in-place --recursive

# 임포트 정렬
poetry run isort .

# 코드 스타일 정리
poetry run black .