-- Truy vấn 1
SELECT
	count(*) as "Số vị vua"
FROM
	vua;

-- Truy vấn 2
SELECT *
FROM vua
LIMIT 3;

-- Truy vấn 3
SELECT
	nien_hieu,
	ten_huy
	ten_huy_khac
FROM
	vua
WHERE
	nien_hieu = 'Thành Thái';

-- Truy vấn 4
SELECT
	nien_hieu,
	ten_huy,
	cha,
	me
FROM
	vua
WHERE
	cha LIKE '%Thiệu Trị%'
	AND me LIKE '%Từ Dụ%';

-- Truy vấn 5
SELECT 
	nien_hieu,
	tai_vi_bat_dau,
	tai_vi_ket_thuc
FROM
	vua
WHERE
	tai_vi_ket_thuc >= 1900
ORDER BY
	tai_vi_bat_dau;