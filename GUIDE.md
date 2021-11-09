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

1. [ ] Cảm ơn
1. [ ] Tôi
1. [ ] Bạn
1. [ ] Gia đình
1. [ ] Đồng hồ
1. [ ] Ba
1. [ ] Lái xe
1. [ ] Đi làm
1. [ ] Xe bus
1. [ ] Dừng
1. [ ] Ở đâu
1. [ ] Mấy
1. [ ] Tuổi
1. [ ] Có
1. [ ] Người
1. [ ] Ai
1. [ ] Thích
1. [ ] Ăn
1. [ ] Nho
1. [ ] Không thích
1. [ ] Màu
1. [ ] Nào / Gì
1. [ ] Bút bi
1. [ ] Sống
1. [ ] Thủ đô
1. [ ] Việt Nam
1. [ ] Hằng ngày
1. [ ] Thức dậy
1. [ ] Lúc
1. [ ] Giờ
