-- =====================================================
-- TRAFFIC VIOLATIONS INSIGHT SYSTEM
-- SQL ANALYSIS QUERIES
-- =====================================================

-- =====================================================
-- 1. TOP 10 VIOLATION TYPES
-- =====================================================

SELECT violation_type,
       COUNT(*) AS total
FROM traffic_violations
GROUP BY violation_type
ORDER BY total DESC
LIMIT 10;

-- =====================================================
-- 2. TOP 10 VEHICLE MAKES
-- =====================================================

SELECT make,
       COUNT(*) AS total
FROM traffic_violations
GROUP BY make
ORDER BY total DESC
LIMIT 10;

-- =====================================================
-- 3. VIOLATIONS BY GENDER
-- =====================================================

SELECT gender,
       COUNT(*) AS total
FROM traffic_violations
GROUP BY gender;

-- =====================================================
-- 4. VIOLATIONS BY RACE
-- =====================================================

SELECT race,
       COUNT(*) AS total
FROM traffic_violations
GROUP BY race
ORDER BY total DESC;

-- =====================================================
-- 5. ACCIDENTS BY VEHICLE TYPE
-- =====================================================

SELECT vehicle_type,
       COUNT(*) AS accidents
FROM traffic_violations
WHERE accident = TRUE
GROUP BY vehicle_type
ORDER BY accidents DESC;

-- =====================================================
-- 6. ALCOHOL RELATED CASES
-- =====================================================

SELECT COUNT(*) AS alcohol_cases
FROM traffic_violations
WHERE alcohol = TRUE;

-- =====================================================
-- 7. MONTHLY TREND ANALYSIS
-- =====================================================

SELECT month,
       COUNT(*) AS total
FROM traffic_violations
GROUP BY month
ORDER BY month;

-- =====================================================
-- 8. TOP DRIVER STATES
-- =====================================================

SELECT driver_state,
       COUNT(*) AS total
FROM traffic_violations
GROUP BY driver_state
ORDER BY total DESC
LIMIT 10;


-- =====================================================
-- 9. ACCIDENT VS NON-ACCIDENT CASES
-- =====================================================

SELECT accident,
       COUNT(*) AS total
FROM traffic_violations
GROUP BY accident;

-- =====================================================
-- 10. ALCOHOL RELATED ACCIDENTS
-- =====================================================

SELECT COUNT(*) AS alcohol_accidents
FROM traffic_violations
WHERE alcohol = TRUE
  AND accident = TRUE;

-- =====================================================
-- 11. SEARCH CONDUCTED ANALYSIS
-- =====================================================

SELECT search_conducted,
       COUNT(*) AS total
FROM traffic_violations
GROUP BY search_conducted;

-- =====================================================
-- 12. TOP 10 DRIVER CITIES
-- =====================================================

SELECT driver_city,
       COUNT(*) AS total
FROM traffic_violations
GROUP BY driver_city
ORDER BY total DESC
LIMIT 10;

-- =====================================================
-- 13. VEHICLE YEAR DISTRIBUTION
-- =====================================================

SELECT year,
       COUNT(*) AS total
FROM traffic_violations
GROUP BY year
ORDER BY year DESC;

-- =====================================================
-- 14. TOP 10 CHARGES
-- =====================================================

SELECT charge,
       COUNT(*) AS total
FROM traffic_violations
GROUP BY charge
ORDER BY total DESC
LIMIT 10;

-- =====================================================
-- 15. WEEKDAY ANALYSIS
-- =====================================================

SELECT day,
       COUNT(*) AS total
FROM traffic_violations
GROUP BY day
ORDER BY total DESC;