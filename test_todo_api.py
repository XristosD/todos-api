import requests
import json

url="https://xristos-todos-api.herokuapp.com/"

class User:
    name="xristos"
    email="xristos@email.com"
    password="123456"
    token=None

def wurl(s):
    return url+s

def print_resp(resp):
    print("status code: "+str(resp.status_code))
    if(resp.text!=''):
        print(json.dumps(resp.json(), indent=2))
          

def signup():
    data = {"name":User.name,"email":User.email,"password":User.password,"password_confirmation":User.password}
    print("Try to sign up...")
    resp = requests.post(wurl("signup"),data)
    print("response:\n")
    print_resp(resp)


print("Try to login...")
resp = requests.post(wurl("auth/login"),params={"email":User.email,"password":User.password})
print("response:\n")
print_resp(resp)
User.token=resp.json()["auth_token"]
input('\nEnter to continue....\n\n')

print("Try to logout...")
resp = requests.get(wurl("auth/logout"),headers={"Authorization":User.token})
print("response:\n")
print_resp(resp)
input('\nEnter to continue....\n\n')

print("Try to create todo...")
resp = requests.post(wurl("auth/login"),params={"email":User.email,"password":User.password})
User.token=resp.json()["auth_token"]
resp = requests.post(wurl("todos"),headers={"Authorization":User.token,"Accept":"'application/vnd.todos.v1+json'"},params={"title":"my first post"})
print("response:\n")
print_resp(resp)
todo_id=resp.json()["id"]
input('\nEnter to continue....\n\n')

print("Try to get first page of todos..")
resp = requests.get(wurl("todos"),headers={"Authorization":User.token,"Accept":"'application/vnd.todos.v1+json'"},params={"page":"1"})
print("response:\n")
print_resp(resp)
input('\nEnter to continue....\n\n')

print("Try to get todo with id="+str(todo_id)+"...")
resp = requests.get(wurl("todos/"+str(todo_id)),headers={"Authorization":User.token,"Accept":"'application/vnd.todos.v1+json'"})
print("response:\n")
print_resp(resp)
input('\nEnter to continue....\n\n')

print("Try to change todo with id="+str(todo_id)+"...")
resp = requests.put(wurl("todos/"+str(todo_id)),headers={"Authorization":User.token,"Accept":"'application/vnd.todos.v1+json'"},params={"title":"Changed title"})
print("response:\n")
print_resp(resp)
input('\nEnter to continue....\n\n')

print("Try to delete todo with id="+str(todo_id)+"...")
resp = requests.delete(wurl("todos/"+str(todo_id)),headers={"Authorization":User.token,"Accept":"'application/vnd.todos.v1+json'"})
print("response:\n")
print_resp(resp)
input('\nEnter to continue....\n\n')

resp = requests.post(wurl("todos"),headers={"Authorization":User.token,"Accept":"'application/vnd.todos.v1+json'"},params={"title":"my first post"})
todo_id2=resp.json()["id"]
print("Try to create item for todo with id="+str(todo_id2)+"...")
resp = requests.post(wurl("todos/"+str(todo_id2)+"/items"),headers={"Authorization":User.token,"Accept":"'application/vnd.todos.v1+json'"},params={"name":"my first comment"})
print("response:\n")
print_resp(resp)
id=resp.json()["items"].pop()["id"]
print("\nitem created with id="+str(resp.json()["items"].pop()["id"]))
input('\nEnter to continue....\n\n')

print("Try to get items for todo with id="+str(todo_id2)+"...")
resp = requests.get(wurl("todos/"+str(todo_id2)+"/items"),headers={"Authorization":User.token,"Accept":"'application/vnd.todos.v1+json'"})
print("response:\n")
print_resp(resp)
input('\nEnter to continue....\n\n')

print("Try to change item with id="+str(id)+" and todo with id="+str(todo_id2)+"...")
resp = requests.put(wurl("todos/"+str(todo_id2)+"/items/"+str(id)),headers={"Authorization":User.token,"Accept":"'application/vnd.todos.v1+json'"},params={"name":"Changed name"})
print("response:\n")
print_resp(resp)
input('\nEnter to continue....\n\n')

print("Try to delete item with id="+str(id)+" and todo with id="+str(todo_id2)+"...")
resp = requests.delete(wurl("todos/"+str(todo_id2)+"/items/"+str(id)),headers={"Authorization":User.token,"Accept":"'application/vnd.todos.v1+json'"})
print("response:\n")
print_resp(resp)
input('\nEnter to continue....\n\n')
