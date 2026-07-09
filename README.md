# Agent Skills

Bộ skill templates cho agent mode, tập trung vào 5 vai trò:

- engineering-mentor: định hướng giải pháp, trade-off, review mindset
- research-engineer: nghiên cứu có nguồn dẫn chiếu trước khi quyết định
- backend-java-developer: implement backend Java production-grade
- frontend-developer: implement frontend production-grade
- project-context-cache: cache context repo để giảm discovery lặp lại

Mục tiêu của repo:

- Chuẩn hóa cách prompt và phạm vi trách nhiệm theo từng vai trò
- Tách phần hướng dẫn tổng quan (SKILL.md) và tài liệu chuyên sâu (references)
- Hỗ trợ luồng làm việc mentor -> implementer rõ ràng, có handoff

## Cấu trúc

```text
agent-skills/
  backend-java-developer/
    SKILL.md
    agents/openai.yaml
    references/
      build-tooling.md
      java-library.md
      java-modern.md
      spring-boot.md
      testing.md
  engineering-mentor/
    SKILL.md
    agents/openai.yaml
  frontend-developer/
    SKILL.md
    agents/openai.yaml
    references/
      angular.md
      app-builder.md
      build-tooling.md
      react-next-vite.md
      styling.md
      vue-nuxt.md
  project-context-cache/
    SKILL.md
    agents/openai.yaml
    scripts/generate_project_context.py
  research-engineer/
    SKILL.md
    agents/openai.yaml
```

## Nguyên tắc thiết kế

- 1 skill = 1 role rõ ràng, không chồng chéo phạm vi
- SKILL.md là router: hướng dẫn vai trò, workflow, output contract
- references/* chứa guidance theo stack/chủ đề
- agents/openai.yaml khai báo display name, short description, default prompt, policy invocation
- Tối ưu cho tasks thực chiến: research -> design -> implement -> review

## Skill map

### engineering-mentor

Dùng khi cần:

- kiến trúc, trade-off, design review
- implementation plan và boundary module
- code review theo mức độ nghiêm trọng

Đầu ra kỳ vọng:

- đề xuất 1 hướng ưu tiên kèm lý do
- nếu cần, đề xuất handoff sang backend/frontend developer

### research-engineer

Dùng khi cần:

- RFC/spec, docs chính thức, migration guide, best practices
- tổng hợp pitfalls và common errors trước khi code

Đầu ra kỳ vọng:

- research brief có source, tách facts và interpretation

### backend-java-developer

Dùng khi cần:

- xây dựng/refactor API, service, persistence, test trong Java backend
- Spring Boot, Maven/Gradle, multi-module, build logic

Đầu ra kỳ vọng:

- code thay đổi nhỏ gọn, đúng boundary
- test/validation đề xuất rõ ràng theo context

### frontend-developer

Dùng khi cần:

- implement UI feature, refactor frontend
- React/Next/Vite, Angular, Vue/Nuxt
- styling và tooling trong monorepo/workspace

Đầu ra kỳ vọng:

- UI maintainable, accessible, responsive
- thích ứng với conventions có sẵn của project

### project-context-cache

Dùng khi cần:

- đọc/tạo/cập nhật context file cho repo đang làm
- tránh discovery lặp lại quá nhiều lần

Đầu ra kỳ vọng:

- context ngắn gọn, operational, dùng để khởi động task nhanh hơn

## Luồng phối hợp đề xuất

### 1) Discovery-first (khuyến nghị)

1. project-context-cache
2. research-engineer (nếu bài toán nhạy cảm version/spec)
3. engineering-mentor
4. backend-java-developer hoặc frontend-developer

### 2) Direct implementation

1. engineering-mentor (chốt hướng ngắn)
2. implementer phù hợp stack

### 3) Deep research task

1. research-engineer
2. engineering-mentor để chốt implication cho implementation

## Mẫu prompt nhanh

```text
Use $project-context-cache to refresh context for this repo.
Use $research-engineer to research Spring Security stateless JWT best practices for Spring Boot 3.x.
Use $engineering-mentor to propose the safest migration path with trade-offs.
Use $backend-java-developer to implement the selected plan.
```

```text
Use $engineering-mentor to review this feature design and suggest a minimal-risk implementation order.
Use $frontend-developer to implement the chosen UI flow in existing project conventions.
```

## Checklist chất lượng cho mỗi skill

- SKILL.md
  - role rõ ràng
  - trigger/when-to-use cụ thể
  - workflow có bước thực thi
  - output contract đo được
- references
  - không trùng lặp quá nhiều với SKILL.md
  - cập nhật theo major versions quan trọng
- openai.yaml
  - display_name, short_description, default_prompt đầy đủ
  - policy invocation nhất quán với mục đích

## Convention để mở rộng repo

Khi thêm skill mới:

1. Tạo folder mới theo mẫu:
   - SKILL.md
   - agents/openai.yaml
   - references/* (nếu cần)
2. Định nghĩa rõ boundary và handoff với skill hiện có.
3. Thêm 1-2 prompt mẫu để dễ discover.
4. Kiểm tra overlap với skill khác, nếu trùng thì tách lại scope.

## Roadmap đề xuất

- Thêm root index cho tất cả skills và trigger matrix
- Thêm lint/check script validate cấu trúc SKILL.md + openai.yaml
- Thêm ví dụ end-to-end workflow cho 2 scenario:
  - Java backend feature with RFC research
  - Frontend feature with mentor-first design
