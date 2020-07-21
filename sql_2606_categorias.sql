select 	pr.id,
		pr.name
from products pr 
join categories c 
	on pr.id_categories = c.id 
where c.name like 'super%'