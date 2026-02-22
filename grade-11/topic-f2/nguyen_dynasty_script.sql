create database nguyen_dynasty;

CREATE TABLE vua (
    id INT PRIMARY KEY,
    ten_huy VARCHAR(50) NOT NULL,
	ten_huy_khac VARCHAR(50),
	nam_sinh INT,
	nam_mat INT,
    nien_hieu VARCHAR(50) NOT NULL,
    mieu_hieu VARCHAR(100),
    thuy_hieu TEXT,
    tai_vi_bat_dau INT,
    tai_vi_ket_thuc INT,
    vo_chinh TEXT,
    cha VARCHAR(50),
    me VARCHAR(50),
    con_dai_dien TEXT,
	so_con_trai SMALLINT, 
	so_con_gai SMALLINT
);

INSERT INTO vua 
(id, ten_huy, ten_huy_khac, nam_sinh, nam_mat, nien_hieu, mieu_hieu, thuy_hieu, tai_vi_bat_dau, tai_vi_ket_thuc, vo_chinh, cha, me, con_dai_dien, so_con_trai, so_con_gai)
VALUES 
(1, 'Nguyễn Phúc Ánh', 'Nguyễn Ánh', 1762, 1820, 'Gia Long', 'Thế Tổ', 'Khai thiên Hoằng đạo Lập kỷ Thùy thống Thần văn Thánh võ Tuấn đức Long công Chí nhân Đại hiếu Cao hoàng đế', 1802, 1820, 'Thừa Thiên Cao Hoàng hậu; Thuận Thiên Cao Hoàng hậu', 'Nguyễn Phúc Luân', 'Nguyễn Thị Hoàn', 'Nguyễn Phúc Đảm (vua Minh Mạng)', 13, 18),
(2, 'Nguyễn Phúc Đảm', 'Nguyễn Phúc Hiểu', 1791, 1841, 'Minh Mạng', 'Thánh Tổ', 'Thể thiên Xương vận Chí hiếu Thuần đức Văn vũ Minh đoán Sáng thuật Đại thành Hậu trạch Phong công Nhân Hoàng đế', 1820, 1841, 'Tá Thiên Nhân Hoàng hậu', 'Gia Long', 'Thuận Thiên Cao Hoàng hậu', 'Nguyễn Phúc Miên Tông (vua Thiệu Trị)', 74, 68),
(3, 'Nguyễn Phúc Dung', 'Nguyễn Phúc Miên Tông', 1807, 1847, 'Thiệu Trị', 'Hiến Tổ', 'Thiệu Thiên Long Vận Chí Thiện Thuần Hiếu Khoan Minh Duệ Đoán Văn Trị Vũ Công Thánh Triết Chương Hoàng đế', 1841, 1847, 'Nghi Thiên Chương Hoàng hậu (Từ Dụ Hoàng thái hậu)', 'Minh Mạng', 'Tá Thiên Nhân Hoàng hậu', 'Nguyễn Phúc Hồng Nhậm (vua Tự Đức)', 29, 35),
(4, 'Nguyễn Phúc Hồng Nhậm', 'Nguyễn Phúc Thì', 1829, 1883, 'Tự Đức', 'Dực Tông', 'Thể Thiên Hanh Vận Chí Thành Đạt Hiếu Thể Kiện Đôn Nhân Khiêm Cung Minh Lược Duệ Văn Anh Hoàng đế', 1847, 1883, 'Lệ Thiên Anh Hoàng hậu', 'Thiệu Trị', 'Nghi Thiên Chương Hoàng hậu (Từ Dụ Hoàng thái hậu)', 'Nguyễn Phúc Ưng Chân (con nuôi, vua Dục Đức); Nguyễn Phúc Ưng Đăng (con nuôi, vua Kiến Phúc)', 0, 0),
(5, 'Nguyễn Phúc Ưng Ái', 'Nguyễn Phúc Ưng Chân', 1852, 1883, 'Dục Đức', 'Cung Tông', 'Khoan Nhân Duệ Triết Tĩnh Minh Huệ Hoàng đế', 1883, 1883, 'Từ Minh Huệ Hoàng hậu', 'Nguyễn Phúc Hồng Y', 'Trần Thị Nga', 'Nguyễn Phúc Bửu Lân (vua Thành Thái)', 11, 8),
(6, 'Nguyễn Phúc Hồng Dật', 'Nguyễn Phúc Thăng', 1847, 1883, 'Hiệp Hòa', NULL, 'Trang Cung Văn Lãng Quận vương', 1883, 1883, NULL, 'Thiệu Trị', 'Trương Thị Thận', 'Nguyễn Phúc Ưng Hiệp; Nguyễn Phúc Ưng Phấn', 11, 6),
(7, 'Nguyễn Phúc Ưng Đăng', 'Nguyễn Phúc Hạo', 1869, 1884, 'Kiến Phúc', 'Giản Tông', 'Thiệu Đức Chí Hiếu Uyên Duệ Nghị Hoàng đế', 1883, 1884, NULL, 'Nguyễn Phúc Hồng Cai (em của vua Tự Đức)', 'Bùi Thị Thanh', NULL, NULL, 0),
(8, 'Nguyễn Phúc Ưng Lịch', 'Nguyễn Phúc Minh', 1871, 1944, 'Hàm Nghi', NULL, NULL, 1884, 1885, 'Marcelle Aimée Léonie Laloë', 'Nguyễn Phúc Hồng Cai (em của vua Tự Đức)', 'Phan Thị Nhàn', 'Nguyễn Phúc Như Mai; Nguyễn Phúc Như Lý; Nguyễn Phúc Minh Đức', 1, 2),
(9, 'Nguyễn Phúc Ưng Thị', 'Nguyễn Phúc Ưng Đường; Nguyễn Phúc Biện', 1864, 1889, 'Đồng Khánh', 'Cảnh Tông', 'Phối Thiên Minh Vận Hiếu Đức Nhân Vũ Vĩ Công Hoằng Liệt Thông Triết Mẫn Huệ Thuần Hoàng đế', 1885, 1889, 'Phụ Thiên Thuần Hoàng hậu; Hựu Thiên Thuần Hoàng hậu', 'Nguyễn Phúc Hồng Cai (em của vua Tự Đức)', 'Bùi Thị Thanh', 'Nguyễn Phúc Bửu Đảo (vua Khải Định)', 6, 3),
(10, 'Nguyễn Phúc Bửu Lân', 'Nguyễn Phúc Chiêu', 1879, 1954, 'Thành Thái', NULL, 'Hoài Trạch Công', 1889, 1907, 'Nguyễn Thị Định', 'Dục Đức', 'Phan Thị Điều', 'Nguyễn Phúc Vĩnh San (vua Duy Tân)', 11, NULL),
(11, 'Nguyễn Phúc Vĩnh San', 'Nguyễn Phúc Hoảng', 1900, 1945, 'Duy Tân', NULL, NULL, 1907, 1916, 'Mai Thị Vàng', 'Thành Thái', 'Nguyễn Thị Định', 'Armand Viale; Thérèse Vinh-San; Rita Suzy Georgette Vinh-San; Solange ; Nguyễn Phúc Bảo Ngọc; Nguyễn Phúc Bảo Vàng; Nguyễn Phúc Bảo Quý; Ginette; André; Andrée Maillot', 4, 5),
(12, 'Nguyễn Phúc Bửu Đảo', 'Nguyễn Phúc Tuấn', 1885, 1925, 'Khải Định', 'Hoằng Tông', 'Tự Thiên Gia Vận Thánh Minh Thần Trí Nhân Hiếu Thành Kính Di Mô Thừa Liệt Tuyên Hoàng đế', 1916, 1925, 'Đoan Huy Hoàng thái hậu (Đức Từ Cung)', 'Đồng Khánh', 'Hựu Thiên Thuần Hoàng hậu', 'Nguyễn Phúc Vĩnh Thụy (vua Bảo Đại)', 1, 0),
(13, 'Nguyễn Phúc Vĩnh Thụy', NULL, 1913, 1997, 'Bảo Đại', NULL, NULL, 1926, 1945, 'Nguyễn Thị Hữu Lan (Nam Phương Hoàng hậu)', 'Khải Định', 'Hoàng Thị Cúc', 'Nguyễn Phúc Bảo Long; Nguyễn Phúc Bảo Thăng; Nguyễn Phúc Phương Mai', 5, 4);