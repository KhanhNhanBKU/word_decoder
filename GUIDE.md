# HƯỚNG DẪN LABEL CHO CÁC WORD

## Overview

Label cho các word được soạn sẵn theo format sau:

```json
{
    PATTERN: (PATTERN_LEFT, PATTER_RIGHT),
    LOCATION: (LOCATION_LEFT, LOCATION_RIGHT),
    DIRECTION: (DIRECTION_LEFT, DIRECTION_RIGHT),
}
```

1. Pattern
   Ví dụ: Nắm -> A
   Xem tại [Google Sheet Hand Pattern Recognition](https://docs.google.com/spreadsheets/d/1wobS-_RUlKgN6tjd2wrLGVjX33iymA9AYrqemFEQlEI/edit?usp=sharing)
2. Location gồm 5 điểm : HEAD, MOUTH, SHOULDER, CHEST, BELLY
3. Direction có 6 loại: UP, DOWN, RIGHT, LEFT, FORWARD, BACKWARD

ví dụ như sau

```
{
  "PATTERN": ("_","E"),
  "LOCATION": ("_","MOUTH"),
  "DIRECTION": ("_","_")
}
```

Các word khi label, cần thỏa

- 1 word có thể có 1 hoặc nhiều bộ 3
- Được bọc trong [] dù có là 1 bộ 3 hay nhiều bộ 3

## Danh sách word cần label

=> 30 word, mỗi đứa 15 từ

1.  [x] Cảm ơn
2.  [x] Tôi
3.  [x] Bạn
4.  [ ] Gia đình
5.  [ ] Đồng hồ
6.  [x] Ba
7.  [x] Lái xe
8.  [x] Đi làm
9.  [x] Xe bus
10. [x] Dừng
11. [x] Ở đâu
12. [x] Mấy
13. [x] Tuổi
14. [ ] Có
15. [ ] Người
16. [x] Ai
17. [x] Thích
18. [x] Ăn
19. [ ] Nho
20. [x] Không thích
21. [ ] Màu
22. [x] Nào / Gì
23. [ ] Bút bi
24. [x] Sống
25. [ ] Thủ đô
26. [x] Việt Nam
27. [ ] Hằng ngày
28. [x] Thức dậy
29. [x] Ngủ
30. [ ] Lúc
31. [x] Giờ
