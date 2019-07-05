{
	'name': 'HR Module',
    'summary' : "HR Module Administration",
	'description' : """HR Module Masters""",
	'author' : "ISGEC IT",
	'license' : "AGPL-3",
	'website' : "www.isgec.com",
	'category' : 'Uncategorized',
	'version' : '12.0.1.0.0',
	'depends' : ['base'],
	'data' : [
		     'security/groups.xml',
			'views/hrmodule_employeetable.xml',
	         'security/ir.model.access.csv',
	         ],	
}
