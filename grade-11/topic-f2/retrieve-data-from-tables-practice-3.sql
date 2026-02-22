-- Truy vấn 1
SELECT
	house_name,
	founder,
	color_1,
	color_2
FROM
	houses
WHERE
	house_name = 'Slytherin';

-- Truy vấn 2	
SELECT
	blood_name,
	blood_description
FROM
	bloods
WHERE
	lower(blood_name) = 'half-blood';

-- Truy vấn 3
SELECT
	count(*) AS "Số lời nguyền"
FROM
	spells
WHERE
	lower(spell_type) = 'curse'
	OR lower(spell_type) = 'jinx';
	
-- Truy vấn 4
SELECT
	subject_name,
	subject_type
FROM
	subjects
WHERE
	lower(subject_type) = 'core'
ORDER BY
	subject_name;

-- Truy vấn 5
SELECT
	spec_name,
	spec_description
FROM
	species
WHERE
	lower(spec_description) like '%human%'
	OR lower(spec_description) like '%homo%';

-- Truy vấn 6
SELECT
	first_name,
	middle_name,
	last_name,
	skills
FROM
	characters
WHERE
	last_name ilike '%weasley%'
ORDER BY last_name,
	first_name desc;


select * from characters
where first_name = 'Hermione'
