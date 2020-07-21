select 	pr.name,
		p.name
from products pr  
join providers p
	on pr.id_providers = p.id 
join categories c 
	on pr.id_categories = c.id 
where c.id = 6 