```
  Label cho các word được soạn sẵn:
    + Format:
      {
        PATTERN: (PATTERN_LEFT, PATTER_RIGHT),
        LOCATION: (LOCATION_LEFT, LOCATION_RIGHT),
        DIRECTION: (DIRECTION_LEFT, DIRECTION_RIGHT), 
      }
    + Example:
        { 
          "PATTERN": ("_","E"),
          "LOCATION": ("_","MOUTH"),
          "DIRECTION": ("_","_") 
        }
    + Tên của các pattern:
      Được hash lại dưới dạng A,B,C,D,E ..
        Ví dụ: Nắm -> A
        Xem tại [Google Sheet](https://docs.google.com/spreadsheets/d/1wobS-_RUlKgN6tjd2wrLGVjX33iymA9AYrqemFEQlEI/edit?usp=sharing)
    + Location:
      5 location : HEAD, MOUTH, SHOULDER, CHEST, BELLY
    +Direction:
      6 direction: UP, DOWN, RIGHT, LEFT, FORWARD, BACKWARD
  Các word khi label:
    + 1 word có thể có 1 hoặc nhiều bộ 3
    + Được bọc trong [] dù có là 1 bộ 3 hay nhiều bộ 3


  Word cần được label:
    + Cảm ơn
    + Tôi
    + Bạn
    + Gia đình
    + Đồng hồ
    + Ba
    + Lái xe
    + Đi làm
    + Xe bus
    + Dừng
    + Ở đâu
    + Mấy
    + Tuổi
    + Có
    + Người
    + Ai
    + Thích
    + Ăn 
    + Nho
    + Không thích
    + Màu
    + Nào / Gì
    + Bút bi
    + Sống
    + Ở đâu
    + Thủ đô
    + Việt Nam
    + Hằng ngày
    + Thức dậy
    + Lúc
    + Giờ

    ......
  => 30 word, mỗi đứa 15 từ


```
