# QueryBuilder
query as text: class list implements class iterable,class list contains class node\
query as graph:\
![query1](https://user-images.githubusercontent.com/62445178/148056668-61379d48-9b40-4419-ae4a-f3c919d67483.png)
#### Query Parser
**So far, the parser deals only with some patterns of syntax in query, as described below:
- class [class_name] extends class [class_name]
- class [class_name] implements class [class_name]
- class [class_name] contains class [class_name]
- class [class_name] contains method [method_name]
- class [class_name] contains field [field_name]
- method method_name contains field [field_name]
