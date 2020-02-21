# ΔΙΑΜΑΝΤΗΣ Χρήστος, p16168


web url: https://xristos-todos-api.herokuapp.com/

API Examples:
http POST :3001/signup name=xristos email=xristos@email.com password=123456 password_confirmation=123456
http POST :3001/auth/login email=xristos@email.com password=123456
http GET :3001/auth/logout Authorization:eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwidXNlcl9yYW5kb21fc3RyaW5nIjoiUXNxLWI0aVgiLCJleHAiOjE1ODA1NjM1OTR9.nK2EOgMZDDciDcZpW8iK-ovPLv31YlAuoWGpdlNe770

http GET :3001/todos Accept:'application/vnd.todos.v1+json' Authorization:eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwidXNlcl9yYW5kb21fc3RyaW5nIjoiU0N4eXFGR0kiLCJleHAiOjE1ODA1NjM2NzJ9.meFW7Vnl8vCRqhALfKf1iLxMQk0RoANpHY4S58ktPdE
http GET :3001/todos page== Accept:'application/vnd.todos.v1+json' Authorization:


eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwidXNlcl9yYW5kb21fc3RyaW5nIjoiYlhyUmNNdGkiLCJleHAiOjE1ODA4Mzc4NDR9.AYfIkIlgFK-xbbgVt52e6RF5_UrR4q6S-LBLxxQjvaY

http POST :3001/todos title="my first post" Authorization:eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwidXNlcl9yYW5kb21fc3RyaW5nIjoiU0N4eXFGR0kiLCJleHAiOjE1ODA1NjM2NzJ9.meFW7Vnl8vCRqhALfKf1iLxMQk0RoANpHY4S58ktPdE
http POST :3001/todos Accept:'application/vnd.todos.v1+json' title= Authorization:

http GET :3001/todos/id Authorization:
http GET :3001/todos/id Accept:'application/vnd.todos.v1+json' Authorization:

http PUT :3001/todos/id title=  Authorization:
http PUT :3001/todos/4 Accept:'application/vnd.todos.v1+json' title="Changed name"  Authorization:

http DELETE :3001/todos/id Authorization:
http DELETE :3001/todos/id Accept:'application/vnd.todos.v1+json' Authorization:

http GET :3001/todos/id/items  Authorization:
http GET :3001/todos/id/items Accept:'application/vnd.todos.v1+json' Authorization:

http POST :3001/todos/id/items name= Authorization:
http POST :3001/todos/id/items name=  Accept:'application/vnd.todos.v1+json' Authorization:

http GET :3001/todos/id/items/id  Authorization:
http GET :3001/todos/id/items/id  Accept:'application/vnd.todos.v1+json' Authorization:

http PUT :3001/todos/id/items/id name=  Authorization:
http PUT :3001/todos/id/items/id name=  Accept:'application/vnd.todos.v1+json' Authorization:

http DELETE :3001/todos/id/items/id  Authorization:
http DELETE :3001/todos/id/items/id  Accept:'application/vnd.todos.v1+json' Authorization:
