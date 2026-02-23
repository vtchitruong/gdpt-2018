-- Truy vấn 1
SELECT
	count(*) as "Số hảo hán"
FROM
	figures;

-- Truy vấn 2
SELECT
	count(*) as "Số lượng địa sát"
FROM
	figures
WHERE
	type_of_destiny_star = 'earthly fiend';

-- Truy vấn 3
SELECT
	type_of_destiny_star,
	count(*) as "Số lượng"
FROM
	figures
GROUP BY
	type_of_destiny_star;

-- Truy vấn 4
SELECT *
FROM figures
OFFSET 99;

-- Truy vấn 5
SELECT
	biet_danh,
	ten,
	type_of_destiny_star
FROM
	figures
WHERE
	type_of_destiny_star = 'heavenly spirit'
ORDER BY
	ten;

-- Truy vấn 6
SELECT
	biet_danh,
	ten,
	chuc_vu_vai_tro
FROM
	figures
WHERE
	chuc_vu_vai_tro LIKE '%ngũ hổ tướng%';

-- Truy vấn 7
SELECT
	biet_danh,
	ten,
	sao_chieu_menh	
FROM
	figures
WHERE
	biet_danh IN ('Mẫu Đại Hổ', 'Mẫu Dạ Xoa', 'Nhất Trượng Thanh');