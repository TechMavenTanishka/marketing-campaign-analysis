-- 1. Overall Response Rate
SELECT 
    COUNT(*) AS total_customers,
    SUM(Response) AS responders,
    ROUND(SUM(Response)*100.0/COUNT(*),2) AS response_rate
FROM customers;

-- 2. Average Spend by Education
SELECT 
    Education,
    AVG(MntWines + MntFruits + MntMeatProducts + 
        MntFishProducts + MntSweetProducts + MntGoldProds) AS avg_spend
FROM customers
GROUP BY Education;

-- 3. Channel Usage
SELECT 
    AVG(NumWebPurchases) AS avg_web,
    AVG(NumStorePurchases) AS avg_store,
    AVG(NumCatalogPurchases) AS avg_catalog
FROM customers;

-- 4. High Income Customers
SELECT COUNT(*) 
FROM customers
WHERE Income > 75000;

-- 5. Campaign Response by Marital Status
SELECT 
    Marital_Status,
    COUNT(*) AS total,
    SUM(Response) AS responders
FROM customers
GROUP BY Marital_Status;
