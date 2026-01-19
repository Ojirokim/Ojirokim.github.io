SELECT Concat(name,' (',substr(occupations,1,1),')')
from occupations
Union
SELECT Concat('There are a total of ',count(Occupation), ' ',Occupation)
FROM OCCUPATIONS
GROUP BY Occupation